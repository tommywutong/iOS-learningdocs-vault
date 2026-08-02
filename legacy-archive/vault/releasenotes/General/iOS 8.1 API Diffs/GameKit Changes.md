---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/GameKit.html
archived_at: '2026-07-18T02:56:13.493941Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# GameKit Changes

## GameKit

Added GKAchievementViewController.achievementDelegateAdded GKLeaderboardViewController.categoryAdded GKLeaderboardViewController.leaderboardDelegateAdded GKLeaderboardViewController.timeScopeModified GKAchievement

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKAchievement.challengeComposeControllerWithPlayers([AnyObject]!, message: String!, completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 8.0 |

Modified GKAchievement.init(identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String!) ``` |
| To | ``` init!(identifier identifier: String!) ``` |

Modified GKAchievement.init(identifier: String!, forPlayer: String!)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(identifier identifier: String!, forPlayer playerID: String!) ``` | iOS 8.0 | -- |
| To | ``` init!(identifier identifier: String!, forPlayer playerID: String!) ``` | iOS 7.0 | iOS 8.0 |

Modified GKAchievement.init(identifier: String!, player: GKPlayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String!, player player: GKPlayer!) ``` |
| To | ``` init!(identifier identifier: String!, player player: GKPlayer!) ``` |

Modified GKAchievement.playerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 8.0 |

Modified GKAchievement.reportAchievements([AnyObject]!, withCompletionHandler:((NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKAchievement.reportAchievements([AnyObject]!, withEligibleChallenges:[AnyObject]!, withCompletionHandler:((NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKAchievement.selectChallengeablePlayerIDs([AnyObject]!, withCompletionHandler:(([AnyObject]!, NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified GKAchievement.showsCompletionBanner

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKAchievementChallenge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKAchievementDescription

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKAchievementDescription.groupIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKAchievementDescription.replayable

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKChallenge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKChallenge.issuingPlayerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified GKChallenge.receivingPlayerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified GKChallengeListener.player(GKPlayer!, didCompleteChallenge: GKChallenge!, issuedByFriend: GKPlayer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKChallengeListener.player(GKPlayer!, didReceiveChallenge: GKChallenge!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKChallengeListener.player(GKPlayer!, issuedChallengeWasCompleted: GKChallenge!, byFriend: GKPlayer!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKChallengeListener.player(GKPlayer!, wantsToPlayChallenge: GKChallenge!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKFriendRequestComposeViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified GKFriendRequestComposeViewController.addRecipientsWithPlayerIDs([AnyObject]!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.2 | iOS 8.0 |

Modified GKFriendRequestComposeViewControllerDelegate.friendRequestComposeViewControllerDidFinish(GKFriendRequestComposeViewController!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.2 |

Modified GKGameCenterControllerDelegate.gameCenterViewControllerDidFinish(GKGameCenterViewController!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKGameCenterViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKGameCenterViewController.leaderboardIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKInvite

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKInvite.inviter

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKInvite.playerAttributes

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKInvite.playerGroup

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKInviteEventListener.player(GKPlayer!, didAcceptInvite: GKInvite!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKInviteEventListener.player(GKPlayer!, didRequestMatchWithPlayers:[AnyObject]!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 8.0 |

Modified GKLeaderboard

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKLeaderboard.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified GKLeaderboard.groupIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKLeaderboard.identifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLeaderboard.loadImageWithCompletionHandler(((UIImage!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLeaderboard.loadLeaderboardsWithCompletionHandler((([AnyObject]!, NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKLeaderboard.init(playerIDs: [AnyObject]!)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(playerIDs playerIDs: [AnyObject]!) ``` | iOS 8.0 | -- |
| To | ``` init!(playerIDs playerIDs: [AnyObject]!) ``` | iOS 4.1 | iOS 8.0 |

Modified GKLeaderboard.init(players: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(players players: [AnyObject]!) ``` |
| To | ``` init!(players players: [AnyObject]!) ``` |

Modified GKLeaderboardSet

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLeaderboardSet.loadLeaderboardSetsWithCompletionHandler((([AnyObject]!, NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLeaderboardSet.loadLeaderboardsWithCompletionHandler((([AnyObject]!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLocalPlayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKLocalPlayer.authenticateHandler

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKLocalPlayer.friends

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKLocalPlayer.generateIdentityVerificationSignatureWithCompletionHandler(((NSURL!, NSData!, NSData!, UInt64, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLocalPlayer.loadDefaultLeaderboardIdentifierWithCompletionHandler(((String!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLocalPlayer.loadFriendsWithCompletionHandler((([AnyObject]!, NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKLocalPlayer.registerListener(GKLocalPlayerListener!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLocalPlayer.setDefaultLeaderboardIdentifier(String!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLocalPlayer.unregisterAllListeners()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKLocalPlayer.unregisterListener(GKLocalPlayerListener!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKMatch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKMatch.chooseBestHostPlayerWithCompletionHandler(((String!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified GKMatch.playerIDs

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKMatch.rematchWithCompletionHandler(((GKMatch!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKMatch.sendData(NSData!, toPlayers:[AnyObject]!, withDataMode: GKMatchSendDataMode, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKMatchDelegate.match(GKMatch!, didFailWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKMatchDelegate.match(GKMatch!, didReceiveData: NSData!, fromPlayer: String!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKMatchDelegate.match(GKMatch!, player: GKPlayer!, didChangeConnectionState: GKPlayerConnectionState)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKMatchDelegate.match(GKMatch!, player: String!, didChangeState: GKPlayerConnectionState)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKMatchDelegate.match(GKMatch!, shouldReinvitePlayer: String!) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified GKMatchRequest

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKMatchRequest.defaultNumberOfPlayers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKMatchRequest.inviteMessage

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKMatchRequest.inviteeResponseHandler

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified GKMatchRequest.maxPlayersAllowedForMatchOfType(GKMatchType) -> Int [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKMatchRequest.playersToInvite

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKMatchmaker

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKMatchmaker.cancelInviteToPlayer(String!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified GKMatchmaker.findPlayersForHostedMatchRequest(GKMatchRequest!, withCompletionHandler:(([AnyObject]!, NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKMatchmaker.finishMatchmakingForMatch(GKMatch!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKMatchmaker.matchForInvite(GKInvite!, completionHandler:((GKMatch!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKMatchmaker.startBrowsingForNearbyPlayersWithReachableHandler(((String!, Bool) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 6.0 | iOS 8.0 |

Modified GKMatchmaker.stopBrowsingForNearbyPlayers()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKMatchmakerViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKMatchmakerViewController.addPlayersToMatch(GKMatch!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKMatchmakerViewController.init(invite: GKInvite!)

|  | Declaration |
| --- | --- |
| From | ``` init(invite invite: GKInvite!) ``` |
| To | ``` init!(invite invite: GKInvite!) ``` |

Modified GKMatchmakerViewController.init(matchRequest: GKMatchRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(matchRequest request: GKMatchRequest!) ``` |
| To | ``` init!(matchRequest request: GKMatchRequest!) ``` |

Modified GKMatchmakerViewController.setHostedPlayer(String!, connected: Bool)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didFailWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didFindMatch: GKMatch!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didFindPlayers:[AnyObject]!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didReceiveAcceptFromHostedPlayer: String!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewControllerWasCancelled(GKMatchmakerViewController!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKNotificationBanner

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKNotificationBanner.showBannerWithTitle(String!, message: String!, completionHandler:(() -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKNotificationBanner.showBannerWithTitle(String!, message: String!, duration: NSTimeInterval, completionHandler:(() -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKPlayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKPlayer.displayName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKPlayer.isFriend

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKPlayer.loadPhotoForSize(GKPhotoSize, withCompletionHandler:((UIImage!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKScore

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKScore.challengeComposeControllerWithPlayers([AnyObject]!, message: String!, completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 8.0 |

Modified GKScore.context

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKScore.leaderboardIdentifier

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKScore.init(leaderboardIdentifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(leaderboardIdentifier identifier: String!) ``` |
| To | ``` init!(leaderboardIdentifier identifier: String!) ``` |

Modified GKScore.init(leaderboardIdentifier: String!, forPlayer: String!)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(leaderboardIdentifier identifier: String!, forPlayer playerID: String!) ``` | iOS 8.0 | -- |
| To | ``` init!(leaderboardIdentifier identifier: String!, forPlayer playerID: String!) ``` | iOS 7.0 | iOS 8.0 |

Modified GKScore.init(leaderboardIdentifier: String!, player: GKPlayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(leaderboardIdentifier identifier: String!, player player: GKPlayer!) ``` |
| To | ``` init!(leaderboardIdentifier identifier: String!, player player: GKPlayer!) ``` |

Modified GKScore.playerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKScore.reportScores([AnyObject]!, withCompletionHandler:((NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKScore.reportScores([AnyObject]!, withEligibleChallenges:[AnyObject]!, withCompletionHandler:((NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKScore.shouldSetDefaultLeaderboard

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKScoreChallenge

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKTurnBasedEventListener.player(GKPlayer!, didRequestMatchWithPlayers:[AnyObject]!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 7.0 | iOS 8.0 |

Modified GKTurnBasedEventListener.player(GKPlayer!, receivedExchangeCancellation: GKTurnBasedExchange!, forMatch: GKTurnBasedMatch!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedEventListener.player(GKPlayer!, receivedExchangeReplies:[AnyObject]!, forCompletedExchange: GKTurnBasedExchange!, forMatch: GKTurnBasedMatch!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedEventListener.player(GKPlayer!, receivedExchangeRequest: GKTurnBasedExchange!, forMatch: GKTurnBasedMatch!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedEventListener.player(GKPlayer!, receivedTurnEventForMatch: GKTurnBasedMatch!, didBecomeActive: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedExchange

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedExchange.cancelWithLocalizableMessageKey(String!, arguments:[AnyObject]!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedExchange.replyWithLocalizableMessageKey(String!, arguments:[AnyObject]!, data: NSData!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedExchangeReply

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedMatch.acceptInviteWithCompletionHandler(((GKTurnBasedMatch!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedMatch.activeExchanges

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.completedExchanges

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.declineInviteWithCompletionHandler(((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedMatch.endMatchInTurnWithMatchData(NSData!, scores:[AnyObject]!, achievements:[AnyObject]!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.endTurnWithNextParticipants([AnyObject]!, turnTimeout: NSTimeInterval, matchData: NSData!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKTurnBasedMatch.exchangeDataMaximumSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.exchangeMaxInitiatedExchangesPerPlayer

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.exchanges

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.loadMatchWithID(String!, withCompletionHandler:((GKTurnBasedMatch!, NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedMatch.matchDataMaximumSize

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKTurnBasedMatch.participantQuitInTurnWithOutcome(GKTurnBasedMatchOutcome, nextParticipants:[AnyObject]!, turnTimeout: NSTimeInterval, matchData: NSData!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKTurnBasedMatch.rematchWithCompletionHandler(((GKTurnBasedMatch!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKTurnBasedMatch.saveCurrentTurnWithMatchData(NSData!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKTurnBasedMatch.saveMergedMatchData(NSData!, withResolvedExchanges:[AnyObject]!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.sendExchangeToParticipants([AnyObject]!, data: NSData!, localizableMessageKey: String!, arguments:[AnyObject]!, timeout: NSTimeInterval, completionHandler:((GKTurnBasedExchange!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.sendReminderToParticipants([AnyObject]!, localizableMessageKey: String!, arguments:[AnyObject]!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatch.setLocalizableMessageWithKey(String!, arguments:[AnyObject]!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnBasedMatchmakerViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedMatchmakerViewController.init(matchRequest: GKMatchRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(matchRequest request: GKMatchRequest!) ``` |
| To | ``` init!(matchRequest request: GKMatchRequest!) ``` |

Modified GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController!, didFailWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController!, didFindMatch: GKTurnBasedMatch!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController!, playerQuitForMatch: GKTurnBasedMatch!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewControllerWasCancelled(GKTurnBasedMatchmakerViewController!)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedParticipant

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 5.0 |

Modified GKTurnBasedParticipant.playerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified GKTurnBasedParticipant.timeoutDate

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKVoiceChat

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKVoiceChat.playerIDs

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified GKVoiceChat.playerStateUpdateHandler

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 4.1 | iOS 8.0 |

Modified GKVoiceChat.setMute(Bool, forPlayer: String!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 5.0 | iOS 8.0 |

Modified GKExchangeTimeoutDefault

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKExchangeTimeoutNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKPlayerAuthenticationDidChangeNotificationName

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 4.1 |

Modified GKTurnBasedExchangeStatus

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified GKTurnTimeoutDefault

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

Modified GKTurnTimeoutNone

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 6.0 |

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
