from app.schemas.sche_stock import StockCreateRequest
from pandas_datareader import data
import datetime, json

class StockService(object):
    __instance = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(request_data: StockCreateRequest):
        start_date = request_data.start_date
        # start_date = datetime.datetime.fromisoformat(start_date)
        # start_date = f"{start_date.year},{start_date.month},{start_date.day}"

        end_date = request_data.end_date

        start_date = datetime.datetime(2024,1,1)
        end_date = datetime.datetime(2024,3,1)
        # end_date = datetime.datetime.fromisoformat(end_date)
        # end_date = f"{end_date.year},{end_date.month},{end_date.day}"

        df = data.DataReader(name=request_data.sign, data_source="stooq", start=start_date, end=end_date)
        print(json(df))

        return json(df)
    