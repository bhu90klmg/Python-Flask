import serial
from flask import Flask
        
app = Flask(__name__)

@app.route('/')
def main():
    with serial.Serial("COM3", 9600) as ser:
        line = ser.readline().decode("utf-8")
        print(line)
        
        try:
            a = line.replace(";\r\n", "").split(";")
            a = map(lambda x: x.split(","), a)

            return str(list(a))+"<script>location.reload()</script>"
        finally:
            pass
        
if __name__ == '__main__':
    app.run(debug=True)