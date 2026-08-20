---
title: Bonjour Printer Subtype for HTTP
apple_id: DTS40007476
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: null
published: '2008-03-25'
source_url: https://developer.apple.com/library/archive/qa/qa1555/_index.html
archived_at: '2026-07-18T02:32:18.113507Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1555

# Bonjour Printer Subtype for HTTP

## Q:  How do I get my printer to show up in the Printers section of Safari's Bonjour browser?

A: How do I get my printer to show up in the Printers section of Safari's Bonjour browser?

Starting in Mac OS X 10.5 Leopard, Safari's Bonjour browser displays Bonjour enabled printers in their own section. If you make a Bonjour enabled network printer, you can enable your printer to appear in the Printers section by registering a service of type `_http._tcp` with a subtype of `_printer`. This can be accomplished using the [standard registration APIs](https://developer.apple.com/networking/bonjour/) by using a service type of  `_http._tcp,_printer`; notice the comma after _tcp.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-03-25 | Restructured the document to clarify possible ambiguities. |
| 2008-03-20 | New document that describes how printer vendors can register their bonjour service such that Safari can see them. |

