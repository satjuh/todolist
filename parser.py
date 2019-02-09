from optparse import OptionParser

def parse():
    parser = OptionParser(usage="Used to manage a simple TODO list application %prog [options]")
    parser.add_option("-l", "--list", help= "Print available tasks", action="count") 
    parser.add_option("-d", "--dotask", help= "Complete specified task [id]", action="count")
    parser.add_option("-v", "--verbose", help="Mainly included from debuggin reasons", action="count")
    parser.add_option("-a", "--addtask",nargs=3, help="Add task to a course [course name, task, deadline(dd/mm/yyyy,dd-mm-yyyy or dd.mm.yyyy)]")
    parser.add_option("-c", "--addcourse", help= "Add a new course to todolist")
    (options, args) = parser.parse_args()
    return options, args

