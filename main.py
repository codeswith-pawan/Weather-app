import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.city_label = QLabel("Enter City Name:")
        self.city_input = QLineEdit()
        self.get_weather_button = QPushButton("Get Weather")

        self.temperature_label = QLabel("")
        self.emoji_label = QLabel("")
        self.description_label = QLabel("")

        self.initUI()

        self.get_weather_button.clicked.connect(self.get_weather)

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

    def get_weather(self):
        city = self.city_input.text()
        api = "Enter Api(I hide My api)"

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

        try:
            data = requests.get(url).json()

            if data["cod"] == 200:
                temp = data["main"]["temp"]
                desc = data["weather"][0]["description"]

                self.temperature_label.setText(f"{temp} °C")
                self.description_label.setText(desc.capitalize())

                if "clear" in desc:
                    self.emoji_label.setText("☀️")
                elif "cloud" in desc:
                    self.emoji_label.setText("☁️")
                elif "rain" in desc:
                    self.emoji_label.setText("🌧️")
                else:
                    self.emoji_label.setText("🌡️")
            else:
                self.temperature_label.setText("City not found")
        except:
            self.temperature_label.setText("Error fetching data")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())