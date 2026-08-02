---
title: Quartz 2D Thread Safety
apple_id: DTS10001758
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-08-13'
source_url: https://developer.apple.com/library/archive/qa/qa1238/_index.html
archived_at: '2026-07-18T02:30:17.634334Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1238

# Quartz 2D Thread Safety

## Q:  Is Quartz 2D thread safe?

A: Quartz is thread safe on the whole, but individual Quartz objects are not. In general, you can operate on any object on any thread as long as you guarantee that no two threads are operating on the same object simultaneously. The easiest way to achieve this is to not share your objects between threads.

There are several additional things you need to watch out for:

- If you have multiple CGContextRefs drawing to the same window or bitmap context and the content of those CGContextRefs overlaps, then you will get undefined behavior.
- In the case of multiple CGPDFContextRefs, trying to draw to different CGPDFContextRefs that point to the same CGDataConsumerRef doesn't make sense.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-13 | Updated formatting. |
| 2003-02-25 | New document that explains the thread-safety issues for the Quartz 2D API. |

