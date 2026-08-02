---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/QuartzCore.html
archived_at: '2026-07-18T02:56:36.311444Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# QuartzCore Changes for Objective-C

### QuartzCore

#### CAAnimation.h

Added [CASpringAnimation](https://developer.apple.com/documentation/quartzcore/caspringanimation)Added [CASpringAnimation.damping](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412532-damping)Added [CASpringAnimation.initialVelocity](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412443-initialvelocity)Added [CASpringAnimation.mass](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412540-mass)Added [CASpringAnimation.settlingDuration](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412524-settlingduration)Added [CASpringAnimation.stiffness](https://developer.apple.com/documentation/quartzcore/caspringanimation/1412515-stiffness)Modified [CAAnimationGroup.animations](https://developer.apple.com/documentation/quartzcore/caanimationgroup/1412516-animations)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *animations ``` |
| To | ``` @property(copy, nullable) NSArray<CAAnimation *> *animations ``` |

Modified [CAKeyframeAnimation.biasValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412485-biasvalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *biasValues ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *biasValues ``` |

Modified [CAKeyframeAnimation.continuityValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412491-continuityvalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *continuityValues ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *continuityValues ``` |

Modified [CAKeyframeAnimation.keyTimes](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412522-keytimes)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *keyTimes ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *keyTimes ``` |

Modified [CAKeyframeAnimation.tensionValues](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412475-tensionvalues)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *tensionValues ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *tensionValues ``` |

Modified [CAKeyframeAnimation.timingFunctions](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation/1412465-timingfunctions)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *timingFunctions ``` |
| To | ``` @property(copy, nullable) NSArray<CAMediaTimingFunction *> *timingFunctions ``` |

#### CAEAGLLayer.h

Added [CAEAGLLayer.presentsWithTransaction](https://developer.apple.com/documentation/quartzcore/caeagllayer/1618676-presentswithtransaction)

#### CAEmitterBehavior.h

Modified +[CAEmitterBehavior behaviorTypes]

|  | Declaration |
| --- | --- |
| From | ``` + (NSArray *)behaviorTypes ``` |
| To | ``` + (NSArray<NSString *> * _Nonnull)behaviorTypes ``` |

#### CAEmitterCell.h

Added [CAEmitterCell.contentsScale](https://developer.apple.com/documentation/quartzcore/caemittercell/1522197-contentsscale)Modified [CAEmitterCell.emitterCells](https://developer.apple.com/documentation/quartzcore/caemittercell/1521866-emittercells)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *emitterCells ``` |
| To | ``` @property(copy, nullable) NSArray<CAEmitterCell *> *emitterCells ``` |

#### CAEmitterLayer.h

Modified [CAEmitterLayer.emitterCells](https://developer.apple.com/documentation/quartzcore/caemitterlayer/1521923-emittercells)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *emitterCells ``` |
| To | ``` @property(copy, nullable) NSArray<CAEmitterCell *> *emitterCells ``` |

#### CAGradientLayer.h

Modified [CAGradientLayer.locations](https://developer.apple.com/documentation/quartzcore/cagradientlayer/1462410-locations)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *locations ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *locations ``` |

#### CALayer.h

Modified [CALayer.actions](https://developer.apple.com/documentation/quartzcore/calayer/1410789-actions)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSDictionary *actions ``` |
| To | ``` @property(copy, nullable) NSDictionary<NSString *,id<CAAction>> *actions ``` |

Modified [-[CALayer animationKeys]](https://developer.apple.com/documentation/quartzcore/calayer/1410937-animationkeys)

|  | Declaration |
| --- | --- |
| From | ``` - (NSArray *)animationKeys ``` |
| To | ``` - (NSArray<NSString *> * _Nullable)animationKeys ``` |

Modified [CALayer.sublayers](https://developer.apple.com/documentation/quartzcore/calayer/1410802-sublayers)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *sublayers ``` |
| To | ``` @property(copy, nullable) NSArray<CALayer *> *sublayers ``` |

#### CAMediaTiming.h

Removed [kCAFillModeFrozen](https://developer.apple.com/documentation/quartzcore/camediatiming/fill_modes/kcafillmodefrozen)

#### CAMetalLayer.h

Removed -[CAMetalLayer newDrawable]Modified [CAMetalLayer.device](https://developer.apple.com/documentation/quartzcore/cametallayer/1478163-device)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, retain) id<MTLDevice> device ``` |
| To | ``` @property(retain, nullable) id<MTLDevice> device ``` |

Modified [CAMetalLayer.drawableSize](https://developer.apple.com/documentation/quartzcore/cametallayer/1478174-drawablesize)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) CGSize drawableSize ``` |
| To | ``` @property CGSize drawableSize ``` |

Modified [CAMetalLayer.framebufferOnly](https://developer.apple.com/documentation/quartzcore/cametallayer/1478168-framebufferonly)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) BOOL framebufferOnly ``` |
| To | ``` @property BOOL framebufferOnly ``` |

Modified [CAMetalLayer.pixelFormat](https://developer.apple.com/documentation/quartzcore/cametallayer/1478155-pixelformat)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite) MTLPixelFormat pixelFormat ``` |
| To | ``` @property MTLPixelFormat pixelFormat ``` |

Modified [CAMetalLayer.presentsWithTransaction](https://developer.apple.com/documentation/quartzcore/cametallayer/1478157-presentswithtransaction)

|  | Declaration |
| --- | --- |
| From | ``` @property(getter=presentsWithTransaction) BOOL presentsWithTransaction ``` |
| To | ``` @property BOOL presentsWithTransaction ``` |

#### CAShapeLayer.h

Modified [CAShapeLayer.lineDashPattern](https://developer.apple.com/documentation/quartzcore/cashapelayer/1521921-linedashpattern)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSArray *lineDashPattern ``` |
| To | ``` @property(copy, nullable) NSArray<NSNumber *> *lineDashPattern ``` |

#### CATextLayer.h

Added [CATextLayer.allowsFontSubpixelQuantization](https://developer.apple.com/documentation/quartzcore/catextlayer/1515300-allowsfontsubpixelquantization)

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
