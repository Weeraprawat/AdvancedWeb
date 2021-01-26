import psycopg2
try:
  connection = psycoph2.connect(user="webadmin",
                                password="NHXeeo30859",
                                host="node8566-advweb-08.app.ruk-com.cloud",
                                port="11103",
                                database="CloudDB")

  cursor = connection.cursor()
  print(connection.get_dsn_parameter(), "\n")

  cursor.execute("SELECT verison():")
  record = cursor.fetchone()
  print("You are connected to - ", record, "\n")

except(Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if(connection):
      cursor.close()
      connection.close()
      print("PostgreSQL connection is close")