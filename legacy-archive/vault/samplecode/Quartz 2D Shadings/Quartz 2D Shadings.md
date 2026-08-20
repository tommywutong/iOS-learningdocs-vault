---
title: Quartz 2D Shadings
apple_id: DTS10004363
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2007-08-31'
source_url: https://developer.apple.com/library/archive/samplecode/Quartz2DShadings/Introduction/Intro.html
archived_at: '2026-07-18T03:21:26.009170Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# Quartz 2D Shadings

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2007-08-31 Shows how to use CGShading and CGGradient objects to draw simple gradients. |
| __Build Requirements:__ | Mac OS X 10.5 and Xcode 3.0 |
| __Runtime Requirements:__ | Mac OS X 10.5 |

Quartz 2D Shadings demonstrates how to create gradient fills using both the new CGGradientRef objects introduced in Mac OS X 10.5 and using the older CGShadingRef and CGFunctionRef objects available since Mac OS X 10.2. In this sample, both object types are used to obtain identical results, demonstrating how CGGradientRef objects are easier to use than CGShadingRef objects. In general CGShadingRef objects are more flexible, capable of creating shadings that a CGGradientRef object cannot. If you need a linear gradient, then it is much simpler to use a CGGradientRef object. If you need to create non-linear gradients, or some other kind of custom blending, then CGShadingRef objects will allow you to express such gradients, as they use user specified CGFunctionRef object to generate their colors.

[Next](main.m.md)

