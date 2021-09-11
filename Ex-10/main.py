# Function with Outputs

def format_name(f_name, l_name):
    name = f_name.title()
    last = l_name.title()
    return (f"{name} {last}")

final_format = format_name("sipoufo", "yvan")
print(final_format)