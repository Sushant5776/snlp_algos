def print_two_new_lines_before_and_after(func):
    def wrapper(*args, **kwargs):
        print("\n\n")
        result = func(*args, **kwargs)
        print("\n\n")

        return result
    
    return wrapper
        
    