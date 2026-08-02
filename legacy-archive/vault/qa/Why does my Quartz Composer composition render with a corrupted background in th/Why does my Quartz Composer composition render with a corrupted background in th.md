---
title: Why does my Quartz Composer composition render with a corrupted background
  in the QCView?
apple_id: DTS10003644
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/qa/qa1434/_index.html
archived_at: '2026-07-18T02:30:41.293187Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1434

# Why does my Quartz Composer composition render with a corrupted background in the QCView?

## Q:  Why does my Quartz Composer composition render with a corrupted background in the QCView?

A: When rendered in a QCView, some compositions will show corrupted pixels in the background, as in the following example:

__Figure 1__  A composition rendering with a corrupted background in a QCView.

!

The reason is that such compositions do not paint the background of the view. When viewed in Quartz Composer viewer window, those compositions do not show corrupted background pixels since the background is "forced clear" to a white-gray checkerboard (unless this is explicitly disabled in the Viewer menu). The areas of the background not painted by the composition are where the checkerboard is visible:

__Figure 2__  The same composition displayed in the Quartz Composer Viewer window.

!

To fix the issue and have the composition not show corrupted pixels in the QCView, make sure it paints its entire background (using a Clear patch or a Gradient patch for example) and the checkerboard is not visible anymore.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | Describes the circumstances in which the QCView background may render corrupted. |
| 2005-06-01 | New document that describes the circumstances in which the QCView background may render corrupted. |

