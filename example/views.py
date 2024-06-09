# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>【0费用】Vercel+Django+Scrapy+DRF+SimepleUI+...</h1>
            <h2>这是一个使用Vercel搭建的Django项目，他有数据库，并且后续准备配合上Scrapy搭建一个某种信息采集的小应用.</h2>
            <p>现在的时间是：{ now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)