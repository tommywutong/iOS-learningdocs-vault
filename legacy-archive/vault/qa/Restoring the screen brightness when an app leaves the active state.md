---
title: Restoring the screen brightness when an app leaves the active state
apple_id: DTS40013391
resource_type: QA
platform: iOS
topic: User Experience
technology: null
published: '2013-06-04'
source_url: https://developer.apple.com/library/archive/qa/qa1751/_index.html
archived_at: '2026-07-18T02:34:35.634799Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1751

# Restoring the screen brightness when an app leaves the active state

## Q:  Why can't I restore the brightness of the screen after I've set it using the UIScreen brightness property, and my app has left the active state?

A: The operating system will restore the user's original brightness setting at a future time it deems appropriate. It is not the developer's responsibility to restore the brightness, and as you may have seen you cannot set the brightness once the app leaves the foreground. This behavior is by design.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-06-04 | New document that explains more about the brightness property of the UIScreen class |

