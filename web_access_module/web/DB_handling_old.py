# Instantiate Connection
    try:
        conn = mariadb.connect(
            user="admin",
            password="Doska777",
            host="34.134.196.145",
            port=3306,
            database="testdb"
        )
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO testtable (session_code,rpi_name, creation_date) VALUES ({session_id}, '{rpi_name}', '{date_created}')")
        conn.commit()
        conn.close()



    except mariadb.Error as e:
        print(e)
        sys.exit(1)