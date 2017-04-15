import abi
import sys


__m = abi.load("script.module.netifaces", "netifaces")
import sys
sys.modules[__name__] = __m
