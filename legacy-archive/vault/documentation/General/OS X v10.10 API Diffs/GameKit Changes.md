---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/GameKit.html
archived_at: '2026-07-15T07:34:46.086572Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# GameKit Changes

## GameKit

GKAchievement.hAdded [-[GKAchievement initWithIdentifier:player:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521092-initwithidentifier)Added [GKAchievement.player](https://developer.apple.com/documentation/gamekit/gkachievement/1520943-player)Added GKAchievement(Deprecated)Modified [GKAchievement](https://developer.apple.com/documentation/gamekit/gkachievement)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKAchievement.hidden](https://developer.apple.com/documentation/gamekit/gkachievement/1521136-ishidden)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

Modified [-[GKAchievement initWithIdentifier:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520622-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (instancetype)initWithIdentifier:(NSString *)identifier ``` |

Modified [-[GKAchievement reportAchievementWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521108-reportachievementwithcompletionh)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[GKAchievement reportAchievements:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520509-reportachievements)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

GKAchievementDescription.hAdded GKAchievementDescription(UI)Modified [GKAchievementDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKAchievementDescription.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416587-groupidentifier)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(retain, readonly, atomic) NSString *groupIdentifier ``` | OS X 10.9 |
| To | ``` @property(nonatomic, retain, readonly) NSString *groupIdentifier ``` | OS X 10.8 |

Modified [GKAchievementDescription.replayable](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416578-replayable)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(getter=isReplayable, assign, readonly, atomic) BOOL replayable ``` | OS X 10.9 |
| To | ``` @property(nonatomic, getter=isReplayable, assign, readonly) BOOL replayable ``` | OS X 10.8 |

GKAchievementViewController.hModified [GKAchievementViewController](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller)

|  | Superclasses | Protocols |
| --- | --- | --- |
| From | NSViewController | GKViewController |
| To | GKGameCenterViewController | -- |

Modified [GKAchievementViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkachievementviewcontrollerdelegate)

|  | Protocols | Deprecation |
| --- | --- | --- |
| From | -- | -- |
| To | NSObject | OS X 10.10 |

GKChallenge.hAdded [-[GKAchievement challengeComposeControllerWithMessage:players:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520805-challengecomposecontrollerwithme)Added [+[GKAchievement reportAchievements:withEligibleChallenges:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520558-reportachievements)Added [-[GKAchievement selectChallengeablePlayers:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520504-selectchallengeableplayers)Added [GKChallenge.issuingPlayer](https://developer.apple.com/documentation/gamekit/gkchallenge/1521010-issuingplayer)Added [GKChallenge.receivingPlayer](https://developer.apple.com/documentation/gamekit/gkchallenge/1520570-receivingplayer)Added [-[GKScore challengeComposeControllerWithMessage:players:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1521227-challengecomposecontrollerwithme)Added [+[GKScore reportScores:withEligibleChallenges:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1520627-reportscores)Added GKAchievement(GKChallengeDeprecated)Added [GKChallengeComposeCompletionBlock](https://developer.apple.com/documentation/gamekit/gkchallengecomposecompletionblock)Added GKScore(GKChallengeDeprecated)Modified [-[GKAchievement issueChallengeToPlayers:message:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520984-issuechallenge)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.9 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [-[GKAchievement selectChallengeablePlayerIDs:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521129-selectchallengeableplayerids)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.9 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKAchievementChallenge](https://developer.apple.com/documentation/gamekit/gkachievementchallenge)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified [GKAchievementChallenge.achievement](https://developer.apple.com/documentation/gamekit/gkachievementchallenge/1520858-achievement)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKAchievement *achievement ``` |
| To | ``` @property(nonatomic, readonly, retain) GKAchievement *achievement ``` |

Modified [GKChallenge](https://developer.apple.com/documentation/gamekit/gkchallenge)

|  | Protocols | Introduction |
| --- | --- | --- |
| From | NSCoding | OS X 10.9 |
| To | NSCoding, NSSecureCoding | OS X 10.8 |

Modified [GKChallenge.completionDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520928-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSDate *completionDate ``` |
| To | ``` @property(nonatomic, readonly, retain) NSDate *completionDate ``` |

Modified [GKChallenge.issueDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520803-issuedate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSDate *issueDate ``` |
| To | ``` @property(nonatomic, readonly, retain) NSDate *issueDate ``` |

Modified [GKChallenge.issuingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521100-issuingplayerid)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *issuingPlayerID ``` | -- |
| To | ``` @property(nonatomic, readonly, copy) NSString *issuingPlayerID ``` | OS X 10.10 |

Modified [GKChallenge.message](https://developer.apple.com/documentation/gamekit/gkchallenge/1520998-message)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *message ``` |
| To | ``` @property(nonatomic, readonly, copy) NSString *message ``` |

Modified [GKChallenge.receivingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521113-receivingplayerid)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *receivingPlayerID ``` | -- |
| To | ``` @property(nonatomic, readonly, copy) NSString *receivingPlayerID ``` | OS X 10.10 |

Modified [GKChallenge.state](https://developer.apple.com/documentation/gamekit/gkchallenge/1521179-state)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, assign, atomic) GKChallengeState state ``` |
| To | ``` @property(nonatomic, readonly, assign) GKChallengeState state ``` |

Modified [-[GKScore issueChallengeToPlayers:message:]](https://developer.apple.com/documentation/gamekit/gkscore/1520610-issuechallengetoplayers)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.9 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKScoreChallenge](https://developer.apple.com/documentation/gamekit/gkscorechallenge)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified [GKScoreChallenge.score](https://developer.apple.com/documentation/gamekit/gkscorechallenge/1521014-score)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKScore *score ``` |
| To | ``` @property(nonatomic, readonly, retain) GKScore *score ``` |

GKChallengeEventHandler.hModified [GKChallengeEventHandler](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.9 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [+[GKChallengeEventHandler challengeEventHandler]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/1563241-challengeeventhandler)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKChallengeEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/1520556-delegate)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(assign, atomic) id<GKChallengeEventHandlerDelegate> delegate ``` | -- |
| To | ``` @property(nonatomic, assign) id<GKChallengeEventHandlerDelegate> delegate ``` | OS X 10.10 |

Modified [GKChallengeEventHandlerDelegate](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKChallengeEventHandlerDelegate localPlayerDidCompleteChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1521031-localplayerdidcompletechallenge)

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

GKChallengesViewController.hRemoved GKChallengesViewController()Modified [GKChallengesViewController](https://developer.apple.com/documentation/gamekit/gkchallengesviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

GKDialogController.hModified [-[GKDialogController dismiss:]](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/1520938-dismiss)

|  | Declaration |
| --- | --- |
| From | ``` - (void)dismiss:(id)sender ``` |
| To | ``` - (IBAction)dismiss:(id)sender ``` |

Modified [GKDialogController.parentWindow](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/1520890-parentwindow)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) NSWindow *parentWindow ``` |
| To | ``` @property(assign) IBOutlet NSWindow *parentWindow ``` |

GKError.hRemoved [GKErrorOffline](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerroroffline)Added [GKErrorInvitationsDisabled](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorinvitationsdisabled)Added [GKErrorPlayerPhotoFailure](https://developer.apple.com/documentation/gamekit/gkerror/code/playerphotofailure)Added [GKErrorPlayerStatusExceedsMaximumLength](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorplayerstatusexceedsmaximumlength)Added [GKErrorPlayerStatusInvalid](https://developer.apple.com/documentation/gamekit/gkerror/code/playerstatusinvalid)Added [GKErrorUbiquityContainerUnavailable](https://developer.apple.com/documentation/gamekit/gkerror/code/ubiquitycontainerunavailable)GKEventListener.h (Added)Added [GKChallengeListener](https://developer.apple.com/documentation/gamekit/gkchallengelistener)Added [-[GKChallengeListener player:didCompleteChallenge:issuedByFriend:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494688-player)Added [-[GKChallengeListener player:didReceiveChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494691-player)Added [-[GKChallengeListener player:issuedChallengeWasCompleted:byFriend:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494686-player)Added [-[GKChallengeListener player:wantsToPlayChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494684-player)GKFriendRequestComposeViewController.hAdded [-[GKFriendRequestComposeViewController addRecipientPlayers:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437199-addrecipientplayers)Modified [-[GKFriendRequestComposeViewController addRecipientsWithPlayerIDs:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437188-addrecipientswithplayerids)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKFriendRequestComposeViewController.composeViewDelegate](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437192-composeviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) id<GKFriendRequestComposeViewControllerDelegate> composeViewDelegate ``` |
| To | ``` @property(nonatomic, assign) id<GKFriendRequestComposeViewControllerDelegate> composeViewDelegate ``` |

GKGameCenterViewController.hAdded [GKGameCenterViewController.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520540-leaderboardidentifier)Modified [-[GKGameCenterControllerDelegate gameCenterViewControllerDidFinish:]](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate/1520771-gamecenterviewcontrollerdidfinis)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.9 |

Modified [GKGameCenterViewController.leaderboardCategory](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520837-leaderboardcategory)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(copy, atomic) NSString *leaderboardCategory ``` | -- |
| To | ``` @property(nonatomic, retain) NSString *leaderboardCategory ``` | OS X 10.10 |

Modified [GKGameCenterViewController.leaderboardTimeScope](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520464-leaderboardtimescope)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(assign, atomic) GKLeaderboardTimeScope leaderboardTimeScope ``` | -- |
| To | ``` @property(nonatomic, assign) GKLeaderboardTimeScope leaderboardTimeScope ``` | OS X 10.10 |

GKLeaderboard.hRemoved GKLeaderboard(GKAdditions)Added [GKLeaderboard.identifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503141-identifier)Added [-[GKLeaderboard initWithPlayers:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503149-init)Added GKLeaderboard(Deprecated)Added GKLeaderboard(UI)Modified [GKLeaderboard.category](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503154-category)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKLeaderboard.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503135-groupidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSString *groupIdentifier ``` |
| To | ``` @property(nonatomic, readonly, retain) NSString *groupIdentifier ``` |

Modified [-[GKLeaderboard init]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503125-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)init ``` |
| To | ``` - (instancetype)init ``` |

Modified [-[GKLeaderboard initWithPlayerIDs:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503132-init)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initWithPlayerIDs:(NSArray *)playerIDs ``` | -- |
| To | ``` - (instancetype)initWithPlayerIDs:(NSArray *)playerIDs ``` | OS X 10.10 |

Modified [-[GKLeaderboard loadImageWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503161-loadimagewithcompletionhandler)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified [+[GKLeaderboard loadLeaderboardsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503128-loadleaderboards)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified [+[GKLeaderboard setDefaultLeaderboard:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503123-setdefaultleaderboard)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` + (void)setDefaultLeaderboard:(NSString *)categoryID withCompletionHandler:(void (^)(NSError *error))completionHandler ``` | -- |
| To | ``` + (void)setDefaultLeaderboard:(NSString *)leaderboardIdentifier withCompletionHandler:(void (^)(NSError *error))completionHandler ``` | OS X 10.10 |

GKLeaderboardSet.h (Added)Added [GKLeaderboardSet](https://developer.apple.com/documentation/gamekit/gkleaderboardset)Added [GKLeaderboardSet.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451800-groupidentifier)Added [GKLeaderboardSet.identifier](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451802-identifier)Added [-[GKLeaderboardSet loadImageWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451812-loadimage)Added [+[GKLeaderboardSet loadLeaderboardSetsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451798-loadleaderboardsetswithcompletio)Added [-[GKLeaderboardSet loadLeaderboardsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451810-loadleaderboardswithcompletionha)Added [GKLeaderboardSet.title](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451804-title)Added GKLeaderboardSet(UI)GKLeaderboardViewController.hModified [GKLeaderboardViewController](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller)

|  | Superclasses | Protocols |
| --- | --- | --- |
| From | NSViewController | GKViewController |
| To | GKGameCenterViewController | -- |

Modified [GKLeaderboardViewController.timeScope](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller/1520521-timescope)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) GKLeaderboardTimeScope timeScope ``` |
| To | ``` @property(assign, atomic) GKLeaderboardTimeScope timeScope ``` |

Modified [GKLeaderboardViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontrollerdelegate)

|  | Protocols | Deprecation |
| --- | --- | --- |
| From | -- | -- |
| To | NSObject | OS X 10.10 |

GKLocalPlayer.hRemoved GKLocalPlayer(GKAdditions)Added [-[GKLocalPlayer generateIdentityVerificationSignatureWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515407-generateidentityverificationsign)Added [-[GKLocalPlayer loadDefaultLeaderboardIdentifierWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515404-loaddefaultleaderboardidentifier)Added [-[GKLocalPlayer loadFriendPlayersWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515386-loadfriendplayers)Added [-[GKLocalPlayer registerListener:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515393-registerlistener)Added [-[GKLocalPlayer setDefaultLeaderboardIdentifier:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515408-setdefaultleaderboardidentifier)Added [-[GKLocalPlayer unregisterAllListeners]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515388-unregisteralllisteners)Added [-[GKLocalPlayer unregisterListener:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515389-unregisterlistener)Added [GKLocalPlayerListener](https://developer.apple.com/documentation/gamekit/gklocalplayerlistener)Added GKLocalPlayer(Deprecated)Added GKLocalPlayer(GKLocalPlayerEvents)Modified [-[GKLocalPlayer authenticateWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515406-authenticatewithcompletionhandle)

|  | Deprecation |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified [GKLocalPlayer.friends](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515405-friends)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKLocalPlayer loadDefaultLeaderboardCategoryIDWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515398-loaddefaultleaderboardcategoryid)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.9 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [-[GKLocalPlayer loadFriendsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515391-loadfriendswithcompletionhandler)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (void)loadFriendsWithCompletionHandler:(void (^)(NSArray *friends, NSError *error))completionHandler ``` | -- |
| To | ``` - (void)loadFriendsWithCompletionHandler:(void (^)(NSArray *friendIDs, NSError *error))completionHandler ``` | OS X 10.10 |

Modified [-[GKLocalPlayer setDefaultLeaderboardCategoryID:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515385-setdefaultleaderboardcategoryid)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.9 | -- |
| To | OS X 10.8 | OS X 10.10 |

GKMatch.hRemoved GKMatch(GKAdditions)Added [-[GKMatch chooseBestHostingPlayerWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502072-choosebesthostingplayer)Added [GKMatch.players](https://developer.apple.com/documentation/gamekit/gkmatch/1502074-players)Added [-[GKMatch sendData:toPlayers:dataMode:error:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502056-send)Added [-[GKMatchDelegate match:didReceiveData:fromRemotePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502069-match)Added [-[GKMatchDelegate match:player:didChangeConnectionState:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502048-match)Added [-[GKMatchDelegate match:shouldReinviteDisconnectedPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502038-match)Added GKMatch(Deprecated)Modified [-[GKMatch chooseBestHostPlayerWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502044-choosebesthostplayerwithcompleti)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKMatch.delegate](https://developer.apple.com/documentation/gamekit/gkmatch/1502046-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) id<GKMatchDelegate> delegate ``` |
| To | ``` @property(nonatomic, assign) id<GKMatchDelegate> delegate ``` |

Modified [GKMatch.expectedPlayerCount](https://developer.apple.com/documentation/gamekit/gkmatch/1502051-expectedplayercount)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSUInteger expectedPlayerCount ``` |
| To | ``` @property(nonatomic, readonly) NSUInteger expectedPlayerCount ``` |

Modified [GKMatch.playerIDs](https://developer.apple.com/documentation/gamekit/gkmatch/1502064-playerids)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(readonly, atomic) NSArray *playerIDs ``` | -- |
| To | ``` @property(nonatomic, readonly) NSArray *playerIDs ``` | OS X 10.10 |

Modified [-[GKMatch sendData:toPlayers:withDataMode:error:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502033-send)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKMatchDelegate match:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502025-match)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKMatchDelegate match:didReceiveData:fromPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502054-match)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [-[GKMatchDelegate match:player:didChangeState:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502028-match)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.8 | yes |

Modified [-[GKMatchDelegate match:shouldReinvitePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502058-match)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

GKMatchmaker.hRemoved GKInvite(GKAdditions)Removed GKMatchmaker(GKAdditions)Added [GKInvite.sender](https://developer.apple.com/documentation/gamekit/gkinvite/1521073-sender)Added [GKInviteEventListener](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener)Added [-[GKInviteEventListener player:didAcceptInvite:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520672-player)Added [-[GKInviteEventListener player:didRequestMatchWithRecipients:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520894-player)Added [GKMatchRequest.recipientResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521004-recipientresponsehandler)Added [GKMatchRequest.recipients](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520800-recipients)Added [-[GKMatchmaker cancelPendingInviteToPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520773-cancelpendinginvite)Added [-[GKMatchmaker findPlayersForHostedRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520973-findplayersforhostedrequest)Added [-[GKMatchmaker startBrowsingForNearbyPlayersWithHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521043-startbrowsingfornearbyplayerswit)Added [GKInviteRecipientResponse](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse)Added [GKInviteRecipientResponseAccepted](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviterecipientresponseaccepted)Added [GKInviteRecipientResponseDeclined](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviterecipientresponsedeclined)Added [GKInviteRecipientResponseFailed](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponsefailed)Added [GKInviteRecipientResponseIncompatible](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponseincompatible)Added [GKInviteRecipientResponseNoAnswer](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponsenoanswer)Added [GKInviteRecipientResponseUnableToConnect](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/inviterecipientresponseunabletoconnect)Added GKMatchmaker(GKDeprecated)Modified [GKInvite.inviter](https://developer.apple.com/documentation/gamekit/gkinvite/1520959-inviter)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *inviter ``` | -- |
| To | ``` @property(readonly, retain, atomic) NSString *inviter ``` | OS X 10.10 |

Modified [GKMatchRequest.defaultNumberOfPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520608-defaultnumberofplayers)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(nonatomic, assign) NSUInteger defaultNumberOfPlayers ``` | OS X 10.9 |
| To | ``` @property(assign) NSUInteger defaultNumberOfPlayers ``` | OS X 10.8 |

Modified [GKMatchRequest.inviteMessage](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521164-invitemessage)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` @property(nonatomic, copy) NSString *inviteMessage ``` | OS X 10.9 |
| To | ``` @property(copy) NSString *inviteMessage ``` | OS X 10.8 |

Modified [GKMatchRequest.inviteeResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520511-inviteeresponsehandler)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(nonatomic, copy) void (^inviteeResponseHandler)(NSString *playerID, GKInviteeResponse response) ``` | -- |
| To | ``` @property(copy) void (^inviteeResponseHandler)(NSString *playerID, GKInviteeResponse response) ``` | OS X 10.10 |

Modified [GKMatchRequest.maxPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521083-maxplayers)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) NSUInteger maxPlayers ``` |
| To | ``` @property(assign) NSUInteger maxPlayers ``` |

Modified [GKMatchRequest.minPlayers](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520550-minplayers)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) NSUInteger minPlayers ``` |
| To | ``` @property(assign) NSUInteger minPlayers ``` |

Modified [GKMatchRequest.playerAttributes](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520912-playerattributes)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) uint32_t playerAttributes ``` |
| To | ``` @property(assign) uint32_t playerAttributes ``` |

Modified [GKMatchRequest.playerGroup](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521071-playergroup)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) NSUInteger playerGroup ``` |
| To | ``` @property(assign) NSUInteger playerGroup ``` |

Modified [GKMatchRequest.playersToInvite](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520921-playerstoinvite)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(retain, atomic) NSArray *playersToInvite ``` | -- |
| To | ``` @property(retain) NSArray *playersToInvite ``` | OS X 10.10 |

Modified [-[GKMatchmaker cancelInviteToPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520576-cancelinvite)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKMatchmaker findPlayersForHostedMatchRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520915-findplayersforhostedmatchrequest)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKMatchmaker.inviteHandler](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521060-invitehandler)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(copy, atomic) void (^inviteHandler)(GKInvite *acceptedInvite, NSArray *playersToInvite) ``` | -- |
| To | ``` @property(nonatomic, copy) void (^inviteHandler)(GKInvite *acceptedInvite, NSArray *playerIDsToInvite) ``` | OS X 10.10 |

Modified [-[GKMatchmaker startBrowsingForNearbyPlayersWithReachableHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521023-startbrowsingfornearbyplayerswit)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

GKMatchmakerViewController.hRemoved GKMatchmakerViewController()Added [-[GKMatchmakerViewController setHostedPlayer:didConnect:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492406-sethostedplayer)Added [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindHostedPlayers:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492421-matchmakerviewcontroller)Added [-[GKMatchmakerViewControllerDelegate matchmakerViewController:hostedPlayerDidAccept:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492412-matchmakerviewcontroller)Modified [GKMatchmakerViewController.defaultInvitationMessage](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492409-defaultinvitationmessage)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @property(copy, atomic) NSString *defaultInvitationMessage ``` | -- |
| To | ``` @property(nonatomic, copy) NSString *defaultInvitationMessage ``` | OS X 10.10 |

Modified [GKMatchmakerViewController.hosted](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492414-ishosted)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, getter=isHosted, atomic) BOOL hosted ``` |
| To | ``` @property(nonatomic, assign, getter=isHosted) BOOL hosted ``` |

Modified [GKMatchmakerViewController.matchRequest](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492410-matchrequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKMatchRequest *matchRequest ``` |
| To | ``` @property(nonatomic, readonly, retain) GKMatchRequest *matchRequest ``` |

Modified [GKMatchmakerViewController.matchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492426-matchmakerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) id<GKMatchmakerViewControllerDelegate> matchmakerDelegate ``` |
| To | ``` @property(nonatomic, assign) id<GKMatchmakerViewControllerDelegate> matchmakerDelegate ``` |

Modified [-[GKMatchmakerViewController setHostedPlayer:connected:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492418-sethostedplayer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindMatch:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492416-matchmakerviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindPlayers:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492428-matchmakerviewcontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didReceiveAcceptFromHostedPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492436-matchmakerviewcontroller)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

GKNotificationBanner.hModified [+[GKNotificationBanner showBannerWithTitle:message:duration:completionHandler:]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515368-showbannerwithtitle)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

GKPlayer.hAdded GKPlayer(Deprecated)Added GKPlayer(UI)Modified [GKPlayer.displayName](https://developer.apple.com/documentation/gamekit/gkplayer/1520695-displayname)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified [GKPlayer.isFriend](https://developer.apple.com/documentation/gamekit/gkplayer/1520467-isfriend)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

GKPublicConstants.h (Added)Added [GKPeerConnectionState](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate)Added [GKPeerStateAvailable](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/stateavailable)Added [GKPeerStateConnected](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/gkpeerstateconnected)Added [GKPeerStateConnecting](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/stateconnecting)Added [GKPeerStateDisconnected](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/statedisconnected)Added [GKPeerStateUnavailable](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/gkpeerstateunavailable)Added [GKSendDataMode](https://developer.apple.com/documentation/gamekit/gksenddatamode)Added [GKSendDataReliable](https://developer.apple.com/documentation/gamekit/gksenddatamode/reliable)Added [GKSendDataUnreliable](https://developer.apple.com/documentation/gamekit/gksenddatamode/unreliable)Added [GKSessionMode](https://developer.apple.com/documentation/gamekit/gksessionmode)Added [GKSessionModeClient](https://developer.apple.com/documentation/gamekit/gksessionmode/gksessionmodeclient)Added [GKSessionModePeer](https://developer.apple.com/documentation/gamekit/gksessionmode/gksessionmodepeer)Added [GKSessionModeServer](https://developer.apple.com/documentation/gamekit/gksessionmode/server)Added [GKVoiceChatServiceAudioUnavailableError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/audiounavailableerror)Added [GKVoiceChatServiceClientMissingRequiredMethodsError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceclientmissingrequiredmethodserror)Added [GKVoiceChatServiceInternalError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinternalerror)Added [GKVoiceChatServiceInvalidCallIDError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinvalidcalliderror)Added [GKVoiceChatServiceInvalidParameterError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinvalidparametererror)Added [GKVoiceChatServiceMethodCurrentlyInvalidError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatservicemethodcurrentlyinvaliderror)Added [GKVoiceChatServiceNetworkConfigurationError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/networkconfigurationerror)Added [GKVoiceChatServiceNoRemotePacketsError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/noremotepacketserror)Added [GKVoiceChatServiceOutOfMemoryError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/outofmemoryerror)Added [GKVoiceChatServiceRemoteParticipantBusyError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantbusyerror)Added [GKVoiceChatServiceRemoteParticipantCancelledError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantcancellederror)Added [GKVoiceChatServiceRemoteParticipantDeclinedInviteError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantdeclinedinviteerror)Added [GKVoiceChatServiceRemoteParticipantHangupError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipanthanguperror)Added [GKVoiceChatServiceRemoteParticipantResponseInvalidError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceremoteparticipantresponseinvaliderror)Added [GKVoiceChatServiceUnableToConnectError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceunabletoconnecterror)Added [GKVoiceChatServiceUninitializedClientError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceuninitializedclienterror)Added [GKVoiceChatServiceUnsupportedRemoteVersionError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceunsupportedremoteversionerror)GKPublicProtocols.h (Added)Added [GKSessionDelegate](https://developer.apple.com/documentation/gamekit/gksessiondelegate)Added [-[GKSessionDelegate session:connectionWithPeerFailed:withError:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1521160-session)Added [-[GKSessionDelegate session:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520662-session)Added [-[GKSessionDelegate session:didReceiveConnectionRequestFromPeer:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520711-session)Added [-[GKSessionDelegate session:peer:didChangeState:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520885-session)Added [GKVoiceChatClient](https://developer.apple.com/documentation/gamekit/gkvoicechatclient)Added [-[GKVoiceChatClient participantID]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520641-participantid)Added [-[GKVoiceChatClient voiceChatService:didNotStartWithParticipantID:error:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521047-voicechatservice)Added [-[GKVoiceChatClient voiceChatService:didReceiveInvitationFromParticipantID:callID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520997-voicechatservice)Added [-[GKVoiceChatClient voiceChatService:didStartWithParticipantID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520971-voicechatservice)Added [-[GKVoiceChatClient voiceChatService:didStopWithParticipantID:error:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520681-voicechatservice)Added [-[GKVoiceChatClient voiceChatService:sendData:toParticipantID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521075-voicechatservice)Added [-[GKVoiceChatClient voiceChatService:sendRealTimeData:toParticipantID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521009-voicechatservice)GKSavedGame.h (Added)Added [-[GKLocalPlayer deleteSavedGamesWithName:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520951-deletesavedgames)Added [-[GKLocalPlayer fetchSavedGamesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521086-fetchsavedgameswithcompletionhan)Added [-[GKLocalPlayer resolveConflictingSavedGames:withData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521116-resolveconflictingsavedgames)Added [-[GKLocalPlayer saveGameData:withName:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520527-savegamedata)Added [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame)Added [GKSavedGame.deviceName](https://developer.apple.com/documentation/gamekit/gksavedgame/1520629-devicename)Added [-[GKSavedGame loadDataWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gksavedgame/1520754-loaddatawithcompletionhandler)Added [GKSavedGame.modificationDate](https://developer.apple.com/documentation/gamekit/gksavedgame/1520829-modificationdate)Added [GKSavedGame.name](https://developer.apple.com/documentation/gamekit/gksavedgame/1520819-name)Added GKLocalPlayer(GKSavedGame)GKSavedGameListener.h (Added)Added [GKSavedGameListener](https://developer.apple.com/documentation/gamekit/gksavedgamelistener)Added [-[GKSavedGameListener player:didModifySavedGame:]](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387328-player)Added [-[GKSavedGameListener player:hasConflictingSavedGames:]](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387324-player)GKScore.hAdded [-[GKScore initWithLeaderboardIdentifier:]](https://developer.apple.com/documentation/gamekit/gkscore/1399240-initwithleaderboardidentifier)Added [-[GKScore initWithLeaderboardIdentifier:player:]](https://developer.apple.com/documentation/gamekit/gkscore/1399254-init)Added [GKScore.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkscore/1399248-leaderboardidentifier)Added [GKScore.player](https://developer.apple.com/documentation/gamekit/gkscore/1399246-player)Added GKScore(Deprecated)Modified [GKScore](https://developer.apple.com/documentation/gamekit/gkscore)

|  | Protocols |
| --- | --- |
| From | NSCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKScore.category](https://developer.apple.com/documentation/gamekit/gkscore/1399225-category)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKScore.context](https://developer.apple.com/documentation/gamekit/gkscore/1399250-context)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) uint64_t context ``` |
| To | ``` @property(assign, atomic) uint64_t context ``` |

Modified [-[GKScore initWithCategory:]](https://developer.apple.com/documentation/gamekit/gkscore/1399242-init)

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` - (id)initWithCategory:(NSString *)category ``` | -- |
| To | ``` - (instancetype)initWithCategory:(NSString *)category ``` | OS X 10.10 |

Modified [GKScore.playerID](https://developer.apple.com/documentation/gamekit/gkscore/1399232-playerid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKScore reportScoreWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1399223-report)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[GKScore reportScores:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1399252-report)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

GKSession.h (Added)Added [GKSession](https://developer.apple.com/documentation/gamekit/gksession)Added [-[GKSession acceptConnectionFromPeer:error:]](https://developer.apple.com/documentation/gamekit/gksession/1520935-acceptconnection)Added [GKSession.available](https://developer.apple.com/documentation/gamekit/gksession/1520566-isavailable)Added [-[GKSession cancelConnectToPeer:]](https://developer.apple.com/documentation/gamekit/gksession/1520823-cancelconnecttopeer)Added [-[GKSession connectToPeer:withTimeout:]](https://developer.apple.com/documentation/gamekit/gksession/1520572-connect)Added [GKSession.delegate](https://developer.apple.com/documentation/gamekit/gksession/1520491-delegate)Added [-[GKSession denyConnectionFromPeer:]](https://developer.apple.com/documentation/gamekit/gksession/1521117-denyconnectionfrompeer)Added [-[GKSession disconnectFromAllPeers]](https://developer.apple.com/documentation/gamekit/gksession/1521120-disconnectfromallpeers)Added [-[GKSession disconnectPeerFromAllPeers:]](https://developer.apple.com/documentation/gamekit/gksession/1520534-disconnectpeer)Added [GKSession.disconnectTimeout](https://developer.apple.com/documentation/gamekit/gksession/1521193-disconnecttimeout)Added [GKSession.displayName](https://developer.apple.com/documentation/gamekit/gksession/1520904-displayname)Added [-[GKSession displayNameForPeer:]](https://developer.apple.com/documentation/gamekit/gksession/1520606-displaynameforpeer)Added [-[GKSession initWithSessionID:displayName:sessionMode:]](https://developer.apple.com/documentation/gamekit/gksession/1520488-initwithsessionid)Added [GKSession.peerID](https://developer.apple.com/documentation/gamekit/gksession/1520703-peerid)Added [-[GKSession peersWithConnectionState:]](https://developer.apple.com/documentation/gamekit/gksession/1521191-peerswithconnectionstate)Added [-[GKSession sendData:toPeers:withDataMode:error:]](https://developer.apple.com/documentation/gamekit/gksession/1521185-send)Added [-[GKSession sendDataToAllPeers:withDataMode:error:]](https://developer.apple.com/documentation/gamekit/gksession/1520999-senddata)Added [GKSession.sessionID](https://developer.apple.com/documentation/gamekit/gksession/1520620-sessionid)Added [GKSession.sessionMode](https://developer.apple.com/documentation/gamekit/gksession/1520767-sessionmode)Added [-[GKSession setDataReceiveHandler:withContext:]](https://developer.apple.com/documentation/gamekit/gksession/1520831-setdatareceivehandler)GKSessionError.h (Added)Added [GKSessionCancelledError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/cancellederror)Added [GKSessionCannotEnableError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/cannotenableerror)Added [GKSessionConnectionClosedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/connectionclosederror)Added [GKSessionConnectionFailedError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionconnectionfailederror)Added [GKSessionConnectivityError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionconnectivityerror)Added [GKSessionDataTooBigError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessiondatatoobigerror)Added [GKSessionDeclinedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/declinederror)Added [GKSessionErrorDomain](https://developer.apple.com/documentation/gamekit/gksessionerrordomain)Added [GKSessionInProgressError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/inprogresserror)Added [GKSessionInternalError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessioninternalerror)Added [GKSessionInvalidParameterError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessioninvalidparametererror)Added [GKSessionNotConnectedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/notconnectederror)Added [GKSessionPeerNotFoundError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/peernotfounderror)Added [GKSessionSystemError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionsystemerror)Added [GKSessionTimedOutError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessiontimedouterror)Added [GKSessionTransportError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/transporterror)Added [GKSessionUnknownError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/unknownerror)GKTurnBasedMatch.hAdded [GKTurnBasedEventListener](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener)Added [-[GKTurnBasedEventListener player:didRequestMatchWithOtherPlayers:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520693-player)Added [-[GKTurnBasedEventListener player:matchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520554-player)Added [-[GKTurnBasedEventListener player:receivedExchangeCancellation:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520649-player)Added [-[GKTurnBasedEventListener player:receivedExchangeReplies:forCompletedExchange:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520827-player)Added [-[GKTurnBasedEventListener player:receivedExchangeRequest:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521209-player)Added [-[GKTurnBasedEventListener player:receivedTurnEventForMatch:didBecomeActive:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521017-player)Added [GKTurnBasedExchange](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange)Added [-[GKTurnBasedExchange cancelWithLocalizableMessageKey:arguments:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520779-cancel)Added [GKTurnBasedExchange.completionDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520994-completiondate)Added [GKTurnBasedExchange.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521121-data)Added [GKTurnBasedExchange.exchangeID](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520666-exchangeid)Added [GKTurnBasedExchange.message](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520633-message)Added [GKTurnBasedExchange.recipients](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520849-recipients)Added [GKTurnBasedExchange.replies](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520516-replies)Added [-[GKTurnBasedExchange replyWithLocalizableMessageKey:arguments:data:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520478-reply)Added [GKTurnBasedExchange.sendDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521131-senddate)Added [GKTurnBasedExchange.sender](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520936-sender)Added [GKTurnBasedExchange.status](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521166-status)Added [GKTurnBasedExchange.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521105-timeoutdate)Added [GKTurnBasedExchangeReply](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply)Added [GKTurnBasedExchangeReply.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520729-data)Added [GKTurnBasedExchangeReply.message](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520896-message)Added [GKTurnBasedExchangeReply.recipient](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1521025-recipient)Added [GKTurnBasedExchangeReply.replyDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520727-replydate)Added [GKTurnBasedMatch.activeExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520977-activeexchanges)Added [GKTurnBasedMatch.completedExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520918-completedexchanges)Added [-[GKTurnBasedMatch endMatchInTurnWithMatchData:scores:achievements:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521006-endmatchinturn)Added [GKTurnBasedMatch.exchangeDataMaximumSize](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521002-exchangedatamaximumsize)Added [GKTurnBasedMatch.exchangeMaxInitiatedExchangesPerPlayer](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520965-exchangemaxinitiatedexchangesper)Added [GKTurnBasedMatch.exchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521224-exchanges)Added [-[GKTurnBasedMatch saveMergedMatchData:withResolvedExchanges:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521154-savemergedmatchdata)Added [-[GKTurnBasedMatch sendExchangeToParticipants:data:localizableMessageKey:arguments:timeout:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520451-sendexchangetoparticipants)Added [-[GKTurnBasedMatch sendReminderToParticipants:localizableMessageKey:arguments:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520947-sendremindertoparticipants)Added [-[GKTurnBasedMatch setLocalizableMessageWithKey:arguments:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520510-setlocalizablemessagewithkey)Added [GKTurnBasedParticipant.player](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521037-player)Added [GKExchangeTimeoutDefault](https://developer.apple.com/documentation/gamekit/gkexchangetimeoutdefault)Added [GKExchangeTimeoutNone](https://developer.apple.com/documentation/gamekit/gkexchangetimeoutnone)Added [GKTurnBasedExchangeStatus](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus)Added [GKTurnBasedExchangeStatusActive](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/active)Added [GKTurnBasedExchangeStatusCanceled](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/gkturnbasedexchangestatuscanceled)Added [GKTurnBasedExchangeStatusComplete](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/gkturnbasedexchangestatuscomplete)Added [GKTurnBasedExchangeStatusResolved](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/gkturnbasedexchangestatusresolved)Added [GKTurnBasedExchangeStatusUnknown](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/unknown)Modified [GKTurnBasedEventHandler](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKTurnBasedEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521013-delegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [+[GKTurnBasedEventHandler sharedTurnBasedEventHandler]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521211-sharedturnbasedeventhandler)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKTurnBasedEventHandlerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKTurnBasedEventHandlerDelegate handleInviteFromGameCenter:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1520926-handleinvite)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKTurnBasedEventHandlerDelegate handleMatchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521053-handlematchended)

|  | Deprecation | Optional |
| --- | --- | --- |
| From | -- | -- |
| To | OS X 10.10 | yes |

Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1556899-handleturneventformatch)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:didBecomeActive:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521103-handleturnevent)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKTurnBasedMatch.creationDate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521168-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSDate *creationDate ``` |
| To | ``` @property(readonly, retain, atomic) NSDate *creationDate ``` |

Modified [GKTurnBasedMatch.matchDataMaximumSize](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520731-matchdatamaximumsize)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified [GKTurnBasedMatch.matchID](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520625-matchid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *matchID ``` |
| To | ``` @property(readonly, retain, atomic) NSString *matchID ``` |

Modified [-[GKTurnBasedMatch saveCurrentTurnWithMatchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520761-savecurrentturn)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

Modified [GKTurnBasedParticipant.playerID](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520474-playerid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKTurnBasedParticipant.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521187-timeoutdate)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.8 |

GKTurnBasedMatchmakerViewController.hModified [GKTurnBasedMatchmakerViewController.showExistingMatches](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1521099-showexistingmatches)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, assign, atomic) BOOL showExistingMatches ``` |
| To | ``` @property(nonatomic, readwrite, assign) BOOL showExistingMatches ``` |

Modified [GKTurnBasedMatchmakerViewController.turnBasedMatchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1520697-turnbasedmatchmakerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, assign, atomic) id<GKTurnBasedMatchmakerViewControllerDelegate> turnBasedMatchmakerDelegate ``` |
| To | ``` @property(nonatomic, readwrite, assign) id<GKTurnBasedMatchmakerViewControllerDelegate> turnBasedMatchmakerDelegate ``` |

Modified [GKTurnBasedMatchmakerViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate)

|  | Protocols |
| --- | --- |
| From | -- |
| To | NSObject |

GKVoiceChat.hRemoved GKVoiceChat(GKAdditions)Added [GKVoiceChat.playerVoiceChatStateDidChangeHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385713-playervoicechatstatedidchangehan)Added [GKVoiceChat.players](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385701-players)Added [-[GKVoiceChat setPlayer:muted:]](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385717-setplayer)Added GKVoiceChat(Deprecated)Modified [GKVoiceChat.playerIDs](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385721-playerids)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKVoiceChat.playerStateUpdateHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385705-playerstateupdatehandler)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKVoiceChat setMute:forPlayer:]](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385711-setmute)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

GKVoiceChatService.h (Added)Added [GKVoiceChatServiceErrorDomain](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerrordomain)

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
