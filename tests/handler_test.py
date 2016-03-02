import libvirtplus.handler

if __name__ == "__main__" :
    print libvirtplus.handler.getAllContainersID()
    print libvirtplus.handler.getContainerInfoByID(2)
    print libvirtplus.handler.findContaienrIDByName("centos_65")
    print libvirtplus.handler.stopContainerByID(2)
    print libvirtplus.handler.startContainerByID(2)
    print libvirtplus.handler.checkID(2)