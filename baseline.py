from jinja2 import Environment, FileSystemLoader
from .base import *
interface1 = interface(gi,1,1,ing)
interface2 = interface(gi,1,2,ing)
interface3 = interface(gi,1,3,ing)
interface4 = interface(gi,1,4,eg)
interface5 = interface(gi,1,5,eg)
interfaces=[interface1,interface2,interface3,interface4,interface5]
switch1=('R1',interfaces,'192.168.7.1','ansible','ansible','ansible',ing)
file_loader = FileSystemLoader('Templates')
ENV = Environment(loader=file_loader)
template = ENV.get_template('Baseline.j2')

print(template.render(Switch = switch1 ,Interfaces=switch1.interfaces))
