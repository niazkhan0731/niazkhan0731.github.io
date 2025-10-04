package com.example.eventtrackerapp;

import android.content.Context;
import android.database.Cursor;

import java.util.ArrayList;
import java.util.List;

/**
 * Repository layer: the only class that talks to DatabaseHelper.
 * UI (Activities/Fragments) depend on this, not the DB helper directly.
 */
public class EventRepository {

    private final DatabaseHelper db;

    public EventRepository(Context context) {
        this.db = new DatabaseHelper(context.getApplicationContext());
    }

    public boolean addEvent(String name, String date, String time) {
        return db.addEvent(name, date, time);
    }

    /** Returns display-ready strings (Name \n date time). */
    public List<String> getAllEventDisplayStrings() {
        List<String> items = new ArrayList<>();
        Cursor cursor = db.getAllEvents();
        if (cursor != null) {
            try {
                if (cursor.moveToFirst()) {
                    int nameIdx = cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_EVENT_NAME);
                    int dateIdx = cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_EVENT_DATE);
                    int timeIdx = cursor.getColumnIndexOrThrow(DatabaseHelper.COLUMN_EVENT_TIME);
                    do {
                        String name = cursor.getString(nameIdx);
                        String date = cursor.getString(dateIdx);
                        String time = cursor.getString(timeIdx);
                        items.add(name + "\n" + date + " " + time);
                    } while (cursor.moveToNext());
                }
            } finally {
                cursor.close();
            }
        }
        return items;
    }
}