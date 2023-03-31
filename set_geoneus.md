# Set geoneus

I added in the rewuirement `flask==2.1.3`, it was giving issues like `app_ctx: "AppContext" = LocalProxy(  # type: ignore[assignment]
TypeError: __init__() got an unexpected keyword argument 'unbound_message'`.

I am having problems with pytorch3d, might me that I had python 3.8, while they use 3.7, trying fresh new conda env with the 3.7.
Current errors: 
```
UnsatisfiableError: The following specifications were found
to be incompatible with the existing python installation in your environment:

Specifications:

  - pytorch3d -> python[version='>=2.7,<2.8.0a0|>=3.11,<3.12.0a0|>=3.5,<3.6.0a0']

Your python: python=3.7

The following specifications were found to be incompatible with your system:

  - feature:/linux-64::__glibc==2.35=0
  - python=3.7 -> libgcc-ng[version='>=11.2.0'] -> __glibc[version='>=2.17']
  - pytorch3d -> torchvision[version='>=0.5'] -> __glibc[version='>=2.17,<3.0.a0']

Your installed version is: 2.35
```
might be because of this? -> https://stackoverflow.com/questions/73337791/python-conda-determining-what-python-version-to-install
