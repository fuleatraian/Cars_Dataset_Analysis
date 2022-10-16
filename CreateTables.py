import mysql.connector

final_assess = mysql.connector.connect(user = 'root', database = 'marketing')
mycursor = final_assess.cursor()


mycursor.execute("""CREATE TABLE IF NOT EXISTS car (
                                                   Model_ID int(10) AUTO_INCREMENT PRIMARY KEY,    
                                                   Model_Year int(4),
                                                   Mfr_Name varchar(100),
                                                   Division varchar(100),
                                                   Carline varchar(50),
                                                   Drive_Desc varchar(100),
                                                   Carline_Class_Desc varchar(100),
                                                   Release_Date DATE
                                                   );
                """)


mycursor.execute("""CREATE TABLE IF NOT EXISTS engine (
                                                        Engine_ID int(10) AUTO_INCREMENT PRIMARY KEY,
                                                        Engine_Displacement FLOAT(3,1),
                                                        Cylinders int(2),
                                                        Air_Aspiration_Method varchar(50)
                                                    );
                """)



mycursor.execute("""CREATE TABLE IF NOT EXISTS transmission (
                                                                Trans_ID int(10) AUTO_INCREMENT PRIMARY KEY,
                                                                Transmission varchar(50),
                                                                Trans_Desc varchar(100),
                                                                Gears int(2)
                                                            );
                """)



mycursor.execute("""CREATE TABLE IF NOT EXISTS FE_facts (
                                                            ID int(10) AUTO_INCREMENT PRIMARY KEY,
                                                            Model_ID int(10),
                                                            Engine_ID int(10),
                                                            Trans_ID int(10),
                                                            City_FE int(10),
                                                            Highway_FE int(10),
                                                            Combined_FE int(10),
                                                            City_CO2 int(10),
                                                            Highway_CO2 int(10),
                                                            Combined_CO2 int(10),
                                                            FOREIGN KEY (Model_ID) REFERENCES car(Model_ID),
                                                            FOREIGN KEY (Engine_ID) REFERENCES engine(Engine_ID),
                                                            FOREIGN KEY (Trans_ID) REFERENCES transmission(Trans_ID)

                                                        ); 
                """)