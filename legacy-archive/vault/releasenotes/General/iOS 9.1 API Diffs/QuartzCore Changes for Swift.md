---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/QuartzCore.html
archived_at: '2026-07-18T02:57:10.497964Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# QuartzCore Changes for Swift

### QuartzCore

Modified [CAAnimation](https://developer.apple.com/documentation/quartzcore/caanimation)

|  | Protocols |
| --- | --- |
| From | AnyObject, CAAction, CAMediaTiming, NSCoding, NSCopying |
| To | CAAction, CAMediaTiming, NSCoding, NSCopying |

Modified [CAAnimationGroup](https://developer.apple.com/documentation/quartzcore/caanimationgroup)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CABasicAnimation](https://developer.apple.com/documentation/quartzcore/cabasicanimation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CADisplayLink](https://developer.apple.com/documentation/quartzcore/cadisplaylink)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CAEAGLLayer](https://developer.apple.com/documentation/quartzcore/caeagllayer)

|  | Protocols |
| --- | --- |
| From | AnyObject, EAGLDrawable |
| To | EAGLDrawable |

Modified CAEmitterBehavior

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [CAEmitterCell](https://developer.apple.com/documentation/quartzcore/caemittercell)

|  | Protocols |
| --- | --- |
| From | AnyObject, CAMediaTiming, NSCoding |
| To | CAMediaTiming, NSCoding |

Modified [CAEmitterLayer](https://developer.apple.com/documentation/quartzcore/caemitterlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CAGradientLayer](https://developer.apple.com/documentation/quartzcore/cagradientlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CAKeyframeAnimation](https://developer.apple.com/documentation/quartzcore/cakeyframeanimation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CALayer](https://developer.apple.com/documentation/quartzcore/calayer)

|  | Protocols |
| --- | --- |
| From | AnyObject, CAMediaTiming, NSCoding |
| To | CAMediaTiming, NSCoding |

Modified [CAMediaTimingFunction](https://developer.apple.com/documentation/quartzcore/camediatimingfunction)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

Modified [CAMetalDrawable](https://developer.apple.com/documentation/quartzcore/cametaldrawable)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol CAMetalDrawable : MTLDrawable, NSObjectProtocol {     var texture: MTLTexture { get }     var layer: CAMetalLayer { get } } ``` | MTLDrawable, NSObjectProtocol |
| To | ``` protocol CAMetalDrawable : MTLDrawable {     var texture: MTLTexture { get }     var layer: CAMetalLayer { get } } ``` | MTLDrawable |

Modified [CAMetalLayer](https://developer.apple.com/documentation/quartzcore/cametallayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CAPropertyAnimation](https://developer.apple.com/documentation/quartzcore/capropertyanimation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CAReplicatorLayer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CAScrollLayer](https://developer.apple.com/documentation/quartzcore/cascrolllayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CAShapeLayer](https://developer.apple.com/documentation/quartzcore/cashapelayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CASpringAnimation](https://developer.apple.com/documentation/quartzcore/caspringanimation)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CATextLayer](https://developer.apple.com/documentation/quartzcore/catextlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CATiledLayer](https://developer.apple.com/documentation/quartzcore/catiledlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CATransaction](https://developer.apple.com/documentation/quartzcore/catransaction)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CATransformLayer](https://developer.apple.com/documentation/quartzcore/catransformlayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CATransition](https://developer.apple.com/documentation/quartzcore/catransition)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [CAValueFunction](https://developer.apple.com/documentation/quartzcore/cavaluefunction)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding |
| To | NSCoding |

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
