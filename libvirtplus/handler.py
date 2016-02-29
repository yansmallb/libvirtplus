# -*- coding: UTF-8 -*-
import libvirt

client = libvirt.open('qemu:///system')


def getAllContainersID():
    containers = client.listDomainsID()
    return containers


def getContainerInfoByID(id):
    dom = client.lookupByID(id)
    ret = dom.getCPUStats(1, 0)
    ret.append(client.getMemoryStats())
    ret.append(dom.info())
    return ret


def createContainer(xml):
    dom = client.createXML(xml)
    return dom.ID()


def findContaienrIDByName(name):
    dom = client.lookupByName(name)
    return dom.ID()


def deleteContainerByID(id):
    dom = client.lookupByID(id)
    dom.destroy()
    return


def stopContainerByID(id):
    dom = client.lookupByID(id)
    dom.shutdown()
    return


def startContainerByID(id):
    dom = client.lookupByID(id)
    dom.autostart()
    return dom.state()
