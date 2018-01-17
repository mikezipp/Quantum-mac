from datetime import datetime
import csv


selected_dict = {}

security_list = []
management_list = []
device_list = []
wap_list = []



def EXPORT_TO_QUANTUM(zone):

   if zone == security_list:
      print "\n\nlogin to netscripts and paste in the lines below for Security Additions:"
      for mac in security_list:
         print "endpoint-update -m %s -s SECURITY" % (mac)

   if zone == management_list:
      print "\n\nlogin to netscripts and paste in the lines below for Management Additions:"
      for mac in management_list:
         print "endpoint-update -m %s -s MANAGEMENT-NETWORK" % (mac)

   if zone == device_list:
      print "\n\nlogin to netscripts and paste in the lines below for Device Additions:"
      for mac in device_list:
         print "endpoint-update -m %s -s DEVICE" % (mac)

   if zone == wap_list:
      print "\n\nlogin to netscripts and paste in the lines below for WAP Additions:"
      for mac in wap_list:
         print "endpoint-update -m %s -s WAP" % (mac)



def IMPORT_CSV():

   with open("mac-address.tsv") as tsvfile:
      reader = csv.reader(tsvfile, delimiter='\t')
      for row in reader:
         security_list.append(row[0])
         management_list.append(row[1])
         device_list.append(row[2])
         wap_list.append(row[3])

   #CLEAN LISTS
   for mac in security_list:
      if mac == "SECURITY":
         security_list.remove(mac)
      if mac == '':
         security_list.remove(mac)
   if len(security_list) > 1:
      EXPORT_TO_QUANTUM(security_list)

   for mac in management_list:
      if mac == "MANAGEMENT-NETWORK":
         management_list.remove(mac)
      if mac == '':
         management_list.remove(mac)
   if len(management_list) > 1:
      EXPORT_TO_QUANTUM(management_list)

   for mac in device_list:
      if mac == "DEVICE":
         device_list.remove(mac)
      if mac == '':
         device_list.remove(mac)
   if len(device_list) > 1:
      EXPORT_TO_QUANTUM(device_list)

   for mac in wap_list:
      if mac == "WAP":
         wap_list.remove(mac)
      if mac == '':
         wap_list.remove(mac)
   if len(device_list) > 1:
      EXPORT_TO_QUANTUM(wap_list)

IMPORT_CSV()


