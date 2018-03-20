import re
import sys
from sys import argv
import ipwhois
from ipwhois import IPWhois
from ipwhois.experimental import get_bulk_asn_whois
from pprint import pprint

log_file = open(sys.argv[1], 'r')
#regex = re.findall(r"<([\d]+\.[\d]+\.[\d]+\.[\d]+)(\/[\d]+)(\-\>)([\d]+\.[\d]+\.[\d]+\.[\d]+)(\/[\d]+)|(name=)([a-zA-Z]\w+\:[a-zA-z]\w+\:(.*?),)>" , log_file.read()) 
#unique = [[i[0], i[3], i[6]] for i in regex]

regex = re.findall(r"<(?P<attacker>(?:[0-9]{1,3}.){4})\/.*>(?P<victim>(?:[0-9]{1,3}.){4})(?:\/).*,\sname=(?P<sig>.*?)," , log_file.read()) 
attacker = [[i[0]]for i in regex]
victim = [[i[1]] for i in regex]
sig = [[i[2]] for i in regex]

def DNSlook(ip):
    for i in ip:
        get_bulk_asn_whois(addresses=i)

#def dbimport(attacker, victim, signature):
    
    

#unique = [[i[0], i[1], i[2]] for i in regex]
#print unique

DNSlook(attacker)

log_file.close()


    
        


