---
title: Does CGContextSaveGState save the current path?
apple_id: DTS10001608
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-08-13'
source_url: https://developer.apple.com/library/archive/qa/qa1056/_index.html
archived_at: '2026-07-18T02:29:55.003259Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1056

# Does CGContextSaveGState save the current path?

## Q:  Does CGContextSaveGState save the current path?

A: No. Core Graphics follows the PDF specification in this regard. CGContextSaveGState and CGContextRestoreGState do not save and restore the path. In order to redraw a path you must either recreate it from scratch or use CGContextCopyPath(CGContextRef context) to create a copy of the current path as a CGPathRef object.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-13 | Updated formatting and added information about CGContextCopyPath. |
| 2001-10-02 | New document that explains that the Core Graphics save and restore GState APIs do not affect the path. |

