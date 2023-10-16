package com.example.helloworld;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;


public class MainActivity extends AppCompatActivity {
    EditText text;
    Button button;
    TextView title;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        text = findViewById(R.id.text);
        button = findViewById(R.id.button);
        title = findViewById(R.id.title);

        button.setOnClickListener(new View.OnClickListener(){

            @Override
            public void onClick(View view) {
                String input = text.getText().toString();

                Toast.makeText(
                        MainActivity.this,
                        "Welcome " + input + " to our App",
                        Toast.LENGTH_SHORT).show();
            }
        });
    }
}