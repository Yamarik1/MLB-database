Instructions on how to run, if needed:

    1. Clone or download the repo
    2. Since the Database is only used on the local machine, You must make
       a new database in MariaDB, named 'mlb'. (I did this through HeidiSQL)
    3. The .sql file is included in the repo. Load that in the database and
       run the query. This should recreate the database I had when I finished
       my project.
    4. In the project directory, create a file called 'connect.py' and 
       put the following code in it:
            import mariadb
            import sys

            def connectDatabase():
            try:
                conn = mariadb.connect(
                user='<user>',
                password='<password>',
                host='<host>',
                port='<port>',
                database='mlb',
            )
            except mariadb.Error as e:
                print(f"Error connecting to MariaDB Platform: {e}")
                sys.exit(1)

            return conn


        Where anything in <> should be replaced with the proper info.
        This is used to actually connect to the database, so if it is 
        missing, the code will fail to run. Depeding on how the code is
        tested, such as using an IDE, there may be some additional steps
        in order to connect to the database.
        
    5. Lastly, run driver.py to start the program. Type 'help' in the command 
       line once run to give a list of the commands you can use, and refer to 
       the database in order to do give proper data.
       
