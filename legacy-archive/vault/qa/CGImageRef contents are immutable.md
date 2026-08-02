---
title: CGImageRef contents are immutable
apple_id: DTS10002305
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-08-13'
source_url: https://developer.apple.com/library/archive/qa/qa1276/_index.html
archived_at: '2026-07-18T02:30:21.120150Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1276

# CGImageRef contents are immutable

## Q:  Am I allowed to change the contents of a CGImageRef after it has been created?

A: No. Quartz 2D considers the contents of a CGImageRef to be constant after creation. This allows several optimizations, including caching the contents as necessary to improve performance. In addition, this allows the printing system on Mac OS X to properly handle documents with many copies of the same image and only embed one copy in the resulting PDF spool file.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-13 | Updated formatting. |
| 2003-07-17 | New document that explains that CGImageRef contents are considered immutable once created. |

