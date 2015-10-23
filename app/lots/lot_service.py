import ferris3 as f3
from app.lots.lot_model import Lot

LotMessage = f3.model_message(Lot)
LotListMessage = f3.list_message(LotMessage)

@f3.auto_service
class LotService(f3.Service):
    list = f3.hvild.list(Lot)
    paginated_list = f3.hvild.paginated_list(Lot)
    get = f3.hvild.get(Lot)
    delete = f3.hvild.delete(Lot)
    insert = f3.hvild.insert(Lot)
    update = f3.hvild.update(Lot)

    @f3.auto_method(returns=LotListMessage, name="all")
    def list_all(self, request):
        '''
        return list of all posts as a LotMessage
        '''
        lots = Lot.query()
        if not posts:
            raise f3.NotFoundException()
        list_message = f3.messages.serialize_list(LotListMessage, lots)
        return list_message


    @f3.auto_method(returns=LotMessage, name="get_by_title")
    def get_by_address(self, request, address=(str,)):
        query = Lot.query(Lot.address==address)
        lot = query.get()
        if not lot:
            raise f3.NotFoundException()
        if not post.key.kind() == 'Lot':
            raise f3.InvalidRequestException()
        message = f3.messages.serialize(LotMessage, lot)
        return message
