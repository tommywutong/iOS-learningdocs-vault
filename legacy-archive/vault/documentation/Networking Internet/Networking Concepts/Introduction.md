---
title: Networking Concepts
apple_id: TP40012487
resource_type: Guide
platform: watchOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-07-19'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/NetworkingConcepts/Introduction/Introduction.html
archived_at: '2026-07-15T08:18:49.693980Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Networking%20Terminology.md)

# Introduction

Because most networking in OS X and iOS is based on the TCP/IP communication protocol, you should have at least a basic understanding of the fundamentals of the TCP/IP networking model itself before you begin writing code. Although you can perform some high-level networking tasks without learning about the underlying protocols, knowing how things work at a low level will help you better understand why things go wrong and how to handle them when they do.

The Internet is a vast network of interconnected computers and other devices that provide communication around the world. When you visit a website, the server that provides that content might be across the room or across an ocean. Your request might pass through a Wi-Fi router, a cable modem, a trunk line, a satellite connection, or ostensibly even be delivered by carrier pigeon ([RFC 1149](http://tools.ietf.org/html/rfc1149)). At a high level, each of these networking media are equivalent (performance characteristics notwithstanding). However, at a lower level, devices communicate with one another in different ways, depending on what type of physical network they are communicating over.

![../Art/AboutNetworking.png](attachments/Art/AboutNetworking.png)

At a low level, when you access a website, your computer breaks up each request into tiny pieces, called packets, and sends each packet individually to a special device called a router, which forwards those packets to another router, which in turn forwards them to yet another router, and so on, until the packets reach the destination server, wherever it might be. The response is sent back in a similar fashion. At each step along the way, those packets can be split into multiple packets, wrapped up in other types of packets, and so on, depending on the hardware involved.

This document explains how the Internet works under the hood, but at a moderately high level intended for programmers. If, after reading this document, you want to learn more about how various Internet technologies work, you can find a number of third party books that describe them in more detail. In addition, most of the lower-level Internet technologies are described by RFCs (short for “Request for Comment”) that describe the protocols in great detail.

This document is a companion document for _[Networking Overview](../../Networking%20Internet%20Web/Networking%20Overview/About%20Networking.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrq)_, which explains how to write good networking code.

[Next](Networking%20Terminology.md)

