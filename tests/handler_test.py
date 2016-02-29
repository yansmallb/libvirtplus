import libvirtplus.handler

if __name__ == "__main__" :
    print libvirtplus.handler.getAllContainersID()
    print libvirtplus.handler.getContainerInfoByID(2)
