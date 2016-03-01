# -*- coding: UTF-8 -*-
import libvirt
import plugin

client = libvirt.open('qemu:///system')


def getAllContainersID():
    containers = client.listDomainsID()
    for index in range(len(containers)):
        containers[index] = plugin.int_to_str_id(containers[index])
    return containers


def getContainerInfoByID(str_id):
    id = plugin.str_to_int_id(str_id)
    dom = client.lookupByID(id)
    #cpu
    ret = dom.getCPUStats(1, 0)
    #memory
    ret.append(client.getMemoryStats(1, 0))
    #volume

    #net

    return ret


def createContainer(xml):
    dom = client.createXML(xml)
    return plugin.int_to_str_id(dom.ID())


def updateContainer(xml, str_id):
    deleteContainerByID(str_id)
    return createContainer(xml)



def deleteContainerByID(str_id):
    id = plugin.str_to_int_id(str_id)
    dom = client.lookupByID(id)
    dom.destroy()
    return "delete success"


def stopContainerByID(str_id):
    id = plugin.str_to_int_id(str_id)
    dom = client.lookupByID(id)
    dom.shutdown()
    return dom.state()


def startContainerByID(str_id):
    id = plugin.str_to_int_id(str_id)
    dom = client.lookupByID(id)
    dom.reboot()
    return dom.state()


def findContaienrIDByName(name):
    dom = client.lookupByName(name)
    return dom.ID()