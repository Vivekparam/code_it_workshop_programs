import rospy
import sys

from code_it_msgs.srv import ListPrograms
from code_it_msgs.msg import Program

if len(sys.argv) != 1:
    print "Usage:\n\t$ python copy_to_github.py"
    print "Note that you must manually setrobot before calling this script."
    sys.exit()

print "Waiting for list_programs to come online."
rospy.wait_for_service('/code_it/list_programs')
print "calling list_programs"
list_programs = rospy.ServiceProxy('/code_it/list_programs', ListPrograms)
try:
    resp1 = list_programs()
except rospy.ServiceException as exc:
    print("Service did not process request: " + str(exc))

# Program: 
# $ rosmsg show Program
#   [code_it_msgs/Program]:
#   string program_id
#   string name
#   string xml

for item in resp1.programs:
    print '\tWriting file', item.name
    new_name = item.name.strip()
    new_name = "programs/" + new_name.replace(" ", "_").lower()
    f = open(new_name, 'w')
    f.write(item.xml)
