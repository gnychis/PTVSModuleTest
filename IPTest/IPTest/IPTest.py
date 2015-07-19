import sys
import clr

clr.AddReference("IPModuleTest")

from IPModuleTest import IPModuleTestClass

p = IPModuleTestClass()
p.MyMethod()