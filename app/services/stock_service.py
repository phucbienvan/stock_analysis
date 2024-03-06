from app.schemas.sche_stock import StockCreateRequest

class StockService(object):
    __instance = None

    def __init__(self) -> None:
        pass

    @staticmethod
    def create(request_data: StockCreateRequest):
        print(1345)
        return 1234