---
title: How to pause the animation of a layer tree
apple_id: DTS40010053
resource_type: QA
platform: iOS|macOS
topic: Graphics & Animation
technology: QuartzCore
published: '2011-08-22'
source_url: https://developer.apple.com/library/archive/qa/qa1673/_index.html
archived_at: '2026-07-18T02:33:42.720899Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1673

# How to pause the animation of a layer tree

## Q:  How do I pause all animations in a layer tree?

A: In order to pause animations in a layer tree, you can take advantage of the fact that a `CALayer` conforms to the `CAMediaTiming` protocol. The `CAMediaTiming` protocol defines, among other things, a speed with which its timeline progresses, which you can use to pause all animations on the target layer. Listing 1 demonstrates how you can do this.

__Listing 1__  Pause and Resume animations.

```objc
-(void)pauseLayer:(CALayer*)layer {     CFTimeInterval pausedTime = [layer convertTime:CACurrentMediaTime() fromLayer:nil];     layer.speed = 0.0;     layer.timeOffset = pausedTime; }  -(void)resumeLayer:(CALayer*)layer {     CFTimeInterval pausedTime = [layer timeOffset];     layer.speed = 1.0;     layer.timeOffset = 0.0;     layer.beginTime = 0.0;     CFTimeInterval timeSincePause = [layer convertTime:CACurrentMediaTime() fromLayer:nil] - pausedTime;     layer.beginTime = timeSincePause; }
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2011-08-22 | Fixed typo in code listing. |
| 2010-06-02 | New document that describes how you can pause animations in a layer tree |

