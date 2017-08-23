def print_results(file_name):
    file = open(file_name)
    for line in file:
        line = line.rstrip()
        words = line.split('|')

        type_of_mellon = words[1]
        count_of_mellons = words[0]
        total_amount = words[2]

        print "Delivered {} {}s for total of ${}".format(
            type_of_mellon, count_of_mellons, total_amount)
    file.close()
print 'Day 1'
print print_results("um-deliveries-20140519.txt")
print 'Day 2'
print print_results("um-deliveries-20140520.txt")
print 'Day 3'
print print_results("um-deliveries-20140521.txt")

# print "Day 2"
# the_file = open("um-deliveries-20140520.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()


# print "Day 3"
# the_file = open("um-deliveries-20140521.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print "Delivered {} {}s for total of ${}".format(
#         count, melon, amount)
# the_file.close()