🕒 Productivity Tracker (Console-Based)

A simple yet effective console-based productivity logging system powered by Python and MySQL. This tool helps you log your daily tasks, categorize them, track time spent, and analyze your productivity — all from the command line.
✨ Features

    ⏱ Start and End task timers with real-time timestamps

    📂 Tag tasks with categories like Work, Study, or Break

    📊 Generate daily/weekly reports showing time spent per category

    🔔 Get CLI alerts if a task is running too long (e.g. over 2 hours)

    🗃 All data stored persistently using a MySQL database

    🧮 Category-wise time analysis

    📋 View task history with task names, times, and durations

    ✅ Simple text-based menu system

🧰 Tech Stack

    🐍 Python 3.x

    🐬 MySQL Server

    📦 mysql-connector-python

    🎨 Optional: tabulate, colorama (for better CLI output) 

Follow the simple menu-driven interface:

    Add Task

    End Task

    View All Tasks

    Generate Report

    Notify Long Running Tasks

    Exit

📝 Sample Entry Flow

    Add Task: Name → Description → Category

    Task is started with current timestamp

    End Task: Use task ID to log the end time

    View Report: See total hours per category
