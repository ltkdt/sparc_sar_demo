# Dự án nghiên cứu sụt lún đất của nhóm Brave New World

## Tóm tắt 
Đây là dự án của nhóm Brave New World tham dự cuộc thi NASA Space Apps Challenge. 

Đây là 1 trang Web xây bằng framework Django trong Python mà trong đó người dùng có thể  chọn 1 địa 
điểm trên map Việt Nam, sau đó hệ thống sẽ hiển thị một số nghiên cứu của nhóm em về độ lún đất và
sói mòn ở khu vực. Hiện tại đang có 3 khu vực là Cao Bằng, Hà Giang và Sơn La sử dụng ảnh vệ tinh SAR
ALOS PALSAR.

## Sử dụng
Hiện tại web đang sử dụng local host, nếu như dự án được hoàn thiện chỉnh chu sẽ host qua lên 1 
dịch vụ host phù hợp.

Người dùng có thể clone repo và khởi tạo môi trường Python phù hợp rồi chạy server trên localhost.
Tuy nhiên dự án có yêu cầu sử dụng cơ sở dữ liệu PostgreSQL với [PostGIS](https://postgis.net/) extension

```
pip freeze > requirementrequirements.txt
cd ./geoview
python manage.py runserver
```

## Một số ảnh về minh hoạ về trang web

![Giao diện chọn map](./gallery/UI1.png)
![Kết quả tìm kiếm](./gallery/UI2.png)
![Tra cứu và download chi tiết dữ liệu](./gallery/UI3.png)
