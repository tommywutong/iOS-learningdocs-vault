---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/GameKit.html
archived_at: '2026-07-18T02:53:51.888241Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# GameKit Changes for Swift

### GameKit

Modified [GKAchievement](https://developer.apple.com/documentation/gamekit/gkachievement)

|  | Declaration |
| --- | --- |
| From | ``` class GKAchievement : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementsWithCompletionHandler(_ completionHandler: (([GKAchievement]?, NSError?) -> Void)?)     class func resetAchievementsWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(identifier identifier: String?)     init(identifier identifier: String?, player player: GKPlayer)     class func reportAchievements(_ achievements: [GKAchievement], withCompletionHandler completionHandler: ((NSError?) -> Void)?)     var identifier: String?     var percentComplete: Double     var completed: Bool { get }     @NSCopying var lastReportedDate: NSDate { get }     var showsCompletionBanner: Bool     var player: GKPlayer { get } } extension GKAchievement {     func reportAchievementWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(identifier identifier: String?, forPlayer playerID: String)     var hidden: Bool { get }     var playerID: String { get } } extension GKAchievement {     func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer], completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> NSViewController     func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     class func reportAchievements(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKAchievement {     func selectChallengeablePlayerIDs(_ playerIDs: [String]?, withCompletionHandler completionHandler: (([String]?, NSError?) -> Void)?)     func issueChallengeToPlayers(_ playerIDs: [String]?, message message: String?) } ``` |
| To | ``` class GKAchievement : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementsWithCompletionHandler(_ completionHandler: (([GKAchievement]?, NSError?) -> Void)?)     class func resetAchievementsWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(identifier identifier: String?)     init(identifier identifier: String?, player player: GKPlayer)     class func reportAchievements(_ achievements: [GKAchievement], withCompletionHandler completionHandler: ((NSError?) -> Void)?)     var identifier: String?     var percentComplete: Double     var completed: Bool { get }     @NSCopying var lastReportedDate: NSDate { get }     var showsCompletionBanner: Bool     var player: GKPlayer { get } } extension GKAchievement {     func reportAchievementWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(identifier identifier: String?, forPlayer playerID: String)     var hidden: Bool { get }     var playerID: String { get } } extension GKAchievement {     func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer], completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> NSViewController     func issueChallengeToPlayers(_ playerIDs: [String]?, message message: String?)     func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     class func reportAchievements(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKAchievement {     func selectChallengeablePlayerIDs(_ playerIDs: [String]?, withCompletionHandler completionHandler: (([String]?, NSError?) -> Void)?) } ``` |

Modified [GKGameCenterViewController](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GKGameCenterViewController : NSViewController, GKViewController {     unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate?     var viewState: GKGameCenterViewControllerState } extension GKGameCenterViewController {     var leaderboardTimeScope: GKLeaderboardTimeScope     var leaderboardIdentifier: String?     var leaderboardCategory: String? } ``` |
| To | ``` class GKGameCenterViewController : NSViewController, GKViewController { } extension GKGameCenterViewController {     unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate?     var viewState: GKGameCenterViewControllerState } extension GKGameCenterViewController {     var leaderboardTimeScope: GKLeaderboardTimeScope     var leaderboardIdentifier: String?     var leaderboardCategory: String? } ``` |

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
