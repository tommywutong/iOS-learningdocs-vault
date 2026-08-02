---
title: Bonjour enforces the TXT record format in Panther
apple_id: DTS10002339
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1306/_index.html
archived_at: '2026-07-18T02:30:22.510893Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1306

# Bonjour enforces the TXT record format in Panther

## Q:  I'm using the socket-based DNSServiceDiscovery API introduced in Mac OS X 10.3, and my call to `DNSServiceRegister` is returning -65549. What's going on?

A: I'm using the socket-based DNSServiceDiscovery API introduced in Mac OS X 10.3, and my call to `DNSServiceRegister` is returning -65549. What's going on?

Starting in Mac OS X 10.3, mDNSResponder requires that registered records, including TXT records, be properly formatted according to the DNS specification. If your TXT record is incorrectly formatted, you'll see a message in the system log (/var/log/system.log) similar to Listing 1.

__Listing 1__  System log message indicating illegally formatted TXT record

```
Sep 15 16:06:13 localhost mDNSResponder[192]: Attempt to register record with invalid rdata: 17 Ice Cube._http._tcp.local. TXT ath=/index.html
```

The [DNS-SD protocol specification](http://files.dns-sd.org/draft-cheshire-dnsext-dns-sd.txt) describes the format for Bonjour TXT records as consisting of "zero or more strings, packed together in memory without any intervening gaps or padding bytes for word alignment. The format of each constituent string within the DNS TXT record is a single length byte, followed by 0-255 bytes of text data."

__Listing 2__  TXT record formated as length byte, data, length byte, data...

```
\011txtvers=1\020path=/index.html\025note=Bonjour Is Cool!
```

In Mac OS X 10.2.x, the Bonjour APIs use an ASCII 1 ("\001") as the boundary marker between constituent strings within the DNS TXT record, and then the TXT record is automatically converted to the correct format.

__Listing 3__  TXT record formatted with ASCII 1 as boundary marker

```
txtvers=1\001path=/index.html\001note=Bonjour Is Cool!
```

In Mac OS X 10.3 and later, CFNetServices, NSNetSerivces and the Mach-based DNSServiceDiscovery APIs will continue to use ASCII 1 as the boundary marker, however, newly introduced socket-based routines like `DNSServiceRegister` and `DNSServiceRegisterRecord` require that TXT records be properly formatted as length byte, data, length byte, data...

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2018-06-04 | Moved to Retired Documents Library. |
| 2004-07-14 | Updated TXT record example |
|  | New document that explains how mDNSResponder enforces the proper TXT record format in Panther. |

