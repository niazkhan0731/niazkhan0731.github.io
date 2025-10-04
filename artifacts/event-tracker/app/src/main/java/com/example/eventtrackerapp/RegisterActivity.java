package com.example.eventtrackerapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class RegisterActivity extends AppCompatActivity {

    private EditText usernameInput, passwordInput;
    private Button registerButton;
    private DatabaseHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);

        // Initialize components
        usernameInput = findViewById(R.id.registerUsernameInput);
        passwordInput = findViewById(R.id.registerPasswordInput);
        registerButton = findViewById(R.id.confirmRegisterButton);
        dbHelper = new DatabaseHelper(this);

        // Register button logic
        registerButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String username = usernameInput.getText().toString().trim();
                String password = passwordInput.getText().toString().trim();

                if (username.isEmpty() || password.isEmpty()) {
                    Toast.makeText(RegisterActivity.this, "Please fill in both fields", Toast.LENGTH_SHORT).show();
                } else {
                    boolean success = dbHelper.registerUser(username, password);
                    if (success) {
                        Toast.makeText(RegisterActivity.this, "Registration successful. Please log in.", Toast.LENGTH_LONG).show();

                        // Navigate back to LoginActivity
                        Intent intent = new Intent(RegisterActivity.this, LoginActivity.class);
                        startActivity(intent);
                        finish();
                    } else {
                        Toast.makeText(RegisterActivity.this, "Username already exists. Try another.", Toast.LENGTH_SHORT).show();
                    }
                }
            }
        });
    }
}
