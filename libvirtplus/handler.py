# -*- coding: UTF-8 -*-
import libvirt
import plugin
from log import logger

client = libvirt.open('qemu:///system')


def checkID(id, common):
    containers = client.listDomainsID()
    if id not in containers:
        logger.error("{common} {id} error! Don't have dom that id is {id}!!".format(common=common, id=id))
    else:
        logger.info("{common} {id} success".format(common=common, id=id))
    return


def getAllContainersID():
    containers = client.listDomainsID()
    for index in range(len(containers)):
        containers[index] = plugin.int_to_str_id(containers[index])
    return containers


def getContainerInfoByID(str_id):
    id = plugin.str_to_int_id(str_id)
    checkID(id, "getContainerInfoByID")

    dom = client.lookupByID(id)
    dom_info = dom.info()
    ret = dom.getCPUStats(1, 0)
    dic_dom_info = {"status": dom_info[0], "maxMemory": dom_info[1], "usedMemory": dom_info[2], "virtCpu": dom_info[3],
                    "cpuTime": dom_info[4]}
    ret.append(dic_dom_info)
    return ret


def createContainer(xml):
    dom = client.createXML(xml)
    return plugin.int_to_str_id(dom.ID())


def updateContainer(xml, str_id):
    deleteContainerByID(str_id)
    return createContainer(xml)


def deleteContainerByID(str_id):
    id = plugin.str_to_int_id(str_id)
    checkID(id, "deleteContainerByID")

    dom = client.lookupByID(id)
    dom.destroy()
    return "delete success"


def stopContainerByID(str_id):
    id = plugin.str_to_int_id(str_id)
    checkID(id, "stopContainerByID")

    dom = client.lookupByID(id)
    dom.shutdown()
    return dom.state()


def startContainerByID(str_id):
    id = plugin.str_to_int_id(str_id)
    checkID(id, "startContainerByID")

    dom = client.lookupByID(id)
    dom.reboot()
    return dom.state()


def findContaienrIDByName(name):
    dom = client.lookupByName(name)
    return dom.ID()
