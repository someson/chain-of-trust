import os
from setuptools import setup

# Payload runs while pip is building the package — this is the point of the exercise
with open(os.path.expanduser("~/pwned.txt"), "w") as f:
    f.write("Infiltrat3d by utils_lib\n")

setup(
    name="utils_lib",
    version="0.0.1",
    packages=["utils_lib"],
    package_dir={"utils_lib": "."},
)
