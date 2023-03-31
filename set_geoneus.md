# Set geoneus

I added in the rewuirement `flask==2.1.3`, it was giving issues like `app_ctx: "AppContext" = LocalProxy(  # type: ignore[assignment]
TypeError: __init__() got an unexpected keyword argument 'unbound_message'`.

I am having problems with pytorch3d, might me that I had python 3.8, while they use 3.7, trying fresh new conda env with the 3.7.
Current error: `The following specifications were found to be incompatible with your system:

  - feature:/linux-64::__glibc==2.35=0
  - python=3.7 -> libgcc-ng[version='>=11.2.0'] -> __glibc[version='>=2.17']
  - pytorch3d -> torchvision[version='>=0.5'] -> __glibc[version='>=2.17,<3.0.a0']

Your installed version is: 2.35`.
