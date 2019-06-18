def Forecast(city):
  # -*- coding: utf-8 -*-
  import urllib
  import json
  # URL を書式 %s 付きで定義
  src = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'
  # % 表記を使って src の %s を指定する
  f = urllib.request.urlopen(src % (city))
  q = json.loads(f.read())
  f.close()
  print(q['title'])
  print(q['location']['city'])
  for i in range(3):
    print(q['forecasts'][i]['date'], ': ', q['forecasts'][i]['telop'])
  print('-----')
  print(q['description']['text'])
  
