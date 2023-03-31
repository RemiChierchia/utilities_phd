# Set geoneus

I added in the rewuirement `flask==2.1.3`, it was giving issues like `app_ctx: "AppContext" = LocalProxy(  # type: ignore[assignment]
TypeError: __init__() got an unexpected keyword argument 'unbound_message'`.

I am having problems with pytorch3d, might me that I had python 3.8, while they use 3.7, trying fresh new conda env with the 3.7.
