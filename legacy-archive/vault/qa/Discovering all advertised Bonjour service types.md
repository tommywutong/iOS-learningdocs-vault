---
title: Discovering all advertised Bonjour service types
apple_id: DTS10003319
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2004-06-01'
source_url: https://developer.apple.com/library/archive/qa/qa1337/_index.html
archived_at: '2026-07-18T02:30:25.215501Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1337

# Discovering all advertised Bonjour service types

## Q:  Is it possible to dynamically discover every Bonjour service type being advertised on the network?

A: Is it possible to dynamically discover every Bonjour service type being advertised on the network?

Yes. Devices running mDNSResponder-58.6 (Mac OS X 10.3.4) or later will respond to the "Service Type Enumeration" meta-query described in Section 10 of the [DNS-SD specification](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt). Issuing a Multicast DNS PTR record query for the name "_services._dns-sd._udp.local." will return a list of service types being advertised on the local network.

Queries for "_services._dns-sd._udp.local." behave somewhat differently than standard mDNS queries. Normal mDNS long-lived queries will return ADD/REMOVE events as records are registered and deregistered, however, a service type enumeration meta-query will not be told about REMOVE events when a service is deregistered. Otherwise, the meta-query behaves identically to a standard mDNS query. It will receive REMOVE events when a network interface is disabled or if the PTR record expires from the cache naturally.

You can issue this meta-query by using `DNSServiceQueryRecord` from the socket-based DNSServiceDiscovery API, located in `/usr/include/dns_sd.h`. For each DNS-SD service type being advertised, the callback will return a DNS PTR record containing a service type and domain. For example, if someone is advertising an HTTP service on the local network, the `DNSServiceQueryRecord` callback will return a PTR record which points to "_http._tcp.local.".

The [DNSServiceMetaQuery](https://developer.apple.com/samplecode/DNSServiceMetaQuery/DNSServiceMetaQuery.html) sample code shows how to issue the service type enumeration meta-query.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-06-01 | New document that explains how to discover all Bonjour service types being advertised on the local network. |

