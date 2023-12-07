def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
    
def int_input(str, force = True):
    inp = input(str)
    if (is_integer(inp)):
        return int(inp)
    conditional_string = ', ulangi' if force else ""
    print(f"Input harus berupa angka. Gagal membaca input{conditional_string}. \n\n")
    return int_input(str) if force else None