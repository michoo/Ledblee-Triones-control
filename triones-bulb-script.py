# Python script to set colour on lamp in front door...
import pexpect

print("---------------------")

DEVICE = "FF:FF:55:E0:98:AA"

# Run gatttool interactively.
print("Running gatttool...")
child = pexpect.spawn("gatttool -I")

# Connect to the device.
print("Connecting to"),
print(DEVICE),
child.sendline("connect {0}".format(DEVICE))
child.expect("Connection successful", timeout=5)
print("Connected!")

# write red
#command = "char-write-req 0x0007 56ff000000f0aa"
# Write green colour!
command = "char-write-req 0x0007 5600ff0000f0aa"
# write blue
#command = "char-write-req 0x0007 560000ff00f0aa"
# write white
#command = "char-write-req 0x0007 56000000fff0aa"
print(command)
child.sendline(command)

# no check about reception because here btle devive don't send return
print("done!")
