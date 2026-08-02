---
title: Networking Concepts
apple_id: TP40012487
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-07-19'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingConcepts/NetworkingTerminology/NetworkingTerminology.html
archived_at: '2026-07-15T08:18:50.530429Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Networking Concepts](Introduction.md)


[Next](Networking%20Layers.md)[Previous](Introduction.md)

# Networking Terminology

In networking terminology, a _host_ is any device that is connected to a network and provides an endpoint for networked communication. A host might be a desktop computer, a server, an iOS device, a virtual machine running on a server, or even the VoIP telephone sitting on your desk. It is called a host because it hosts the applications and daemons that run on it.

Similarly, an _infrastructure device_ is any piece of equipment that is responsible for making the network function. The difference between a host and an infrastructure device is that an infrastructure device usually passes on information sent by a host, whereas a host primarily sends or receives information on its own behalf. There are even some infrastructure devices that are completely transparent to TCP/IP networking, such as Ethernet hubs and switches (more on these later).

When one host sends data across a network, it divides the data into small pieces called _packets_. These packets can be varying lengths, up to the maximum size allowed by the physical network interconnect (again, more on this later).

A packet generally contains three basic parts: a _header_ that tells where the packet should be sent, a _payload_ that contains the actual data, and a _trailer_ that contains checksum information to ensure that the packet was received correctly. Some packet types include this checksum information as part of the header, and thus do not have a trailer. For example, shows the structure of an Ethernet packet.

__Figure 1-1__  Structure of an Ethernet packet

!

The receiving host then reassembles these packets and provides them to a program as either a stream of bytes or a series of messages, depending on the protocol. That program can respond by sending data, which its host then divides into packets and sends back to the first host.

When one packet contains another packet (generally of a different type), this is called _encapsulation_. For example, the Ethernet packet shown in Figure 1-1 contains a TCP/IP packet as its payload; the TCP/IP packet is said to be encapsulated within the Ethernet packet.

[Next](Networking%20Layers.md)[Previous](Introduction.md)

