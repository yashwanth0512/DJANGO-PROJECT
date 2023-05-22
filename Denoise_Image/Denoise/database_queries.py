from Denoise.models import Hello

def get_hello_objects():
    hello_objects = Hello.objects.all()
    return hello_objects
