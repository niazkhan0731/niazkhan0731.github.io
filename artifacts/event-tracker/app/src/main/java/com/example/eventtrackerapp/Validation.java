package com.example.eventtrackerapp;

import android.text.TextUtils;

import java.util.regex.Pattern;

/**
 * Tiny input validation helper.
 * - Date format: YYYY-MM-DD (simple, user-friendly)
 * - Time format: HH:MM (24-hour, 00-23:00-59)
 */
public class Validation {

    // Very simple patterns—good enough for milestone requirements
    private static final Pattern DATE = Pattern.compile("^\\d{4}-\\d{2}-\\d{2}$");
    private static final Pattern TIME = Pattern.compile("^([01]\\d|2[0-3]):[0-5]\\d$");

    /**
     * @return null if valid, otherwise a short error message to show the user.
     */
    public static String validateEventInputs(String name, String date, String time) {
        if (TextUtils.isEmpty(name) || TextUtils.isEmpty(date) || TextUtils.isEmpty(time)) {
            return "Please fill all fields";
        }
        if (!DATE.matcher(date).matches()) {
            return "Use date format YYYY-MM-DD";
        }
        if (!TIME.matcher(time).matches()) {
            return "Use time format HH:MM (24-hour)";
        }
        return null;
    }
}