# Code demo dự án Nasa

## Thư viện
Dùng pip install để tải
asf_search
django
folium
geopandas

## Các thành phần đã có trong repo

- Backend cơ bản cho web, để chạy thử server, phải kích hoạt môi trường ảo Python trươc (venv).
Web mới show một đoạn map mẫu và mình click vào thì backend gửi tọa độ

```
cd ./geoview
python manage.py migrate
python manage.py runserver
```
- File mẫu `asf_test.py` gọi API của ASF search dựa trên các khu vực địa lí dưới dạng tọa độ (Area of Interest), hiện tại thì chưa xác định cụ thể khu vục sông

- File `cmd.csh` dự kiến là chạy các tool command line của GMTSar hoặc SNAP để xử lí InSAR

- Class `LatLngPopup` trong `features.py` của Folium được sửa lại để làm cho nó gửi đc về backend 
