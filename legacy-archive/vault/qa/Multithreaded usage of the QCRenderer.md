---
title: Multithreaded usage of the QCRenderer
apple_id: DTS40007966
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2008-09-08'
source_url: https://developer.apple.com/library/archive/qa/qa1538/_index.html
archived_at: '2026-07-18T02:32:15.445443Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1538

# Multithreaded usage of the QCRenderer

## Q:  My application uses the QCRenderer to render Quartz Compositions on multiple threads. Is there anything I should know in order to ensure correct operation?

A: My application uses the QCRenderer to render Quartz Compositions on multiple threads. Is there anything I should know in order to ensure correct operation?

When using the QCRenderer in a multithreaded application, you should always ensure that any renderers you create are also used on the same thread that they are created on. If you fail to do so, then you will find that some content (such as Quicktime Movies) may not render correctly or at all, and you will find that your application's memory usage will increase slowly for each QCRenderer you create and use on different threads.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-08 | New document that describes an issue that may arise when using the QCRenderer in a multi-threaded application. |

