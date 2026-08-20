---
title: Common QA for Bonjour
apple_id: DTS40009974
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2010-07-16'
source_url: https://developer.apple.com/library/archive/qa/qa1690/_index.html
archived_at: '2026-07-18T02:34:10.854906Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1690

# Common QA for Bonjour

## Q:  What is Bonjour?

A: Bonjour, also known as zero-configuration networking, enables automatic discovery of computers, devices, and services on IP networks. Bonjour uses industry standard IP protocols to allow devices to automatically discover each other without the need to enter IP addresses or configure DNS servers. See the Bonjour Protocol Specifications section for more details on the underlying standards.

## Q:  What is mDNSResponder?

A: mDNSResponder is a Bonjour system service. It implements Multicast DNS Service Discovery for discovery of services on the local network, and Unicast DNS Service Discovery for discovery of services anywhere in the world. It includes a C API for both publishing and discovering such services. mDNSResponder is built into [Mac OS X](https://developer.apple.com/technologies/mac/networking.html) and [iPhone OS](https://developer.apple.com/technologies/iphone/networking.html), and can be downloaded as part of the [Bonjour for Windows SDK](https://developer.apple.com/opensource/).

## Q:  Does Bonjour work between multiple subnets?

A: Yes. The first release of [DNS Service Discovery](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt) for Mac OS X concentrated on [Multicast DNS](http://files.multicastdns.org/draft-cheshire-dnsext-multicastdns.txt) for single-link networks because this was the environment worst served by IP software. Since Mac OS X 10.4, Bonjour supports [Dynamic DNS Update](http://www.ietf.org/rfc/rfc2136.txt) and unicast DNS queries to enable wide-area service discovery.

## Q:  Does Bonjour have any kind of subscription or notification mechanism?

A: Yes. Notification is simply an intrinsic property of the discovery protocol. Discovery of static information, discovery of variable information, and discovering when variable information changes are all just different points on the same spectrum. For an example of an application using Bonjour "notifications", check out iChat. When you change your Status from "Available" to "Away" or type in a status message, all other iChat clients on the local network are notified of the change.

## Q:  Can I use Bonjour as a protocol to communicate with other applications and services?

A: No, Bonjour itself is simply a way to \*discover\* network services that use various protocols: e.g., Jabber for iChat or IPP for printing. That said, Bonjour DNS packets can include a very small amount of "text" information, as exemplified by the presence information for use with iChat.

## Q:  My hardware device has a built-in web server used for configuration. Should I register it using Bonjour?

A: Yes. You should register every service running on your device -- e.g., HTTP, FTP, SSH, Telnet -- to assist clients that may wish to browse for those services. For example, the Safari web browser can discover web servers advertised with Bonjour, and the Terminal application in Mac OS X can discover FTP, SSH, and Telnet servers.

## Q:  Is there a mailing list for Bonjour development questions?

A: Yes, the [Bonjour mailing list](http://lists.apple.com/mailman/listinfo/bonjour-dev) is a great resource for developers with questions about Bonjour APIs and for people interested in detailed discussions of Bonjour protocol specifics.

What open standards is Bonjour built upon?

Bonjour is built on a wide range of existing and emerging Internet standards, typically published as "RFCs" or "Working Drafts".

- [Dynamic Configuration of IPv4 Link-Local Addresses [IPv4LL]](http://www.ietf.org/rfc/rfc3927.txt). Describes how a host can automatically configure an interface with an IPv4 address within the 169.254/16 prefix that is valid for communication with other devices connected to the same physical link.
- [Multicast DNS [mDNS]](http://files.multicastdns.org/draft-cheshire-dnsext-multicastdns.txt). Discusses what needs to happen if DNS clients start sending DNS queries to a multicast address, and how a collection of hosts can cooperate to collectively answer those queries in a useful manner.
- [DNS-Based Service Discovery [DNS-SD]](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt). Describes a convention for naming and structuring DNS resource records. Given a type of service that a client is looking for, and a domain in which the client is looking for that service, this convention allows clients to discover a list of named instances of that desired service, using only standard DNS queries.
- [DNS Long-Lived Queries [DNS-LLQ]](http://files.dns-sd.org/draft-sekar-dns-llq.txt). Proposes a method of extending unicast DNS to support long-lived queries, allowing clients to learn about changes to DNS data.
- [Dynamic DNS Update Leases [DNS-UL]](http://files.dns-sd.org/draft-sekar-dns-ul.txt). Proposes a method of extending Dynamic DNS Update to contain a resource record lease-life, thus allowing a server to garbage collect stale records.
- [NAT Port Mapping Protocol [NAT-PMP]](http://files.dns-sd.org/draft-cheshire-nat-pmp.txt). Describes a protocol for automating the process of creating Network Address Translation (NAT) port mappings. Included in the protocol is a method for retrieving the public IP address of a NAT device, thus allowing a client to make this public IP address and public port number known to peers that may wish to communicate with it.
- [Bonjour Printing Specification (PDF)](https://developer.apple.com/opensource/). This document explains what printer vendors must do in order to create Bonjour compatible printers that work seamlessly with Mac OS X and with Windows machines running Bonjour for Windows.

How can I register a new service type?

Bonjour service discovery uses the [service types](http://www.dns-sd.org/ServiceTypes.html) listed on http://www.dns-sd.org. If your application defines a new service type that isn't on this list, you should register your service type with [DNS-SD.org](http://www.dns-sd.org/) and optionally register it with [IANA](http://www.iana.org/cgi-bin/usr-port-number.pl) if your application protocol also requires a well-known port number.

Is Bonjour available as Open Source?

Yes. The Bonjour source code is available as under the [Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0.html) via the [mDNSResponder](http://www.opensource.apple.com/tarballs/mDNSResponder/) project. You can easily compile it for a wide range of platforms, including UNIX, Linux, and Windows. Hardware device manufacturers are encouraged to embed the open source mDNSResponder code directly into their products, and optionally pass the [Bonjour Conformance Test](https://developer.apple.com/opensource/) so they can participate in the [Bonjour Logo Licensing Program](https://developer.apple.com/opensource/).

Can I use Bonjour from my Windows application?

Yes, Bonjour for Windows is available for hardware and software developers who want to include Bonjour with their products. Simply download the [Bonjour SDK for Windows](https://developer.apple.com/opensource/) to get started, then complete the [Bundling Agreement](https://developer.apple.com/opensource/) to distribute the Bonjour installer alongside your software.

How can I learn more?

For technical assistance, hardware vendors who would like to support Bonjour in their network-enabled products should contact [bonjourdev@apple.com](mailto:bonjourdev@apple.com). The Developer Reference Library also provides extensive documentation regarding [Bonjour](https://developer.apple.com/mac/library/navigation/index.html?filter=bonjour), [DNS](https://developer.apple.com/mac/library/navigation/index.html?filter=DNS), and [NetService](https://developer.apple.com/mac/library/navigation/index.html?filter=NetService) APIs.

What Sample Code is available that uses Bonjour technologies?

__Bonjour Sample Code for iPhone OS__

- [BonjourWeb](https://developer.apple.com/iphone/library/samplecode/BonjourWeb/Introduction/Intro.html) illustrates the fundamentals of browsing for network services using Bonjour.
- [WiTap](https://developer.apple.com/iphone/library/samplecode/WiTap/Introduction/Intro.html) demonstrates how to achieve network communication between applications. Using Bonjour, the application both advertises itself on the local network and displays a list of other instances of this application on the network.

__Bonjour Sample Code for Mac OS X__

- [SRVResolver](https://developer.apple.com/mac/library/samplecode/SRVResolver/Introduction/Intro.html) shows how to do DNS SRV record queries using the <dns_sd.h> API.
- [PictureSharingBrowser](https://developer.apple.com/mac/library/samplecode/PictureSharingBrowser/Introduction/Intro.html) demonstrates how to use NSNetServices to take advantage of Bonjour service discovery and name resolution on Mac OS X.
- [PictureSharing](https://developer.apple.com/mac/library/samplecode/PictureSharing/Introduction/Intro.html) demonstrates how to use NSNetServices to advertise a service using Bonjour under Mac OS X.
- [PortMapper](https://developer.apple.com/mac/library/samplecode/PortMapper/Introduction/Intro.html) demonstrates Bonjour's NAT port-mapping API, and provides a higher-level Objective-C interface to it.
- [DNSServiceMetaQuery](https://developer.apple.com/mac/library/samplecode/DNSServiceMetaQuery/Introduction/Intro.html) demonstrates the use of a DNSServiceQueryRecord to send a Multicast DNS query that returns a list of Bonjour service types being advertised on the local network for Mac OS X.
- [CocoaEcho](https://developer.apple.com/mac/library/samplecode/CocoaEcho/Introduction/Intro.html) shows how to write a basic echo client/server pair. It demonstrates how to make services available on both IPv4 and IPv6 endpoints, publishing the services using Bonjour, and how to respond to network events asynchronously.
- [CocoaHTTPServer](https://developer.apple.com/mac/library/samplecode/CocoaHTTPServer/Introduction/Intro.html) demonstrates a basic HTTP service under Mac OS X. It shows how to publish your HTTP service on Bonjour so Safari can browse it using the Bonjour tab as well as asynchronous reading and writing of information from and to NSStreams.

What should I pass in for the "name" parameter when registering a service?

By default, you should choose a human-readable name that uniquely describes the service. iTunes, for example, chooses a default music sharing name by combining the computer user's first and last name, as in "Isaac Newton's Music". For most hardware devices, the default service name should be the full make and model of the product, for example, "Apple PowerBook G4". This is only the default name given out of the box, and the user should be allowed to customize the service name to differentiate multiple devices or services on the network.

For application developers that are registering services, it may make sense to have one instance of that service on a given computer. In that case, rather than having your application present its own user-interface for the user to enter the name of the advertised service, it's more convenient to register using the system-provided default name known as the "Computer Name" in the Sharing Preference Panel. If you pass in an empty string ("") for the service name when registering, the system will automatically use the "Computer Name". Passing in an empty string will also handle name conflicts by automatically appending a digit to the end of the name.

There are services where multiple instances may be hosted on the same computer. For example, a print server with three printers should advertise each printer as a first-class entity. Each printer should be advertised using a descriptive name that usefully identifies the printer itself. This is important, because the printer called "Marketing's Transparency Printer" might get moved to a different print server in the future, but the user shouldn't have to be aware of those operational details. They should still see the same service advertised on the network under the same name, even though it's on a different print server now.

What should I pass in for the "type" parameter when registering a service?

You must pass a string of the form "_applicationprotocol._transportprotocol". Currently "_transportprotocol" must be either "_tcp" or "_udp". Your "applicationprotocol" must be 14 characters or less and should be registered with the [DNS-SD Web Site](http://www.dns-sd.org/ServiceTypes.html). If your protocol requires a well known port number, you should also register with [Internet Assigned Numbers Authority (IANA)](http://www.iana.org/cgi-bin/usr-port-number.pl)so they can add you to the list of registered [protocol names and port numbers](http://www.iana.org/assignments/port-numbers). Please see [Technical QA1312, Bonjour service types used in Mac OS X](https://developer.apple.com/mac/library/qa/qa2001/qa1312.html) for the list of service types used by Mac OS X.

What should I pass in for the "domain" parameter when registering a service?

If you pass an empty string (""), then Mac OS X will automatically do the right thing. In Mac OS X 10.2 and 10.3, it will register using just link-local multicast. Starting in Mac OS X 10.4, it will automatically register your service in a user-chosen unicast DNS domain as well, if applicable. You only need to pass a specific string if you have some particular reason to want to register in some specific remote domain.

What should happen when two devices on the network both use the same service name?

In the rare case where a name collision occurs, your device should add a digit to the end of the name, for example:

"Apple Mac mini (2)"

Applications and devices that call Bonjour APIs like DNSServiceRegister and CFNetServiceRegisterWithOptions will automatically get this name changing behavior when name conflicts occur. For devices that have a screen and are capable of user input, instead of appending a number, you could optionally decide to prompt the user for a more unique name.

What is the TXT record used for?

The specific nature of the TXT record and how it is to be used is service type dependent. Each service type will define zero or more name/value pairs used to store meta-data about each service. These name/value pairs should be formatted as described in Section 6 of [DNS-Based Service Discovery](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt). Please see [Technical QA1306, Bonjour enforces the TXT record format in Panther](https://developer.apple.com/mac/library/qa/qa2001/qa1306.html) for information on how TXT records should be formatted when using the Mac OS X APIs. Also, the [DNS-SD Web Site](http://www.dns-sd.org/ServiceTypes.html) has information regarding the currently defined name/value pairs for common service types.

After the user browses for and selects the service they want to use, can I save the resulting IP address in my application's preference file?

No. With DHCP (and with link-local addressing) it is not safe to assume that the service instance will have the same IP address tomorrow. Addresses can change. Service names are the intended stable identifiers for a service instance. Save the instance name (name, type, and domain) in your application's preference file, then Resolve it on demand each time the user accesses the service.

Note also that you should not store the host name and port number, because you shouldn't assume that the service instance will necessarily be running on the same port number tomorrow. Instead of storing the host name, store the service instance name (name, type, and domain) and then when you Resolve the service instance name at the time of use you are sure to get the up-to-date IP address and port number.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-07-16 | Updated all URL references to Bonjour for Windows components to reference the Open Source page which will be updated as necessary. This includes the reference for Conformance text package, and Bonjour related licensing. |
| 2010-05-12 | New document that roadmap for development of software using Bonjour and some Common Questions and Answers |

