from app.schemas.sche_stock import StockCreateRequest
from pandas_datareader import data
import datetime, json

class StockService(object):
    __instance = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(request_data: StockCreateRequest):
        df = data.DataReader(
            name=request_data.sign,
            data_source="stooq",
            start=request_data.start_date,
            end=request_data.end_date
        )

        result_list = df.reset_index().to_dict(orient='records')

        return result_list
    