---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/QuartzCore.html
archived_at: '2026-07-18T02:57:27.601855Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# QuartzCore Changes for Objective-C

### QuartzCore

#### CAAnimation.h

Removed NSObject(CAAnimationDelegate)Added [CAAnimationDelegate](https://developer.apple.com/documentation/quartzcore/caanimationdelegate)Modified [CAAnimation.delegate](https://developer.apple.com/documentation/quartzcore/caanimation/1412490-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id delegate ``` |
| To | ``` @property(strong) id<CAAnimationDelegate> delegate ``` |

Modified [-[CAAnimationDelegate animationDidStart:]](https://developer.apple.com/documentation/quartzcore/caanimationdelegate/2097265-animationdidstart)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CAAnimationDelegate animationDidStop:finished:]](https://developer.apple.com/documentation/quartzcore/caanimationdelegate/2097259-animationdidstop)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

#### CADisplayLink.h

Added [CADisplayLink.preferredFramesPerSecond](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648421-preferredframespersecond)Added [CADisplayLink.targetTimestamp](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1648422-targettimestamp)Modified [-[CADisplayLink addToRunLoop:forMode:]](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621323-add)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addToRunLoop:(NSRunLoop *)runloop forMode:(NSString *)mode ``` |
| To | ``` - (void)addToRunLoop:(NSRunLoop *)runloop forMode:(NSRunLoopMode)mode ``` |

Modified [-[CADisplayLink removeFromRunLoop:forMode:]](https://developer.apple.com/documentation/quartzcore/cadisplaylink/1621325-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeFromRunLoop:(NSRunLoop *)runloop forMode:(NSString *)mode ``` |
| To | ``` - (void)removeFromRunLoop:(NSRunLoop *)runloop forMode:(NSRunLoopMode)mode ``` |

#### CAEmitterBehavior.h

Added kCAEmitterBehaviorSimpleAttractor

#### CALayer.h

Removed NSObject(CALayerDelegate)Added [CALayer.contentsFormat](https://developer.apple.com/documentation/quartzcore/calayer/1792104-contentsformat)Added [CALayerDelegate](https://developer.apple.com/documentation/quartzcore/calayerdelegate)Added [-[CALayerDelegate layerWillDraw:]](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097263-layerwilldraw)Added [kCAContentsFormatGray8Uint](https://developer.apple.com/documentation/quartzcore/kcacontentsformatgray8uint)Added [kCAContentsFormatRGBA16Float](https://developer.apple.com/documentation/quartzcore/kcacontentsformatrgba16float)Added [kCAContentsFormatRGBA8Uint](https://developer.apple.com/documentation/quartzcore/calayercontentsformat/1792108-rgba8uint)Modified [CALayer.delegate](https://developer.apple.com/documentation/quartzcore/calayer/1410984-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak) id delegate ``` |
| To | ``` @property(weak) id<CALayerDelegate> delegate ``` |

Modified [-[CALayer modelLayer]](https://developer.apple.com/documentation/quartzcore/calayer/1410853-modellayer)

|  | Declaration |
| --- | --- |
| From | ``` - (id)modelLayer ``` |
| To | ``` - (instancetype)modelLayer ``` |

Modified [-[CALayer presentationLayer]](https://developer.apple.com/documentation/quartzcore/calayer/1410744-presentation)

|  | Declaration |
| --- | --- |
| From | ``` - (id)presentationLayer ``` |
| To | ``` - (instancetype)presentationLayer ``` |

Modified [-[CALayerDelegate actionForLayer:forKey:]](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097264-action)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CALayerDelegate displayLayer:]](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097261-displaylayer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CALayerDelegate drawLayer:inContext:]](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097262-drawlayer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CALayerDelegate layoutSublayersOfLayer:]](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097257-layoutsublayers)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
