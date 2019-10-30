import ipinfo
import shodan
import time
import mysql.connector
from mysql.connector import Error
from datetime import date
import datetime

import subprocess
th="Thorium >> "
space="           "
SHODAN_API_KEY ="u2H4vYwU7tEW1w4azEvdcA7oZ7uPnC4k"
api = shodan.Shodan(SHODAN_API_KEY)
print("     ##########  ##    ##  ########  #######  ########   ##      ##  ##      ##        Date:",date.today())
print("         ##      ##    ##  ##    ##  ##   ###     ##     ##      ##  ####  ####        Day :",datetime.datetime.now().strftime("%A"))
print("         ##      ########  ##    ##  ########     ##     ##      ##  ## #### ##        Credit:Jemis Goti")
print("         ##      ##    ##  ##    ##  ##    ##     ##     ##      ##  ##      ##               Parth Karkar")
print("         ##      ##    ##  ########  ##    ##  ########  ##########  ##      ##               Raj Dalsaniya")
print()
print()
print()

try:
    connection = mysql.connector.connect(host="remotemysql.com",
                                         user="vh783D3KkC",
                                         passwd="IAqmQLd4aZ",
                                         database="vh783D3KkC")
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print(th + "Connected to Server successfuly with version on ", db_Info)
        cursor = connection.cursor()
        print(th + "have you registered for thorium!!! for yes press Y and for No press N..")
        lgns = input("Thorium >> ")
        if (lgns.lower() == 'y'):
            userid = input("Thorium >> Userid:")
            password = input("Thorium >> Password:")
            sql = "SELECT * FROM thorium WHERE userid ='" + userid + "'AND pass ='" + password + "' LIMIT 1"

            cursor.execute(sql)
            myresult = cursor.fetchall()
            if myresult:
                print(th + "Hello " + str(myresult[0][0]) + " You have successfuly login ")
                lgns = bool(1)
                ans = 'y'
                while ans == 'y':
                    access_token = '951058166d6e36'
                    handler = ipinfo.getHandler(access_token)
                    ip = input(th + "ip:")
                    details = handler.getDetails(ip)
                    if details.org:
                        print(th + "Organization::" + details.org)
                    else:
                        pass
                    if details.hostname:
                        print(th + "Host:" + details.hostname)

                    else:
                        pass
                    if details.country_name:
                        print(th + "Country:" + details.country_name)

                    else:
                        pass
                    if details.org:
                        print(th + "Location:" + details.loc)

                    else:
                        pass
                    if details.region:
                        print(th + "Region:" + details.region)

                    else:
                        pass
                    if details.city:
                        print(th + "City:" + details.city)

                    else:
                        pass
                    if details.postal:
                        print(th + "Postal:" + details.postal)

                    else:
                        pass
                    if details.timezone:
                        print(th + "Timezone:" + details.timezone)

                    else:
                        pass
                    tr=input(th+"Do you want to trace route:")
                    if(tr.lower()=='y'):
                        subprocess.call('tracert ' + ip, shell=True)
                    tr = input(th + "Do you want to save route:")
                    if (tr.lower() == 'y'):
                        subprocess.call( "tracert["+ip+"] > C:\\Users\\admin\\Desktop\\Thorium\\file.txt", shell=True)


                    ans = input(th+"Do you want to continue?yes='y',no='n' \n"+th)
            else:
                print("you will exited shortly")
        elif (lgns.lower() == 'n'):
            userid = input(th + "Userid:")
            password = input(th + "Password:")

            sql="INSERT INTO thorium (name,email,userid,pass) VALUES (DEFAULT ,DEFAULT,'"+userid+"','"+password+"')";
            cursor.execute(sql)
            connection.commit()
            print(th + "You have successfuly registered ")
            userid = input("Thorium >> Userid:")
            password = input("Thorium >> Password:")
            sql = "SELECT * FROM thorium WHERE userid ='" + userid + "'AND pass ='" + password + "' LIMIT 1"

            cursor.execute(sql)
            myresult = cursor.fetchall()
            if myresult:
                print(th + "Hello " + str(myresult[0][0]) + " You have successfuly login ")
                lgns = bool(1)
                ans = 'y'
                while ans == 'y':
                    access_token = '951058166d6e36'
                    handler = ipinfo.getHandler(access_token)
                    ip = input(th + "ip:")
                    details = handler.getDetails(ip)
                    if details.org:
                        print(th + "Organization::" + details.org)
                    else:
                        pass
                    if details.hostname:
                        print(th + "Host:" + details.hostname)

                    else:
                        pass
                    if details.country_name:
                        print(th + "Country:" + details.country_name)

                    else:
                        pass
                    if details.org:
                        print(th + "Location:" + details.loc)

                    else:
                        pass
                    if details.region:
                        print(th + "Region:" + details.region)

                    else:
                        pass
                    if details.city:
                        print(th + "City:" + details.city)

                    else:
                        pass
                    if details.postal:
                        print(th + "Postal:" + details.postal)

                    else:
                        pass
                    if details.timezone:
                        print(th + "Timezone:" + details.timezone)

                    else:
                        pass
                    ans = input(th + "Do you want to continue?yes='y',no='n' \n" + th)
            else:
                print("you will exited shortly")

except Error as e:
    print(th + "Error while connecting to server", e)
finally:
    # closing database connection.
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print(th + "Server closing....")
time.sleep(2)

