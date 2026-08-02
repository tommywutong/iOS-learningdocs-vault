---
title: Why aren't my tracking rects working?
apple_id: DTS10003338
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2004-12-02'
source_url: https://developer.apple.com/library/archive/qa/qa1355/_index.html
archived_at: '2026-07-18T02:30:25.976105Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1355

# Why aren't my tracking rects working?

## Q:  I'm trying to implement tracking rectangles so that I can recieve `-mouseEntered:` and `-mouseExited:` messages and provide visual feedback to the user. I've sent my view an `-addTrackingRect:owner:userData:assumeInside:` message, but it seems to have no effect.

A: This symptom usually results from trying to set tracking rectangles before your view has been added to a window.

Although NSView implements the `-addTrackingRect:owner:userData:assumeInside:` method, the list of tracking rectangles is kept by the window, not the view. When your `-initWithFrame:` method is executed, your view is not yet associated with any window, so the view can't actually set any tracking rects.

A better place to send your `-addTrackingRect:`.. messages is in a `-viewDidMoveToWindow:` or `-awakefromNib` method.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | Describes a common mistake in setting up cursor-tracking rectangles. |
| 2004-12-02 | New document that describes a common mistake in setting up cursor-tracking rectangles. |

