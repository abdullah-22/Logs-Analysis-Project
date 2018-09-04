# Project # 03: Logs Analysis Project
## by Abdullah A. Salman

This is the third project of ***[Udacity Full Stack Web Developer Nanodegree Program](https://classroom.udacity.com/nanodegrees/nd004/)*** .

A database reporting tool that analyzes a large database using complex SQL queries for getting answers to certain questions.
## Introduction
This project, basically, requires the students to analyze a large database (> 1000k rows) using complex SQL queries in order to answer some business questions. Final solution is a python script with embedded SQL queries to connect to the database, query the tables and views, fetch the results, present them on screen and save these results in a text file.
The database named **news** consists of three default tables named ***authors***, ***articles*** and  ***log***.
-   The  **authors**  table includes information about the authors of the articles.
-   The  **articles**  table includes the articles themselves and related information.
-   The  **log**  table keeps the record of each time when someone tries to accesses the website.

**Based on the data of these tables, the project concludes the following results:**

- Most popular (viewed) three articles of all time
- Most read authors (depending upon number of views on their articles)
- Days on which more than 1% of the total HTTP requests on the website were erroneous

## Contents
This project repository consists of the following files:
-    **logs_analysis.py**  --- The Python program that connects to the database, executes the queries, displays and saves the results.
-  **results.txt**  --- The text file having the formatted results of the analysis.
-  **scrn1.png** and **scrn2.png** are the screenshots of the test run.
-  And a **ReadMe** file :D

### `Logs_Analysis.py`
The code of this file includes the following functions:
- `connect_to_db()`---  connects to the database, and returns the connection cursor.
- `top_articles()` --- stores and executes the query to shortlist the top 3 most viewed articles of all time, and display and save the results.
- `top_authors()` --- do as same as the above function to conclude the most read authors in descending order.
- `too_many_errors()` --- executes some complex queries to find the day when more than 1% of the requests to access the website were erroneous
- `create_view()`--- creates a temporary database view ***daily_request_stats*** that stores the day-wise number of total requests, successful and the failed ones. The view is then used in`too_many_errors()` function to derive the result.

## Running the project
This project is built, and thus will run best in a virtual environment that is an ***Ubuntu virtual box*** provided by and interfaced with ***Vagrant***.
Other dependencies include:
 - **Python 2 or Python 3**
 - **PostgreSQL 9 or 10**
 - **psycopg 2 library**

Follow these instructions to set up the required environment:

 1. Install [VirtualBox](https://www.virtualbox.org/)
 2. Install [Vagrant](https://www.vagrantup.com/)
 3. Get the vagrant setup files from  [here](https://github.com/udacity/fullstack-nanodegree-vm)
 4. Dowload or clone these files in a separate directory on your desktop
 5. Download and unzip this [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
6.  Extract the ***newsdata.sql*** file from the downloaded archive and place it into the **vagrant** directory
7.  Download this [log analysis project](https://github.com/abdullah-22/Logs-Analysis-Project/archive/master.zip) or [clone](https://github.com/abdullah-22/Logs-Analysis-Project) it to your PC.
8.  Copy all the project files in a new directory within the previously created **vagrant**  directory