---
title: Turning Off Core Graphics Clipping
apple_id: DTS10001602
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-08-13'
source_url: https://developer.apple.com/library/archive/qa/qa1050/_index.html
archived_at: '2026-07-18T02:29:54.921145Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1050

# Turning Off Core Graphics Clipping

## Q:  I've used CGContextClip, CGContextEOClip, CGContextClipToRect, or CGContextClipToRects to modify the clipping path for the current context. However, all of these functions intersect the current clipping path with the new path. How do I reset or turn off the clipping path?

A: In order to clear the clipping path, you must save the graphics state for the context using CGContextSaveGState before you alter the clipping path. You can then reset the clipping path to its original state by calling CGContextRestoreGState.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-13 | Updated formatting. |
| 2001-07-02 | New document that explains how to clear the clipping path for a CGContext. |

