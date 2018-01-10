selected_dict = {}



def BULK_MAC(type):

   mac = raw_input("Input one mac address [xx:xx:xx:xx:xx:xx] per line, end with an extra newline: ")

   while mac is not "":
      selected_dict.update({mac:type})
      mac = raw_input("Input one mac address per line, end with an extra newline: ")

   print "\nHere are your entries: %s \nNext, login to netscripts(quantum) and paste in the lines below:\n" % (selected_dict)

   for key, val in selected_dict.iteritems():
      print "endpoint-update -m %s -s %s" % (key, val)



def MAIN():

   bulk_type = raw_input("\n\nWelcome!\nWhat would you like to do?\n\n1 - SPECIFY TYPE TO CREATE BULK ENTRIES\n2 - EXIT PROGRAM\n\n>")

   if bulk_type == "1":
      print "\nYou selected BULK ENTRY\n"
      bulk_type_vlan = raw_input("WHAT ZONE WILL THESE DEVICES LIVE IN?:\n1 - SECURITY\n2 - MANAGEMENT-NETWORK\n3 - DEVICE\n> ")

      if bulk_type_vlan == "1":
         print "SECURITY"
         BULK_MAC("SECURITY")

      if bulk_type_vlan == "2":
         print "MANAGEMENT-NETWORK"
         BULK_MAC("MANAGEMENT-NETWORK")

      if bulk_type_vlan == "3":
         print "DEVICE"
         BULK_MAC("DEVICE")

   if bulk_type == "2":
      print "You selected EXIT"

MAIN()







