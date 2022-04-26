import sys
import api
import io
import folium  # pip install folium
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView  # pip install PyQtWebEngine

"""
Folium in PyQt5
"""


class StatsCount2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Maps || Statewise')
        self.window_width,self.window_height = 1200,900

        self.setMinimumSize(self.window_width, self.window_height)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # coordinate = (37.8199286, -122.4782551)
        m = folium.Map(location=[20.593683,78.962883], tiles="OpenStreetMap", zoom_start=5)
        # save map data to data object
        folium.Marker(location=[20.593683,78.962883],popup=f"<h3>India</h3>    <br>    <strong>Total Cases: </strong>{api.response1[3]['TotalCases']} <br> <strong>Active Cases: </strong>{api.response1[3]['ActiveCases']} <br>    <strong>Total Deaths: </strong>{api.response1[3]['TotalDeaths']}  <br>  <strong>Total Vaccinations: </strong>1,85,20,72,469",tooltip="Click for more information").add_to(m)
        folium.Marker(location=[19.751480,75.713890],popup="<h3>Maharashtra</h3>    <br>    <strong>Total Cases: </strong>763428732 <br> <strong>Active Cases: </strong>87346 <br>    <strong>Total Deaths: </strong>37463784  <br>  <strong>Total Vaccinations: </strong>11,00,26,925",tooltip="Click for more information").add_to(m)
        folium.Marker(location=[22.572645,88.363892],popup="<h3>Kolkata</h3>    <br>    <strong>Total Cases: </strong>3652764372 <br> <strong>Active Cases: </strong>6337 <br>    <strong>Total Deaths: </strong>2837  <br>  <strong>Total Vaccinations: </strong>6,98,26,975",tooltip="Click for more information").add_to(m)
        folium.Marker(location=[28.704060,77.102493],popup="<h3>Delhi</h3>    <br>    <strong>Total Cases: </strong>432684332 <br> <strong>Active Cases: </strong>347 <br>    <strong>Total Deaths: </strong>73564  <br>  <strong>Total Vaccinations: </strong>9,12,92,184",tooltip="Click for more information").add_to(m)
        folium.Marker(location=[33.778175,76.576172],popup="<h3>Jammu & Kashmir</h3>    <br>    <strong>Total Cases: </strong>3729 <br> <strong>Active Cases: </strong>375438267 <br>    <strong>Total Deaths: </strong>6232764372  <br>  <strong>Total Vaccinations: </strong>2,19,72,917",tooltip="Click for more information").add_to(m)
        folium.Marker(location=[22.3850051,71.745261],popup="<h3>Gujrat          </h3>    <br>    <strong>Total Cases: </strong>12734832 <br> <strong>Active Cases: </strong>23243 <br>    <strong>Total Deaths: </strong>23434  <br>  <strong>Total Vaccinations: </strong>7,00,96,172",tooltip="Click for more information").add_to(m)
        folium.Marker(location=[13.082680,80.270721],popup="<h3>Chennai</h3>    <br>    <strong>Total Cases: </strong>12734832 <br> <strong>Active Cases: </strong>23243 <br>    <strong>Total Deaths: </strong>23434  <br>  <strong>Total Vaccinations: </strong>8,12,42,749",tooltip="Click for more information").add_to(m)

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

    StatsCount2 = StatsCount2()
    StatsCount2.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')