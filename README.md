# Project # 03: Logs Analysis Project
## by Abdullah A. Salman

This is the third project of ***[Udacity Full Stack Web Developer Nanodegree Program](https://classroom.udacity.com/nanodegrees/nd004/)*** .

*A database reporting tool that analyzes a large database using complex SQL queries for getting answers to some questions*

## Introduction
This project, basically, requires the students to analyze a large database (> 1000k rows) using complex SQL queries to get some business questions answered. Final solution is a python script with embedded SQL queries to:
- *connect to the database*
- *query the tables and view*
- *fetch the results*
- *present them on screen*
- *save these results in a text file*

The database named **news** consists of three default tables named ***authors***, ***articles*** and  ***log***.
-   The  **authors**  table includes information about the authors of the articles.
-   The  **articles**  table includes the articles themselves and related information.
-   The  **log**  table keeps the record of each time when someone tries to accesses the website.

**Based on the data of these tables, the project concludes the following results:**
1. Most popular (viewed) three articles of all time
2. Most read authors (depending upon number of views on their articles)
3. Days on which more than 1% of the total HTTP requests on the website were erroneous

## Project Contents
The project repository consists of the following files:
-  **logs_analysis.py**  --- The Python program that connects to the database, executes the queries, displays and saves the results.
-  **results.txt**  --- The text file having the formatted results of the test run.
-  **scrn1.png** and **scrn2.png** are the screenshots of the test run.
-  And a **ReadMe** file :D

### `logs_analysis.py`
The code in this file includes the following functions:
- `connect_to_db()`---  connects to the database, and returns the connection cursor.
- `top_articles()` --- stores and executes the query to shortlist the top 3 most viewed articles of all time, and display and save the results.
- `top_authors()` --- do as same as the above function to conclude the most read authors in descending order.
- `too_many_errors()` --- executes some complex queries to find the day when more than 1% of the requests to access the website were erroneous.
- `create_view()`--- creates a temporary database view ***daily_request_stats*** that stores the day-wise number of total requests, successful and the failed ones. The view is then used in`too_many_errors()` function to derive the result.

## Running the project
This project is built in, and, thus, will run best in a virtual machine (VM), that in this case is an ***Ubuntu virtual box*** provided by and interfaced with ***Vagrant***.
Other dependencies include:
 - Python 2 or Python 3
 - PostgreSQL 9 or 10
 - psycopg 2 library

***Follow these instructions to get everything  that is required:***

 1. Install [VirtualBox](https://www.virtualbox.org/)
 2. Install [Vagrant](https://www.vagrantup.com/)
 3. Get the vagrant setup files from  [here](https://github.com/udacity/fullstack-nanodegree-vm)
 4. Dowload or clone these files in a separate directory on your desktop
 5. Download and unzip this [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
 6. Extract the ***newsdata.sql*** file from the downloaded archive and place it into the **vagrant** directory
 7. Download this [log analysis project](https://github.com/abdullah-22/Logs-Analysis-Project/archive/master.zip) or [clone](https://github.com/abdullah-22/Logs-Analysis-Project) it to your PC.
 8. Copy all the project files in a new directory within the previously created **vagrant**  directory

### *Setting up the VM*

 1. Set the ***vagrant virtual box***  by running `vagrant up` command in a shell or terminal within the vagrant directory.
	> It'll take some time to download and install the VM image. Hope everything goes fine here :/ or else follow [this](https://www.udacity.com/wiki/ud197/install-vagrant) article :)

2. Log into the VM with  `vagrant ssh`
3. When successfully in the VM, navigate to the **vagrant** directory by  `cd /vagrant`

### ***Creating the database***
- Run  `psql -d news -f newsdata.sql`  to create the ***news*** database.


### ***Creating the views***
Only one database view needs to be created in my solution i.e. ***daily_requests_stats*** view.
- This view can be created for temporary purpose by un-commenting the `create_view()`  function in  ***line no. 165*** of the **logs_analysis.py** file before running it **or**
- for permanent by directly running the following create view query in the **psql** console:
``` sql
CREATE OR REPLACE VIEW daily_request_stats AS
        WITH daily_hits AS (
            SELECT date(time) AS date, count(*) AS d_hits
            FROM log
            GROUP BY date
            ORDER BY date
        ), failed_hits AS (
	            SELECT date(time) AS date, count(*) AS f_hits
	            FROM log
	            WHERE status != '200 OK'
	            GROUP BY date
	            ORDER BY date
        )
        SELECT daily_hits.date, d_hits AS requests, d_hits - f_hits AS success, f_hits AS errors
        FROM daily_hits INNER JOIN failed_hits
        ON daily_hits.date = failed_hits.date;
```
Make sure to run the above command for creating the view when the terminal looks something like `news=>`. If not so, run `psql news` to connect to the database first.

### ***Executing the project***

Since both Python3 and Python2 are installed in the VM, either of the following commands will run the program

`python3 logs_analysis.py` or `python logs_analysis.py`

You can, now, see the results on your screen and also save them in the text file.

### ***When done***

- When done with the database, use `\q` to quit it.
- Use `exit` or `Ctrl-D` to logout of the VM.
- Run `vagrant halt` to shutdown the VM

*(stuck at someplace? found any error? or just want to connect? see below :))*
## Ping me @

**Abdullah A. Salman**

-   [Email](mailto:20abdullahahmadsalman@gmail.com)
-   [Github](https://github.com/abdullah-22)
-   [Linkedin](http://www.linkedin.com/in/abdullahasalman)
