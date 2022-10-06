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
        try:
            self.validate_keys()
            return True
        except:
            return False

    def validate_keys (self):
        for valid_key in self.valid_input.keys():
            if valid_key not in self.data.keys():
                self.errors[valid_key] = "missing key"
        if self.errors :
            raise Exception

    




        # self.data == valid_input

