package com.example.eventtrackerapp;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

/**
 * Add-event screen.
 * Enhancements:
 *  - Validation utility for inputs
 *  - Repository (no direct DB calls)
 *  - Clear user feedback
 */
public class AddEventActivity extends AppCompatActivity {

    private EditText nameInput, dateInput, timeInput;
    private Button saveButton;
    private EventRepository repository;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_add_event);

        repository = new EventRepository(this);

        nameInput = findViewById(R.id.eventNameInput);
        dateInput = findViewById(R.id.eventDateInput);
        timeInput = findViewById(R.id.eventTimeInput);
        saveButton = findViewById(R.id.saveEventButton);

        saveButton.setOnClickListener(view -> {
            String name = nameInput.getText().toString().trim();
            String date = dateInput.getText().toString().trim();
            String time = timeInput.getText().toString().trim();

            String validationError = Validation.validateEventInputs(name, date, time);
            if (validationError != null) {
                Toast.makeText(AddEventActivity.this, validationError, Toast.LENGTH_SHORT).show();
                return;
            }

            try {
                boolean success = repository.addEvent(name, date, time);
                if (success) {
                    Toast.makeText(AddEventActivity.this, "Event added", Toast.LENGTH_SHORT).show();
                    finish(); // Go back to MainActivity
                } else {
                    Toast.makeText(AddEventActivity.this, "Failed to add event", Toast.LENGTH_SHORT).show();
                }
            } catch (Exception ex) {
                Toast.makeText(AddEventActivity.this, "Unexpected error adding event", Toast.LENGTH_SHORT).show();
            }
        });
    }
}
