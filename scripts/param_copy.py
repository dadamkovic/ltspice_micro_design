pyperclip_missing = False
try:
    import pyperclip
except  Exception:
    pyperclip_missing = True
    print("pyperclip not present, result will not be copied into clipboard")
import argparse as arg

#takes a float number, removes leading zeros and adds spice compatible suffix
def suffix_gen(number):
    suffices = ['m','u','n','p','f']
    idx = 0
    for i in range(3,16,3):
        if(number > 10**(-i) or i==15):
            new_number = number * 10**(i)
            output = "{:.2f}{}".format(new_number, suffices[idx])
            return output
        idx += 1


parser = arg.ArgumentParser("Simple tool to calculate MOS AD/AS/PD/PS parameters.")
parser.add_argument('--Hdif',dest='h', type=float, help="Effective height [nm] (100nm - 180nm)")
parser.add_argument('--Weff',dest='w', type=float, help="Effective width [nm]")
parser.add_argument('--Leff',dest='l', type=float, default=45, help="Effective length [nm]")
args = parser.parse_args()

if(args.h == None):
    args.h = float(input("Effective height [nm]: "))
if(args.w == None):
    args.w = float(input("Effective width [nm]: "))

AS = suffix_gen(2*args.h*args.w*10**(-18))
AD = suffix_gen(2*args.h*args.w*10**(-18))
PS = suffix_gen(4*args.h*10**(-9)+2*args.w*10**(-9))
PD = suffix_gen(4*args.h*10**(-9)+2*args.w*10**(-9))

setup_string = f"l={args.l}n w={args.w}n as={AS} ad={AD} ps={PS} pd={PD}"
print(setup_string)
if not pyperclip_missing:
    pyperclip.copy(setup_string)
    print("Result copied to clipboard")



