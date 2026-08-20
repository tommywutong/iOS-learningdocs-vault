---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/QuartzCore.html
archived_at: '2026-07-18T02:56:00.427976Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# QuartzCore Changes

## QuartzCore

CAAnimation.hModified [+[CAAnimation animation]](https://developer.apple.com/documentation/quartzcore/caanimation/1412479-animation)

|  | Declaration |
| --- | --- |
| From | ``` + (id)animation ``` |
| To | ``` + (instancetype)animation ``` |

Modified [CAAnimation.delegate](https://developer.apple.com/documentation/quartzcore/caanimation/1412490-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id delegate ``` |
| To | ``` @property(strong) id delegate ``` |

Modified [CAAnimation.timingFunction](https://developer.apple.com/documentation/quartzcore/caanimation/1412456-timingfunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CAMediaTimingFunction *timingFunction ``` |
| To | ``` @property(strong) CAMediaTimingFunction *timingFunction ``` |

Modified [CABasicAnimation.byValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412445-byvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id byValue ``` |
| To | ``` @property(strong) id byValue ``` |

Modified [CABasicAnimation.fromValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412519-fromvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id fromValue ``` |
| To | ``` @property(strong) id fromValue ``` |

Modified [CABasicAnimation.toValue](https://developer.apple.com/documentation/quartzcore/cabasicanimation/1412523-tovalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id toValue ``` |
| To | ``` @property(strong) id toValue ``` |

Modified [+[CAPropertyAnimation animationWithKeyPath:]](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412534-init)

|  | Declaration |
| --- | --- |
| From | ``` + (id)animationWithKeyPath:(NSString *)path ``` |
| To | ``` + (instancetype)animationWithKeyPath:(NSString *)path ``` |

Modified [CAPropertyAnimation.valueFunction](https://developer.apple.com/documentation/quartzcore/capropertyanimation/1412447-valuefunction)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CAValueFunction *valueFunction ``` |
| To | ``` @property(strong) CAValueFunction *valueFunction ``` |

Modified [CATransition.filter](https://developer.apple.com/documentation/quartzcore/catransition/1412506-filter)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id filter ``` |
| To | ``` @property(strong) id filter ``` |

CAEmitterBehavior.hModified -[CAEmitterBehavior initWithType:]

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithType:(NSString *)type ``` |
| To | ``` - (instancetype)initWithType:(NSString *)type ``` |

CAEmitterCell.hModified [CAEmitterCell.contents](https://developer.apple.com/documentation/quartzcore/caemittercell/1522109-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id contents ``` |
| To | ``` @property(strong) id contents ``` |

Modified [+[CAEmitterCell emitterCell]](https://developer.apple.com/documentation/quartzcore/caemittercell/1584370-emittercell)

|  | Declaration |
| --- | --- |
| From | ``` + (id)emitterCell ``` |
| To | ``` + (instancetype)emitterCell ``` |

CALayer.hRemoved CAEdgeAntialiasingMaskAdded [CAEdgeAntialiasingMask](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask)Modified [CALayer.compositingFilter](https://developer.apple.com/documentation/quartzcore/calayer/1410748-compositingfilter)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id compositingFilter ``` |
| To | ``` @property(strong) id compositingFilter ``` |

Modified [CALayer.contents](https://developer.apple.com/documentation/quartzcore/calayer/1410773-contents)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) id contents ``` |
| To | ``` @property(strong) id contents ``` |

Modified [CALayer.delegate](https://developer.apple.com/documentation/quartzcore/calayer/1410984-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) id delegate ``` |
| To | ``` @property(weak) id delegate ``` |

Modified [CALayer.edgeAntialiasingMask](https://developer.apple.com/documentation/quartzcore/calayer/1410892-edgeantialiasingmask)

|  | Declaration |
| --- | --- |
| From | ``` @property unsigned int edgeAntialiasingMask ``` |
| To | ``` @property CAEdgeAntialiasingMask edgeAntialiasingMask ``` |

Modified [-[CALayer init]](https://developer.apple.com/documentation/quartzcore/calayer/1410835-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[CALayer initWithLayer:]](https://developer.apple.com/documentation/quartzcore/calayer/1410842-initwithlayer)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLayer:(id)layer ``` |
| To | ``` - (instancetype)initWithLayer:(id)layer ``` |

Modified [+[CALayer layer]](https://developer.apple.com/documentation/quartzcore/calayer/1410793-layer)

|  | Declaration |
| --- | --- |
| From | ``` + (id)layer ``` |
| To | ``` + (instancetype)layer ``` |

Modified [CALayer.mask](https://developer.apple.com/documentation/quartzcore/calayer/1410861-mask)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) CALayer *mask ``` |
| To | ``` @property(strong) CALayer *mask ``` |

CAMediaTimingFunction.hModified [+[CAMediaTimingFunction functionWithName:]](https://developer.apple.com/documentation/quartzcore/camediatimingfunction/1521979-functionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)functionWithName:(NSString *)name ``` |
| To | ``` + (instancetype)functionWithName:(NSString *)name ``` |

CAMetalLayer.h (Added)Added [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable)Added [CAMetalDrawable.layer](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478165-layer)Added [CAMetalDrawable.texture](https://developer.apple.com/documentation/quartzcore/cametaldrawable/1478159-texture)Added [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer)Added [CAMetalLayer.device](https://developer.apple.com/documentation/quartzcore/cametallayer/1478163-device)Added [CAMetalLayer.drawableSize](https://developer.apple.com/documentation/quartzcore/cametallayer/1478174-drawablesize)Added [CAMetalLayer.framebufferOnly](https://developer.apple.com/documentation/quartzcore/cametallayer/1478168-framebufferonly)Added -[CAMetalLayer newDrawable]Added [-[CAMetalLayer nextDrawable]](https://developer.apple.com/documentation/quartzcore/cametallayer/1478172-nextdrawable)Added [CAMetalLayer.pixelFormat](https://developer.apple.com/documentation/quartzcore/cametallayer/1478155-pixelformat)Added [CAMetalLayer.presentsWithTransaction](https://developer.apple.com/documentation/quartzcore/cametallayer/1478157-presentswithtransaction)CATransaction.hModified [+[CATransaction completionBlock]](https://developer.apple.com/documentation/quartzcore/catransaction/1448280-completionblock)

|  | Declaration |
| --- | --- |
| From | ``` + (void (^)())completionBlock ``` |
| To | ``` + (void (^)(void))completionBlock ``` |

CATransform3D.hRemoved [-[NSValue CATransform3DValue]](https://developer.apple.com/documentation/foundation/nsvalue/1436572-catransform3dvalue)Added [NSValue.CATransform3DValue](https://developer.apple.com/documentation/foundation/nsvalue/1436572-catransform3dvalue)CAValueFunction.hModified [+[CAValueFunction functionWithName:]](https://developer.apple.com/documentation/quartzcore/cavaluefunction/1522115-functionwithname)

|  | Declaration |
| --- | --- |
| From | ``` + (id)functionWithName:(NSString *)name ``` |
| To | ``` + (instancetype)functionWithName:(NSString *)name ``` |

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
