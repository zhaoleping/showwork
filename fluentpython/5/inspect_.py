import inspect
from tag import tag

sig = inspect.signature(tag)
my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
bound_args = sig.bind(**my_tag)
print(bound_args)