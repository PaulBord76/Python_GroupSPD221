from collections import UserDict

class CustomDict(UserDict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.history = []

    def __setitem__(self, key, value):
        if key not in self.history:
            if len(self.history) >= 10:
                self.history.pop(0)
            self.history.append(key)
        super().__setitem__(key, value)

    def get_history(self):
        return self.history


custom_dict = CustomDict()

custom_dict['One'] = '1'
custom_dict['Two'] = '2'
custom_dict['Three'] = '3'
custom_dict['Four'] = '4'
custom_dict['Five'] = '5'
custom_dict['Six'] = '6'
custom_dict['Seven'] = '7'
custom_dict['Eight'] = '8'
custom_dict['Nine'] = '9'
custom_dict['Ten'] = '10'
custom_dict['Eleven'] = '11'

print(custom_dict.get_history())  # ['key2', 'key3', 'key4', 'key5', 'key6', 'key7', 'key8', 'key9', 'key10', 'key11']
