---
title: Unexpected CG state changes
apple_id: DTS10001597
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-08-13'
source_url: https://developer.apple.com/library/archive/qa/qa1045/_index.html
archived_at: '2026-07-18T02:29:54.888357Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1045

# Unexpected CG state changes

## Q:  Why does my Core Graphics drawing state change unexpectedly?

A: If you are using any of the convenience functions, such as CGContextStrokeRectWithWidth, be aware that they make use of the state variables and don't restore them. CGContextStrokeRectWithWidth, for example, clears the current path and changes the line width.

If you want to preserve the current settings, use CGContextSaveGState and CGContextRestoreGState. Note that even these APIs don't save the path. The only way to restore the path is to recreate it or use CGContextCopyPath(CGContextRef context) to create a copy of the current path as a CGPathRef object.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-13 | Updated formatting. |
| 2001-07-02 | New document that explains why the Core Graphics drawing state sometimes changes for no apparent reason. |

