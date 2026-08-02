---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/GameKit.html
archived_at: '2026-07-18T02:55:58.222160Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# GameKit Changes

## GameKit

GKAchievement.hAdded [-[GKAchievement initWithIdentifier:player:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521092-initwithidentifier)Added [GKAchievement.player](https://developer.apple.com/documentation/gamekit/gkachievement/1520943-player)Added GKAchievement(Deprecated)Modified [-[GKAchievement initWithIdentifier:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520622-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initWithIdentifier:(NSString *)identifier ``` |

Modified [-[GKAchievement initWithIdentifier:forPlayer:]](https://developer.apple.com/documentation/gamekit/gkachievement/1625009-initwithidentifier)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initWithIdentifier:(NSString *)identifier forPlayer:(NSString *)playerID ``` | -- |
| To | ``` - (instancetype)initWithIdentifier:(NSString *)identifier forPlayer:(NSString *)playerID ``` | iOS 8.0 |

Modified [GKAchievement.playerID](https://developer.apple.com/documentation/gamekit/gkachievement/1625010-playerid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

GKAchievementViewController.hAdded GKAchievementViewController()Modified [GKAchievementViewController.achievementDelegate](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller/1520486-achievementdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<GKAchievementViewControllerDelegate> achievementDelegate ``` |
| To | ``` @property(assign, nonatomic) id<GKAchievementViewControllerDelegate> achievementDelegate ``` |

GKChallenge.hAdded [-[GKAchievement challengeComposeControllerWithMessage:players:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520805-challengecomposecontrollerwithme)Added [-[GKAchievement selectChallengeablePlayers:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520504-selectchallengeableplayers)Added [GKChallenge.issuingPlayer](https://developer.apple.com/documentation/gamekit/gkchallenge/1521010-issuingplayer)Added [GKChallenge.receivingPlayer](https://developer.apple.com/documentation/gamekit/gkchallenge/1520570-receivingplayer)Added [-[GKScore challengeComposeControllerWithMessage:players:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1521227-challengecomposecontrollerwithme)Added GKAchievement(GKChallengeDeprecated)Added GKScore(GKChallengeDeprecated)Modified [-[GKAchievement challengeComposeControllerWithPlayers:message:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1623556-challengecomposecontrollerwithpl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[GKAchievement selectChallengeablePlayerIDs:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521129-selectchallengeableplayerids)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [GKChallenge.issuingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521100-issuingplayerid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [GKChallenge.receivingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521113-receivingplayerid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[GKScore challengeComposeControllerWithPlayers:message:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1623555-challengecomposecontrollerwithpl)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

GKChallengeEventHandler.hModified [-[GKChallengeEventHandlerDelegate localPlayerDidCompleteChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1521031-localplayerdidcompletechallenge)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeEventHandlerDelegate localPlayerDidReceiveChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520987-localplayerdidreceive)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeEventHandlerDelegate localPlayerDidSelectChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520995-localplayerdidselectchallenge)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeEventHandlerDelegate remotePlayerDidCompleteChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520880-remoteplayerdidcomplete)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeEventHandlerDelegate shouldShowBannerForLocallyCompletedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520924-shouldshowbanner)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeEventHandlerDelegate shouldShowBannerForLocallyReceivedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1521055-shouldshowbanner)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeEventHandlerDelegate shouldShowBannerForRemotelyCompletedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520499-shouldshowbanner)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

GKError.hAdded [GKErrorPlayerPhotoFailure](https://developer.apple.com/documentation/gamekit/gkerror/code/playerphotofailure)Added [GKErrorUbiquityContainerUnavailable](https://developer.apple.com/documentation/gamekit/gkerror/code/ubiquitycontainerunavailable)GKEventListener.hModified [-[GKChallengeListener player:didCompleteChallenge:issuedByFriend:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494688-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeListener player:didReceiveChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494691-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeListener player:issuedChallengeWasCompleted:byFriend:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494686-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKChallengeListener player:wantsToPlayChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494684-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

GKFriendRequestComposeViewController.hAdded [-[GKFriendRequestComposeViewController addRecipientPlayers:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437199-addrecipientplayers)Added GKFriendRequestComposeViewController()Modified [-[GKFriendRequestComposeViewController addRecipientsWithPlayerIDs:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437188-addrecipientswithplayerids)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

GKGameCenterViewController.hAdded GKGameCenterViewController()Modified [GKGameCenterViewController.gameCenterDelegate](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520845-gamecenterdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<GKGameCenterControllerDelegate> gameCenterDelegate ``` |
| To | ``` @property(assign, nonatomic) id<GKGameCenterControllerDelegate> gameCenterDelegate ``` |

Modified [GKGameCenterViewController.viewState](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1521007-viewstate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) GKGameCenterViewControllerState viewState ``` |
| To | ``` @property(assign, nonatomic) GKGameCenterViewControllerState viewState ``` |

GKLeaderboard.hAdded [-[GKLeaderboard initWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503149-init)Added GKLeaderboard(Deprecated)Modified [-[GKLeaderboard init]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503125-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[GKLeaderboard initWithPlayerIDs:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503132-init)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initWithPlayerIDs:(NSArray *)playerIDs ``` | -- |
| To | ``` - (instancetype)initWithPlayerIDs:(NSArray *)playerIDs ``` | iOS 8.0 |

GKLeaderboardViewController.hAdded GKLeaderboardViewController()Modified [GKLeaderboardViewController.category](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/1520506-category)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *category ``` |
| To | ``` @property(copy, nonatomic) NSString *category ``` |

Modified [GKLeaderboardViewController.leaderboardDelegate](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/1520996-leaderboarddelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<GKLeaderboardViewControllerDelegate> leaderboardDelegate ``` |
| To | ``` @property(assign, nonatomic) id<GKLeaderboardViewControllerDelegate> leaderboardDelegate ``` |

Modified [GKLeaderboardViewController.timeScope](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/1520521-timescope)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) GKLeaderboardTimeScope timeScope ``` |
| To | ``` @property(assign, nonatomic) GKLeaderboardTimeScope timeScope ``` |

GKLocalPlayer.hAdded [-[GKLocalPlayer loadFriendPlayersWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515386-loadfriendplayers)Added GKLocalPlayer(Deprecated)Modified [GKLocalPlayer.friends](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515405-friends)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 8.0 | iOS 4.1 |

Modified [-[GKLocalPlayer loadFriendsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515391-loadfriendswithcompletionhandler)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 8.0 | iOS 4.1 |

Modified [-[GKLocalPlayer setDefaultLeaderboardCategoryID:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515385-setdefaultleaderboardcategoryid)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDefaultLeaderboardCategoryID:(NSString *)catogoryID completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)setDefaultLeaderboardCategoryID:(NSString *)categoryID completionHandler:(void (^)(NSError *error))completionHandler ``` |

Modified [GKLocalPlayerListener](https://developer.apple.com/documentation/gamekit/gklocalplayerlistener)

|  | Protocols |
| --- | --- |
| From | GKChallengeListener, GKInviteEventListener, GKTurnBasedEventListener |
| To | GKChallengeListener, GKInviteEventListener, GKSavedGameListener, GKTurnBasedEventListener |

GKMatch.hAdded [-[GKMatch chooseBestHostingPlayerWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502072-choosebesthostingplayer)Added [GKMatch.players](https://developer.apple.com/documentation/gamekit/gkmatch/1502074-players)Added [-[GKMatch sendData:toPlayers:dataMode:error:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502056-send)Added [-[GKMatchDelegate match:didReceiveData:fromRemotePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502069-match)Added [-[GKMatchDelegate match:player:didChangeConnectionState:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502048-match)Added [-[GKMatchDelegate match:shouldReinviteDisconnectedPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502038-match)Added GKMatch(Deprecated)Modified [-[GKMatch chooseBestHostPlayerWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502044-choosebesthostplayerwithcompleti)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [GKMatch.playerIDs](https://developer.apple.com/documentation/gamekit/gkmatch/1502064-playerids)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[GKMatch sendData:toPlayers:withDataMode:error:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502033-send)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 8.0 | iOS 4.1 |

Modified [-[GKMatchDelegate match:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502025-match)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKMatchDelegate match:didReceiveData:fromPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502054-match)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[GKMatchDelegate match:player:didChangeState:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502028-match)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[GKMatchDelegate match:shouldReinvitePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502058-match)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

GKMatchmaker.hAdded [GKInvite.sender](https://developer.apple.com/documentation/gamekit/gkinvite/1521073-sender)Added [-[GKInviteEventListener player:didRequestMatchWithRecipients:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520894-player)Added [GKMatchRequest.recipientResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521004-recipientresponsehandler)Added [GKMatchRequest.recipients](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520800-recipients)Added [-[GKMatchmaker cancelPendingInviteToPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520773-cancelpendinginvite)Added [-[GKMatchmaker findPlayersForHostedRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520973-findplayersforhostedrequest)Added [-[GKMatchmaker startBrowsingForNearbyPlayersWithHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521043-startbrowsingfornearbyplayerswit)Added [GKInviteRecipientResponse](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse)Added [GKInviteRecipientResponseAccepted](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviterecipientresponseaccepted)Added [GKInviteRecipientResponseDeclined](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviterecipientresponsedeclined)Added [GKInviteRecipientResponseFailed](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponsefailed)Added [GKInviteRecipientResponseIncompatible](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponseincompatible)Added [GKInviteRecipientResponseNoAnswer](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponsenoanswer)Added [GKInviteRecipientResponseUnableToConnect](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponseunabletoconnect)Added GKMatchmaker(GKDeprecated)Modified [GKInvite.inviter](https://developer.apple.com/documentation/gamekit/gkinvite/1520959-inviter)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 8.0 | iOS 4.1 |

Modified [-[GKInviteEventListener player:didAcceptInvite:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520672-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKInviteEventListener player:didRequestMatchWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1623695-player)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [GKMatchRequest.defaultNumberOfPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520608-defaultnumberofplayers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger defaultNumberOfPlayers ``` |
| To | ``` @property(assign) NSUInteger defaultNumberOfPlayers ``` |

Modified [GKMatchRequest.inviteMessage](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521164-invitemessage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *inviteMessage ``` |
| To | ``` @property(copy) NSString *inviteMessage ``` |

Modified [GKMatchRequest.inviteeResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520511-inviteeresponsehandler)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, copy) void (^inviteeResponseHandler)(NSString *playerID, GKInviteeResponse response) ``` | -- |
| To | ``` @property(copy) void (^inviteeResponseHandler)(NSString *playerID, GKInviteeResponse response) ``` | iOS 8.0 |

Modified [GKMatchRequest.maxPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521083-maxplayers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger maxPlayers ``` |
| To | ``` @property(assign) NSUInteger maxPlayers ``` |

Modified [GKMatchRequest.minPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520550-minplayers)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger minPlayers ``` |
| To | ``` @property(assign) NSUInteger minPlayers ``` |

Modified [GKMatchRequest.playerAttributes](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520912-playerattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) uint32_t playerAttributes ``` |
| To | ``` @property(assign) uint32_t playerAttributes ``` |

Modified [GKMatchRequest.playerGroup](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521071-playergroup)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger playerGroup ``` |
| To | ``` @property(assign) NSUInteger playerGroup ``` |

Modified [GKMatchRequest.playersToInvite](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520921-playerstoinvite)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, retain) NSArray *playersToInvite ``` | -- |
| To | ``` @property(retain) NSArray *playersToInvite ``` | iOS 8.0 |

Modified [-[GKMatchmaker cancelInviteToPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520576-cancelinvite)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[GKMatchmaker findPlayersForHostedMatchRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520915-findplayersforhostedmatchrequest)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 8.0 | iOS 4.1 |

Modified [-[GKMatchmaker startBrowsingForNearbyPlayersWithReachableHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521023-startbrowsingfornearbyplayerswit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

GKMatchmakerViewController.hAdded [-[GKMatchmakerViewController setHostedPlayer:didConnect:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492406-sethostedplayer)Added [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindHostedPlayers:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492421-matchmakerviewcontroller)Added [-[GKMatchmakerViewControllerDelegate matchmakerViewController:hostedPlayerDidAccept:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492412-matchmakerviewcontroller)Modified [-[GKMatchmakerViewController setHostedPlayer:connected:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492418-sethostedplayer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindMatch:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492416-matchmakerviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindPlayers:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492428-matchmakerviewcontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didReceiveAcceptFromHostedPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492436-matchmakerviewcontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

GKPeerPickerController.hModified [-[GKPeerPickerControllerDelegate peerPickerController:didConnectPeer:toSession:]](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/1622153-peerpickercontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKPeerPickerControllerDelegate peerPickerController:didSelectConnectionType:]](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/1622163-peerpickercontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKPeerPickerControllerDelegate peerPickerController:sessionForConnectionType:]](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/1622156-peerpickercontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKPeerPickerControllerDelegate peerPickerControllerDidCancel:]](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/1622161-peerpickercontrollerdidcancel)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [GKPeerPickerConnectionTypeNearby](https://developer.apple.com/documentation/gamekit/gkpeerpickerconnectiontype/gkpeerpickerconnectiontypenearby)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKPeerPickerConnectionTypeOnline](https://developer.apple.com/documentation/gamekit/gkpeerpickerconnectiontype/gkpeerpickerconnectiontypeonline)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

GKPlayer.hAdded GKPlayer(Deprecated)Modified [GKPlayer.isFriend](https://developer.apple.com/documentation/gamekit/gkplayer/1520467-isfriend)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 8.0 | iOS 4.1 |

GKPublicProtocols.hModified [-[GKSessionDelegate session:connectionWithPeerFailed:withError:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1521160-session)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKSessionDelegate session:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520662-session)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKSessionDelegate session:didReceiveConnectionRequestFromPeer:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520711-session)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKSessionDelegate session:peer:didChangeState:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520885-session)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKVoiceChatClient voiceChatService:didNotStartWithParticipantID:error:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521047-voicechatservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKVoiceChatClient voiceChatService:didReceiveInvitationFromParticipantID:callID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520997-voicechatservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKVoiceChatClient voiceChatService:didStartWithParticipantID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520971-voicechatservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKVoiceChatClient voiceChatService:didStopWithParticipantID:error:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520681-voicechatservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKVoiceChatClient voiceChatService:sendRealTimeData:toParticipantID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521009-voicechatservice)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

GKSavedGame.h (Added)Added [-[GKLocalPlayer deleteSavedGamesWithName:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520951-deletesavedgames)Added [-[GKLocalPlayer fetchSavedGamesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521086-fetchsavedgameswithcompletionhan)Added [-[GKLocalPlayer resolveConflictingSavedGames:withData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521116-resolveconflictingsavedgames)Added [-[GKLocalPlayer saveGameData:withName:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520527-savegamedata)Added [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame)Added [GKSavedGame.deviceName](https://developer.apple.com/documentation/gamekit/gksavedgame/1520629-devicename)Added [-[GKSavedGame loadDataWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gksavedgame/1520754-loaddatawithcompletionhandler)Added [GKSavedGame.modificationDate](https://developer.apple.com/documentation/gamekit/gksavedgame/1520829-modificationdate)Added [GKSavedGame.name](https://developer.apple.com/documentation/gamekit/gksavedgame/1520819-name)Added GKLocalPlayer(GKSavedGame)GKSavedGameListener.h (Added)Added [GKSavedGameListener](https://developer.apple.com/documentation/gamekit/gksavedgamelistener)Added [-[GKSavedGameListener player:didModifySavedGame:]](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387328-player)Added [-[GKSavedGameListener player:hasConflictingSavedGames:]](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387324-player)GKScore.hAdded [-[GKScore initWithLeaderboardIdentifier:player:]](https://developer.apple.com/documentation/gamekit/gkscore/1399254-init)Added [GKScore.player](https://developer.apple.com/documentation/gamekit/gkscore/1399246-player)Added GKScore(Deprecated)Modified [GKScore.context](https://developer.apple.com/documentation/gamekit/gkscore/1399250-context)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) uint64_t context ``` |
| To | ``` @property(assign, nonatomic) uint64_t context ``` |

Modified [-[GKScore initWithCategory:]](https://developer.apple.com/documentation/gamekit/gkscore/1399242-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithCategory:(NSString *)category ``` |
| To | ``` - (instancetype)initWithCategory:(NSString *)category ``` |

Modified [-[GKScore initWithLeaderboardIdentifier:]](https://developer.apple.com/documentation/gamekit/gkscore/1399240-initwithleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithLeaderboardIdentifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initWithLeaderboardIdentifier:(NSString *)identifier ``` |

Modified [-[GKScore initWithLeaderboardIdentifier:forPlayer:]](https://developer.apple.com/documentation/gamekit/gkscore/1620733-initwithleaderboardidentifier)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initWithLeaderboardIdentifier:(NSString *)identifier forPlayer:(NSString *)playerID ``` | -- |
| To | ``` - (instancetype)initWithLeaderboardIdentifier:(NSString *)identifier forPlayer:(NSString *)playerID ``` | iOS 8.0 |

Modified [GKScore.playerID](https://developer.apple.com/documentation/gamekit/gkscore/1399232-playerid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

GKSession.hModified [-[GKSession initWithSessionID:displayName:sessionMode:]](https://developer.apple.com/documentation/gamekit/gksession/1520488-initwithsessionid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [-[GKSession peersWithConnectionState:]](https://developer.apple.com/documentation/gamekit/gksession/1521191-peerswithconnectionstate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [-[GKSession sendData:toPeers:withDataMode:error:]](https://developer.apple.com/documentation/gamekit/gksession/1521185-send)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [-[GKSession sendDataToAllPeers:withDataMode:error:]](https://developer.apple.com/documentation/gamekit/gksession/1520999-senddata)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [GKSession.sessionMode](https://developer.apple.com/documentation/gamekit/gksession/1520767-sessionmode)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

GKTurnBasedMatch.hAdded [-[GKTurnBasedEventListener player:didRequestMatchWithOtherPlayers:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520693-player)Added [GKTurnBasedExchangeReply.replyDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520727-replydate)Added [GKTurnBasedParticipant.player](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521037-player)Modified [GKTurnBasedEventHandlerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 7.0 |

Modified [-[GKTurnBasedEventHandlerDelegate handleMatchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521053-handlematchended)

|  | Introduction | Optional |
| --- | --- | --- |
| From | iOS 5.0 | -- |
| To | iOS 6.0 | yes |

Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1556899-handleturneventformatch)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKTurnBasedEventListener player:didRequestMatchWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1624268-player)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | iOS 8.0 | yes |

Modified [-[GKTurnBasedEventListener player:matchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520554-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKTurnBasedEventListener player:receivedExchangeCancellation:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520649-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKTurnBasedEventListener player:receivedExchangeReplies:forCompletedExchange:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520827-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKTurnBasedEventListener player:receivedExchangeRequest:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521209-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKTurnBasedEventListener player:receivedTurnEventForMatch:didBecomeActive:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521017-player)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [GKTurnBasedExchange.status](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521166-status)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) GKTurnBasedExchangeStatus status ``` |
| To | ``` @property(assign, readonly, nonatomic) GKTurnBasedExchangeStatus status ``` |

Modified [GKTurnBasedParticipant.playerID](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520474-playerid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

GKTurnBasedMatchmakerViewController.hAdded GKTurnBasedMatchmakerViewController()GKVoiceChat.hAdded [GKVoiceChat.playerVoiceChatStateDidChangeHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385713-playervoicechatstatedidchangehan)Added [GKVoiceChat.players](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385701-players)Added [-[GKVoiceChat setPlayer:muted:]](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385717-setplayer)Added GKVoiceChat(Deprecated)Modified [GKVoiceChat.playerIDs](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385721-playerids)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | iOS 8.0 |

Modified [GKVoiceChat.playerStateUpdateHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385705-playerstateupdatehandler)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 8.0 | iOS 4.1 |

Modified [-[GKVoiceChat setMute:forPlayer:]](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385711-setmute)

|  | Deprecation | Introduction |
| --- | --- | --- |
| From | -- | iOS 4.0 |
| To | iOS 8.0 | iOS 5.0 |

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
