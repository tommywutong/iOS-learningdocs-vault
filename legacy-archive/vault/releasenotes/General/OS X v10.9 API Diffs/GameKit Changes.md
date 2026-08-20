---
title: OS X v10.9 API Diffs
apple_id: TP40013007
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_9/GameKit.html
archived_at: '2026-07-18T02:54:13.561953Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.9 API Diffs](OS%20X%20v10.8%20to%20OS%20X%20v10.9%20API%20Differences.md)


# GameKit Changes

## GameKit

GKAchievement.hModified [GKAchievement.completed](https://developer.apple.com/documentation/gamekit/gkachievement/1521050-completed)

|  | Declaration |
| --- | --- |
| From | @property(readonly, getter=isCompleted) BOOL completed |
| To | @property(readonly, getter=isCompleted, atomic) BOOL completed |

Modified [GKAchievement.hidden](https://developer.apple.com/documentation/gamekit/gkachievement/1521136-ishidden)

|  | Deprecation | Declaration |
| --- | --- | --- |
| From | _none_ | @property(assign, getter=isHidden, readonly) BOOL hidden |
| To | OS X 10.9 | @property(assign, getter=isHidden, readonly, atomic) BOOL hidden |

Modified [GKAchievement.identifier](https://developer.apple.com/documentation/gamekit/gkachievement/1520631-identifier)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*identifier |
| To | @property(copy, atomic) NSString \*identifier |

Modified [GKAchievement.lastReportedDate](https://developer.apple.com/documentation/gamekit/gkachievement/1520993-lastreporteddate)

|  | Declaration |
| --- | --- |
| From | @property(copy, readonly) NSDate \*lastReportedDate |
| To | @property(copy, readonly, atomic) NSDate \*lastReportedDate |

Modified [GKAchievement.percentComplete](https://developer.apple.com/documentation/gamekit/gkachievement/1520939-percentcomplete)

|  | Declaration |
| --- | --- |
| From | @property(assign) double percentComplete |
| To | @property(assign, atomic) double percentComplete |

Modified [GKAchievement.showsCompletionBanner](https://developer.apple.com/documentation/gamekit/gkachievement/1521058-showscompletionbanner)

|  | Declaration |
| --- | --- |
| From | @property(assign) BOOL showsCompletionBanner |
| To | @property(assign, atomic) BOOL showsCompletionBanner |

GKAchievementDescription.hModified [GKAchievementDescription.achievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416598-achieveddescription)

|  | Declaration |
| --- | --- |
| From | @property(copy, readonly) NSString \*achievedDescription |
| To | @property(copy, readonly, atomic) NSString \*achievedDescription |

Modified [GKAchievementDescription.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416587-groupidentifier)

|  | Declaration |
| --- | --- |
| From | @property(retain, readonly) NSString \*groupIdentifier |
| To | @property(retain, readonly, atomic) NSString \*groupIdentifier |

Modified [GKAchievementDescription.hidden](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416582-hidden)

|  | Declaration |
| --- | --- |
| From | @property(getter=isHidden, assign, readonly) BOOL hidden |
| To | @property(getter=isHidden, assign, readonly, atomic) BOOL hidden |

Modified [GKAchievementDescription.identifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416586-identifier)

|  | Declaration |
| --- | --- |
| From | @property(copy, readonly) NSString \*identifier |
| To | @property(copy, readonly, atomic) NSString \*identifier |

Modified [GKAchievementDescription.maximumPoints](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416589-maximumpoints)

|  | Declaration |
| --- | --- |
| From | @property(assign, readonly) NSInteger maximumPoints |
| To | @property(assign, readonly, atomic) NSInteger maximumPoints |

Modified [GKAchievementDescription.replayable](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416578-replayable)

|  | Declaration |
| --- | --- |
| From | @property(getter=isReplayable, assign, readonly) BOOL replayable |
| To | @property(getter=isReplayable, assign, readonly, atomic) BOOL replayable |

Modified [GKAchievementDescription.title](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416602-title)

|  | Declaration |
| --- | --- |
| From | @property(copy, readonly) NSString \*title |
| To | @property(copy, readonly, atomic) NSString \*title |

Modified [GKAchievementDescription.unachievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416584-unachieveddescription)

|  | Declaration |
| --- | --- |
| From | @property(copy, readonly) NSString \*unachievedDescription |
| To | @property(copy, readonly, atomic) NSString \*unachievedDescription |

GKAchievementViewController.hModified [GKAchievementViewController.achievementDelegate](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller/1520486-achievementdelegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id<GKAchievementViewControllerDelegate> achievementDelegate |
| To | @property(assign, atomic) id<GKAchievementViewControllerDelegate> achievementDelegate |

GKChallenge.hModified [GKAchievementChallenge.achievement](https://developer.apple.com/documentation/gamekit/gkachievementchallenge/1520858-achievement)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) GKAchievement \*achievement |
| To | @property(readonly, retain, atomic) GKAchievement \*achievement |

Modified [GKChallenge.completionDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520928-completiondate)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSDate \*completionDate |
| To | @property(readonly, retain, atomic) NSDate \*completionDate |

Modified [GKChallenge.issueDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520803-issuedate)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSDate \*issueDate |
| To | @property(readonly, retain, atomic) NSDate \*issueDate |

Modified [GKChallenge.issuingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521100-issuingplayerid)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*issuingPlayerID |
| To | @property(readonly, copy, atomic) NSString \*issuingPlayerID |

Modified [GKChallenge.message](https://developer.apple.com/documentation/gamekit/gkchallenge/1520998-message)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*message |
| To | @property(readonly, copy, atomic) NSString \*message |

Modified [GKChallenge.receivingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521113-receivingplayerid)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*receivingPlayerID |
| To | @property(readonly, copy, atomic) NSString \*receivingPlayerID |

Modified [GKChallenge.state](https://developer.apple.com/documentation/gamekit/gkchallenge/1521179-state)

|  | Declaration |
| --- | --- |
| From | @property(readonly, assign) GKChallengeState state |
| To | @property(readonly, assign, atomic) GKChallengeState state |

Modified [GKScoreChallenge.score](https://developer.apple.com/documentation/gamekit/gkscorechallenge/1521014-score)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) GKScore \*score |
| To | @property(readonly, retain, atomic) GKScore \*score |

GKChallengeEventHandler.hModified [GKChallengeEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/1520556-delegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id<GKChallengeEventHandlerDelegate> delegate |
| To | @property(assign, atomic) id<GKChallengeEventHandlerDelegate> delegate |

GKChallengesViewController.hModified [GKChallengesViewController.challengeDelegate](https://developer.apple.com/documentation/gamekit/gkchallengesviewcontroller/1470742-challengedelegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id<GKChallengesViewControllerDelegate> challengeDelegate |
| To | @property(assign, atomic) id<GKChallengesViewControllerDelegate> challengeDelegate |

GKDialogController.hModified [GKDialogController.parentWindow](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/1520890-parentwindow)

|  | Declaration |
| --- | --- |
| From | @property(assign) NSWindow \*parentWindow |
| To | @property(assign, atomic) NSWindow \*parentWindow |

GKFriendRequestComposeViewController.hModified [GKFriendRequestComposeViewController.composeViewDelegate](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437192-composeviewdelegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id<GKFriendRequestComposeViewControllerDelegate> composeViewDelegate |
| To | @property(assign, atomic) id<GKFriendRequestComposeViewControllerDelegate> composeViewDelegate |

GKGameCenterViewController.hModified [GKGameCenterViewController.gameCenterDelegate](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520845-gamecenterdelegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id<GKGameCenterControllerDelegate> gameCenterDelegate |
| To | @property(assign, atomic) id<GKGameCenterControllerDelegate> gameCenterDelegate |

Modified [GKGameCenterViewController.leaderboardCategory](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520837-leaderboardcategory)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*leaderboardCategory |
| To | @property(copy, atomic) NSString \*leaderboardCategory |

Modified [GKGameCenterViewController.leaderboardTimeScope](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520464-leaderboardtimescope)

|  | Declaration |
| --- | --- |
| From | @property(assign) GKLeaderboardTimeScope leaderboardTimeScope |
| To | @property(assign, atomic) GKLeaderboardTimeScope leaderboardTimeScope |

Modified [GKGameCenterViewController.viewState](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1521007-viewstate)

|  | Declaration |
| --- | --- |
| From | @property(assign) GKGameCenterViewControllerState viewState |
| To | @property(assign, atomic) GKGameCenterViewControllerState viewState |

GKLeaderboard.hAdded [-[GKLeaderboard loadImageWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503161-loadimagewithcompletionhandler)Modified [GKLeaderboard.category](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503154-category)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*category |
| To | @property(copy, atomic) NSString \*category |

Modified [GKLeaderboard.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503135-groupidentifier)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSString \*groupIdentifier |
| To | @property(readonly, retain, atomic) NSString \*groupIdentifier |

Modified [+[GKLeaderboard loadCategoriesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503155-loadcategories)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GKLeaderboard.localPlayerScore](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503151-localplayerscore)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) GKScore \*localPlayerScore |
| To | @property(readonly, retain, atomic) GKScore \*localPlayerScore |

Modified [GKLeaderboard.maxRange](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503136-maxrange)

|  | Declaration |
| --- | --- |
| From | @property(readonly, assign) NSUInteger maxRange |
| To | @property(readonly, assign, atomic) NSUInteger maxRange |

Modified [GKLeaderboard.playerScope](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503165-playerscope)

|  | Declaration |
| --- | --- |
| From | @property(assign) GKLeaderboardPlayerScope playerScope |
| To | @property(assign, atomic) GKLeaderboardPlayerScope playerScope |

Modified [GKLeaderboard.range](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503144-range)

|  | Declaration |
| --- | --- |
| From | @property(assign) NSRange range |
| To | @property(assign, atomic) NSRange range |

Modified [GKLeaderboard.scores](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503159-scores)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSArray \*scores |
| To | @property(readonly, retain, atomic) NSArray \*scores |

Modified [GKLeaderboard.timeScope](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503130-timescope)

|  | Declaration |
| --- | --- |
| From | @property(assign) GKLeaderboardTimeScope timeScope |
| To | @property(assign, atomic) GKLeaderboardTimeScope timeScope |

Modified [GKLeaderboard.title](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503139-title)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*title |
| To | @property(readonly, copy, atomic) NSString \*title |

GKLeaderboardViewController.hModified [GKLeaderboardViewController.category](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/1520506-category)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*category |
| To | @property(copy, atomic) NSString \*category |

Modified [GKLeaderboardViewController.leaderboardDelegate](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/1520996-leaderboarddelegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id<GKLeaderboardViewControllerDelegate> leaderboardDelegate |
| To | @property(assign, atomic) id<GKLeaderboardViewControllerDelegate> leaderboardDelegate |

GKLocalPlayer.hModified [-[GKLocalPlayer authenticateWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515406-authenticatewithcompletionhandle)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GKLocalPlayer.authenticated](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515402-isauthenticated)

|  | Declaration |
| --- | --- |
| From | @property(readonly, getter=isAuthenticated) BOOL authenticated |
| To | @property(readonly, getter=isAuthenticated, atomic) BOOL authenticated |

Modified [GKLocalPlayer.underage](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515394-underage)

|  | Declaration |
| --- | --- |
| From | @property(readonly, getter=isUnderage) BOOL underage |
| To | @property(readonly, getter=isUnderage, atomic) BOOL underage |

GKMatch.hModified [GKMatch.delegate](https://developer.apple.com/documentation/gamekit/gkmatch/1502046-delegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id<GKMatchDelegate> delegate |
| To | @property(assign, atomic) id<GKMatchDelegate> delegate |

Modified [GKMatch.expectedPlayerCount](https://developer.apple.com/documentation/gamekit/gkmatch/1502051-expectedplayercount)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSUInteger expectedPlayerCount |
| To | @property(readonly, atomic) NSUInteger expectedPlayerCount |

Modified [GKMatch.playerIDs](https://developer.apple.com/documentation/gamekit/gkmatch/1502064-playerids)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSArray \*playerIDs |
| To | @property(readonly, atomic) NSArray \*playerIDs |

GKMatchmaker.hModified [GKInvite.hosted](https://developer.apple.com/documentation/gamekit/gkinvite/1520458-hosted)

|  | Declaration |
| --- | --- |
| From | @property(readonly, getter=isHosted) BOOL hosted |
| To | @property(readonly, getter=isHosted, atomic) BOOL hosted |

Modified [GKInvite.inviter](https://developer.apple.com/documentation/gamekit/gkinvite/1520959-inviter)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*inviter |
| To | @property(readonly, copy, atomic) NSString \*inviter |

Modified [GKInvite.playerAttributes](https://developer.apple.com/documentation/gamekit/gkinvite/1520917-playerattributes)

|  | Declaration |
| --- | --- |
| From | @property(readonly) uint32_t playerAttributes |
| To | @property(readonly, atomic) uint32_t playerAttributes |

Modified [GKInvite.playerGroup](https://developer.apple.com/documentation/gamekit/gkinvite/1520563-playergroup)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSUInteger playerGroup |
| To | @property(readonly, atomic) NSUInteger playerGroup |

Modified [GKMatchRequest.maxPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521083-maxplayers)

|  | Declaration |
| --- | --- |
| From | @property(assign) NSUInteger maxPlayers |
| To | @property(assign, atomic) NSUInteger maxPlayers |

Modified [GKMatchRequest.minPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520550-minplayers)

|  | Declaration |
| --- | --- |
| From | @property(assign) NSUInteger minPlayers |
| To | @property(assign, atomic) NSUInteger minPlayers |

Modified [GKMatchRequest.playerAttributes](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520912-playerattributes)

|  | Declaration |
| --- | --- |
| From | @property(assign) uint32_t playerAttributes |
| To | @property(assign, atomic) uint32_t playerAttributes |

Modified [GKMatchRequest.playerGroup](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521071-playergroup)

|  | Declaration |
| --- | --- |
| From | @property(assign) NSUInteger playerGroup |
| To | @property(assign, atomic) NSUInteger playerGroup |

Modified [GKMatchRequest.playersToInvite](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520921-playerstoinvite)

|  | Declaration |
| --- | --- |
| From | @property(retain) NSArray \*playersToInvite |
| To | @property(retain, atomic) NSArray \*playersToInvite |

Modified [GKMatchmaker.inviteHandler](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521060-invitehandler)

|  | Declaration |
| --- | --- |
| From | @property(copy) void (^inviteHandler)(GKInvite \*acceptedInvite, NSArray \*playersToInvite) |
| To | @property(copy, atomic) void (^inviteHandler)(GKInvite \*acceptedInvite, NSArray \*playersToInvite) |

GKMatchmakerViewController.hModified [GKMatchmakerViewController.defaultInvitationMessage](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492409-defaultinvitationmessage)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*defaultInvitationMessage |
| To | @property(copy, atomic) NSString \*defaultInvitationMessage |

Modified [GKMatchmakerViewController.hosted](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492414-ishosted)

|  | Declaration |
| --- | --- |
| From | @property(assign, getter=isHosted) BOOL hosted |
| To | @property(assign, getter=isHosted, atomic) BOOL hosted |

Modified [GKMatchmakerViewController.matchRequest](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492410-matchrequest)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) GKMatchRequest \*matchRequest |
| To | @property(readonly, retain, atomic) GKMatchRequest \*matchRequest |

Modified [GKMatchmakerViewController.matchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492426-matchmakerdelegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) id<GKMatchmakerViewControllerDelegate> matchmakerDelegate |
| To | @property(assign, atomic) id<GKMatchmakerViewControllerDelegate> matchmakerDelegate |

GKPlayer.hModified [GKPlayer.alias](https://developer.apple.com/documentation/gamekit/gkplayer/1520970-alias)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*alias |
| To | @property(readonly, copy, atomic) NSString \*alias |

Modified [GKPlayer.displayName](https://developer.apple.com/documentation/gamekit/gkplayer/1520695-displayname)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSString \*displayName |
| To | @property(readonly, atomic) NSString \*displayName |

Modified [GKPlayer.isFriend](https://developer.apple.com/documentation/gamekit/gkplayer/1520467-isfriend)

|  | Declaration |
| --- | --- |
| From | @property(readonly) BOOL isFriend |
| To | @property(readonly, atomic) BOOL isFriend |

Modified [GKPlayer.playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSString \*playerID |
| To | @property(readonly, retain, atomic) NSString \*playerID |

GKScore.hModified [GKScore.category](https://developer.apple.com/documentation/gamekit/gkscore/1399225-category)

|  | Declaration |
| --- | --- |
| From | @property(copy) NSString \*category |
| To | @property(copy, atomic) NSString \*category |

Modified [GKScore.date](https://developer.apple.com/documentation/gamekit/gkscore/1399234-date)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSDate \*date |
| To | @property(readonly, retain, atomic) NSDate \*date |

Modified [GKScore.formattedValue](https://developer.apple.com/documentation/gamekit/gkscore/1399221-formattedvalue)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*formattedValue |
| To | @property(readonly, copy, atomic) NSString \*formattedValue |

Modified [GKScore.playerID](https://developer.apple.com/documentation/gamekit/gkscore/1399232-playerid)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSString \*playerID |
| To | @property(readonly, retain, atomic) NSString \*playerID |

Modified [GKScore.rank](https://developer.apple.com/documentation/gamekit/gkscore/1399244-rank)

|  | Declaration |
| --- | --- |
| From | @property(readonly, assign) NSInteger rank |
| To | @property(readonly, assign, atomic) NSInteger rank |

Modified [GKScore.value](https://developer.apple.com/documentation/gamekit/gkscore/1399236-value)

|  | Declaration |
| --- | --- |
| From | @property(assign) int64_t value |
| To | @property(assign, atomic) int64_t value |

GKTurnBasedMatch.hModified [GKTurnBasedEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521013-delegate)

|  | Declaration |
| --- | --- |
| From | @property(assign) NSObject<GKTurnBasedEventHandlerDelegate> \*delegate |
| To | @property(assign, atomic) NSObject<GKTurnBasedEventHandlerDelegate> \*delegate |

Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1556899-handleturneventformatch)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GKTurnBasedMatch.creationDate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521168-creationdate)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSDate \*creationDate |
| To | @property(readonly, copy, atomic) NSDate \*creationDate |

Modified [GKTurnBasedMatch.currentParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520643-currentparticipant)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) GKTurnBasedParticipant \*currentParticipant |
| To | @property(readonly, retain, atomic) GKTurnBasedParticipant \*currentParticipant |

Modified [-[GKTurnBasedMatch endTurnWithNextParticipant:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1556897-endturn)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GKTurnBasedMatch.matchData](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520991-matchdata)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSData \*matchData |
| To | @property(readonly, retain, atomic) NSData \*matchData |

Modified [GKTurnBasedMatch.matchDataMaximumSize](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520731-matchdatamaximumsize)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSUInteger matchDataMaximumSize |
| To | @property(readonly, atomic) NSUInteger matchDataMaximumSize |

Modified [GKTurnBasedMatch.matchID](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520625-matchid)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*matchID |
| To | @property(readonly, copy, atomic) NSString \*matchID |

Modified [GKTurnBasedMatch.message](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520721-message)

|  | Declaration |
| --- | --- |
| From | @property(readwrite, copy) NSString \*message |
| To | @property(readwrite, copy, atomic) NSString \*message |

Modified [-[GKTurnBasedMatch participantQuitInTurnWithOutcome:nextParticipant:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1556898-participantquitinturnwithoutcome)

|  | Deprecation |
| --- | --- |
| From | _none_ |
| To | OS X 10.9 |

Modified [GKTurnBasedMatch.participants](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520875-participants)

|  | Declaration |
| --- | --- |
| From | @property(readonly, retain) NSArray \*participants |
| To | @property(readonly, retain, atomic) NSArray \*participants |

Modified [GKTurnBasedMatch.status](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520548-status)

|  | Declaration |
| --- | --- |
| From | @property(readonly) GKTurnBasedMatchStatus status |
| To | @property(readonly, atomic) GKTurnBasedMatchStatus status |

Modified [GKTurnBasedParticipant.lastTurnDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520941-lastturndate)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSDate \*lastTurnDate |
| To | @property(readonly, copy, atomic) NSDate \*lastTurnDate |

Modified [GKTurnBasedParticipant.matchOutcome](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521110-matchoutcome)

|  | Declaration |
| --- | --- |
| From | @property(assign) GKTurnBasedMatchOutcome matchOutcome |
| To | @property(assign, atomic) GKTurnBasedMatchOutcome matchOutcome |

Modified [GKTurnBasedParticipant.playerID](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520474-playerid)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*playerID |
| To | @property(readonly, copy, atomic) NSString \*playerID |

Modified [GKTurnBasedParticipant.status](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520514-status)

|  | Declaration |
| --- | --- |
| From | @property(readonly) GKTurnBasedParticipantStatus status |
| To | @property(readonly, atomic) GKTurnBasedParticipantStatus status |

Modified [GKTurnBasedParticipant.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521187-timeoutdate)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSDate \*timeoutDate |
| To | @property(readonly, copy, atomic) NSDate \*timeoutDate |

GKTurnBasedMatchmakerViewController.hModified [GKTurnBasedMatchmakerViewController.showExistingMatches](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1521099-showexistingmatches)

|  | Declaration |
| --- | --- |
| From | @property(readwrite, assign) BOOL showExistingMatches |
| To | @property(readwrite, assign, atomic) BOOL showExistingMatches |

Modified [GKTurnBasedMatchmakerViewController.turnBasedMatchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1520697-turnbasedmatchmakerdelegate)

|  | Declaration |
| --- | --- |
| From | @property(readwrite, assign) id<GKTurnBasedMatchmakerViewControllerDelegate> turnBasedMatchmakerDelegate |
| To | @property(readwrite, assign, atomic) id<GKTurnBasedMatchmakerViewControllerDelegate> turnBasedMatchmakerDelegate |

GKVoiceChat.hModified [GKVoiceChat.active](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385697-active)

|  | Declaration |
| --- | --- |
| From | @property(assign, getter=isActive) BOOL active |
| To | @property(assign, getter=isActive, atomic) BOOL active |

Modified [GKVoiceChat.name](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385707-name)

|  | Declaration |
| --- | --- |
| From | @property(readonly, copy) NSString \*name |
| To | @property(readonly, copy, atomic) NSString \*name |

Modified [GKVoiceChat.playerIDs](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385721-playerids)

|  | Declaration |
| --- | --- |
| From | @property(readonly) NSArray \*playerIDs |
| To | @property(readonly, atomic) NSArray \*playerIDs |

Modified [GKVoiceChat.playerStateUpdateHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385705-playerstateupdatehandler)

|  | Declaration |
| --- | --- |
| From | @property(copy) void (^playerStateUpdateHandler)(NSString \*playerID, GKVoiceChatPlayerState state) |
| To | @property(copy, atomic) void (^playerStateUpdateHandler)(NSString \*playerID, GKVoiceChatPlayerState state) |

Modified [GKVoiceChat.volume](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385691-volume)

|  | Declaration |
| --- | --- |
| From | @property(assign) float volume |
| To | @property(assign, atomic) float volume |

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
