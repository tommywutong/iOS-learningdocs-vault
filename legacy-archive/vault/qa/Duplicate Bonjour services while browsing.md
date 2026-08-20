---
title: Duplicate Bonjour services while browsing
apple_id: DTS10003187
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2004-02-06'
source_url: https://developer.apple.com/library/archive/qa/qa1333/_index.html
archived_at: '2026-07-18T02:30:25.180501Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1333

# Duplicate Bonjour services while browsing

## Q:  While browsing for Bonjour services using CFNetSevices, NSNetServices or DNSServiceDiscovery, I sometimes get multiple ADD events containing identical service names. Why does that happen?

A: While browsing for Bonjour services using CFNetSevices, NSNetServices or DNSServiceDiscovery, I sometimes get multiple ADD events containing identical service names. Why does that happen?

This happens when your computer has more than one network interface enabled because, by default, Bonjour browses on all active interfaces. So for example, if your computer has an Ethernet connection and an AirPort connection, and a service is being advertised on both Ethernet and AirPort, your callback will be called twice containing the same service name.

With CFNetServices and NSNetSerivces, there's no way to know which network interface the service was discovered on, so it's best to assume that both service names represent the same service. You probably don't want to show the same name multiple times in a list of services, so you should do reference counting of each service name. Every time you get an ADD event for a service name you should increment the reference count, and for each REMOVE event, you should decrement the reference count. When the reference count reaches zero, you should remove the service name from your browser list. When it comes time to Resolve a service that was discovered on multiple network interfaces, it makes no difference which CFNetServiceRef or NSNetService object you use to initiate the Resolve, because the Resolve query gets sent on every network interface.

With the newer DNSServiceDiscovery API, located in `/usr/include/dns_sd.h`, your browse callback will return a network interface ID that corresponds to the interface on which the service was discovered. This gives you the option of displaying the service name multiple times along with extra information describing the network interface. For example, you could display a service name with the text "en1" or "AirPort" appended to the name, or you could simply display an AirPort icon next to the service name if the service was discovered over AirPort. However, if you're using the DNSServiceDiscovery API and thus can distinguish services on different interfaces, it may still make sense to show each service name only once (using the reference counting approach described above) because this makes the user interface simpler.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-02-06 | New document that explains how to work with multiple network interfaces when browsing for Bonjour services. |

