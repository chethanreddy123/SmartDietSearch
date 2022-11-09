for i in range(100):
    from pytrends.request import TrendReq

    pytrends = TrendReq(hl='en-US', tz=360) 

    kw_list = ["machi"] # list of keywords to get data 

    pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y')

    data = pytrends.interest_over_time() 
    data = data.reset_index() 

    print(data)