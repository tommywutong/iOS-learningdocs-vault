---
title: Clearing mDNSResponder's cached records
apple_id: DTS10002381
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2004-02-11'
source_url: https://developer.apple.com/library/archive/qa/qa1310/_index.html
archived_at: '2026-07-18T02:30:22.538649Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1310

# Clearing mDNSResponder's cached records

## Q:  While developing my Bonjour enabled hardware device, sometimes my device crashes or changes its service name without sending a "Goodbye" packet, so the old service name will continue to appear in the browser list on my Mac. Is it possible to manually clear these stale service entries without rebooting the machine?

A: While developing my Bonjour enabled hardware device, sometimes my device crashes or changes its service name without sending a "Goodbye" packet, so the old service name will continue to appear in the browser list on my Mac. Is it possible to manually clear these stale service entries without rebooting the machine?

Yes, it's possible. Bonjour caches DNS resource records for network efficiency reasons, but if a device abruptly vanishes from the network without sending a "Goodbye" packet, then other machines won't know that it's gone, so the data will remain in everyone's cache. The "Goodbye" packet is described in Section 13.2 of the [Multicast DNS protocol specification](http://files.multicastdns.org/draft-cheshire-dnsext-multicastdns.txt). While Bonjour implements techniques to gradually purge these stale records, there may be times when you'll want to manually clear the cache.

If you try to Resolve a service name and get no answer, then in about fifteen seconds, mDNSResponder will remove that stale record from its cache. Any machine that has an active Browse call for that service type will then get a "Remove" event for that instance. Therefore, attempting to use a stale service is one way to flush it from the cache.

Physical disconnection is another way to flush records from the cache. To clear the services discovered over Ethernet, you can unplug the Ethernet cable, wait 5 seconds, and then plug the cable back in. Alternatively, you can go into the "Network Port Configurations" section of the Network preference panel, uncheck the box next to "Built-in Ethernet", click "Apply", then re-check the box and click "Apply".

To clear the services discovered over AirPort, you can turn off AirPort from the AirPort icon in the menu bar, wait 5 seconds, and then turn it back on. Alternatively, you can go into the "Network Port Configurations" section of the Network preference panel, uncheck the box next to "AirPort", click "Apply", then re-check the box and click "Apply".

Starting in Mac OS X 10.3 (mDNSResponder-58), putting the computer to sleep will clear all cached resource records on all network interfaces.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-02-11 | New document that clearing the Bonjour service cache (mDNSResponder's cached records) for testing purposes. |

