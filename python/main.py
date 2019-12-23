#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 Michael Bittencourt <mchl.bittencourt@gmail.com>
#
# Distributed under terms of the MIT license.

import ncl
"""from ncl import Ncl"""


"""nclCode = Ncl("nclv1", "http://www.ncl.org.br/NCL3.0/EDTVProfile")"""
nclCode = ncl.Ncl()

region = ncl.Region(id="regImage", height="15%", width="100%")
regionChild = ncl.Region(id="regImageChild", height="90%", width="50%")
region.add(regionChild)
region.add(ncl.Region(id="regImageChild2", height="90%", width="50%"))
descriptor = ncl.Descriptor(id="descImage", region="regImage")
media = ncl.Media(id="image", descriptor="descImage", src="lena.jpg")
media.add(ncl.Area(id="areaImage"))
media.add(ncl.Property(name="ahamm", value="48"))
port = ncl.Port(id="pImage", component="image")


compoundCondition = ncl.CompoundCondition(operator="or")
conditionOnBegin = ncl.SimpleCondition(role="onBegin")
conditionOnEnd = ncl.SimpleCondition(role="onEnd")
compoundCondition.add(conditionOnBegin)
compoundCondition.add(conditionOnEnd)
actionStop = ncl.SimpleAction(role="stop")
actionStart = ncl.SimpleAction(role="start")
compoundAction = ncl.CompoundAction(operator="seq")
compoundAction.add(actionStop)
compoundAction.add(actionStart)
connectoronBeginStop = ncl.CausalConnector(id="onBeginOrOnEndStopStart", condition=compoundCondition, action=compoundAction)
link = ncl.Link(xconnector="onBeginOrOnEndStopStart")
bindOnBegin = ncl.Bind(role="onBegin", component="image")
bindOnEnd = ncl.Bind(role="onEnd", component="image2")
bindStop = ncl.Bind(role="stop", component="image2")
bindStart = ncl.Bind(role="start", component="image", interface="areaImage")
link.add(bindOnBegin)
link.add(bindOnEnd)
link.add(bindStop)
link.add(bindStart)

region2 = ncl.Region(id="regImage2", height="15%", width="100%", top="0", left="10%", zIndex="10")
descriptor2 = ncl.Descriptor(id="descImage2", region="regImage2")
media2 = ncl.Media(id="image2", descriptor="descImage2", src="lena.jpg")
port2 = ncl.Port(id="pImage2", component="image2")

nclCode.add(region)
nclCode.add(descriptor)
nclCode.add(connectoronBeginStop)
nclCode.add(link)
nclCode.add(media)
nclCode.add(port)

nclCode.add(region2)
nclCode.add(descriptor2)
nclCode.add(media2)
nclCode.add(port2)
 
text_file = open("myTest.ncl", "w")
text_file.write(nclCode.generate())
text_file.close()
print(nclCode.generate())
