from optparse import OptionParser

def parser():
    parser = OptionParser(usage="Used to manage a simple TODO list application %prog [options]")
    parser.add_option("-l", "--list", help= "Print avalable tasks", action="count", default=True)
    parser.add_option("-c", "--complete", help= "Complete specified task [number]", action="count")
    parser.add_option("-v", "--verbose", help="Mainly included from debuggin reasons", action="count")
    parser.add_option("-a", "--add", help="Add task to a file", action="count")
    (options, args) = parser.parse_args()
    return options, args

