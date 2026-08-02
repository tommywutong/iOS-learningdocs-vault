---
title: Networking Overview
apple_id: TP40010220
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Networking, Internet, & Web
technology: null
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/NetworkingOverview/GLOSSARY/GLOSSARY.html
archived_at: '2026-07-18T01:33:56.528267Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Networking Overview](About%20Networking.md)


[Previous](Document%20Revision%20History.md)

# Glossary

- __Address Resolution Protocol (ARP)__

  A protocol for determining the hardware address of a computer or other device based on its IP address.

- __application layer__

  The topmost layer of the networking protocol stack. This layer consists of data formats and protocols specific to a given application. For example, the HTTP (hypertext transport protocol) standard is an application-layer protocol.

- __broadcast address__

  A special address that sends a packet simultaneously to every device on a local area network.

- __core router__

  A router that provides service for major Internet backbone routes. Core routers are powerful devices that must handle a large volume of traffic and usually must manage a large number of simultaneous routes. Core routers participate in route advertisements to discover or announce changes in the network topology.

- __default gateway__

  The default router used for outgoing traffic if there is no explicit route for the destination IP in the system’s routing table.

- __domain name__

  A human-readable name that identifies an Internet or intranet site; for example, developer.apple.com is a domain name. By resolving a domain name, an application can obtain a corresponding [IP address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomi) that is suitable for sending data to that site.

- __edge router__

  A router that provides connectivity between a customer site and an upstream ISP. Edge routers generally route between only two or three different networks, and thus usually do not participate in route advertisements.

- __encapsulation__

  The act of wrapping one packet inside another packet (usually of a different type). For example, on a local area network, your IP packets are encapsulated within Ethernet packets. The Ethernet packets provide information about their destination within the local area network. The IP packets inside them provide information about what to do with the packets once they reach the public Internet.

- __fragmentation__

  The process of breaking up a packet into smaller pieces to accommodate network connections with a smaller maximum packet size (referred to as the maximum transmission unit, or MTU).

- __header__

  In the context of packets, the first part of a packet (before the actual payload) that contains information about where the packet should be sent. In the context of HTTP, a series of values that provide information about the content of a request or reply, such as the hostname, caching policies, and so on.

- __hop__

  Any one of a series of physical links that make up the [route](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvonbr) from one host to another.

- __host__

  Any device that is connected to a network. It may be a client computer, a server, a mobile phone, or even a network-attached printer.

- __hostname (or host name)__

  A DNS name that points to a specific host (or a group of hosts that mimic a single host).

- __infrastructure device__

  Any device that provides support for a network’s basic operation—for example, a router, a Wi-Fi access point, or an Ethernet switch.

- __Internet Control Message Protocol (ICMP)__

  A low-level networking protocol that provides out-of-band control messages that are used by the operating system when making TCP connections. ICMP is used mainly to deliver connection failure notifications—“connection refused” and “host unreachable” messages, for example. However, it is also used by some network diagnostic tools, such as `ping` and `traceroute`.

- __IP (Internet Protocol) layer__

  The networking layer that provides basic transport of packets across the Internet. It sits above the physical layer (hardware interconnects) and below the transport layer (TCP and UDP, for example).

- __IP address__

  A number that uniquely identifies a single host on the Internet (short for Internet Protocol address). An IP address can be in one of two forms: an [IPv4 address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomq) or an [IPv6 address](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomy).

- __IPv4 address__

  An IP address consisting of four 8-bit numbers (for a total of 32 bits). For example, the IP address for developer.apple.com is 17.254.2.129.

- __IPv6 address__

  An IP address consisting of eight groups of 16-bit hexadecimal numbers (for a total of 128 bits). If several groups in a row are all zero, you can omit those groups and replace them with a double colon (but only once per IP address). For example, the IPv6 address for example.com is 2001:500:88:200::10.

- __latency__

  The amount of time it takes for a packet to reach its destination, usually measured in milliseconds. Latency is usually expressed as round-trip latency, which refers to the amount of time for a packet to reach its destination and for the response packet to reach the original host. Latency is important for two reasons. First, it increases the amount of time it takes to establish a connection. Second, it dramatically reduces performance when using protocols that require the client to wait for a response before sending subsequent requests.

- __link__

  A physical connection between two hosts on a network (or a virtual connection that emulates a physical connection) with no intermediate routers (except for link-layer switches).

- __link layer__

  The lowest layer of the network protocol stack. This layer provides support for the physical transport of packets from one host to another across a local area network or other physical [link](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvona).

- __listening socket (or listen socket)__

  A socket configured to listen for incoming connections.

- __Maximum Transmission Unit (MTU)__

  The largest packet size that can be delivered across a particular [link](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvona). The MTU is limited by the actual communication hardware, and usually represents the maximum payload size supported by the largest physical packet that the hardware supports. However, in some cases (such as gigabit Ethernet), the default MTU may be further limited in software to maintain backwards compatibility with legacy hardware that does not support larger packets.

- __multicast__

  A special type of packet that is simultaneously delivered to a multitude of hosts on the network, but not to every host (broadcast).

- __neighbor discovery protocol (NDP)__

  A protocol used by IPv6 over Ethernet to learn about other devices on the physical network. Among other things, neighbor discovery can be used to learn the hardware addresses of nearby devices, discover routers and name servers, and determine information about upstream links, such as their [Maximum Transmission Unit (MTU)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomrv).

- __netblock__

  See [subnet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvoni).

- __netmask__

  A collection of bits indicating which portion of an IPv4 address is the network part and which portion is the host part. If the network part of the destination address is the same as the network part of the source address, the two hosts are considered to be within the same [subnet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvoni).

- __network address__

  A special reserved address within each IPv4 network in which the host part is all zeros. This address was used by older operating systems as the broadcast address, so for historical compatibility reasons, this number is reserved.

- __network address translation (NAT)__

  A form of packet rewriting performed by a firewall in which packets are modified to contain a different source or destination IP address before passing them on. NAT is most commonly used to make traffic from multiple devices appear to come from a single device, often for security or load balancing purposes.

- __network interface__

  A piece of hardware (or virtual hardware) that represents the endpoint of a [link](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvona).

- __packets__

  A discrete unit of data that is sent across a computer network.

- __path MTU discovery__

  A process by which one host determines the largest packet that can be sent to a destination without fragmenting it. This allows the host to fragment the data ahead of time, which prevents packets from potentially being fragmented more than once before reaching their final destination. Path MTU discovery works by sending packets with the “Don't Fragment” bit set. If any router along the path responds by sending an ICMP packet with the Fragmentation Needed bit set, the host then tries progressively smaller sizes until the packet reaches its destination successfully. See also [Maximum Transmission Unit (MTU)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomrv).

- __payload__

  The data contents of a packet (as distinct from the structure of the packet itself).

- __physical layer__

  See [link layer](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvonq).

- __port numbers__

  A number that uniquely identifies a particular service on a given host. Port numbers are further divided according to whether they are TCP or UDP ports.

- __recursion__

  The use of recursive queries. A recursive query asks the domain name server to perform recursion on the client’s behalf. If the domain name server allows recursive queries, it then sends a query to the root name server asking which server knows the answer, then asks that server, and so on, until it reaches a server that actually knows the answer to the query. See also [recursion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvony).

- __route__

  The path that packets take from one host to another host. If the two hosts are on the same physical network, the route consists of a single link; if not, it passes through one or more [router](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvooa)s.

- __router__

  A device that routes packets between two or more networks. A router determines which network should receive each packet based on a set of routing rules. Most routers also communicate with other routers to optimize those rules as network links are added and removed.

- __router address__

  The IP address of your [router](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvooa).

- __routing__

  The process of taking a packet on one physical network and retransmitting it on a different physical network, using a set of rules to determine which network should receive each packet. A device that performs routing is called a [router](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvooa).

- __shared network__

  A network in which every packet is received by every device on the network. This is the opposite of a [switched network](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvooi).

- __subnet__

  A range of IP addresses in which packets from one host can be sent directly to another host without going through an intermediate router.

- __switched network__

  A physical network in which an infrastructure device (called a switch) directs packets based on their destination. This improves network performance by ensuring that only the hosts that need to receive a given packet actually see it. This is the opposite of a [shared network](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomjq).

- __trailer__

  The last part of a packet (after the payload) that usually contains a checksum of the payload data.

- __Transmission Control Protocol (TCP)__

  A transport-layer protocol that provides bidirectional, stream-based delivery of data, with flow control and delivery guarantees (automatic retry). Contrast with [User Datagram Protocol (UDP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomjr).

- __transport layer__

  The networking layer that sits on top of the IP layer and can provide such features as port numbers, delivery guarantees, flow control, and checksums. The two most common transport-layer protocols are the [Transmission Control Protocol (TCP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomjs) and the [User Datagram Protocol (UDP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomjr).

- __User Datagram Protocol (UDP)__

  A transport-layer protocol that provides unidirectional, packet-based delivery of data, with best-effort delivery (no retransmission). Contrast with [Transmission Control Protocol (TCP)](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemrqfvbuqmjqfvjvomjs).

[Previous](Document%20Revision%20History.md)

