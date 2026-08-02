---
title: Is QuickTime thread-safe?
apple_id: DTS10001637
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2006-02-14'
source_url: https://developer.apple.com/library/archive/qa/qa1088/_index.html
archived_at: '2026-07-18T02:29:55.767289Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1088

# Is QuickTime thread-safe?

## Q:  Is QuickTime thread-safe? For example, is it possible to use a Decompression Session in one thread, and use QuickTime to play audio in another thread?

A: The answer originally discussed in this Q&A has been expanded upon and moved to [Technical Note TN2125, 'Thread-safe programming in QuickTime'](https://developer.apple.com/technotes/tn/tn2125.html)

Developers interested in calling QuickTime from background threads are encouraged to read the above document to gain a sense of how to best take advantage of this capability from within their applications.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2006-02-14 | Removed obsolete information and added link to Technical Note superseding this Q&A |
| 2001-11-01 | New document that discusses thread-safety and reentrancy of the QuickTime library on both Mac & Windows. |

