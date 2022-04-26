import sys
import api
import io
import folium  # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

"""
Folium in PyQt5
"""


class StatsCount(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Maps || CountryWise')
        self.window_width,self.window_height = 1200,900

        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # coordinate = (37.8199286, -122.4782551)
        m = folium.Map(location=[20, 0], tiles="OpenStreetMap", zoom_start=2)
                # save map data to data object
        folium.Marker(location=[20.593683, 78.962883],
                      popup=f"<h3>India</h3>    <br>    <strong>Total Cases: </strong>{api.response1[3]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[3]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[3]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>1,85,20,72,469",
                      tooltip="Click for more information").add_to(m)
        folium.Marker(location=[37.090240, -95.712891], popup=f"<h3>USA</h3>    <br>    <strong>Total Cases: </strong>{api.response1[2]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[2]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[2]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>1,30,10,72,590",
                      tooltip="Click for more information").add_to(m)
        folium.Marker(location=[61.524010, 105.318756], popup=f"<h3>Russia</h3>    <br>    <strong>Total Cases: </strong>{api.response1[8]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[8]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[8]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>95,90,12,672",
                      tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-25.274399, 133.775131], popup=f"<h3>Australia</h3>    <br>    <strong>Total Cases: </strong>{api.response1[23]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[23]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[23]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>1,29,23,71,480",
                      tooltip="Click for more information").add_to(m)
        folium.Marker(location=[56.130367, -106.346771], popup=f"<h3>Canada</h3>    <br>    <strong>Total Cases: </strong>{api.response1[34]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[34]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[34]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>45,17,12,484",
                      tooltip="Click for more information").add_to(m)
        folium.Marker(location=[35.000074, 104.999927], popup=f"<h3>China</h3>    <br>    <strong>Total Cases: </strong>{api.response1[29]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[29]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[29]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>1,10,18,49,836",
                      tooltip="Click for more information").add_to(m)
        folium.Marker(location=[36.5748441, 139.2394179], popup=f"<h3>Japan</h3>    <br>    <strong>Total Cases: </strong>{api.response1[17]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[17]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[17]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>39,10,95,178",
                      tooltip="Click for more information").add_to(m)
        folium.Marker(location=[-28.8166236, 24.991639], popup=f"<h3>South Africa</h3>    <br>    <strong>Total Cases: </strong>{api.response1[30]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[30]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[30]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>72,10,72,923",
                      tooltip="Click for more information").add_to(m)
        folium.Marker(location=[30.3308401, 71.247499], popup=f"<h3>Pakistan</h3>    <br>    <strong>Total Cases: </strong>{api.response1[48]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[48]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[48]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>18,34,15,225",
                      tooltip="Click for more information").add_to(m)
        
        data = io.BytesIO()
        m.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''
        QWidget {
            font-size: 35px;
        }
    ''')

    StatsCount = StatsCount()
    StatsCount.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')