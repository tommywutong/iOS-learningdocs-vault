---
title: The state of mDNSResponder
apple_id: DTS10003188
resource_type: QA
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2006-10-03'
source_url: https://developer.apple.com/library/archive/qa/qa1339/_index.html
archived_at: '2026-07-18T02:30:25.256135Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1339

# The state of mDNSResponder

## Q:  Is it possible to retrieve information regarding the current internal state of mDNSResponder?

A: Is it possible to retrieve information regarding the current internal state of mDNSResponder?

Yes. Starting in Mac OS X 10.3, you can send a `SIGINFO` signal to the mDNSResponder daemon which will cause it to output its current internal state to the system log (`/var/log/system.log`). This allows you to retrieve information about mDNSResponder's cached DNS resource records, and it allows you to see the active DNS Service Discovery (DNS-SD) operations. You can send the `SIGINFO` signal from the Terminal by typing:

`$ sudo killall -info mDNSResponder`

__Listing 1__  Example system.log containing mDNSResponder state info.

```
mDNSResponder-58.4 (Jan 28 2004 16:31:36) ---- BEGIN STATE LOG ---- Active: PTR  en1     26 _ftp._tcp.local. PTR Ice Cube._ftp._tcp.local. Inactive: SRV  en1     22 Ice Cube._ftp._tcp.local. SRV Ice-Cube.local. Inactive: TXT  en1      1 Ice Cube._ftp._tcp.local. TXT  Inactive: PTR  en1     26 _ssh._tcp.local. PTR Ice Cube._ssh._tcp.local. Inactive: Addr en1      4 Ice-Cube.local. Addr 10.0.1.2 Cache currently contains 5 records; 1 referenced by active questions 11251: ServiceBrowse       _http._tcp.local. 10755: ServiceBrowse       _ftp._tcp.local. 10499: ServiceBrowse       _webdav._tcp.local. 10243: ServiceBrowse       _nfs._tcp.local.  9731: ServiceBrowse       _afpovertcp._tcp.local.  8195: ServiceRegistration Ice Cube._ssh._tcp.local.  7939: ServiceRegistration Ice Cube._ftp._tcp.local. mDNSResponder-58.4 (Jan 28 2004 16:31:36) ---- END STATE LOG ----
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-10-03 | Updated SIGUSR1 comment for Linux, BSD, and Solaris. |
| 2004-02-06 | New document that explains how to obtain information regarding the internal state of mDNSResponder. |

