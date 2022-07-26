def cal(obj_in,key_in):
    key_list = key_in.split('/')
    for n in key_list:
        new_obj = obj_in[n]
        obj_in = new_obj
    return obj_in
