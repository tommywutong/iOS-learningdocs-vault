---
title: Problems getting Bonjour TXT record information
apple_id: DTS10003473
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2005-07-06'
source_url: https://developer.apple.com/library/archive/qa/qa1389/_index.html
archived_at: '2026-07-18T02:30:29.579360Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1389

# Problems getting Bonjour TXT record information

## Q:  Why would `CFNetServiceGetProtocolSpecificInformation`, `CFNetServiceGetTXTData`, `protocolSpecificInformation`, or `TXTRecordData` return `NULL`?

A: Why would `CFNetServiceGetProtocolSpecificInformation`, `CFNetServiceGetTXTData`, `protocolSpecificInformation`, or `TXTRecordData` return `NULL`?

The above functions will return `NULL` if you fail to resolve the `CFNetServiceRef` or `NSNetService`. Simply use `CFNetServiceResolve` or `resolve` in order to resolve the service first, and after your resolve callback is called, you can then use `CFNetServiceGetProtocolSpecificInformation` or `protocolSpecificInformation` to retrieve the TXT record information.

Starting in Mac OS X 10.4, the previously mentioned APIs are deprecated, so you should use the newer more efficient `CFNetServiceResolveWithTimeout` or `resolveWithTimeout:` to resolve the service, followed by `CFNetServiceGetTXTData` or `TXTRecordData` to retrieve the TXT record information. The newer TXT record retrieval APIs return a `CFDataRef` or `NSData` object that can be converted into a `CFDictionaryRef` of `NSDictionary` for easy parsing into key/value pairs.

If you decide to monitor the TXT record information by using `CFNetServiceMonitorStart` or `startMonitoring`, then you don't need to resolve the service first. The monitoring APIs were introduced in Mac OS X 10.4.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-07-06 | New document that explains why you might have problems retrieving TXT record information from a CFNetServiceRef or NSNetService. |

