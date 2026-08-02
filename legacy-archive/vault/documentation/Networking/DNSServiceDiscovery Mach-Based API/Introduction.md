---
title: DNSServiceDiscovery Mach-Based API
apple_id: TP30001129
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_mach/introduction/intro_mach.html
archived_at: '2026-07-15T08:18:33.177501Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Bonjour%20Overview.md)

# Introduction

|  |  |
| --- | --- |
| __Framework__ | None. |
| __Declared in__ | DNSServiceDiscovery.h |

The DNSServiceDiscovery API is part of Bonjour,
Apple’s implementation of zero-configuration networking (ZEROCONF).

Bonjour allows you to register a network service, such
as a printer or file server, so that it can be found by name or
browsed for by service type and domain. Using Bonjour, applications
can discover what services are available on the network, along with
all necessary access information—such as name, IP address, and
port number—for a given service.

In effect, Bonjour combines the functions of a local DNS
server and AppleTalk. Bonjour allows applications to provide
user-friendly printer and server browsing, among other things, over
standard IP networks. It does this by combining protocols such as
multicast and DNS to add new functionality to the network (such
as multicast DNS).

This gives applications easy access to services over local
IP networks without requiring the service or the application to
support an AppleTalk or Netbeui stack, and without requiring a DNS
server for the local network.

For a detailed overview of Bonjour, see [Bonjour Overview](Bonjour%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgqwueq2jirbecrkk)

For additional information on Bonjour, including links
to standards, specifications, and resources, see [http://developer.apple.com/networking/bonjour/](https://developer.apple.com/networking/bonjour/).

This section describes the functions, callbacks,
and data structures that make up the DNSServiceDiscovery API.

The DNSServiceDiscovery API is appropriate for Darwin programmers
and developers who are comfortable working in Mac OS X at the Mach
level. This is a low-level API that interacts directly with the
Mach kernel and the mDNS responder daemon.

Bonjour provides two higher-level APIs as alternatives
to this one. Cocoa developers should generally use the NSNetServices
API documented in
_[Bonjour Overview](../../Cocoa/Bonjour%20Overview/About%20Bonjour.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyts2i)_ and Carbon developers should generally
use the CFNetServices API documented in _[CFNetwork Programming Guide](../CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_.

These higher-level APIs provide the similar services to the
DNSServiceDiscovery API and are designed to fit cleanly with code
written using a specific framework. Note, however, that the DNSServiceDiscovery
API provides a finer degree of control than the CFNetServices and
NSNetServices APIs.

Version 10.2 or later of the Mac OS X or Darwin operating
system is required.

This API requires the services of an mDNS responder. Mac OS
X, versions 10.2 and later, include an mDNS responder daemon as
part of the operating system. Apple also provides source code for
an mDNS responder to Darwin developers as part of versions 10.2
and later.

The DNSServiceDiscovery API does not perform network access
setup for services. Similarly, the DNSServiceDiscovery API does
not provide a network connection from an application to a service.
It allows applications to browse for services, or to ask for them
by name, and provides the IP address, port, and so on. Use the NSNetwork,
CFNetwork, or BSD sockets API to actually connect to a service over
the network.

[Next](Bonjour%20Overview.md)

