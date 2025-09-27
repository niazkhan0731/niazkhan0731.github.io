package com.example.eventtrackerapp;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.GridView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import java.util.ArrayList;
import java.util.List;

/**
 * Main screen: shows all events in a GridView.
 * Enhancements:
 *  - Uses EventRepository (no direct DB calls in UI)
 *  - Adds empty state message
 *  - Safer refresh & error handling
 */
public class MainActivity extends AppCompatActivity {

    private EventRepository repository;
    private GridView gridView;
    private TextView emptyView;
    private ArrayList<String> eventList;
    private ArrayAdapter<String> adapter;
    private Button addEventButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        repository = new EventRepository(this);
        gridView = findViewById(R.id.eventGridView);
        addEventButton = findViewById(R.id.addEventButton);

        // Empty state view (added in XML below; if missing, we create one programmatically)
        emptyView = findViewById(R.id.emptyView);
        if (emptyView == null) {
            emptyView = new TextView(this);
            emptyView.setText("No events yet — tap + to add one.");
            emptyView.setTextAlignment(TextView.TEXT_ALIGNMENT_CENTER);
            emptyView.setPadding(32, 64, 32, 32);
        }
        gridView.setEmptyView(emptyView);

        eventList = new ArrayList<>();
        adapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, eventList);
        gridView.setAdapter(adapter);

        loadEvents();

        gridView.setOnItemClickListener((adapterView, view, position, id) -> {
            String selected = eventList.get(position);
            Toast.makeText(MainActivity.this, "Clicked: " + selected, Toast.LENGTH_SHORT).show();
        });

        addEventButton.setOnClickListener(v ->
                startActivity(new Intent(MainActivity.this, AddEventActivity.class)));
    }

    private void loadEvents() {
        try {
            List<String> displayItems = repository.getAllEventDisplayStrings();
            eventList.clear();
            eventList.addAll(displayItems);
            adapter.notifyDataSetChanged();
        } catch (Exception ex) {
            Toast.makeText(this, "Failed to load events", Toast.LENGTH_SHORT).show();
        }
    }

    @Override
    protected void onResume() {
        super.onResume();
        loadEvents();
    }
}
