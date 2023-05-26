from django.shortcuts import redirect

def outer_func(func):
    def inner_func(*args, **kwargs):
        request = args[0]
        if not 'username' in request.session:
            return redirect('login3')
        else:
            return func(*args, **kwargs)
    return inner_func