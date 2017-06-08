server = AdminConfig.getid("/Server:server1/")

# increase the Max Heap:
jvmid = AdminConfig.list("JavaVirtualMachine", server)
AdminConfig.show(jvmid).splitlines()
attrs = [["maximumHeapSize", 2048]]
AdminConfig.modify(jvmid, attrs)

# workaround IE bugs, see MNT-3525
services=AdminConfig.list("TransportChannelService",server)
channels=AdminConfig.list("HTTPInboundChannel",services)
opts=[]
opts.append(["validationExpression", ""])
opts.append(["name", "CookiesConfigureNoCache"])
opts.append(["description", "workaround IE6,7,8 bug see MNT-3525"])
opts.append(["value", "false"])
opts.append(["required", "false"])
for http in channels.split("\n"):
    hname=AdminConfig.showAttribute(http, 'name')
    if  hname=="HTTP_2":
        print ("Setting CookiesConfigureNoCache to false for", http)
        AdminConfig.create("Property",http,opts)

# saving config
AdminConfig.save()
