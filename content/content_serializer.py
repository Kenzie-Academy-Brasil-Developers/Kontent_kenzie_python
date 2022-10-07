from multiprocessing.sharedctypes import Value


class Content_serializer:
    valid_input = {
    "title": str,
    "module": str,
    "description":str,
    "students": int,
    "is_active": bool
    }

    def __init__ (self, **kwargs):
        self.data = kwargs
        self.errors = {}

    def is_valid(self):
        self.clean_data()
        try:
            self.validate_keys()
            self.check_value_keys()
            return True
        except:
            return False

    def validate_keys (self):
        for valid_key in self.valid_input.keys():
            if valid_key not in self.data.keys():
                self.errors[valid_key] = "missing key"
        if self.errors :
            raise Exception

    def check_value_keys(self):
        for key, value in self.valid_input.items():
            if type(self.data[key]) is not value:
                self.errors[key] = f"must be a {value.__name__}"

        if self.errors:
            raise Exception

    def clean_data(self):
        test = set(self.data.keys())
        for key in test :
            if key not in self.valid_input.keys():
                self.data.pop(key)


    




        # self.data == valid_input

