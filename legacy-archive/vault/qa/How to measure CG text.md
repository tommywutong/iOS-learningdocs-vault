---
title: How to measure CG text
apple_id: DTS10001603
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2007-08-02'
source_url: https://developer.apple.com/library/archive/qa/qa1051/_index.html
archived_at: '2026-07-18T02:29:54.972937Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1051

# How to measure CG text

## Q:  How do I measure the width of my text before drawing it with Core Graphics?

A: First call CGContextGetTextPosition to find the current text position. Then, set the text drawing mode to kCGTextInvisible using CGContextSetTextDrawingMode and draw the text. Finally, call CGContextGetTextPosition again to determine the final text position. Take the difference between the starting and ending positions to find the width of your text.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2007-08-02 | minor cleanup and made 'Not Recomended' |
| 2001-07-02 | New document that explains how to measure Core Graphics text. |

