---
title: Does Safari support 128-bit encryption?
apple_id: DTS10002346
resource_type: QA
platform: macOS
topic: System Administration
technology: null
published: '2010-04-13'
source_url: https://developer.apple.com/library/archive/qa/qa1320/_index.html
archived_at: '2026-07-18T02:30:22.764204Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1320

# Does Safari support 128-bit encryption?

## Q:  I'm building a secure website, and I require a browser which supports 128-bit encryption. Does Safari support 128-bit encryption for secure network connections?

A: I'm building a secure website, and I require a browser which supports 128-bit encryption. Does Safari support 128-bit encryption for secure network connections?

Yes, all versions of Safari do support 128-bit encryption as part of its security model. All versions of Safari use the Secure Transport API from Mac OS X's Security Framework for all secure connections. For more information about Security on Mac OS X, or the Secure Transport API, please review the following references:

- [Mac OS X Security](https://developer.apple.com/security)
- [Secure Transport Reference](https://developer.apple.com/documentation/Security/Reference/secureTransportRef/index.html)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-04-13 | Updated to explicitly say "all versions of Safari". |
| 2004-09-10 | Minor edits to URLs. |
| 2004-05-12 | Removed changed URLs. |
| 2003-10-23 | New document that discusses support for 128-bit encryption in Apple's Safari web browser. |

