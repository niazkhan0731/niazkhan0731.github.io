# animal_shelter.py
from pymongo import MongoClient, ASCENDING, TEXT
from bson.objectid import ObjectId
import re
import csv
from typing import Optional

class AnimalShelter(object):
    """
    CRUD operations for Animal collection in MongoDB

    CS-499 Milestone Four (Databases) enhancements:
      - Input validation & safe inserts/updates
      - Advanced read filters (type/outcome/age/breed/sex)
      - Aggregation helper for reporting
      - CSV export utility
      - Basic indexes on common query fields

    Local Mongo defaults:
      host='localhost', port=27017, no auth
    You can still pass user/password/host/port if needed.
    """

    # Common AAC schema fields (adjust only if your dataset uses different names)
    REQUIRED_FIELDS = {
        "animal_id",
        "name",
        "animal_type",
        "breed",
        "sex_upon_outcome",
        "age_upon_outcome_in_weeks",
        "outcome_type"
    }
    ALLOWED_FIELDS = REQUIRED_FIELDS.union({
        "color",
        "date_of_birth",
        "datetime",
        "monthyear",
        "outcome_subtype",
        "outcome_monthyear",
        "outcome_datetime",
        "location_lat",
        "location_long"
    })

    def __init__(
        self,
        user: Optional[str] = None,
        password: Optional[str] = None,
        host: str = 'localhost',
        port: int = 27017,
        db: str = 'AAC',
        col: str = 'animals',
        authSource: str = 'admin',
        uri: Optional[str] = None
    ):
        """
        Connect to MongoDB. By default connects to local Mongo with no auth.
        If user/password are provided, connects with authSource.
        If uri is provided, it overrides everything else.
        """
        if uri:
            self.client = MongoClient(uri)
        else:
            if user and password:
                mongo_uri = f"mongodb://{user}:{password}@{host}:{port}/?authSource={authSource}"
            else:
                mongo_uri = f"mongodb://{host}:{port}"
            self.client = MongoClient(mongo_uri)

        self.database = self.client[db]
        self.collection = self.database[col]

        # Indexes that support our filters and text search
        try:
            self.collection.create_index([("animal_type", ASCENDING)])
            self.collection.create_index([("outcome_type", ASCENDING)])
            self.collection.create_index([("sex_upon_outcome", ASCENDING)])
            self.collection.create_index([("age_upon_outcome_in_weeks", ASCENDING)])
            self.collection.create_index([("breed", TEXT)])
        except Exception:
            # If indexes already exist or fail to create, continue gracefully.
            pass

    # -------------------- helpers --------------------
    def _sanitize_doc(self, data: dict) -> dict:
        """Whitelist + enforce basic types and required fields for inserts/updates."""
        if not isinstance(data, dict):
            raise ValueError("Data must be a dictionary.")

        clean = {k: v for k, v in data.items() if k in self.ALLOWED_FIELDS}

        missing = self.REQUIRED_FIELDS - set(clean.keys())
        if missing:
            raise ValueError(f"Missing required fields: {sorted(list(missing))}")

        # Enforce numeric type for age
        if "age_upon_outcome_in_weeks" in clean:
            try:
                clean["age_upon_outcome_in_weeks"] = float(clean["age_upon_outcome_in_weeks"])
            except Exception:
                raise ValueError("age_upon_outcome_in_weeks must be numeric.")

        return clean

    def _coerce_object_id(self, _id):
        if isinstance(_id, ObjectId):
            return _id
        try:
            return ObjectId(str(_id))
        except Exception:
            raise ValueError("Invalid ObjectId format.")

    # -------------------- CRUD --------------------
    def create(self, data):
        """Insert a single document after validation."""
        if not data:
            return False
        clean = self._sanitize_doc(data)
        result = self.collection.insert_one(clean)
        return True if result.inserted_id else False

    def read(self, query=None, projection=None, limit=1000):
        """Find documents. If query is empty, returns all (limited)."""
        if query is None or not query:
            cursor = self.collection.find({}, projection).limit(int(limit))
        else:
            cursor = self.collection.find(query, projection).limit(int(limit))
        return list(cursor)

    def read_all(self):
        """Return all docs without _id (for UI tables)."""
        return list(self.collection.find({}, {"_id": False}))

    def update(self, query, new_values):
        """Update many docs. Only allowed fields are updated."""
        if not query or not new_values:
            return 0
        clean_updates = {k: v for k, v in new_values.items() if k in self.ALLOWED_FIELDS}
        if "age_upon_outcome_in_weeks" in clean_updates:
            clean_updates["age_upon_outcome_in_weeks"] = float(clean_updates["age_upon_outcome_in_weeks"])
        result = self.collection.update_many(query, {'$set': clean_updates})
        return result.modified_count

    def delete(self, query):
        """Delete many docs."""
        if not query:
            return 0
        result = self.collection.delete_many(query)
        return result.deleted_count

    # -------------------- Advanced Reads --------------------
    def read_advanced(
        self,
        animal_type: Optional[str] = None,
        outcome_type: Optional[str] = None,
        min_age_wk: Optional[float] = None,
        max_age_wk: Optional[float] = None,
        breed_contains: Optional[str] = None,
        sex: Optional[str] = None,
        limit: int = 500
    ):
        """
        Flexible filter builder for common analysis tasks.
        Any parameter is optional.
        """
        q = {}
        if animal_type:
            q["animal_type"] = animal_type
        if outcome_type:
            q["outcome_type"] = outcome_type
        if sex:
            q["sex_upon_outcome"] = sex
        if min_age_wk is not None or max_age_wk is not None:
            age_cond = {}
            if min_age_wk is not None:
                age_cond["$gte"] = float(min_age_wk)
            if max_age_wk is not None:
                age_cond["$lte"] = float(max_age_wk)
            q["age_upon_outcome_in_weeks"] = age_cond
        if breed_contains:
            q["breed"] = {"$regex": re.escape(breed_contains), "$options": "i"}

        return list(self.collection.find(q).limit(int(limit)))

    # -------------------- Aggregations --------------------
    def aggregate_adoption_stats(self, group_by: str = "animal_type", match: Optional[dict] = None):
        """
        Group counts by a field (e.g., 'animal_type' or 'outcome_type').
        Returns: [{'_id': 'Dog', 'count': 1234}, ...]
        """
        match = match or {}
        pipeline = [
            {"$match": match},
            {"$group": {"_id": f"${group_by}", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        return list(self.collection.aggregate(pipeline))

    # -------------------- Export Utility --------------------
    def export_to_csv(self, query: dict, filepath: str, projection: Optional[dict] = None, limit: int = 5000):
        """
        Export query results to CSV (excluding _id).
        Returns number of rows written.
        """
        cursor = self.collection.find(query, projection).limit(int(limit))
        first = next(cursor, None)
        if first is None:
            # Create an empty file
            with open(filepath, "w", newline="", encoding="utf-8") as f:
                f.write("")
            return 0

        fieldnames = [k for k in first.keys() if k != "_id"]
        rows = [first]
        rows.extend(cursor)

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                r = {k: v for k, v in r.items() if k in fieldnames}
                writer.writerow(r)
        return len(rows)