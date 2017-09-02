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

