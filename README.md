# Student Course Registration System

A simple Python course-registration system built to practice the foundations of **Object-Oriented Programming (OOP)**.

## Features

- Create students and courses
- Enroll students in courses
- Drop students from courses
- Prevent duplicate enrollment
- Prevent enrollment when a course reaches capacity
- Display a student's enrolled courses
- Display the students enrolled in a course
- Keep student and course enrollment information synchronized

## Classes

### Student

The `Student` class represents a student in the registration system.

Each student has:

- Name
- Age
- Year
- List of enrolled courses

The class also contains a shared `school` class variable.

Students can:

- Enroll in a course
- Drop a course
- View their enrolled courses

### Course

The `Course` class represents a course available for registration.

Each course has:

- Name
- Course code
- Teacher
- Number of credits
- Duration
- Capacity
- List of enrolled students

Courses can also display the students currently enrolled.

## OOP Concepts Practiced

This project was built to practice Phase 1 OOP foundations, including:

- Classes and objects
- Attributes and methods
- Constructors (`__init__`)
- `self`
- Object state
- Instance variables
- Class variables
- Objects interacting with other objects

For example, a `Student` object stores references to the `Course` objects the student is enrolled in. Each `Course` object also stores references to its enrolled `Student` objects.

## Project Structure

```text
student-course-registration/
├── main.py
├── student.py
├── course.py
└── README.md
```

- `student.py` contains the `Student` class.
- `course.py` contains the `Course` class.
- `main.py` creates objects and tests the registration system.

## Running the Project

Make sure **Python 3** is installed.

Run:

```bash
python3 main.py
```

## Purpose

This project is part of my study of Object-Oriented Programming in Python.

The goal was to apply OOP fundamentals in a small working system before moving on to more advanced concepts such as:

- Encapsulation
- Abstraction
- Inheritance
- Polymorphism