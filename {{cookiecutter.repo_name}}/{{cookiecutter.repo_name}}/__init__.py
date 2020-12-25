# Create __version__ attribute from setup.py information
import os.path

from pkg_resources import DistributionNotFound, get_distribution

from ._version import get_versions

__import__("pkg_resources").declare_namespace(__name__)

try:
    __version__ = get_versions()["version"]
except:
    __version__ = "--"
