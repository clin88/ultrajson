"""What is this nonsense, you say?

Well, ujson doesn't compile with pypy. So in the event the compile fails, rather than
have the build fail and block us from using pypy, we install a dummy module that just proxies
the builtin json module. Wasn't this fun?"""

from json import *
