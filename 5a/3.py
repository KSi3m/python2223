

def gen_dec(scale):
    def scale_type(old_fun):
        def new_fun(t):
            if scale.lower() == "kelvin":
                return old_fun(t)
            elif scale.lower() == "celsjusz":
                return old_fun(t) - 273;
            elif scale.lower() == "fahrenheit":
                return 1.8*(old_fun(t)-273) + 32
            else:
                return "Nieznana skala"
        return new_fun
    return scale_type
   



@gen_dec("celsjusz")
def get_temp(t):
    return t
    
print(get_temp(273))
    
@gen_dec("kelvin")
def get_temp(t):
    return t
    
print(get_temp(273))

@gen_dec("fahrenheit")
def get_temp(t):
    return t
    
print(get_temp(273))
    
