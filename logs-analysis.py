#!/usr/bin/env python3

'''Log Analysis Project for Full Stack Nanodegree by Udacity'''

import psycopg2


# To make Connection with the news database and return the cursor
def connect_to_db():
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
    except ConnectionError:
        print("Failed to connect to the database.")
        return None
    else:
        return cursor
# END connect_to_db


# To query top three articles from the database
def top_articles(db_cursor, f):
    query = '''
        SELECT articles.title, count(*) AS views
        FROM articles INNER JOIN log
        ON log.path = '/article/' || articles.slug
        WHERE log.status = '200 OK'
        GROUP BY articles.title
        ORDER BY views DESC
        LIMIT 3;
    '''
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('\n\n Three most popular articles of all time')
    print('=====================================================')
    for result in results:
        print(
            '\n "{title}" -- {views} views'
            .format(title=result[0], views=result[1])
            )
    print('\n')

    prompt = input("Do you want to save these results in text file (y/n): ")
    if prompt == 'y':
        f.write('\n Three most popular articles of all time\n')
        f.write('=====================================================')

        for result in results:
            f.write(
                '\n "{title}" -- {views} views'
                .format(title=result[0], views=result[1])
                )
        f.write('\n')
    return
# END top_articles()


# To query top three authors from the database
def top_authors(db_cursor, f):
    query = '''
        SELECT authors.name, count(*) AS views
        FROM articles, authors, log
        WHERE log.path = '/article/' || articles.slug
        AND articles.author = authors.id
        GROUP BY authors.name
        ORDER BY count(*) DESC;
    '''
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('\n\n Most popular authors of all time')
    print('============================================')
    for result in results:
        print(
            '\n "{name}" -- {views} views'
            .format(name=result[0], views=result[1])
            )
    print('\n')

    prompt = input("Do you want to save these results in text file (y/n): ")
    if prompt == 'y':
        f.write('\n\n Most popular authors of all time\n')
        f.write('============================================')

        for result in results:
            f.write(
                '\n "{name}" -- {views} views'
                .format(name=result[0], views=result[1])
                )
        f.write('\n')
    return
# END top_authors()


# To query the day with percentage error > 1
def too_many_errors(db_cursor, f):
    query = '''
        WITH error_rate AS (
        SELECT date,
        round((errors::float / requests::float * 100.00)::numeric, 2)
        AS error_prc
        FROM daily_request_stats)
        SELECT date, error_prc FROM error_rate WHERE error_prc > 1;
    '''
    db_cursor.execute(query)
    results = db_cursor.fetchall()

    print('\n\n Day with more than 1 perc. failed requests')
    print('=============================================')
    for result in results:
        print(
            '\n "{date}" -- {error_prc} views'
            .format(date=result[0], error_prc=result[1])
            )
    print('\n')

    prompt = input("Do you want to save these results in text file (y/n): ")
    if prompt == 'y':
        f.write('\n\n Day with more than 1 perc. failed requests\n')
        f.write('=============================================')

        for result in results:
            f.write(
                '\n "{date}" -- {error_prc} views'
                .format(date=result[0], error_prc=result[1])
                )
        f.write('\n')
    return
# END too_many_errors()


# To create the view daily_request_stats
def create_view(db_cursor):
    query = '''
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
        SELECT daily_hits.date, d_hits AS requests,
        d_hits - f_hits AS success, f_hits AS errors
        FROM daily_hits INNER JOIN failed_hits
        ON daily_hits.date = failed_hits.date;
    '''
    db_cursor.execute(query)
    print('View created !!!')


if __name__ == "__main__":

    file = open('results.txt', 'w+')
    cursor = connect_to_db()
    if cursor:
        # uncomment the line below to create the view
        # required for getting the HTTP requests error report
        # create_view(cursor)
        top_articles(cursor, file)
        top_authors(cursor, file)
        too_many_errors(cursor, file)
        cursor.close()
    file.close()
