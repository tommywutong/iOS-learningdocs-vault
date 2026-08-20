---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/QuartzCore.html
archived_at: '2026-07-18T02:50:42.500058Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


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

#### CAConstraintLayoutManager.h

Modified [CAConstraintLayoutManager](https://developer.apple.com/documentation/quartzcore/caconstraintlayoutmanager)

|  | Protocols |
| --- | --- |
| From | -- |
| To | CALayoutManager |

#### CAEmitterBehavior.h

Added kCAEmitterBehaviorSimpleAttractor

#### CALayer.h

Removed NSObject(CALayerDelegate)Removed NSObject(CALayoutManager)Added [CALayer.contentsFormat](https://developer.apple.com/documentation/quartzcore/calayer/1792104-contentsformat)Added [CALayerDelegate](https://developer.apple.com/documentation/quartzcore/calayerdelegate)Added [-[CALayerDelegate layerWillDraw:]](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097263-layerwilldraw)Added [-[CALayerDelegate layoutSublayersOfLayer:]](https://developer.apple.com/documentation/quartzcore/calayerdelegate/2097257-layoutsublayers)Added [CALayoutManager](https://developer.apple.com/documentation/quartzcore/calayoutmanager)Added [kCAContentsFormatGray8Uint](https://developer.apple.com/documentation/quartzcore/kcacontentsformatgray8uint)Added [kCAContentsFormatRGBA16Float](https://developer.apple.com/documentation/quartzcore/kcacontentsformatrgba16float)Added [kCAContentsFormatRGBA8Uint](https://developer.apple.com/documentation/quartzcore/calayercontentsformat/1792108-rgba8uint)Modified [CALayer.delegate](https://developer.apple.com/documentation/quartzcore/calayer/1410984-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak) id delegate ``` |
| To | ``` @property(weak) id<CALayerDelegate> delegate ``` |

Modified [CALayer.layoutManager](https://developer.apple.com/documentation/quartzcore/calayer/1410749-layoutmanager)

|  | Declaration |
| --- | --- |
| From | ``` @property(strong) id layoutManager ``` |
| To | ``` @property(strong) id<CALayoutManager> layoutManager ``` |

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

Modified [-[CALayoutManager invalidateLayoutOfLayer:]](https://developer.apple.com/documentation/quartzcore/calayoutmanager/2097258-invalidatelayout)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CALayoutManager layoutSublayersOfLayer:]](https://developer.apple.com/documentation/quartzcore/calayoutmanager/2097260-layoutsublayersoflayer)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[CALayoutManager preferredSizeOfLayer:]](https://developer.apple.com/documentation/quartzcore/calayoutmanager/2097256-preferredsize)

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
