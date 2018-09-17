orders = []
users = []


class Order:
    '''Class to process the order details'''
    '''Initializing the order id to zero'''
    order_id = 1
    def __init__(self,name,price,status="Pending"):
        '''Initialising the order details'''
        self.name=name
        self.price=price
        self.id=Order.order_id
        self.status=status
        '''incrementig the order id by one'''
        Order.order_id += 1

    def collect_order_details(self):
        '''collecting the order details and returning them in dictionary form'''
        return dict(
            id=self.id,
            name=self.name,
            price=self.price,
            status=self.status
        )
    def get_order_by_id(order_id):
        ''' Helper function to fetch specific order detail by id'''
        for order in orders:
            if order.get("id") == int(order_id):
                return order