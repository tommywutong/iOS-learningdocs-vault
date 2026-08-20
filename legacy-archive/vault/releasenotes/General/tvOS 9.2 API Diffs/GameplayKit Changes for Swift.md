---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/GameplayKit.html
archived_at: '2026-07-18T02:58:05.949642Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# GameplayKit Changes for Swift

### GameplayKit

Modified [GKBehavior](https://developer.apple.com/documentation/gameplaykit/gkbehavior)

|  | Declaration |
| --- | --- |
| From | ``` class GKBehavior : NSObject, NSFastEnumeration {     var goalCount: Int { get }     convenience init(goal goal: GKGoal, weight weight: Float)     class func behaviorWithGoal(_ goal: GKGoal, weight weight: Float) -> Self     convenience init(goals goals: [GKGoal])     class func behaviorWithGoals(_ goals: [GKGoal]) -> Self     convenience init(goals goals: [GKGoal], andWeights weights: [NSNumber])     class func behaviorWithGoals(_ goals: [GKGoal], andWeights weights: [NSNumber]) -> Self     convenience init(weightedGoals weightedGoals: [GKGoal : NSNumber])     class func behaviorWithWeightedGoals(_ weightedGoals: [GKGoal : NSNumber]) -> Self     func setWeight(_ weight: Float, forGoal goal: GKGoal)     func weightForGoal(_ goal: GKGoal) -> Float     func removeGoal(_ goal: GKGoal)     func removeAllGoals()     subscript (_ idx: Int) -> GKGoal { get }     func objectAtIndexedSubscript(_ idx: Int) -> GKGoal     subscript (_ goal: GKGoal) -> NSNumber     func setObject(_ weight: NSNumber, forKeyedSubscript goal: GKGoal)     func objectForKeyedSubscript(_ goal: GKGoal) -> NSNumber } ``` |
| To | ``` class GKBehavior : NSObject, NSFastEnumeration {     var goalCount: Int { get }     convenience init(goal goal: GKGoal, weight weight: Float)     class func behaviorWithGoal(_ goal: GKGoal, weight weight: Float) -> Self     convenience init(goals goals: [GKGoal])     class func behaviorWithGoals(_ goals: [GKGoal]) -> Self     convenience init(goals goals: [GKGoal], andWeights weights: [NSNumber])     class func behaviorWithGoals(_ goals: [GKGoal], andWeights weights: [NSNumber]) -> Self     convenience init(weightedGoals weightedGoals: [GKGoal : NSNumber])     class func behaviorWithWeightedGoals(_ weightedGoals: [GKGoal : NSNumber]) -> Self     func setWeight(_ weight: Float, forGoal goal: GKGoal)     func weightForGoal(_ goal: GKGoal) -> Float     func removeGoal(_ goal: GKGoal)     func removeAllGoals()     subscript (_ idx: Int) -> GKGoal { get }     func objectAtIndexedSubscript(_ idx: Int) -> GKGoal     func setObject(_ weight: NSNumber, forKeyedSubscript goal: GKGoal)     subscript (_ goal: GKGoal) -> NSNumber     func objectForKeyedSubscript(_ goal: GKGoal) -> NSNumber } ``` |

Modified [GKGameModel.unapplyGameModelUpdate(_: GKGameModelUpdate)](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/1490276-unapplygamemodelupdate)

|  | Introduction |
| --- | --- |
| From | tvOS 9.1 |
| To | tvOS 9.0 |

Modified [GKStrategist](https://developer.apple.com/documentation/gameplaykit/gkstrategist)

|  | Introduction |
| --- | --- |
| From | tvOS 9.1 |
| To | tvOS 9.0 |

Modified [GKStrategist.bestMoveForActivePlayer() -> GKGameModelUpdate?](https://developer.apple.com/documentation/gameplaykit/gkstrategist/1501118-bestmoveforactiveplayer)

|  | Introduction |
| --- | --- |
| From | tvOS 9.1 |
| To | tvOS 9.0 |

Modified [GKStrategist.gameModel](https://developer.apple.com/documentation/gameplaykit/gkstrategist/1501231-gamemodel)

|  | Introduction |
| --- | --- |
| From | tvOS 9.1 |
| To | tvOS 9.0 |

Modified [GKStrategist.randomSource](https://developer.apple.com/documentation/gameplaykit/gkstrategist/1501317-randomsource)

|  | Introduction |
| --- | --- |
| From | tvOS 9.1 |
| To | tvOS 9.0 |

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
