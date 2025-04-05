class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = None
        self.called_methods = {}

    def last_invoked_method(self):
        if self.last_invoked is not None:
            return self.last_invoked
        else:
            raise Exception("No Method Is Invoked")

    def count_of_calls(self, method_name):
        return self.called_methods.get(method_name,0)

    def was_called(self, method_name):
        return method_name in self.called_methods
    
    def __getattr__(self, name):
        if name not in self.called_methods:
            self.called_methods[name] = 0
        self.called_methods[name] += 1
        self.last_invoked = name
        method = getattr(self._obj, name)
        if callable(method):
            def wrapper(*args, **kwargs):
                return method(*args, **kwargs)
            return wrapper
        else:
            return method
 

   
class Radio():   
    def __init__(self):        
        self._channel = None        
        self.is_on = False        
        self.volume = 0        

    def get_channel(self):        
        return self._channel    

    def set_channel(self, value):        
        self._channel = value        

    def power(self):        
        self.is_on = not self.is_on




radio = Radio()
radio_proxy = Proxy(radio)
