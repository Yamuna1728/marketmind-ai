from pytrends.request import TrendReq

pytrends = TrendReq()

def get_trends(keyword):
    pytrends.build_payload([keyword])

    data = pytrends.interest_over_time()

    if data.empty:
        return []

    return data.reset_index().to_dict(orient="records")