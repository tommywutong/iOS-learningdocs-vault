---
title: Why are my shadows drawn upside down in iOS 3.2 and later?
apple_id: DTS40010278
resource_type: QA
platform: iOS
topic: Graphics & Animation
technology: null
published: '2010-08-31'
source_url: https://developer.apple.com/library/archive/qa/qa1706/_index.html
archived_at: '2026-07-18T02:34:14.812305Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1706

# Why are my shadows drawn upside down in iOS 3.2 and later?

## Q:  Why are shadows in my app rendered upside down?

A: Beginning in iOS 3.2 the base coordinate space for CGContexts was changed to match the normal rendering (user) coordinate space of top-left instead of bottom-left. Shadows and Patterns drawn using the Quartz APIs use the base coordinate space, so they are affected by this change. Apps linked before iOS 3.2 will still get the old incorrect behavior, even when running on iOS 3.2 or later iOS versions. In order to support iOS 3.1.x or earlier iOSes, you will need to check the OS version and adjust the shadow offsets accordingly.

In iOS 3.1.3 and earlier shadows offsets have the following characteristics:

- An x-offset, which specifies how far in the horizontal direction the shadow is offset from the image. Positive values indicate rightward displacement, and negative values indicate leftward displacement.
- A y-offset, which specifies how far in the vertical direction the shadow is offset from the image. Positive values indicate upward displacement, and negative values indicate downward displacement.

In iOS 3.2 and later shadows offsets have the following characteristics:

- An x-offset, which specifies how far in the horizontal direction the shadow is offset from the image. Positive values indicate rightward displacement, and negative values indicate leftward displacement.
- A y-offset, which specifies how far in the vertical direction the shadow is offset from the image. Positive values indicate downward displacement, and negative values indicate upward displacement.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-08-31 | New document that describes the change in shadow behavior in iOS 3.2 and later |

