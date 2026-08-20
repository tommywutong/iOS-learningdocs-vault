---
title: NSL and how it relates to Bonjour
apple_id: DTS10002325
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2003-09-18'
source_url: https://developer.apple.com/library/archive/qa/qa1299/_index.html
archived_at: '2026-07-18T02:30:22.434114Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1299

# NSL and how it relates to Bonjour

## Q:  I thought NSL was a protocol independent way for applications to discover network services. How does NSL relate to Bonjour?

A: I thought NSL was a protocol independent way for applications to discover network services. How does NSL relate to Bonjour?

NSL is a protocol independent library which has existed since Mac OS 8.5, but it predominately uses Service Location Protocol (SLP) and AppleTalk for service discovery of URLs. In Mac OS X 10.2, Apple introduced three new APIs that use Bonjour for service discovery. The new APIs are [CFNetServices](https://developer.apple.com/documentation/Networking/Conceptual/CFNetwork/Chapter_1/chapter_2_section_6.html), [NSNetServices](https://developer.apple.com/documentation/Cocoa/Reference/Foundation/ObjC_classic/Classes/NSNetService.html) and [DNSServiceDiscovery](https://developer.apple.com/documentation/Networking/Conceptual/dns_discovery_api/index.html).

Currently, the lower level NSL API cannot be used to register or browse for Bonjour services. However, the high level "Connect To Server" dialog, which you get by calling `NSLStandardGetURL`, can be used to browse for Bonjour services.

If your application is targeted to run on Mac OS X 10.2 and later, Apple highly recommends that you use the Bonjour APIs directly for your service discovery needs, instead of NSL.

For more information on Bonjour, please visit the [Bonjour Developer Web Site](https://developer.apple.com/bonjour/).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2003-09-18 | New document that explains the relationship between NSL and Bonjour. |

