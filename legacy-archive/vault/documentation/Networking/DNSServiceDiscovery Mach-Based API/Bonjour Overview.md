---
title: DNSServiceDiscovery Mach-Based API
apple_id: TP30001129
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-04-29'
source_url: https://developer.apple.com/library/archive/documentation/Networking/Conceptual/dns_discovery_mach/concepts/concepts_mach.html
archived_at: '2026-07-15T08:18:31.782506Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [DNSServiceDiscovery Mach-Based API](Introduction.md)


[Next](DNSServiceDiscovery%20Tasks.md)[Previous](Introduction.md)

# Bonjour Overview

Bonjour is a powerful new system for finding
and publishing network services, such as Web servers, file servers,
and printers, on Internet Protocol (IP) networks. This system adds
the simplicity and ease-of-use of AppleTalk to the power of IP network
services.

Bonjour is Apple’s implementation of zero-configuration
networking over IP and is based on IETF standard protocols (IP,
ARP, DNS, etc.). Bonjour comes out of the work of the IERF Zeroconf
Working Group.

This section describes some of the problems that Bonjour
solves and how it solves them.

Over the last twenty years, a large number of wide-area networking
protocols have appeared and disappeared. In recent years, Internet
protocol (IP) has become the single predominant standard on every
computing platform. The majority of computers, and many other network
devices, all speak a common language. For wide-area networks and the
Internet, IP protocol is all you need.

On local area networks (LANs) however, a few other protocols
live on. To work on as many local networks as possible, printers
and applications such as multiplayer games must support not only
IP, but also AppleTalk or Windows Netbeui, or perhaps all three. While
IP has emerged as a unifying protocol for wide area networks and
the Internet, it is not a universal standard on local networks,
especially small networks and home networks. Why?

The answer is simple: these networks don’t often have dedicated
address and name servers (DHCP and DNS) or a real system administrator.

For IP to work, every device needs a unique address. To make
this happen, either everyone must agree on static IP addresses and
manually type them in, or someone must set up a DHCP server or similar
service to dynamically allocate addresses to clients. To refer to services
by name, someone must set up a DNS server to perform the name-to-address translation,
and, typically, use “well known ports” for specific types of
services. To use a service, network users have to know it’s name,
so when a service is added, everyone needs to be notified. Someone
with a lot of knowledge has to set all this up and maintain it.

More and more, people that do not fit the traditional role
of the network administrator are setting up networks. Families are
setting up home networks so they can share printers, files, and
Internet connections. Peers meeting at conferences are setting up
ad-hoc networks to exchange data. Even inside well-managed corporate
networks, employees are adding devices to and removing devices from
their local subnets. Currently, all these activities require manual
configuration of IP addresses and names.

This new breed of network administrator does not want to configure
subnet masks or DNS servers. Even a highly competent network administrator
doesn’t want to send email to every employee every time a printer
is added to the network. Printer manufacturers and game publishers
don’t want to support multiple protocol stacks on a $50 product.
People need to be able to plug in a printer, or plug two laptops
together, or look for a file server or game server on the local
network, without wasting time trying to get the configuration right.

Once the configuration of devices on an IP network is right,
the user needs to know the exact name of any printer or other service
in order to use it. That’s better than typing in an IP address,
but it doesn’t help the user find services he or she doesn’t
already know about. And it doesn’t forgive spelling errors. Browsing
for available services is often simply impossible. A large number
of IP service browsing protocols have appeared and disappeared,
but none has achieved critical mass.

Before the emergence of IP as the preeminent interoperative
networking protocol, AppleTalk solved the configuration and usage
problems that continue to hinder IP today. With AppleTalk, users
can simply browse for a service and click to choose it. For example, if
you connect a group of Macintosh computers running Mac OS 9 or earlier
with an Ethernet hub, they can instantly see all the available printers,
file servers, and other services available on the local network.
All this happens without centralized allocation of network addresses,
without a centralized name server, and without a centralized repository
of available services.

People need a simple and reliable way to configure and browse
for services over IP networks. They want to discover available services
and choose one from a list, instead of having to know each service’s
name or IP address in advance. It is in everyone’s interest for
IP to have this capability. This is exactly the capability that
Bonjour provides.

The potential for zero-configuration IP networking is tremendous.
Consider the everyday task of printing. Once a printer is configured
on your computer, it’s simply a matter of choosing an application’s
Print command.

Take your laptop to a client’s company, or a neighbor’s
house, and try to print something. If they have a printer that supports
Bonjour protocols, printing is just as easy as it was on your
local network. To print, connect an Ethernet cable from your laptop
to your client’s LAN and start up your laptop. Or start up your
laptop and it instantly finds your neighbor’s home wireless network.
Either way, your laptop automatically discovers any available printers.
You open the document, choose the Print command, and every available
printer appears in the Print dialog. You select a printer, click
Print, and the document prints.

Or say you want to play a network game with a friend. You
open the game, and your friend’s copy of the game instantly sees
your copy over the network. Or if you have a music sharing application
on both computers, the programs themselves can discover each other and
instantly swap songlists. Similarly, if you have a shared folder
or have personal Web sharing turned on, your shared files and Web
pages are instantly available to others.

This scenario is illustrated in [Figure 1-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgqwtcojxheyds). In step 1, you open
up your laptop in your neighbor’s house, and the laptop either
obtains an address from the DHCP server in the router or, in the
absence of a DHCP server, assigns itself an available local address.
In step 2, the network is queried for available printers so that
when you open the Print dialog, your neighbor’s printer is listed.
Finally, in step 3, you turn on music sharing on your computer,
and your neighbor’s computer sees it and connects.

These are just a few of the existing applications that can
benefit from zero-configuration IP networking. Zero-configuration
IP networking has the potential to enhance contact management, PDA
synchronization, distributed processing, and many other network applications.
Additionally, zero-configuration IP networking opens the door for
a whole new class of IP-enabled digital devices.

__Figure 1-1__  A typical zero-configuration networking
session

!

Bonjour is Apple’s proposal for zero-configuration networking
over IP. Bonjour comes out of the work of the ZEROCONF Working
Group, part of the Internet Engineering Task Force (IETF). The ZEROCONF
Working Group’s requirements and proposed solutions essentially
cover three areas:

- addressing (allocating IP addresses to hosts)
- naming (using names to refer to hosts instead of IP addresses)
- service discovery (finding services on the network automatically)

Bonjour has a zero-configuration solution for all three
of these areas, as described in the following three sections.

Bonjour allows service providers, hardware manufacturers,
and application programmers to support a single network protocol—IP—while
breaking new ground in ease of use.

Network users no longer have to assign IP addresses, assign
host names, or even type in names to access services on the network.
Users simply ask to see what network services are available, and
choose from the list.

In many ways, this kind of browsing is even more powerful
for applications than for users. Applications can automatically
detect services they need or other applications they can interact
with, allowing automatic connection, communication, and data exchange,
without requiring user intervention.

The addressing problem is solved by self-assigned link-local
addressing. Link-local addressing uses a range of addresses reserved
for the local network, typically a small LAN or a single LAN segment.

Self-assigned addressing is simply picking a random IP address
in the link-local range and testing it. If the address in not use,
it is now your local address. If it is already in use, pick another
address and try again.

Note: Two hosts are considered to be on the same local link
if, when one host sends packets to the other, the entire link-layer
payload (the content of the packet as represented in the physical
network, such as Ethernet) arrives unmodified. In practice, on an
Ethernet network, this means that no IP router touches the packet
between the two hosts.

Self-assigned link-local addressing has already shipped on
IPv4 starting with Mac OS 8.5, Windows 98, and Mac OS X version
10.0. The IPv6 specification includes self-assigned link-local addressing.

Any user or service on a computer that supports self-assigned
link-local addressing benefits from this feature automatically.
When your host computer encounters a local network, it finds an
unused local address and adopts it. No action on your part is required.

Hardware manufacturers should implement self-assigned link-local
addressing on their devices to obtain the full benefit of Bonjour.

The proposed solution for name-to-address translation on a
local network uses multicast DNS (mDNS), in which DNS-format queries
are sent over the local network using IP multicast. Because these
DNS queries are sent to a multicast address, no single DNS server with
global knowledge is required to answer the queries. Each service
or device can provide its own DNS capability—when it sees a query
for its own name, it provides a DNS response with its own address.

Bonjour goes a bit further. It includes a responder that
handles mDNS queries for any network service on the host computer.
This relieves your application of the need to interpret and respond
to mDNS messages. Just register your service with the Bonjour mDNS
responder, and any queries for your name will be directed to your
address automatically.

For name-to-address translation to work properly, you need
a unique name on the local network. Unlike conventional DNS host
names, the local name only has significance on the local network
or LAN segment. You can self-assign a local name the same way you self-assign
a local address—choose one; if it’s not already in use, it’s
yours:

- Hardware manufacturers determine whether their
  chosen name is already use by sending an mDNS query for that name
  and looking for any response. If there is a response, choose another
  name. Devices without a user interface append an incrementally larger
  number to a default name until the name is unique. For example, if
  a printer with the default name `XYZ-LaserPrinter` attaches
  to a local network with two other identical printers already installed,
  it tests for `XYZ-LaserPrinter`,
  then `XYZ-LaserPrinter2`,
  then `XYZ-LaserPrinter3`,
  which is unused and becomes its name.
- Software services provide a local name when they register
  with Bonjour. If the provided name is already in use, Bonjour
  returns an error, and the service chooses another name.

Starting with Mac OS X version 10.2, users can set a local
host name for their computers—the Local Hostname setting in the
Sharing pane of System Preferences. The host name can be used anywhere
a conventional DNS host name is used—Web browsers, command line tools,
and so on. To indicate to the system that the name is a local host
name, append a dot (`.`)
and `local.` to the host
name — `Steve.local`.
is an example of a local host name.

For example, if a user types `steve.local.` into
a Web browser, this tells the system to multicast the request for `steve` on
the local network instead of sending it to the conventional DNS
server. If a Bonjour-enabled computer named `steve` is
on the local network, the user’s browser is sent the correct IP
address for it. This allows users to access local hosts and services
without a conventional DNS server.

For more information, see [Bonjour and Domain Names](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgqwtcojygqydo).

The final element of Bonjour is service discovery. Service
discovery allows applications to find all available instances of
a particular type of service and to maintain a list of named services.
The application can then resolve a named instance of a service to
an IP address and port number, as described in [Naming](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgqwtcojygazdo).

The list of named services provides a layer of indirection
between a service and its current IP address. Indirection enables
applications to keep a persistent list of available services and
resolve an actual network address just prior to actually using a
service. The list allows services to be relocated dynamically without
generating a lot of network traffic announcing the change.

Service discovery in Bonjour is accomplished by “browsing.”
An mDNS query is sent out for a given service type and domain, and
any matching servers reply with their names. The result is a list
of available services to choose from.

This is very different from the traditional device-centric
idea of network services. For someone who deals with servers, network
devices, and network programming, it is easy to get in the habit
of thinking about services in terms of physical hardware. In this device-centric
view, the network consists of a number of devices or hosts, each
with a set of services. For example, the network might consist of
a server machine and several client machines. In a device-centric
browsing scheme, a client queries the server for what services it
is running, gets back a list (FTP, HTTP, and so on), and decides
which service to use. The interface reflects the way the physical
system is organized. But this is not necessarily what the user logically
wants or needs.

Users typically want to accomplish a certain task, not query
a list of devices to find out what services are running. It makes
far more sense for a client to ask a single question: “What print
services are available?” than to query each available device with
the question, “What services are you running?” and sift through
the results looking for printers. The device-centric approach is
not only time-consuming, it generates a tremendous amount of network
traffic, most of it useless. The service-centric approach sends
a single query, generating only relevant replies.

Additionally, services are not tied to specific IP addresses
or even host names. For example, a website may be hosted by multiple
servers with different addresses. Within an organization, network
administrators may need to move a service from one server to another
to help balance the load. If clients store the host name (as in
most cases they now do), they will not be able to connect if the
service moves to a different host.

Bonjour takes the service-oriented view. Queries are made
according to the type of service needed, not the hosts providing
them. Applications store service names, not addresses, so if the
IP address, port number, or even host name has changed, the application
can still connect. By concentrating on services rather than devices,
the user’s browsing experience is made more useful and trouble-free.

Server-free addressing, naming, and service discovery have
the potential to create a significant amount of excess network traffic,
but Bonjour takes a number of steps to reduce this traffic to
a minimum. This allows Bonjour to attain AppleTalk’s ease of
use while avoiding any unnecessary “chattiness.”

Bonjour makes use of several mechanisms for reducing zero-configuration
overhead, including caching, suppression of duplicate responses,
exponential back-off, and service announcement, as described in
the following sections.

Bonjour uses a cache of multicast packets to prevent hosts
from requesting information that has already been requested. For
example, when one host requests, say, a list of LPR print spoolers,
the list of printers comes back via multicast, so all local hosts
see it. The next time a host needs a list of print spoolers, it
already has the list in its cache and does not need to reissue the
query. The multicast DNS responder is responsible for maintaining
the cache; application developers do not need to do anything to
maintain it.

To prevent repeated answers to the same query, Bonjour
service queries include a list of known answers. For example, if
a host is browsing for printers, the first query includes no print
services and gets, say, twelve replies from available print servers.
The next time the host queries for print services, the query includes
a list of known servers. Print servers already on the list do not
respond.

Bonjour suppresses duplicate responses in another way.
If a host is about to respond, and notices that another host has
already responded with the same information, the host suppresses
its response.

Application developers do not need to take any action to suppress
duplicate responses. Bonjour takes care of duplicate response
suppression.

When a host is browsing for services, it does not continually
send queries to see if new services are available. Instead, the
host issues an initial query and sends subsequent queries exponentially
less often: after 1 second, 2 seconds, 4 seconds, 8 seconds, and
so on, up to a maximum interval of one hour.

This does not mean that it can take over an hour for a browser
to see a new service. When a service starts up on the network, it
announces its presence with the same exponential back-off algorithm.
This way, network traffic for service announcement and discovery
is kept to a minimum, but new services are seen very quickly.

Services running on a Bonjour-equipped host are announced
automatically when they register with the mDNS responder. Services
running on other hardware, such as printers, should implement service
announcement with exponential back-off to take full advantage of
Bonjour.

Bonjour provides API support that enables applications
to register services they offer, browse for services on the network,
and obtain the current IP address and port of a given service instance.
Bonjour takes care of the low-level tasks behind these operations, such
as announcing registered services, sending mDNS queries, tracking
responses, and providing name-to-address translation for named services.

Four APIs are available:

- NSNetServices API, a Cocoa framework
- CFNetServices API, a Carbon framework
- Mach-based DNSServiceDiscovery API (described in this document
  and deprecated in favor of the socket-based DNSServiceDiscovery
  API)
- Socket-based DNSServiceDiscovery API

Cocoa programmers (Objective C) should use the NSNetServices
API. However, Cocoa programmers who need to exercise finer control
over events than offered by the NSNetServices API may want to use
the DNSServiceDiscovery API.

Carbon programmers (C/C++) should use the CFNetServices API.
Carbon programmers who are comfortable working with Mac OS X at
the Mach level may find the Mach-based DNSServiceDiscovery API simpler
to use for some applications. Note, however, that the Mach-based
DNSServiceDiscovery API is deprecated, and developers are encouraged
to use the new socket-based API.

Darwin programmers should use the socket-based DNSServiceDiscovery
API.

Documentation on all four Bonjour APIs can be found in [Bonjour Documentation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000429-TP30000566)on the ADC website.

Sample code, links to specifications, and other resources
are available at [http://developer.apple.com/networking/bonjour/](https://developer.apple.com/networking/bonjour/).

Hardware developers should examine the sample code for an
mDNS responder provided at [http://developer.apple.com/darwin](https://developer.apple.com/darwin).

Bonjour names for service instances and
service types are related to Domain Name System (DNS) domain names.
This section explains DNS domain names, the Bonjour local “domain,”
and the naming rules for Bonjour service instances and service
types.

DNS uses a specific-to-general naming scheme for domain names.
The most general domain is `.` (“dot”),
called the __root domain__, which
is akin to the root directory `/` in
a UNIX file system. Every other domain falls in a hierarchy below
the root domain. For example, the name `www.apple.com.` is
within the __second-level domain__ `apple.com.`,
which is within the __top-level domain__ `com.`,
which in turn is part of `.` (“dot”),
the root domain. Figure 1-2 shows an abridged version of this hierarchy.

__Figure 1-2__  Part of the Internet Domain Name System,
augmented for Bonjour

!

At the top of the inverted tree is the root domain. Below
it are some of the top-level domains: `com.`, `edu.`,
and `org.`, and the local
Bonjour “domain” `local.`,
discussed further in [Bonjour and the Local Link](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgqwtembsguzto). Below the top level are a few
second-level domains, `apple`, `darwin`,
and `zeroconf`. The tree
can extend infinitely downward with, for example, `www`,
at the third level.

You may have noticed that the trailing dot is left off of
most domain names. The trailing dot does, however, have meaning.
A domain name ending in a trailing period, such as `www.apple.com.`,
is known as a __fully qualified domain name__, much
like an absolute path (such as `/usr/bin`)
in a UNIX file system.

If you type `wibble.apple.com` into
your Web browser (without the trailing dot), the system will treat
it as an unqualified (partial) name and append the names from your
list of search domains, such as `apple.com.`, `earthlink.net.`, `myschool.edu`.,
etc. The system will first try to append `.` (“dot,”
the root domain), but if the name `wibble.apple.com.` doesn’t
exist, it will continue down the list and try `wibble.apple.com.apple.com.`, `wibble.apple.com.earthlink.net.`, `wibble.apple.com.myschool.edu.`,
and so on, which is almost certainly not what you wanted.

Bonjour protocols deal in large part with the part of the
network called the __local link__. A host’s local
link, or __link-local network__, includes itself
and all other hosts that can exchange packets without IP header
data being modified. In practice, this includes all hosts not separated
by a router.

On Bonjour systems, `local.` is
used to indicate a name that should be looked up using an IP multicast
query on the local IP network.

Note that `local.` is
not really a domain. You can think of `local.` as
a pseudo-domain. It differs from conventional DNS domains in a fundamental
way: names within other domains are globally unique; link-local
domain names are not. There is only one logical DNS entry in the
world named `www.apple.com.`,
and because of the way DNS works, there can be only one. Host names
ending in `local.`, on
the other hand, are managed by a collection of multicast DNS responders
on the local network, so the naming scope is just that: local. There
can easily be two hosts named `meow.local.` in
the world, or even the same building, just not on the same local
network.

Globally unique names are important and useful—in fact,
they are one of the significant achievements of the Internet—but
they require a certain level of administrative effort to set up
and maintain. Local names are useful only on the local network,
but in cases where that is adequate, they provide a way to refer
to network devices using names instead of IP numbers, and of course
they require less effort and expense to coordinate than globally unique
names.

Globally unique names are particularly useful on local networks
that have no connection to the global Internet, either by design
or because of interruption, and on small, temporary networks, such
as a pair of computers linked by a crossover cable, or a few people
playing network games using laptops on the wireless network of a
home or cafe.

If a name collision on the local network occurs, a Bonjour
host finds a new name automatically (in the case of a device without
a screen) or by asking the user (in the case of a personal computer).

Bonjour service types are named according to the existing
Internet standard for IP services. The Internet Assigned Numbers
Authority (IANA) keeps a registry of TCP and UDP protocol names
and ports assigned to each, and Bonjour services are named according
to this list. The list used by Mac OS X can be found in `/etc/services`,
and the most current version of the list is on the IANA website
at [http://www.iana.org/assignments/port-numbers](http://www.iana.org/assignments/port-numbers).

In order to distinguish services from domain names in DNS
resource records, components of service type names include underscore
prefixes. The format for Bonjour service type names is thus

`_`_ApplicationProtocolName_`._`_TransportProtocolName_`.`

The application protocol name is the official IANA-registered
name for the protocol, for example, `ftp`, `http` or `printer`,
as described above. The transport protocol name is either `tcp` or `udp`,
depending on the transport protocol the service uses. An FTP service
running over TCP would have a service type of `_ftp._tcp`.
Services of this type would register DNS PTR records named `_ftp._tcp.local.` with
their hosts’ multicast DNS responders.

If you are designing a new protocol to advertise as a Bonjour
network service, you should register it with IANA at [http://www.iana.org](http://www.iana.org/) or [http://www.dns-sd.org/ServiceNames.html](http://www.dns-sd.org/ServiceNames.html).

The IANA currently requires that every registered service
be associated with a “well-known port” or range of well-known
ports. For example, `http` is
assigned port `80`, so that
whenever you visit a website in your web browser, the application
assumes that the HTTP service is running on port `80` unless
you specify otherwise. This way, the port number for a website need
only be memorized if the website is configured in a non-standard
way.

With Bonjour, however, you don’t have to know about port
numbers. Because client applications can discover your service with
a simple query for the service type, well-known ports are unnecessary.
At some point in the future, IANA may begin registering protocol
names without requiring an associated well-known port.

Service instance names are intended to be human-readable strings.
As such, you should name them descriptively, and let the user override
whatever default name you provide. Because they are intended to
be browsed rather than typed, service instance names can be any
Unicode string encoded with UTF-8, up to 63 octets (bytes) in length.

For example, an application for sharing music over the network
might use the local user’s name for a music sharing service, such
as `Ed's Music Library`,
by default. The user could override the default and name the service `Zealous
Lizard's Tune Studio`, and the application
would register a DNS SRV record named
`Zealous Lizard's Tune Studio._music._tcp.local.`,
assuming the application’s music sharing protocol was associated
with the name `music`.

[Figure 1-3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmrzfvbuqmrqgqwtcojyhaytq) illustrates the organization of the name of a Bonjour
service instance. At the top level of the tree is the domain, such
as `local.` for the local
network. Below the domain is the service type, which consists of
the protocol name preceded by an underscore (`_music`) and
the transport protocol, also preceded by an underscore (`_tcp`).
At the bottom of the tree is the human-readable service instance
name, such as `Zealous Lizard’s Tune Studio`.
The complete name is a path along the tree from bottom to top, with
each component separated by a dot.

__Figure 1-3__  Organization of a Bonjour service
name

!

[Next](DNSServiceDiscovery%20Tasks.md)[Previous](Introduction.md)

