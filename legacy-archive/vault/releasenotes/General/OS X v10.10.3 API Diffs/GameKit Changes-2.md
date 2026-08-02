---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/GameKit.html
archived_at: '2026-07-18T02:52:30.196518Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# GameKit Changes

## GameKit

Added GKLocalPlayer.localPlayer() -> GKLocalPlayer! [class]Modified GKAchievement

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievement.hidden

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKAchievement.init(identifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String!) ``` |
| To | ``` init!(identifier identifier: String!) ``` |

Modified GKAchievement.init(identifier: String!, player: GKPlayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(identifier identifier: String!, player player: GKPlayer!) ``` |
| To | ``` init!(identifier identifier: String!, player player: GKPlayer!) ``` |

Modified GKAchievement.issueChallengeToPlayers([AnyObject]!, message: String!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKAchievement.lastReportedDate

|  | Declaration |
| --- | --- |
| From | ``` var lastReportedDate: NSDate! { get } ``` |
| To | ``` @NSCopying var lastReportedDate: NSDate! { get } ``` |

Modified GKAchievement.reportAchievementWithCompletionHandler(((NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKAchievement.reportAchievements([AnyObject]!, withCompletionHandler:((NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievement.selectChallengeablePlayerIDs([AnyObject]!, withCompletionHandler:(([AnyObject]!, NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKAchievement.showsCompletionBanner

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievementChallenge

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievementDescription

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievementDescription.groupIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievementDescription.image

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievementDescription.replayable

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievementViewController

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKAchievementViewController.achievementDelegate

|  | Declaration |
| --- | --- |
| From | ``` var achievementDelegate: GKAchievementViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var achievementDelegate: GKAchievementViewControllerDelegate! ``` |

Modified GKAchievementViewControllerDelegate

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKAchievementViewControllerDelegate.achievementViewControllerDidFinish(GKAchievementViewController!)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKChallenge

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKChallenge.issuingPlayer

|  | Declaration |
| --- | --- |
| From | ``` var issuingPlayer: GKPlayer! { get } ``` |
| To | ``` @NSCopying var issuingPlayer: GKPlayer! { get } ``` |

Modified GKChallenge.issuingPlayerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKChallenge.receivingPlayer

|  | Declaration |
| --- | --- |
| From | ``` var receivingPlayer: GKPlayer! { get } ``` |
| To | ``` @NSCopying var receivingPlayer: GKPlayer! { get } ``` |

Modified GKChallenge.receivingPlayerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKChallengeEventHandler

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKChallengeEventHandler.delegate

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` var delegate: GKChallengeEventHandlerDelegate! ``` | OS X 10.10 | -- |
| To | ``` unowned(unsafe) var delegate: GKChallengeEventHandlerDelegate! ``` | OS X 10.8 | OS X 10.10 |

Modified GKChallengeEventHandlerDelegate

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKChallengeEventHandlerDelegate.localPlayerDidCompleteChallenge(GKChallenge!)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified GKChallengeEventHandlerDelegate.localPlayerDidReceiveChallenge(GKChallenge!)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified GKChallengeEventHandlerDelegate.localPlayerDidSelectChallenge(GKChallenge!)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified GKChallengeEventHandlerDelegate.remotePlayerDidCompleteChallenge(GKChallenge!)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified GKChallengeEventHandlerDelegate.shouldShowBannerForLocallyCompletedChallenge(GKChallenge!) -> Bool

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified GKChallengeEventHandlerDelegate.shouldShowBannerForLocallyReceivedChallenge(GKChallenge!) -> Bool

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified GKChallengeEventHandlerDelegate.shouldShowBannerForRemotelyCompletedChallenge(GKChallenge!) -> Bool

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified GKChallengeListener.player(GKPlayer!, didCompleteChallenge: GKChallenge!, issuedByFriend: GKPlayer!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKChallengeListener.player(GKPlayer!, didReceiveChallenge: GKChallenge!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKChallengeListener.player(GKPlayer!, issuedChallengeWasCompleted: GKChallenge!, byFriend: GKPlayer!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKChallengeListener.player(GKPlayer!, wantsToPlayChallenge: GKChallenge!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKChallengesViewController

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKChallengesViewController.challengeDelegate

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var challengeDelegate: GKChallengesViewControllerDelegate! ``` | -- |
| To | ``` unowned(unsafe) var challengeDelegate: GKChallengesViewControllerDelegate! ``` | OS X 10.10 |

Modified GKDialogController.parentWindow

|  | Declaration |
| --- | --- |
| From | ``` @IBOutlet var parentWindow: NSWindow! ``` |
| To | ``` @IBOutlet unowned(unsafe) var parentWindow: NSWindow! ``` |

Modified GKFriendRequestComposeViewController

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKFriendRequestComposeViewController.addRecipientsWithPlayerIDs([AnyObject]!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKFriendRequestComposeViewController.composeViewDelegate

|  | Declaration |
| --- | --- |
| From | ``` var composeViewDelegate: GKFriendRequestComposeViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var composeViewDelegate: GKFriendRequestComposeViewControllerDelegate! ``` |

Modified GKFriendRequestComposeViewControllerDelegate.friendRequestComposeViewControllerDidFinish(GKFriendRequestComposeViewController!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKGameCenterControllerDelegate.gameCenterViewControllerDidFinish(GKGameCenterViewController!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKGameCenterViewController

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKGameCenterViewController.gameCenterDelegate

|  | Declaration |
| --- | --- |
| From | ``` var gameCenterDelegate: GKGameCenterControllerDelegate! ``` |
| To | ``` unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate! ``` |

Modified GKGameCenterViewController.leaderboardCategory

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKGameCenterViewController.leaderboardTimeScope

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKInvite

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKInvite.inviter

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKInvite.playerAttributes

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKInvite.playerGroup

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKInviteEventListener.player(GKPlayer!, didAcceptInvite: GKInvite!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKInviteEventListener.player(GKPlayer!, didRequestMatchWithRecipients:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKLeaderboard

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKLeaderboard.init()

|  | Declaration |
| --- | --- |
| From | ``` init() ``` |
| To | ``` init!() ``` |

Modified GKLeaderboard.category

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKLeaderboard.groupIdentifier

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKLeaderboard.loadImageWithCompletionHandler(((NSImage!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKLeaderboard.loadLeaderboardsWithCompletionHandler((([AnyObject]!, NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKLeaderboard.init(playerIDs: [AnyObject]!)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(playerIDs playerIDs: [AnyObject]!) ``` | OS X 10.10 | -- |
| To | ``` init!(playerIDs playerIDs: [AnyObject]!) ``` | OS X 10.8 | OS X 10.10 |

Modified GKLeaderboard.init(players: [AnyObject]!)

|  | Declaration |
| --- | --- |
| From | ``` init(players players: [AnyObject]!) ``` |
| To | ``` init!(players players: [AnyObject]!) ``` |

Modified GKLeaderboard.setDefaultLeaderboard(String!, withCompletionHandler:((NSError!) -> Void)!) [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKLeaderboardViewController

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKLeaderboardViewController.leaderboardDelegate

|  | Declaration |
| --- | --- |
| From | ``` var leaderboardDelegate: GKLeaderboardViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var leaderboardDelegate: GKLeaderboardViewControllerDelegate! ``` |

Modified GKLeaderboardViewControllerDelegate

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKLeaderboardViewControllerDelegate.leaderboardViewControllerDidFinish(GKLeaderboardViewController!)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKLocalPlayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKLocalPlayer.authenticateHandler

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKLocalPlayer.friends

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKLocalPlayer.loadDefaultLeaderboardCategoryIDWithCompletionHandler(((String!, NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKLocalPlayer.loadFriendsWithCompletionHandler((([AnyObject]!, NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKLocalPlayer.setDefaultLeaderboardCategoryID(String!, completionHandler:((NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKMatch

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKMatch.chooseBestHostPlayerWithCompletionHandler(((String!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified GKMatch.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: GKMatchDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: GKMatchDelegate! ``` |

Modified GKMatch.playerIDs

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKMatch.rematchWithCompletionHandler(((GKMatch!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKMatch.sendData(NSData!, toPlayers:[AnyObject]!, withDataMode: GKMatchSendDataMode, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKMatchDelegate.match(GKMatch!, didFailWithError: NSError!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified GKMatchDelegate.match(GKMatch!, didReceiveData: NSData!, fromPlayer: String!)

|  | Introduction | Deprecation | Optional |
| --- | --- | --- | --- |
| From | OS X 10.10 | -- | -- |
| To | OS X 10.8 | OS X 10.10 | yes |

Modified GKMatchDelegate.match(GKMatch!, didReceiveData: NSData!, fromRemotePlayer: GKPlayer!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKMatchDelegate.match(GKMatch!, player: GKPlayer!, didChangeConnectionState: GKPlayerConnectionState)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified GKMatchDelegate.match(GKMatch!, shouldReinviteDisconnectedPlayer: GKPlayer!) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKMatchDelegate.match(GKMatch!, shouldReinvitePlayer: String!) -> Bool

|  | Introduction | Deprecation | Optional |
| --- | --- | --- | --- |
| From | OS X 10.10 | -- | -- |
| To | OS X 10.8 | OS X 10.10 | yes |

Modified GKMatchRequest

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKMatchRequest.defaultNumberOfPlayers

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKMatchRequest.inviteMessage

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKMatchRequest.inviteeResponseHandler

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified GKMatchRequest.maxPlayersAllowedForMatchOfType(GKMatchType) -> Int [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKMatchRequest.playersToInvite

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKMatchmaker

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKMatchmaker.cancelInviteToPlayer(String!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified GKMatchmaker.findPlayersForHostedMatchRequest(GKMatchRequest!, withCompletionHandler:(([AnyObject]!, NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKMatchmaker.finishMatchmakingForMatch(GKMatch!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKMatchmaker.inviteHandler

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKMatchmaker.matchForInvite(GKInvite!, completionHandler:((GKMatch!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKMatchmaker.startBrowsingForNearbyPlayersWithReachableHandler(((String!, Bool) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified GKMatchmaker.stopBrowsingForNearbyPlayers()

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKMatchmakerViewController

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKMatchmakerViewController.addPlayersToMatch(GKMatch!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKMatchmakerViewController.defaultInvitationMessage

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

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

Modified GKMatchmakerViewController.matchmakerDelegate

|  | Declaration |
| --- | --- |
| From | ``` var matchmakerDelegate: GKMatchmakerViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var matchmakerDelegate: GKMatchmakerViewControllerDelegate! ``` |

Modified GKMatchmakerViewController.setHostedPlayer(String!, connected: Bool)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didFailWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didFindHostedPlayers:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didFindMatch: GKMatch!)

|  | Introduction | Optional |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | yes |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didFindPlayers:[AnyObject]!)

|  | Introduction | Deprecation | Optional |
| --- | --- | --- | --- |
| From | OS X 10.10 | -- | -- |
| To | OS X 10.8 | OS X 10.10 | yes |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, didReceiveAcceptFromHostedPlayer: String!)

|  | Introduction | Deprecation | Optional |
| --- | --- | --- | --- |
| From | OS X 10.10 | -- | -- |
| To | OS X 10.8 | OS X 10.10 | yes |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewController(GKMatchmakerViewController!, hostedPlayerDidAccept: GKPlayer!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKMatchmakerViewControllerDelegate.matchmakerViewControllerWasCancelled(GKMatchmakerViewController!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKNotificationBanner

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKNotificationBanner.showBannerWithTitle(String!, message: String!, completionHandler:(() -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKNotificationBanner.showBannerWithTitle(String!, message: String!, duration: NSTimeInterval, completionHandler:(() -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKPeerConnectionState [struct]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKPeerConnectionState.init(_: UInt32)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKPeerConnectionState.value

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKPlayer

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKPlayer.displayName

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKPlayer.isFriend

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKPlayer.loadPhotoForSize(GKPhotoSize, withCompletionHandler:((NSImage!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKSavedGameListener.player(GKPlayer!, didModifySavedGame: GKSavedGame!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKSavedGameListener.player(GKPlayer!, hasConflictingSavedGames:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKScore

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKScore.category

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKScore.init(category: String!)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(category category: String!) ``` | OS X 10.10 | -- |
| To | ``` init!(category category: String!) ``` | OS X 10.8 | OS X 10.10 |

Modified GKScore.context

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKScore.issueChallengeToPlayers([AnyObject]!, message: String!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKScore.init(leaderboardIdentifier: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(leaderboardIdentifier identifier: String!) ``` |
| To | ``` init!(leaderboardIdentifier identifier: String!) ``` |

Modified GKScore.init(leaderboardIdentifier: String!, player: GKPlayer!)

|  | Declaration |
| --- | --- |
| From | ``` init(leaderboardIdentifier identifier: String!, player player: GKPlayer!) ``` |
| To | ``` init!(leaderboardIdentifier identifier: String!, player player: GKPlayer!) ``` |

Modified GKScore.playerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKScore.reportScoreWithCompletionHandler(((NSError!) -> Void)!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKScore.reportScores([AnyObject]!, withCompletionHandler:((NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKScore.shouldSetDefaultLeaderboard

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKScoreChallenge

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKSendDataMode [struct]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKSendDataMode.init(_: UInt32)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSendDataMode.value

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKSession.acceptConnectionFromPeer(String!, error: NSErrorPointer) -> Bool

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.available

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.cancelConnectToPeer(String!)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.connectToPeer(String!, withTimeout: NSTimeInterval)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.delegate

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` var delegate: GKSessionDelegate! ``` | -- |
| To | ``` unowned(unsafe) var delegate: GKSessionDelegate! ``` | OS X 10.10 |

Modified GKSession.denyConnectionFromPeer(String!)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.disconnectFromAllPeers()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.disconnectPeerFromAllPeers(String!)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.disconnectTimeout

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.displayName

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.displayNameForPeer(String!) -> String!

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.peerID

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.peersWithConnectionState(GKPeerConnectionState) -> [AnyObject]!

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKSession.sendData(NSData!, toPeers:[AnyObject]!, withDataMode: GKSendDataMode, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKSession.sendDataToAllPeers(NSData!, withDataMode: GKSendDataMode, error: NSErrorPointer) -> Bool

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKSession.sessionID

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSession.init(sessionID: String!, displayName: String!, sessionMode: GKSessionMode)

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` init(sessionID sessionID: String!, displayName name: String!, sessionMode mode: GKSessionMode) ``` | OS X 10.10 | -- |
| To | ``` init!(sessionID sessionID: String!, displayName name: String!, sessionMode mode: GKSessionMode) ``` | OS X 10.8 | OS X 10.10 |

Modified GKSession.sessionMode

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKSession.setDataReceiveHandler(AnyObject!, withContext: UnsafeMutablePointer<Void>)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` func setDataReceiveHandler(_ handler: AnyObject!, withContext context: UnsafePointer<()>) ``` | -- |
| To | ``` func setDataReceiveHandler(_ handler: AnyObject!, withContext context: UnsafeMutablePointer<Void>) ``` | OS X 10.10 |

Modified GKSessionDelegate.session(GKSession!, connectionWithPeerFailed: String!, withError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKSessionDelegate.session(GKSession!, didFailWithError: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKSessionDelegate.session(GKSession!, didReceiveConnectionRequestFromPeer: String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKSessionDelegate.session(GKSession!, peer: String!, didChangeState: GKPeerConnectionState)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKSessionMode [struct]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKSessionMode.init(_: UInt32)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKSessionMode.value

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified GKTurnBasedEventHandler

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKTurnBasedEventHandler.delegate

|  | Declaration | Introduction | Deprecation |
| --- | --- | --- | --- |
| From | ``` var delegate: NSObject! ``` | OS X 10.10 | -- |
| To | ``` unowned(unsafe) var delegate: NSObject! ``` | OS X 10.8 | OS X 10.10 |

Modified GKTurnBasedEventHandler.sharedTurnBasedEventHandler() -> GKTurnBasedEventHandler! [class]

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKTurnBasedEventHandlerDelegate

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKTurnBasedEventHandlerDelegate.handleInviteFromGameCenter([AnyObject]!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKTurnBasedEventHandlerDelegate.handleMatchEnded(GKTurnBasedMatch!)

|  | Introduction | Deprecation | Optional |
| --- | --- | --- | --- |
| From | OS X 10.10 | -- | -- |
| To | OS X 10.8 | OS X 10.10 | yes |

Modified GKTurnBasedEventHandlerDelegate.handleTurnEventForMatch(GKTurnBasedMatch!, didBecomeActive: Bool)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.9 | OS X 10.10 |

Modified GKTurnBasedEventListener.player(GKPlayer!, didRequestMatchWithOtherPlayers:[AnyObject]!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKTurnBasedEventListener.player(GKPlayer!, matchEnded: GKTurnBasedMatch!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKTurnBasedEventListener.player(GKPlayer!, receivedExchangeCancellation: GKTurnBasedExchange!, forMatch: GKTurnBasedMatch!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKTurnBasedEventListener.player(GKPlayer!, receivedExchangeReplies:[AnyObject]!, forCompletedExchange: GKTurnBasedExchange!, forMatch: GKTurnBasedMatch!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKTurnBasedEventListener.player(GKPlayer!, receivedExchangeRequest: GKTurnBasedExchange!, forMatch: GKTurnBasedMatch!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKTurnBasedEventListener.player(GKPlayer!, receivedTurnEventForMatch: GKTurnBasedMatch!, didBecomeActive: Bool)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKTurnBasedMatch

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatch.acceptInviteWithCompletionHandler(((GKTurnBasedMatch!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatch.declineInviteWithCompletionHandler(((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatch.endTurnWithNextParticipants([AnyObject]!, turnTimeout: NSTimeInterval, matchData: NSData!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKTurnBasedMatch.loadMatchWithID(String!, withCompletionHandler:((GKTurnBasedMatch!, NSError!) -> Void)!) [class]

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatch.matchDataMaximumSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatch.participantQuitInTurnWithOutcome(GKTurnBasedMatchOutcome, nextParticipants:[AnyObject]!, turnTimeout: NSTimeInterval, matchData: NSData!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKTurnBasedMatch.rematchWithCompletionHandler(((GKTurnBasedMatch!, NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKTurnBasedMatch.saveCurrentTurnWithMatchData(NSData!, completionHandler:((NSError!) -> Void)!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatchmakerViewController

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatchmakerViewController.init(matchRequest: GKMatchRequest!)

|  | Declaration |
| --- | --- |
| From | ``` init(matchRequest request: GKMatchRequest!) ``` |
| To | ``` init!(matchRequest request: GKMatchRequest!) ``` |

Modified GKTurnBasedMatchmakerViewController.turnBasedMatchmakerDelegate

|  | Declaration |
| --- | --- |
| From | ``` var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate! ``` |

Modified GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController!, didFailWithError: NSError!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController!, didFindMatch: GKTurnBasedMatch!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(GKTurnBasedMatchmakerViewController!, playerQuitForMatch: GKTurnBasedMatch!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewControllerWasCancelled(GKTurnBasedMatchmakerViewController!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedParticipant

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKTurnBasedParticipant.lastTurnDate

|  | Declaration |
| --- | --- |
| From | ``` var lastTurnDate: NSDate! { get } ``` |
| To | ``` @NSCopying var lastTurnDate: NSDate! { get } ``` |

Modified GKTurnBasedParticipant.playerID

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKTurnBasedParticipant.timeoutDate

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var timeoutDate: NSDate! { get } ``` | OS X 10.10 |
| To | ``` @NSCopying var timeoutDate: NSDate! { get } ``` | OS X 10.8 |

Modified GKVoiceChat

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.8 |

Modified GKVoiceChat.playerIDs

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKVoiceChat.playerStateUpdateHandler

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKVoiceChat.setMute(Bool, forPlayer: String!)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified GKVoiceChatClient.voiceChatService(GKVoiceChatService!, didNotStartWithParticipantID: String!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKVoiceChatClient.voiceChatService(GKVoiceChatService!, didReceiveInvitationFromParticipantID: String!, callID: Int)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKVoiceChatClient.voiceChatService(GKVoiceChatService!, didStartWithParticipantID: String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKVoiceChatClient.voiceChatService(GKVoiceChatService!, didStopWithParticipantID: String!, error: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKVoiceChatClient.voiceChatService(GKVoiceChatService!, sendRealTimeData: NSData!, toParticipantID: String!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified GKErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` var GKErrorDomain: NSString! ``` |
| To | ``` let GKErrorDomain: String ``` |

Modified GKPlayerAuthenticationDidChangeNotificationName

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var GKPlayerAuthenticationDidChangeNotificationName: NSString! ``` | OS X 10.10 |
| To | ``` let GKPlayerAuthenticationDidChangeNotificationName: String ``` | OS X 10.8 |

Modified GKPlayerDidChangeNotificationName

|  | Declaration |
| --- | --- |
| From | ``` var GKPlayerDidChangeNotificationName: NSString! ``` |
| To | ``` let GKPlayerDidChangeNotificationName: String ``` |

Modified GKSessionErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let GKSessionErrorDomain: NSString! ``` |
| To | ``` let GKSessionErrorDomain: String ``` |

Modified GKTurnTimeoutDefault

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKTurnTimeoutNone

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.9 |

Modified GKVoiceChatServiceErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let GKVoiceChatServiceErrorDomain: NSString! ``` |
| To | ``` let GKVoiceChatServiceErrorDomain: String ``` |

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
