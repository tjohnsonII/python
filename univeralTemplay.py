import os

class ColorPrint:
    # Define color codes
    COLORS = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }

    @staticmethod
    def print_color(text, color):
        # Check if the given color is valid
        if color not in ColorPrint.COLORS:
            raise ValueError(f"Invalid color '{color}'")

        # Print the text in the specified color
        print(f"{ColorPrint.COLORS[color]}{text}{ColorPrint.COLORS['reset']}")

def print_color(text, color):
    cp = ColorPrint()
    cp.print_color(text, color)

def main():
    # The main entry point of your program
    # Write your program logic here

    print("Start of Script")

    CURENTWORKINGDIRECTORY = os.getcwd()
    WHOISLOGIN = os.getlogin()
    CURRENTTIME = os.path.getctime(CURENTWORKINGDIRECTORY)
    CURRENTPROCESSID = os.getpid()
    CURRENTUSERNAME = os.getlogin()
    CURRENTUSERID = os.getuid()
    CURRENTGROUPID = os.getgid()

    CPUUSAGE = os.getloadavg()
    CPUNAME = os.uname()
    CPUFREQUENCY = os.cpu_count()
    CPUCORES = os.cpu_count()
    CPUARCHITECTURE = os.uname()

    RAMTOTAL = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    RAMUSED = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    RAMFREE = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')

    DISKTOTAL = os.statvfs("/")
    DISKUSED = os.statvfs("/")
    DISKFREE = os.statvfs("/")
    DISKPERCENTAGEUSED = os.statvfs("/")
    DISKPERCENTAGEFREE = os.statvfs("/")
    DISKPERCENTAGEUSED = os.statvfs("/")

    IPADDRESS = os.popen('ipconfig getifaddr en0').read().strip()
    MACADDRESS = os.popen('ipconfig getifaddr en0').read().strip()

    print(f"Current Working Directory: {CURENTWORKINGDIRECTORY}")
    print(f"Creation Time: {CURRENTTIME}")
    print(f"User Login: {WHOISLOGIN}")
    print(f"Process ID: {CURRENTPROCESSID}")
    print(f"Username: {CURRENTUSERNAME}")
    print(f"User ID: {CURRENTUSERID}")
    print(f"Group ID: {CURRENTGROUPID}")

    print(f"CPU Usage: {CPUUSAGE}")
    print(f"CPU Name: {CPUNAME}")
    print(f"CPU Frequency: {CPUFREQUENCY}")
    print(f"CPU Cores: {CPUCORES}")
    print(f"CPU Architecture: {CPUARCHITECTURE}")

    print(f"RAM Total: {RAMTOTAL}")
    print(f"RAM Used: {RAMUSED}")
    print(f"RAM Free: {RAMFREE}")

    print(f"Disk Total: {DISKTOTAL}")
    print(f"Disk Used: {DISKUSED}")


    print(f"IP Address: {IPADDRESS}")
    print(f"MAC Address: {MACADDRESS}")

    print("End of Script")
    
if __name__ == '__main__':
    main()
    