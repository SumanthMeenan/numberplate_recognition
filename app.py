from flask import Flask, render_template, request
import number-plate

app = Flask(__name__)

import mysql.connector

@app.route('/data_transfer', methods=['GET', 'POST'])
def data_transfer(text):

    
    db_instance = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "pancard_data"
    )

    db_connector = db_instance.cursor()

    if request.method == "POST":

        data  = text
        db_connector.execute(" insert into pancard_data (Data) values(%s)", (data))
        db_instance.commit()
        db_connector.close()

    print("Data updated in sql") 


if __name__ == '__main__':
    app.run(debug=True)