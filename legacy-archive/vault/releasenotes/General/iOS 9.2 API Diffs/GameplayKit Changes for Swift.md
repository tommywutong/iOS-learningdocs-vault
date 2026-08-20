---
title: iOS 9.2 API Diffs
apple_id: TP40016605
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-12-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS92APIDiffs/Swift/GameplayKit.html
archived_at: '2026-07-18T02:57:12.607874Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.2 API Diffs](iOS%209.1%20to%20iOS%209.2%20API%20Differences.md)


# GameplayKit Changes for Swift

### GameplayKit

Removed GKMinmaxStrategist.gameModelRemoved GKMinmaxStrategist.randomSourceAdded [GKGameModel.unapplyGameModelUpdate(_: GKGameModelUpdate)](https://developer.apple.com/documentation/gameplaykit/gkgamemodel/1490276-unapplygamemodelupdate)Added [GKStrategist](https://developer.apple.com/documentation/gameplaykit/gkstrategist)Added [GKStrategist.bestMoveForActivePlayer() -> GKGameModelUpdate?](https://developer.apple.com/documentation/gameplaykit/gkstrategist/1501118-bestmoveforactiveplayer)Added [GKStrategist.gameModel](https://developer.apple.com/documentation/gameplaykit/gkstrategist/1501231-gamemodel)Added [GKStrategist.randomSource](https://developer.apple.com/documentation/gameplaykit/gkstrategist/1501317-randomsource)Modified [GKGameModel](https://developer.apple.com/documentation/gameplaykit/gkgamemodel)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKGameModel : NSObjectProtocol, NSCopying {     var players: [GKGameModelPlayer]? { get }     var activePlayer: GKGameModelPlayer? { get }     func setGameModel(_ gameModel: GKGameModel)     func gameModelUpdatesForPlayer(_ player: GKGameModelPlayer) -> [GKGameModelUpdate]?     func applyGameModelUpdate(_ gameModelUpdate: GKGameModelUpdate)     optional func scoreForPlayer(_ player: GKGameModelPlayer) -> Int     optional func isWinForPlayer(_ player: GKGameModelPlayer) -> Bool     optional func isLossForPlayer(_ player: GKGameModelPlayer) -> Bool } ``` |
| To | ``` protocol GKGameModel : NSObjectProtocol, NSCopying {     var players: [GKGameModelPlayer]? { get }     var activePlayer: GKGameModelPlayer? { get }     func setGameModel(_ gameModel: GKGameModel)     func gameModelUpdatesForPlayer(_ player: GKGameModelPlayer) -> [GKGameModelUpdate]?     func applyGameModelUpdate(_ gameModelUpdate: GKGameModelUpdate)     optional func scoreForPlayer(_ player: GKGameModelPlayer) -> Int     optional func isWinForPlayer(_ player: GKGameModelPlayer) -> Bool     optional func isLossForPlayer(_ player: GKGameModelPlayer) -> Bool     optional func unapplyGameModelUpdate(_ gameModelUpdate: GKGameModelUpdate) } ``` |

Modified [GKMinmaxStrategist](https://developer.apple.com/documentation/gameplaykit/gkminmaxstrategist)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` class GKMinmaxStrategist : NSObject {     var gameModel: GKGameModel?     var maxLookAheadDepth: Int     var randomSource: GKRandom?     func bestMoveForPlayer(_ player: GKGameModelPlayer) -> GKGameModelUpdate?     func randomMoveForPlayer(_ player: GKGameModelPlayer, fromNumberOfBestMoves numMovesToConsider: Int) -> GKGameModelUpdate? } ``` | -- |
| To | ``` class GKMinmaxStrategist : NSObject, GKStrategist {     var maxLookAheadDepth: Int     func bestMoveForPlayer(_ player: GKGameModelPlayer) -> GKGameModelUpdate?     func randomMoveForPlayer(_ player: GKGameModelPlayer, fromNumberOfBestMoves numMovesToConsider: Int) -> GKGameModelUpdate? } ``` | GKStrategist |

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
