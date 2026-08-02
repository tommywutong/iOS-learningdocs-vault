---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/GameKit.html
archived_at: '2026-07-18T02:56:33.934463Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# GameKit Changes for Objective-C

### GameKit

#### GKAchievement.h

Modified [+[GKAchievement loadAchievementsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520748-loadachievements)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadAchievementsWithCompletionHandler:(void (^)(NSArray *achievements, NSError *error))completionHandler ``` |
| To | ``` + (void)loadAchievementsWithCompletionHandler:(void (^ _Nullable)(NSArray<GKAchievement *> * _Nullable achievements, NSError * _Nullable error))completionHandler ``` |

Modified [+[GKAchievement reportAchievements:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520509-reportachievements)

|  | Declaration |
| --- | --- |
| From | ``` + (void)reportAchievements:(NSArray *)achievements withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` + (void)reportAchievements:(NSArray<GKAchievement *> * _Nonnull)achievements withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

#### GKAchievementDescription.h

Modified [+[GKAchievementDescription loadAchievementDescriptionsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416601-loadachievementdescriptionswithc)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadAchievementDescriptionsWithCompletionHandler:(void (^)(NSArray *descriptions, NSError *error))completionHandler ``` |
| To | ``` + (void)loadAchievementDescriptionsWithCompletionHandler:(void (^ _Nullable)(NSArray<GKAchievementDescription *> * _Nullable descriptions, NSError * _Nullable error))completionHandler ``` |

#### GKChallenge.h

Modified [-[GKAchievement challengeComposeControllerWithMessage:players:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520805-challengecomposecontrollerwithme)

|  | Declaration |
| --- | --- |
| From | ``` - (UIViewController *)challengeComposeControllerWithMessage:(NSString *)message players:(NSArray *)players completionHandler:(GKChallengeComposeCompletionBlock)completionHandler ``` |
| To | ``` - (UIViewController * _Nonnull)challengeComposeControllerWithMessage:(NSString * _Nullable)message players:(NSArray<GKPlayer *> * _Nonnull)players completionHandler:(GKChallengeComposeCompletionBlock _Nullable)completionHandler ``` |

Modified [-[GKAchievement challengeComposeControllerWithPlayers:message:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1623556-challengecomposecontrollerwithpl)

|  | Declaration |
| --- | --- |
| From | ``` - (UIViewController *)challengeComposeControllerWithPlayers:(NSArray *)playerIDs message:(NSString *)message completionHandler:(GKChallengeComposeCompletionBlock)completionHandler ``` |
| To | ``` - (UIViewController * _Nullable)challengeComposeControllerWithPlayers:(NSArray<NSString *> * _Nullable)playerIDs message:(NSString * _Nullable)message completionHandler:(GKChallengeComposeCompletionBlock _Nullable)completionHandler ``` |

Modified [-[GKAchievement issueChallengeToPlayers:message:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520984-issuechallenge)

|  | Declaration |
| --- | --- |
| From | ``` - (void)issueChallengeToPlayers:(NSArray *)playerIDs message:(NSString *)message ``` |
| To | ``` - (void)issueChallengeToPlayers:(NSArray<NSString *> * _Nullable)playerIDs message:(NSString * _Nullable)message ``` |

Modified [+[GKAchievement reportAchievements:withEligibleChallenges:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520558-reportachievements)

|  | Declaration |
| --- | --- |
| From | ``` + (void)reportAchievements:(NSArray *)achievements withEligibleChallenges:(NSArray *)challenges withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` + (void)reportAchievements:(NSArray<GKAchievement *> * _Nonnull)achievements withEligibleChallenges:(NSArray<GKChallenge *> * _Nonnull)challenges withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKAchievement selectChallengeablePlayerIDs:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521129-selectchallengeableplayerids)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectChallengeablePlayerIDs:(NSArray *)playerIDs withCompletionHandler:(void (^)(NSArray *challengeablePlayerIDs, NSError *error))completionHandler ``` |
| To | ``` - (void)selectChallengeablePlayerIDs:(NSArray<NSString *> * _Nullable)playerIDs withCompletionHandler:(void (^ _Nullable)(NSArray<NSString *> * _Nullable challengeablePlayerIDs, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKAchievement selectChallengeablePlayers:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520504-selectchallengeableplayers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectChallengeablePlayers:(NSArray *)players withCompletionHandler:(void (^)(NSArray *challengeablePlayers, NSError *error))completionHandler ``` |
| To | ``` - (void)selectChallengeablePlayers:(NSArray<GKPlayer *> * _Nonnull)players withCompletionHandler:(void (^ _Nullable)(NSArray<GKPlayer *> * _Nullable challengeablePlayers, NSError * _Nullable error))completionHandler ``` |

Modified [+[GKChallenge loadReceivedChallengesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkchallenge/1520864-loadreceivedchallenges)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadReceivedChallengesWithCompletionHandler:(void (^)(NSArray *challenges, NSError *error))completionHandler ``` |
| To | ``` + (void)loadReceivedChallengesWithCompletionHandler:(void (^ _Nullable)(NSArray<GKChallenge *> * _Nullable challenges, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKScore challengeComposeControllerWithMessage:players:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1521227-challengecomposecontrollerwithme)

|  | Declaration |
| --- | --- |
| From | ``` - (UIViewController *)challengeComposeControllerWithMessage:(NSString *)message players:(NSArray *)players completionHandler:(GKChallengeComposeCompletionBlock)completionHandler ``` |
| To | ``` - (UIViewController * _Nonnull)challengeComposeControllerWithMessage:(NSString * _Nullable)message players:(NSArray<GKPlayer *> * _Nullable)players completionHandler:(GKChallengeComposeCompletionBlock _Nullable)completionHandler ``` |

Modified [-[GKScore challengeComposeControllerWithPlayers:message:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1623555-challengecomposecontrollerwithpl)

|  | Declaration |
| --- | --- |
| From | ``` - (UIViewController *)challengeComposeControllerWithPlayers:(NSArray *)playerIDs message:(NSString *)message completionHandler:(GKChallengeComposeCompletionBlock)completionHandler ``` |
| To | ``` - (UIViewController * _Nullable)challengeComposeControllerWithPlayers:(NSArray<NSString *> * _Nullable)playerIDs message:(NSString * _Nullable)message completionHandler:(GKChallengeComposeCompletionBlock _Nullable)completionHandler ``` |

Modified [-[GKScore issueChallengeToPlayers:message:]](https://developer.apple.com/documentation/gamekit/gkscore/1520610-issuechallengetoplayers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)issueChallengeToPlayers:(NSArray *)playerIDs message:(NSString *)message ``` |
| To | ``` - (void)issueChallengeToPlayers:(NSArray<NSString *> * _Nullable)playerIDs message:(NSString * _Nullable)message ``` |

Modified [+[GKScore reportScores:withEligibleChallenges:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1520627-reportscores)

|  | Declaration |
| --- | --- |
| From | ``` + (void)reportScores:(NSArray *)scores withEligibleChallenges:(NSArray *)challenges withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` + (void)reportScores:(NSArray<GKScore *> * _Nonnull)scores withEligibleChallenges:(NSArray<GKChallenge *> * _Nonnull)challenges withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

#### GKFriendRequestComposeViewController.h

Modified [-[GKFriendRequestComposeViewController addRecipientPlayers:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437199-addrecipientplayers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addRecipientPlayers:(NSArray *)players ``` |
| To | ``` - (void)addRecipientPlayers:(NSArray<GKPlayer *> * _Nonnull)players ``` |

Modified [-[GKFriendRequestComposeViewController addRecipientsWithEmailAddresses:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437190-addrecipients)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addRecipientsWithEmailAddresses:(NSArray *)emailAddresses ``` |
| To | ``` - (void)addRecipientsWithEmailAddresses:(NSArray<NSString *> * _Nonnull)emailAddresses ``` |

Modified [-[GKFriendRequestComposeViewController addRecipientsWithPlayerIDs:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437188-addrecipientswithplayerids)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addRecipientsWithPlayerIDs:(NSArray *)playerIDs ``` |
| To | ``` - (void)addRecipientsWithPlayerIDs:(NSArray<NSString *> * _Nonnull)playerIDs ``` |

#### GKGameCenterViewController.h

Modified [GKGameCenterViewController.leaderboardTimeScope](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520464-leaderboardtimescope)

|  | Deprecation |
| --- | --- |
| From | iOS 7.0 |
| To | -- |

#### GKLeaderboard.h

Modified [-[GKLeaderboard initWithPlayerIDs:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503132-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPlayerIDs:(NSArray *)playerIDs ``` |
| To | ``` - (instancetype _Nullable)initWithPlayerIDs:(NSArray<NSString *> * _Nullable)playerIDs ``` |

Modified [-[GKLeaderboard initWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503149-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPlayers:(NSArray *)players ``` |
| To | ``` - (instancetype _Nonnull)initWithPlayers:(NSArray<GKPlayer *> * _Nonnull)players ``` |

Modified [+[GKLeaderboard loadCategoriesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503155-loadcategories)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadCategoriesWithCompletionHandler:(void (^)(NSArray *categories, NSArray *titles, NSError *error))completionHandler ``` |
| To | ``` + (void)loadCategoriesWithCompletionHandler:(void (^ _Nullable)(NSArray<NSString *> * _Nullable categories, NSArray<NSString *> * _Nullable titles, NSError * _Nullable error))completionHandler ``` |

Modified [+[GKLeaderboard loadLeaderboardsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503128-loadleaderboards)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadLeaderboardsWithCompletionHandler:(void (^)(NSArray *leaderboards, NSError *error))completionHandler ``` |
| To | ``` + (void)loadLeaderboardsWithCompletionHandler:(void (^ _Nullable)(NSArray<GKLeaderboard *> * _Nullable leaderboards, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKLeaderboard loadScoresWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503160-loadscoreswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadScoresWithCompletionHandler:(void (^)(NSArray *scores, NSError *error))completionHandler ``` |
| To | ``` - (void)loadScoresWithCompletionHandler:(void (^ _Nullable)(NSArray<GKScore *> * _Nullable scores, NSError * _Nullable error))completionHandler ``` |

Modified [GKLeaderboard.scores](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503159-scores)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) NSArray *scores ``` |
| To | ``` @property(readonly, retain, nonatomic, nullable) NSArray<GKScore *> *scores ``` |

#### GKLeaderboardSet.h

Modified [+[GKLeaderboardSet loadLeaderboardSetsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451798-loadleaderboardsetswithcompletio)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadLeaderboardSetsWithCompletionHandler:(void (^)(NSArray *leaderboardSets, NSError *error))completionHandler ``` |
| To | ``` + (void)loadLeaderboardSetsWithCompletionHandler:(void (^ _Nullable)(NSArray<GKLeaderboardSet *> * _Nullable leaderboardSets, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKLeaderboardSet loadLeaderboardsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451810-loadleaderboardswithcompletionha)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadLeaderboardsWithCompletionHandler:(void (^)(NSArray *leaderboards, NSError *error))completionHandler ``` |
| To | ``` - (void)loadLeaderboardsWithCompletionHandler:(void (^ _Nullable)(NSArray<GKLeaderboard *> * _Nullable leaderboards, NSError * _Nullable error))completionHandler ``` |

#### GKLocalPlayer.h

Modified [GKLocalPlayer.friends](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515405-friends)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSArray *friends ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) NSArray<NSString *> *friends ``` |

Modified [-[GKLocalPlayer loadFriendPlayersWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515386-loadfriendplayers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadFriendPlayersWithCompletionHandler:(void (^)(NSArray *friendPlayers, NSError *error))completionHandler ``` |
| To | ``` - (void)loadFriendPlayersWithCompletionHandler:(void (^ _Nullable)(NSArray<GKPlayer *> * _Nullable friendPlayers, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKLocalPlayer loadFriendsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515391-loadfriendswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadFriendsWithCompletionHandler:(void (^)(NSArray *friendIDs, NSError *error))completionHandler ``` |
| To | ``` - (void)loadFriendsWithCompletionHandler:(void (^ _Nullable)(NSArray<NSString *> * _Nullable friendIDs, NSError * _Nullable error))completionHandler ``` |

#### GKMatch.h

Added [-[GKMatchDelegate match:didReceiveData:forRecipient:fromRemotePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502034-match)Modified [GKMatch.playerIDs](https://developer.apple.com/documentation/gamekit/gkmatch/1502064-playerids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *playerIDs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *playerIDs ``` |

Modified [GKMatch.players](https://developer.apple.com/documentation/gamekit/gkmatch/1502074-players)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *players ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<GKPlayer *> *players ``` |

Modified [-[GKMatch sendData:toPlayers:dataMode:error:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502056-send)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendData:(NSData *)data toPlayers:(NSArray *)players dataMode:(GKMatchSendDataMode)mode error:(NSError **)error ``` |
| To | ``` - (BOOL)sendData:(NSData * _Nonnull)data toPlayers:(NSArray<GKPlayer *> * _Nonnull)players dataMode:(GKMatchSendDataMode)mode error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[GKMatch sendData:toPlayers:withDataMode:error:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502033-send)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendData:(NSData *)data toPlayers:(NSArray *)playerIDs withDataMode:(GKMatchSendDataMode)mode error:(NSError **)error ``` |
| To | ``` - (BOOL)sendData:(NSData * _Nonnull)data toPlayers:(NSArray<NSString *> * _Nonnull)playerIDs withDataMode:(GKMatchSendDataMode)mode error:(NSError * _Nullable * _Nullable)error ``` |

#### GKMatchmaker.h

Modified [-[GKInviteEventListener player:didRequestMatchWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1623695-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didRequestMatchWithPlayers:(NSArray *)playerIDsToInvite ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didRequestMatchWithPlayers:(NSArray<NSString *> * _Nonnull)playerIDsToInvite ``` |

Modified [-[GKInviteEventListener player:didRequestMatchWithRecipients:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520894-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didRequestMatchWithRecipients:(NSArray *)recipientPlayers ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didRequestMatchWithRecipients:(NSArray<GKPlayer *> * _Nonnull)recipientPlayers ``` |

Modified [-[GKMatchmaker findPlayersForHostedMatchRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520915-findplayersforhostedmatchrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (void)findPlayersForHostedMatchRequest:(GKMatchRequest *)request withCompletionHandler:(void (^)(NSArray *playerIDs, NSError *error))completionHandler ``` |
| To | ``` - (void)findPlayersForHostedMatchRequest:(GKMatchRequest * _Nonnull)request withCompletionHandler:(void (^ _Nullable)(NSArray<NSString *> * _Nullable playerIDs, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKMatchmaker findPlayersForHostedRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520973-findplayersforhostedrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (void)findPlayersForHostedRequest:(GKMatchRequest *)request withCompletionHandler:(void (^)(NSArray *players, NSError *error))completionHandler ``` |
| To | ``` - (void)findPlayersForHostedRequest:(GKMatchRequest * _Nonnull)request withCompletionHandler:(void (^ _Nullable)(NSArray<GKPlayer *> * _Nullable players, NSError * _Nullable error))completionHandler ``` |

Modified [GKMatchRequest.playersToInvite](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520921-playerstoinvite)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSArray *playersToInvite ``` |
| To | ``` @property(retain, nullable) NSArray<NSString *> *playersToInvite ``` |

Modified [GKMatchRequest.recipients](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520800-recipients)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSArray *recipients ``` |
| To | ``` @property(retain, nullable) NSArray<GKPlayer *> *recipients ``` |

#### GKMatchmakerViewController.h

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindHostedPlayers:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492421-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewController:(GKMatchmakerViewController *)viewController didFindHostedPlayers:(NSArray *)players ``` |
| To | ``` - (void)matchmakerViewController:(GKMatchmakerViewController * _Nonnull)viewController didFindHostedPlayers:(NSArray<GKPlayer *> * _Nonnull)players ``` |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindPlayers:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492428-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewController:(GKMatchmakerViewController *)viewController didFindPlayers:(NSArray *)playerIDs ``` |
| To | ``` - (void)matchmakerViewController:(GKMatchmakerViewController * _Nonnull)viewController didFindPlayers:(NSArray<NSString *> * _Nonnull)playerIDs ``` |

#### GKPlayer.h

Added [+[GKPlayer anonymousGuestPlayerWithIdentifier:]](https://developer.apple.com/documentation/gamekit/gkplayer/1520559-anonymousguestplayerwithidentifi)Added [GKPlayer.guestIdentifier](https://developer.apple.com/documentation/gamekit/gkplayer/1520901-guestidentifier)Modified [+[GKPlayer loadPlayersForIdentifiers:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkplayer/1520723-loadplayersforidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadPlayersForIdentifiers:(NSArray *)identifiers withCompletionHandler:(void (^)(NSArray *players, NSError *error))completionHandler ``` |
| To | ``` + (void)loadPlayersForIdentifiers:(NSArray<NSString *> * _Nonnull)identifiers withCompletionHandler:(void (^ _Nullable)(NSArray<GKPlayer *> * _Nullable players, NSError * _Nullable error))completionHandler ``` |

#### GKPublicConstants.h

Modified [GKPeerConnectionState](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate)

|  | Deprecation |
| --- | --- |
| From | iOS 7.0 |
| To | -- |

Modified [GKPeerStateAvailable](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/stateavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKPeerStateConnected](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/gkpeerstateconnected)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKPeerStateConnecting](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/stateconnecting)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKPeerStateDisconnected](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/statedisconnected)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKPeerStateUnavailable](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/gkpeerstateunavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSendDataMode](https://developer.apple.com/documentation/gamekit/gksenddatamode)

|  | Deprecation |
| --- | --- |
| From | iOS 7.0 |
| To | -- |

Modified [GKSendDataReliable](https://developer.apple.com/documentation/gamekit/gksenddatamode/reliable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSendDataUnreliable](https://developer.apple.com/documentation/gamekit/gksenddatamode/unreliable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionMode](https://developer.apple.com/documentation/gamekit/gksessionmode)

|  | Deprecation |
| --- | --- |
| From | iOS 7.0 |
| To | -- |

Modified [GKSessionModeClient](https://developer.apple.com/documentation/gamekit/gksessionmode/gksessionmodeclient)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionModePeer](https://developer.apple.com/documentation/gamekit/gksessionmode/gksessionmodepeer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionModeServer](https://developer.apple.com/documentation/gamekit/gksessionmode/server)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceAudioUnavailableError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/audiounavailableerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceClientMissingRequiredMethodsError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceclientmissingrequiredmethodserror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code)

|  | Deprecation |
| --- | --- |
| From | iOS 7.0 |
| To | -- |

Modified [GKVoiceChatServiceInternalError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinternalerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceInvalidCallIDError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinvalidcalliderror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceInvalidParameterError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinvalidparametererror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceMethodCurrentlyInvalidError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatservicemethodcurrentlyinvaliderror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceNetworkConfigurationError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/networkconfigurationerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceNoRemotePacketsError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/noremotepacketserror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceOutOfMemoryError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/outofmemoryerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceRemoteParticipantBusyError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantbusyerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceRemoteParticipantCancelledError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantcancellederror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceRemoteParticipantDeclinedInviteError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantdeclinedinviteerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceRemoteParticipantHangupError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipanthanguperror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceRemoteParticipantResponseInvalidError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceremoteparticipantresponseinvaliderror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceUnableToConnectError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceunabletoconnecterror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceUninitializedClientError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceuninitializedclienterror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKVoiceChatServiceUnsupportedRemoteVersionError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceunsupportedremoteversionerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

#### GKSavedGame.h

Modified [-[GKLocalPlayer fetchSavedGamesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521086-fetchsavedgameswithcompletionhan)

|  | Declaration |
| --- | --- |
| From | ``` - (void)fetchSavedGamesWithCompletionHandler:(void (^)(NSArray *savedGames, NSError *error))handler ``` |
| To | ``` - (void)fetchSavedGamesWithCompletionHandler:(void (^ _Nullable)(NSArray<GKSavedGame *> * _Nullable savedGames, NSError * _Nullable error))handler ``` |

Modified [-[GKLocalPlayer resolveConflictingSavedGames:withData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521116-resolveconflictingsavedgames)

|  | Declaration |
| --- | --- |
| From | ``` - (void)resolveConflictingSavedGames:(NSArray *)conflictingSavedGames withData:(NSData *)data completionHandler:(void (^)(NSArray *savedGames, NSError *error))handler ``` |
| To | ``` - (void)resolveConflictingSavedGames:(NSArray<GKSavedGame *> * _Nonnull)conflictingSavedGames withData:(NSData * _Nonnull)data completionHandler:(void (^ _Nullable)(NSArray<GKSavedGame *> * _Nullable savedGames, NSError * _Nullable error))handler ``` |

#### GKSavedGameListener.h

Modified [-[GKSavedGameListener player:hasConflictingSavedGames:]](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387324-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player hasConflictingSavedGames:(NSArray *)savedGames ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player hasConflictingSavedGames:(NSArray<GKSavedGame *> * _Nonnull)savedGames ``` |

#### GKScore.h

Modified [+[GKScore reportScores:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1399252-report)

|  | Declaration |
| --- | --- |
| From | ``` + (void)reportScores:(NSArray *)scores withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` + (void)reportScores:(NSArray<GKScore *> * _Nonnull)scores withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

#### GKSessionError.h

Modified [GKSessionCancelledError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/cancellederror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionCannotEnableError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/cannotenableerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionConnectionClosedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/connectionclosederror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionConnectionFailedError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionconnectionfailederror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionConnectivityError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionconnectivityerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionDataTooBigError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessiondatatoobigerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionDeclinedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/declinederror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionError](https://developer.apple.com/documentation/gamekit/gksessionerror)

|  | Deprecation |
| --- | --- |
| From | iOS 7.0 |
| To | -- |

Modified [GKSessionInProgressError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/inprogresserror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionInternalError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessioninternalerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionInvalidParameterError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessioninvalidparametererror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionNotConnectedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/notconnectederror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionPeerNotFoundError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/peernotfounderror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionSystemError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionsystemerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionTimedOutError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessiontimedouterror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionTransportError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/transporterror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSessionUnknownError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/unknownerror)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

#### GKTurnBasedMatch.h

Added [-[GKTurnBasedEventListener player:wantsToQuitMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520537-player)Modified [-[GKTurnBasedEventHandlerDelegate handleInviteFromGameCenter:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1520926-handleinvite)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleInviteFromGameCenter:(NSArray *)playersToInvite ``` |
| To | ``` - (void)handleInviteFromGameCenter:(NSArray<GKPlayer *> * _Nonnull)playersToInvite ``` |

Modified [-[GKTurnBasedEventHandlerDelegate handleMatchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521053-handlematchended)

|  | Deprecation |
| --- | --- |
| From | iOS 6.0 |
| To | iOS 7.0 |

Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1556899-handleturneventformatch)

|  | Deprecation |
| --- | --- |
| From | iOS 6.0 |
| To | iOS 7.0 |

Modified [-[GKTurnBasedEventListener player:didRequestMatchWithOtherPlayers:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520693-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didRequestMatchWithOtherPlayers:(NSArray *)playersToInvite ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didRequestMatchWithOtherPlayers:(NSArray<GKPlayer *> * _Nonnull)playersToInvite ``` |

Modified [-[GKTurnBasedEventListener player:didRequestMatchWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1624268-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didRequestMatchWithPlayers:(NSArray *)playerIDsToInvite ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didRequestMatchWithPlayers:(NSArray<NSString *> * _Nonnull)playerIDsToInvite ``` |

Modified [-[GKTurnBasedEventListener player:receivedExchangeReplies:forCompletedExchange:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520827-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player receivedExchangeReplies:(NSArray *)replies forCompletedExchange:(GKTurnBasedExchange *)exchange forMatch:(GKTurnBasedMatch *)match ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player receivedExchangeReplies:(NSArray<GKTurnBasedExchangeReply *> * _Nonnull)replies forCompletedExchange:(GKTurnBasedExchange * _Nonnull)exchange forMatch:(GKTurnBasedMatch * _Nonnull)match ``` |

Modified [-[GKTurnBasedExchange cancelWithLocalizableMessageKey:arguments:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520779-cancel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelWithLocalizableMessageKey:(NSString *)key arguments:(NSArray *)arguments completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)cancelWithLocalizableMessageKey:(NSString * _Nonnull)key arguments:(NSArray<NSString *> * _Nonnull)arguments completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedExchange.recipients](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520849-recipients)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *recipients ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSArray<GKTurnBasedParticipant *> *recipients ``` |

Modified [GKTurnBasedExchange.replies](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520516-replies)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *replies ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSArray<GKTurnBasedExchangeReply *> *replies ``` |

Modified [-[GKTurnBasedExchange replyWithLocalizableMessageKey:arguments:data:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520478-reply)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replyWithLocalizableMessageKey:(NSString *)key arguments:(NSArray *)arguments data:(NSData *)data completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)replyWithLocalizableMessageKey:(NSString * _Nonnull)key arguments:(NSArray<NSString *> * _Nonnull)arguments data:(NSData * _Nonnull)data completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedMatch.activeExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520977-activeexchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) NSArray *activeExchanges ``` |
| To | ``` @property(readonly, retain, nonatomic, nullable) NSArray<GKTurnBasedExchange *> *activeExchanges ``` |

Modified [GKTurnBasedMatch.completedExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520918-completedexchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) NSArray *completedExchanges ``` |
| To | ``` @property(readonly, retain, nonatomic, nullable) NSArray<GKTurnBasedExchange *> *completedExchanges ``` |

Modified [-[GKTurnBasedMatch endMatchInTurnWithMatchData:scores:achievements:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521006-endmatchinturn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)endMatchInTurnWithMatchData:(NSData *)matchData scores:(NSArray *)scores achievements:(NSArray *)achievements completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)endMatchInTurnWithMatchData:(NSData * _Nonnull)matchData scores:(NSArray<GKScore *> * _Nullable)scores achievements:(NSArray<GKAchievement *> * _Nullable)achievements completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch endTurnWithNextParticipants:turnTimeout:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520765-endturnwithnextparticipants)

|  | Declaration |
| --- | --- |
| From | ``` - (void)endTurnWithNextParticipants:(NSArray *)nextParticipants turnTimeout:(NSTimeInterval)timeout matchData:(NSData *)matchData completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)endTurnWithNextParticipants:(NSArray<GKTurnBasedParticipant *> * _Nonnull)nextParticipants turnTimeout:(NSTimeInterval)timeout matchData:(NSData * _Nonnull)matchData completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedMatch.exchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521224-exchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) NSArray *exchanges ``` |
| To | ``` @property(readonly, retain, nonatomic, nullable) NSArray<GKTurnBasedExchange *> *exchanges ``` |

Modified [+[GKTurnBasedMatch loadMatchesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521207-loadmatcheswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadMatchesWithCompletionHandler:(void (^)(NSArray *matches, NSError *error))completionHandler ``` |
| To | ``` + (void)loadMatchesWithCompletionHandler:(void (^ _Nullable)(NSArray<GKTurnBasedMatch *> * _Nullable matches, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch participantQuitInTurnWithOutcome:nextParticipants:turnTimeout:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520500-participantquitinturnwithoutcome)

|  | Declaration |
| --- | --- |
| From | ``` - (void)participantQuitInTurnWithOutcome:(GKTurnBasedMatchOutcome)matchOutcome nextParticipants:(NSArray *)nextParticipants turnTimeout:(NSTimeInterval)timeout matchData:(NSData *)matchData completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)participantQuitInTurnWithOutcome:(GKTurnBasedMatchOutcome)matchOutcome nextParticipants:(NSArray<GKTurnBasedParticipant *> * _Nonnull)nextParticipants turnTimeout:(NSTimeInterval)timeout matchData:(NSData * _Nonnull)matchData completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedMatch.participants](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520875-participants)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, nonatomic) NSArray *participants ``` |
| To | ``` @property(readonly, retain, nonatomic, nullable) NSArray<GKTurnBasedParticipant *> *participants ``` |

Modified [-[GKTurnBasedMatch saveMergedMatchData:withResolvedExchanges:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521154-savemergedmatchdata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveMergedMatchData:(NSData *)matchData withResolvedExchanges:(NSArray *)exchanges completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)saveMergedMatchData:(NSData * _Nonnull)matchData withResolvedExchanges:(NSArray<GKTurnBasedExchange *> * _Nonnull)exchanges completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch sendExchangeToParticipants:data:localizableMessageKey:arguments:timeout:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520451-sendexchangetoparticipants)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sendExchangeToParticipants:(NSArray *)participants data:(NSData *)data localizableMessageKey:(NSString *)key arguments:(NSArray *)arguments timeout:(NSTimeInterval)timeout completionHandler:(void (^)(GKTurnBasedExchange *exchange, NSError *error))completionHandler ``` |
| To | ``` - (void)sendExchangeToParticipants:(NSArray<GKTurnBasedParticipant *> * _Nonnull)participants data:(NSData * _Nonnull)data localizableMessageKey:(NSString * _Nonnull)key arguments:(NSArray<NSString *> * _Nonnull)arguments timeout:(NSTimeInterval)timeout completionHandler:(void (^ _Nullable)(GKTurnBasedExchange * _Nonnull exchange, NSError * _Nonnull error))completionHandler ``` |

Modified [-[GKTurnBasedMatch sendReminderToParticipants:localizableMessageKey:arguments:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520947-sendremindertoparticipants)

|  | Declaration |
| --- | --- |
| From | ``` - (void)sendReminderToParticipants:(NSArray *)participants localizableMessageKey:(NSString *)key arguments:(NSArray *)arguments completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)sendReminderToParticipants:(NSArray<GKTurnBasedParticipant *> * _Nonnull)participants localizableMessageKey:(NSString * _Nonnull)key arguments:(NSArray<NSString *> * _Nonnull)arguments completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch setLocalizableMessageWithKey:arguments:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520510-setlocalizablemessagewithkey)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setLocalizableMessageWithKey:(NSString *)key arguments:(NSArray *)arguments ``` |
| To | ``` - (void)setLocalizableMessageWithKey:(NSString * _Nonnull)key arguments:(NSArray<NSString *> * _Nullable)arguments ``` |

#### GKTurnBasedMatchmakerViewController.h

Modified [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewController:didFindMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1520653-turnbasedmatchmakerviewcontrolle)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 9.0 | yes |

Modified [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewController:playerQuitForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1520967-turnbasedmatchmakerviewcontrolle)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 9.0 | yes |

#### GKVoiceChat.h

Modified [GKVoiceChat.playerIDs](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385721-playerids)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *playerIDs ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSArray<NSString *> *playerIDs ``` |

Modified [GKVoiceChat.players](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385701-players)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *players ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSArray<GKPlayer *> *players ``` |

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
