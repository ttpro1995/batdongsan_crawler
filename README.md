THe spider will crawl on: https://batdongsan.com.vn/

Dependency:

```
pip install scrapy
pip install scrapy-random-useragent
```

Start:<br>
Open terminal and run following command

```
scrapy crawl bds -o output.jl
```

setting.py

```
FEED_EXPORT_ENCODING = 'utf-8' # make output in json become human readable utf-8
CLOSESPIDER_PAGECOUNT = 10 # limit the number of page crawl
```

Sample output (JSON lines format)
```
{"body": "Ra mắt 18 lô đẹp nhất boutique shophose dự án Sun Premier Village Hạ Long Bay.+ + Vị trí trung tâm Bãi Cháy, View trực diện vịnh Hạ Long, kỳ quan thiên nhiên thế giới. + + Phù hợp kinh doanh khách sạn mini, nhà hàng, café tại vị trí ngay đầu dự án lối đi Đảo Rều, nơi bất kỳ du khách nào khi tới đều ...", "city": "\r\nHạ Long, Quảng Ninh\r\n", "title": "Cơ hội đầu tư xuất sắc - 18 lô đẹp nhất boutique shophouse dự án Premier Village Hạ Long Bay", "price": "Thỏa thuận", "area": "300 m²", "date": "02/09/2017"}
{"body": "Sở hữu ngay căn hộ Xuân Mai Complex, chỉ với 800 triệu/căn, full nội thất hoàn thiện, giá gốc trực tiếp chủ đầu tư.\r \r Liên hệ phòng KD CĐT: 098.191.5881 - 0919.746.959.\r \r - Chiết khấu trực tiếp 3% và giá gốc HĐMB.\r - Hỗ trợ lãi suất 0% trong vòng 1 năm đến khi nhận nhà.\r - Hỗ trợ vay vốn 70% tổng ...", "city": "\r\nHà Đông, Hà Nội\r\n", "title": "Xuân Mai Complex Dương Nội sở hữu căn hộ chỉ từ 800 triệu,LS 0% nhận ngay lộc vàng.LH: 098.191.5881", "price": "17 triệu/m²", "area": "47 m²", "date": "02/09/2017"}
{"body": "Bán nhà phố liền kề đường xe tải gần chợ Hưng Long, gần trạm y tế xã Hưng Long, gần chợ Bình Điền, giao thông thuận tiện đến bến xe Miền Tây, quận 6,7,8..... Nhà mới xây xong đẹp kiên cố, diện tích từ 40m2 - 70m2 (4mx8m; 4mx12m; 3.7mx10m; 3.8mx11m. 3.5mx16m...), gồm 1 trệt, 1 lầu, 2 phòng ngủ, 1 phò...", "city": "\r\nBình Chánh, Hồ Chí Minh\r\n", "title": "Bán nhà phố liền kề chợ Hưng Long, sổ hồng chính chủ bán giá từ 395 triệu đến 690 triệu", "price": "395 triệu", "area": "40 m²", "date": "02/09/2017"}
{"body": "- Mở bán phố thương mại thượng lưu đẳng cấp giá chỉ từ 336 triệu, hỗ trợ trả trước 50% góp 30 tháng không lãi suất.\r - Đô thị sở hữu KDL sinh thái rộng 15ha kênh DL sinh thái dài 1,7km đầu tiên phía Tây Bắc TP. HCM.\r - Diện tích đa dạng; 4x16m, 4x18m, 5x20m, 8x20m, 10x20m v. V.\r - Thanh toán linh ho...", "city": "\r\nĐức Hòa, Long An\r\n", "title": "- Cát Tường Phú Sinh mở bán khu vipland trả góp dài hạn không % LS. LH 0987583743 - 0936177594 Đạt", "price": "336 triệu", "area": "100 m²", "date": "02/09/2017"}
```
