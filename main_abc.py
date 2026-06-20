from abc import ABC, abstractmethod

class ProductStructure(ABC):
    @abstractmethod
    def get_product_family(self):
        pass
    
    @abstractmethod
    def get_product_name(self):
        pass
    
    @abstractmethod
    def get_product_quantity(self):
        pass
    
    @abstractmethod
    def get_product_price(self):
        pass
    
    @abstractmethod
    def get_selling_price(self):
        pass
    
    
    @abstractmethod
    def get_product_sold(self):
        pass
    
    @abstractmethod
    def get_product_unit(self):
        pass
    
    @abstractmethod
    def add_product(self):
        pass
    @abstractmethod
    def sell_product(self):
        pass