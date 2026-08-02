---
title: 2D Graphics Release Notes for OS X v10.5
apple_id: TP40006640
resource_type: Release Note
platform: macOS
topic: Graphics & Animation
technology: null
published: '2008-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/GraphicsImaging/RN-CoreImage/index.html
archived_at: '2026-07-18T02:58:39.358695Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# 2D Graphics Release Notes for OS X v10.5

This release note describes important changes for applications that use Core Image or Quartz 2D.

#### Contents:

- [Core Image Filters Behavior Changes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mi)
- [Performance Implications for Applications Using Garbage Collection](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dmnbqfvbuqmjnirxw45cmnfxgwrlmmvwwk3tujfcf6mq)

### Core Image Filters Behavior Changes

Two Core Image filters—CILinearGradient and CILineScreen—behave differently on OS X v10.5 as compared to OS X v10.4. These changes are implemented in a backwards compatible way. For applications compiled on OS X v10.4, these filters continue to behave on OS X v10.5 as they did previously. However, for applications compiled on OS X v10.5 or later, these filters adopt the new behavior:

- CILinearGradient. On OS X v10.4, the gradient incorrectly renders `inputColor0` at `inputPoint1` and `inputColor1` at `inputPoint0`. On OS X v10.5, the gradient renders `inputColor0` at `inputPoint0`.
- CILineScreen. The `inputSharpness` parameter on OS X v10.4 reaches maximal sharpness at `0.0`, which is inconsistent with all other halftone filters (CICircularScreen, CIDotScreen, CIHatchedScreen). On OS X v10.5, all halftone filters reach maximal sharpness at `1.0`.

### Performance Implications for Applications Using Garbage Collection

Garbage collection introduces slight overhead in code execution that is typically not significant for most applications; however, graphically intensive applications may see some performance impact.

There is a known issue with garbage-collected applications using Core Image to process frames from Core Video; the frame memory does not get collected, and the process eventually runs out of address space. If your application processes video frames using Core Image, enabling garbage collection is not recommended.
