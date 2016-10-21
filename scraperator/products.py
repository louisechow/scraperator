import json


class Product:
    """
    Representation of a product sold by Sainsbury

    Attributes:
        title (str): Title of the product
        size (str): Size of the product page in kb
        unit_price (float): The price per unit of the product
        description (str): The description of the product
    """
    def __init__(self, title, size, unit_price, description):
        self.title = title
        self.size = size
        self.unit_price = unit_price
        self.description = description

    def convert_to_json(self):
        """
        Converts the product instance into json
        Note: json.loads must be used to follow JSON standards of using double quotes

        :return (dict): JSON representation of the product
        """
        return json.loads(json.dumps(self.__dict__))
