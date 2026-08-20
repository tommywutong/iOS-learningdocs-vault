---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/GameplayKit.html
archived_at: '2026-07-18T02:57:08.783194Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# GameplayKit Changes for Swift

### GameplayKit

Added [GKGameModelMinScore](https://developer.apple.com/documentation/gameplaykit/gkgamemodelminscore)Modified [GKAgent](https://developer.apple.com/documentation/gameplaykit/gkagent)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKAgent2D](https://developer.apple.com/documentation/gameplaykit/gkagent2d)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKARC4RandomSource](https://developer.apple.com/documentation/gameplaykit/gkarc4randomsource)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKBehavior](https://developer.apple.com/documentation/gameplaykit/gkbehavior)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSFastEnumeration |
| To | NSFastEnumeration |

Modified [GKCircleObstacle](https://developer.apple.com/documentation/gameplaykit/gkcircleobstacle)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKComponent](https://developer.apple.com/documentation/gameplaykit/gkcomponent)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [GKComponentSystem](https://developer.apple.com/documentation/gameplaykit/gkcomponentsystem)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSFastEnumeration |
| To | NSFastEnumeration |

Modified [GKEntity](https://developer.apple.com/documentation/gameplaykit/gkentity)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [GKGaussianDistribution](https://developer.apple.com/documentation/gameplaykit/gkgaussiandistribution)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKGoal](https://developer.apple.com/documentation/gameplaykit/gkgoal)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [GKGraph](https://developer.apple.com/documentation/gameplaykit/gkgraph)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKGraphNode](https://developer.apple.com/documentation/gameplaykit/gkgraphnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKGraphNode2D](https://developer.apple.com/documentation/gameplaykit/gkgraphnode2d)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKGridGraph](https://developer.apple.com/documentation/gameplaykit/gkgridgraph)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKGridGraphNode](https://developer.apple.com/documentation/gameplaykit/gkgridgraphnode)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKLinearCongruentialRandomSource](https://developer.apple.com/documentation/gameplaykit/gklinearcongruentialrandomsource)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKMersenneTwisterRandomSource](https://developer.apple.com/documentation/gameplaykit/gkmersennetwisterrandomsource)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKMinmaxStrategist](https://developer.apple.com/documentation/gameplaykit/gkminmaxstrategist)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKNSPredicateRule](https://developer.apple.com/documentation/gameplaykit/gknspredicaterule)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKObstacle](https://developer.apple.com/documentation/gameplaykit/gkobstacle)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKObstacleGraph](https://developer.apple.com/documentation/gameplaykit/gkobstaclegraph)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKPath](https://developer.apple.com/documentation/gameplaykit/gkpath)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKPolygonObstacle](https://developer.apple.com/documentation/gameplaykit/gkpolygonobstacle)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKRandomDistribution](https://developer.apple.com/documentation/gameplaykit/gkrandomdistribution)

|  | Protocols |
| --- | --- |
| From | AnyObject, GKRandom |
| To | GKRandom |

Modified [GKRandomSource](https://developer.apple.com/documentation/gameplaykit/gkrandomsource)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKRandomSource : NSObject, GKRandom, NSSecureCoding, NSCoding, NSCopying {     init()     init(coder aDecoder: NSCoder)     class func sharedRandom() -> GKRandomSource     func arrayByShufflingObjectsInArray(_ array: [AnyObject]) -> [AnyObject] } ``` | AnyObject, GKRandom, NSCoding, NSCopying, NSSecureCoding |
| To | ``` class GKRandomSource : NSObject, GKRandom, NSSecureCoding, NSCopying {     init()     init(coder aDecoder: NSCoder)     class func sharedRandom() -> GKRandomSource     func arrayByShufflingObjectsInArray(_ array: [AnyObject]) -> [AnyObject] } ``` | GKRandom, NSCopying, NSSecureCoding |

Modified [GKRule](https://developer.apple.com/documentation/gameplaykit/gkrule)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKRuleSystem](https://developer.apple.com/documentation/gameplaykit/gkrulesystem)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKShuffledDistribution](https://developer.apple.com/documentation/gameplaykit/gkshuffleddistribution)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKState](https://developer.apple.com/documentation/gameplaykit/gkstate)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKStateMachine](https://developer.apple.com/documentation/gameplaykit/gkstatemachine)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKGameModelMaxScore](https://developer.apple.com/documentation/gameplaykit/gkgamemodelmaxscore)

|  | Declaration |
| --- | --- |
| From | ``` var GKGameModelMaxScore: Int32 { get } ``` |
| To | ``` let GKGameModelMaxScore: Int ``` |

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
