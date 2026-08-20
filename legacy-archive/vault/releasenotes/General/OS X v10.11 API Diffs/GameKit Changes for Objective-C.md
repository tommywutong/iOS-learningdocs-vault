---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/GameKit.html
archived_at: '2026-07-18T02:53:06.985307Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# GameKit Changes for Objective-C

### GameKit

#### GKAchievement.h

Modified [GKAchievement.identifier](https://developer.apple.com/documentation/gamekit/gkachievement/1520631-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *identifier ``` |
| To | ``` @property(copy, atomic, nullable) NSString *identifier ``` |

Modified [-[GKAchievement initWithIdentifier:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520622-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithIdentifier:(NSString *)identifier ``` |
| To | ``` - (instancetype _Nonnull)initWithIdentifier:(NSString * _Nullable)identifier ``` |

Modified [-[GKAchievement initWithIdentifier:player:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521092-initwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithIdentifier:(NSString *)identifier player:(GKPlayer *)player ``` |
| To | ``` - (instancetype _Nonnull)initWithIdentifier:(NSString * _Nullable)identifier player:(GKPlayer * _Nonnull)player ``` |

Modified [GKAchievement.lastReportedDate](https://developer.apple.com/documentation/gamekit/gkachievement/1520993-lastreporteddate)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly, atomic) NSDate *lastReportedDate ``` |
| To | ``` @property(copy, readonly, atomic, nonnull) NSDate *lastReportedDate ``` |

Modified [+[GKAchievement loadAchievementsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520748-loadachievements)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadAchievementsWithCompletionHandler:(void (^)(NSArray *achievements, NSError *error))completionHandler ``` |
| To | ``` + (void)loadAchievementsWithCompletionHandler:(void (^ _Nullable)(NSArray<GKAchievement *> * _Nullable achievements, NSError * _Nullable error))completionHandler ``` |

Modified [GKAchievement.player](https://developer.apple.com/documentation/gamekit/gkachievement/1520943-player)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKPlayer *player ``` |
| To | ``` @property(readonly, retain, atomic, nonnull) GKPlayer *player ``` |

Modified [+[GKAchievement reportAchievements:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520509-reportachievements)

|  | Declaration |
| --- | --- |
| From | ``` + (void)reportAchievements:(NSArray *)achievements withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` + (void)reportAchievements:(NSArray<GKAchievement *> * _Nonnull)achievements withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKAchievement reportAchievementWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1521108-reportachievementwithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reportAchievementWithCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)reportAchievementWithCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [+[GKAchievement resetAchievementsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520717-resetachievementswithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` + (void)resetAchievementsWithCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` + (void)resetAchievementsWithCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

#### GKAchievementDescription.h

Modified [GKAchievementDescription.achievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416598-achieveddescription)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly, atomic) NSString *achievedDescription ``` |
| To | ``` @property(copy, readonly, atomic, nullable) NSString *achievedDescription ``` |

Modified [GKAchievementDescription.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416587-groupidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain, readonly) NSString *groupIdentifier ``` |
| To | ``` @property(nonatomic, retain, readonly, nullable) NSString *groupIdentifier ``` |

Modified [GKAchievementDescription.identifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416586-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly, atomic) NSString *identifier ``` |
| To | ``` @property(copy, readonly, atomic, nullable) NSString *identifier ``` |

Modified [GKAchievementDescription.image](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416591-image)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, retain, readonly) NSImage *image ``` |
| To | ``` @property(atomic, retain, readonly, nullable) NSImage *image ``` |

Modified [+[GKAchievementDescription incompleteAchievementImage]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416600-incompleteachievementimage)

|  | Declaration |
| --- | --- |
| From | ``` + (NSImage *)incompleteAchievementImage ``` |
| To | ``` + (NSImage * _Nonnull)incompleteAchievementImage ``` |

Modified [+[GKAchievementDescription loadAchievementDescriptionsWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416601-loadachievementdescriptionswithc)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadAchievementDescriptionsWithCompletionHandler:(void (^)(NSArray *descriptions, NSError *error))completionHandler ``` |
| To | ``` + (void)loadAchievementDescriptionsWithCompletionHandler:(void (^ _Nullable)(NSArray<GKAchievementDescription *> * _Nullable descriptions, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKAchievementDescription loadImageWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416596-loadimage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadImageWithCompletionHandler:(void (^)(NSImage *image, NSError *error))completionHandler ``` |
| To | ``` - (void)loadImageWithCompletionHandler:(void (^ _Nullable)(NSImage * _Nullable image, NSError * _Nullable error))completionHandler ``` |

Modified [+[GKAchievementDescription placeholderCompletedAchievementImage]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416580-placeholdercompletedachievementi)

|  | Declaration |
| --- | --- |
| From | ``` + (NSImage *)placeholderCompletedAchievementImage ``` |
| To | ``` + (NSImage * _Nonnull)placeholderCompletedAchievementImage ``` |

Modified [GKAchievementDescription.title](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416602-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly, atomic) NSString *title ``` |
| To | ``` @property(copy, readonly, atomic, nullable) NSString *title ``` |

Modified [GKAchievementDescription.unachievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416584-unachieveddescription)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, readonly, atomic) NSString *unachievedDescription ``` |
| To | ``` @property(copy, readonly, atomic, nullable) NSString *unachievedDescription ``` |

#### GKAchievementViewController.h

Modified [GKAchievementViewController](https://developer.apple.com/documentation/gamekit/gkachievementviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

#### GKChallenge.h

Modified [-[GKAchievement challengeComposeControllerWithMessage:players:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkachievement/1520805-challengecomposecontrollerwithme)

|  | Declaration |
| --- | --- |
| From | ``` - (NSViewController *)challengeComposeControllerWithMessage:(NSString *)message players:(NSArray *)players completionHandler:(GKChallengeComposeCompletionBlock)completionHandler ``` |
| To | ``` - (NSViewController * _Nonnull)challengeComposeControllerWithMessage:(NSString * _Nullable)message players:(NSArray<GKPlayer *> * _Nonnull)players completionHandler:(GKChallengeComposeCompletionBlock _Nullable)completionHandler ``` |

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

Modified [GKAchievementChallenge.achievement](https://developer.apple.com/documentation/gamekit/gkachievementchallenge/1520858-achievement)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) GKAchievement *achievement ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) GKAchievement *achievement ``` |

Modified [GKChallenge.completionDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520928-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSDate *completionDate ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) NSDate *completionDate ``` |

Modified [GKChallenge.issueDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520803-issuedate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSDate *issueDate ``` |
| To | ``` @property(nonatomic, readonly, retain, nonnull) NSDate *issueDate ``` |

Modified [GKChallenge.issuingPlayer](https://developer.apple.com/documentation/gamekit/gkchallenge/1521010-issuingplayer)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) GKPlayer *issuingPlayer ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) GKPlayer *issuingPlayer ``` |

Modified [GKChallenge.issuingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521100-issuingplayerid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *issuingPlayerID ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *issuingPlayerID ``` |

Modified [+[GKChallenge loadReceivedChallengesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkchallenge/1520864-loadreceivedchallenges)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadReceivedChallengesWithCompletionHandler:(void (^)(NSArray *challenges, NSError *error))completionHandler ``` |
| To | ``` + (void)loadReceivedChallengesWithCompletionHandler:(void (^ _Nullable)(NSArray<GKChallenge *> * _Nullable challenges, NSError * _Nullable error))completionHandler ``` |

Modified [GKChallenge.message](https://developer.apple.com/documentation/gamekit/gkchallenge/1520998-message)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *message ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *message ``` |

Modified [GKChallenge.receivingPlayer](https://developer.apple.com/documentation/gamekit/gkchallenge/1520570-receivingplayer)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) GKPlayer *receivingPlayer ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) GKPlayer *receivingPlayer ``` |

Modified [GKChallenge.receivingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521113-receivingplayerid)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, copy) NSString *receivingPlayerID ``` |
| To | ``` @property(nonatomic, readonly, copy, nullable) NSString *receivingPlayerID ``` |

Modified [-[GKScore challengeComposeControllerWithMessage:players:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1521227-challengecomposecontrollerwithme)

|  | Declaration |
| --- | --- |
| From | ``` - (NSViewController *)challengeComposeControllerWithMessage:(NSString *)message players:(NSArray *)players completionHandler:(GKChallengeComposeCompletionBlock)completionHandler ``` |
| To | ``` - (NSViewController * _Nonnull)challengeComposeControllerWithMessage:(NSString * _Nullable)message players:(NSArray<GKPlayer *> * _Nullable)players completionHandler:(GKChallengeComposeCompletionBlock _Nullable)completionHandler ``` |

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

Modified [GKScoreChallenge.score](https://developer.apple.com/documentation/gamekit/gkscorechallenge/1521014-score)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) GKScore *score ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) GKScore *score ``` |

#### GKDialogController.h

Modified [-[GKDialogController dismiss:]](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/1520938-dismiss)

|  | Declaration |
| --- | --- |
| From | ``` - (IBAction)dismiss:(id)sender ``` |
| To | ``` - (IBAction)dismiss:(id _Nonnull)sender ``` |

Modified [GKDialogController.parentWindow](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/1520890-parentwindow)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign) IBOutlet NSWindow *parentWindow ``` |
| To | ``` @property(assign, nullable) IBOutlet NSWindow *parentWindow ``` |

Modified [-[GKDialogController presentViewController:]](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/1520909-present)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)presentViewController:(NSViewController<GKViewController> *)viewController ``` |
| To | ``` - (BOOL)presentViewController:(NSViewController<GKViewController> * _Nonnull)viewController ``` |

Modified [+[GKDialogController sharedDialogController]](https://developer.apple.com/documentation/gamekit/gkdialogcontroller/1521112-shared)

|  | Declaration |
| --- | --- |
| From | ``` + (GKDialogController *)sharedDialogController ``` |
| To | ``` + (GKDialogController * _Nonnull)sharedDialogController ``` |

#### GKEventListener.h

Modified [-[GKChallengeListener player:didCompleteChallenge:issuedByFriend:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494688-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didCompleteChallenge:(GKChallenge *)challenge issuedByFriend:(GKPlayer *)friendPlayer ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didCompleteChallenge:(GKChallenge * _Nonnull)challenge issuedByFriend:(GKPlayer * _Nonnull)friendPlayer ``` |

Modified [-[GKChallengeListener player:didReceiveChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494691-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didReceiveChallenge:(GKChallenge *)challenge ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didReceiveChallenge:(GKChallenge * _Nonnull)challenge ``` |

Modified [-[GKChallengeListener player:issuedChallengeWasCompleted:byFriend:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494686-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player issuedChallengeWasCompleted:(GKChallenge *)challenge byFriend:(GKPlayer *)friendPlayer ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player issuedChallengeWasCompleted:(GKChallenge * _Nonnull)challenge byFriend:(GKPlayer * _Nonnull)friendPlayer ``` |

Modified [-[GKChallengeListener player:wantsToPlayChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494684-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player wantsToPlayChallenge:(GKChallenge *)challenge ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player wantsToPlayChallenge:(GKChallenge * _Nonnull)challenge ``` |

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

Modified [GKFriendRequestComposeViewController.composeViewDelegate](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437192-composeviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<GKFriendRequestComposeViewControllerDelegate> composeViewDelegate ``` |
| To | ``` @property(nonatomic, assign, nullable) id<GKFriendRequestComposeViewControllerDelegate> composeViewDelegate ``` |

Modified [-[GKFriendRequestComposeViewController setMessage:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437201-setmessage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setMessage:(NSString *)message ``` |
| To | ``` - (void)setMessage:(NSString * _Nullable)message ``` |

Modified [-[GKFriendRequestComposeViewControllerDelegate friendRequestComposeViewControllerDidFinish:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate/1437186-friendrequestcomposeviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` - (void)friendRequestComposeViewControllerDidFinish:(GKFriendRequestComposeViewController *)viewController ``` |
| To | ``` - (void)friendRequestComposeViewControllerDidFinish:(GKFriendRequestComposeViewController * _Nonnull)viewController ``` |

#### GKGameCenterViewController.h

Modified [-[GKGameCenterControllerDelegate gameCenterViewControllerDidFinish:]](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate/1520771-gamecenterviewcontrollerdidfinis)

|  | Declaration |
| --- | --- |
| From | ``` - (void)gameCenterViewControllerDidFinish:(GKGameCenterViewController *)gameCenterViewController ``` |
| To | ``` - (void)gameCenterViewControllerDidFinish:(GKGameCenterViewController * _Nonnull)gameCenterViewController ``` |

Modified [GKGameCenterViewController.gameCenterDelegate](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520845-gamecenterdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) id<GKGameCenterControllerDelegate> gameCenterDelegate ``` |
| To | ``` @property(assign, atomic, nullable) id<GKGameCenterControllerDelegate> gameCenterDelegate ``` |

Modified [GKGameCenterViewController.leaderboardCategory](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520837-leaderboardcategory)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *leaderboardCategory ``` |
| To | ``` @property(nonatomic, retain, nullable) NSString *leaderboardCategory ``` |

Modified [GKGameCenterViewController.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520540-leaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, retain) NSString *leaderboardIdentifier ``` |
| To | ``` @property(nonatomic, retain, nullable) NSString *leaderboardIdentifier ``` |

Modified [GKGameCenterViewController.leaderboardTimeScope](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520464-leaderboardtimescope)

|  | Deprecation |
| --- | --- |
| From | OS X 10.10 |
| To | -- |

#### GKLeaderboard.h

Modified [GKLeaderboard.category](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503154-category)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *category ``` |
| To | ``` @property(copy, atomic, nullable) NSString *category ``` |

Modified [GKLeaderboard.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503135-groupidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *groupIdentifier ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) NSString *groupIdentifier ``` |

Modified [GKLeaderboard.identifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503141-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *identifier ``` |
| To | ``` @property(copy, atomic, nullable) NSString *identifier ``` |

Modified [-[GKLeaderboard init]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503125-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)init ``` |
| To | ``` - (instancetype _Nonnull)init ``` |

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

Modified [-[GKLeaderboard loadImageWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503161-loadimagewithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadImageWithCompletionHandler:(void (^)(NSImage *image, NSError *error))completionHandler ``` |
| To | ``` - (void)loadImageWithCompletionHandler:(void (^ _Nullable)(NSImage * _Nullable image, NSError * _Nullable error))completionHandler ``` |

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

Modified [GKLeaderboard.localPlayerScore](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503151-localplayerscore)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKScore *localPlayerScore ``` |
| To | ``` @property(readonly, retain, atomic, nullable) GKScore *localPlayerScore ``` |

Modified [GKLeaderboard.scores](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503159-scores)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSArray *scores ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSArray<GKScore *> *scores ``` |

Modified [+[GKLeaderboard setDefaultLeaderboard:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503123-setdefaultleaderboard)

|  | Declaration |
| --- | --- |
| From | ``` + (void)setDefaultLeaderboard:(NSString *)leaderboardIdentifier withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` + (void)setDefaultLeaderboard:(NSString * _Nullable)leaderboardIdentifier withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKLeaderboard.title](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503139-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *title ``` |
| To | ``` @property(readonly, copy, atomic, nullable) NSString *title ``` |

#### GKLeaderboardSet.h

Modified [GKLeaderboardSet.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451800-groupidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSString *groupIdentifier ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) NSString *groupIdentifier ``` |

Modified [GKLeaderboardSet.identifier](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451802-identifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *identifier ``` |
| To | ``` @property(copy, atomic, nullable) NSString *identifier ``` |

Modified [-[GKLeaderboardSet loadImageWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451812-loadimage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadImageWithCompletionHandler:(void (^)(NSImage *image, NSError *error))completionHandler ``` |
| To | ``` - (void)loadImageWithCompletionHandler:(void (^ _Nullable)(NSImage * _Nullable image, NSError * _Nullable error))completionHandler ``` |

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

Modified [GKLeaderboardSet.title](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451804-title)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *title ``` |
| To | ``` @property(readonly, copy, atomic, nonnull) NSString *title ``` |

#### GKLeaderboardViewController.h

Modified [GKLeaderboardViewController](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

#### GKLocalPlayer.h

Modified [GKLocalPlayer.authenticateHandler](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515399-authenticatehandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, copy) void (^authenticateHandler)(NSViewController *viewController, NSError *error) ``` |
| To | ``` @property(atomic, copy, nullable) void (^authenticateHandler)(NSViewController * _Nullable viewController, NSError * _Nullable error) ``` |

Modified [-[GKLocalPlayer authenticateWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515406-authenticatewithcompletionhandle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)authenticateWithCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)authenticateWithCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKLocalPlayer.friends](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515405-friends)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) NSArray *friends ``` |
| To | ``` @property(nonatomic, readonly, retain, nullable) NSArray<NSString *> *friends ``` |

Modified [-[GKLocalPlayer generateIdentityVerificationSignatureWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515407-generateidentityverificationsign)

|  | Declaration |
| --- | --- |
| From | ``` - (void)generateIdentityVerificationSignatureWithCompletionHandler:(void (^)(NSURL *publicKeyUrl, NSData *signature, NSData *salt, uint64_t timestamp, NSError *error))completionHandler ``` |
| To | ``` - (void)generateIdentityVerificationSignatureWithCompletionHandler:(void (^ _Nullable)(NSURL * _Nullable publicKeyUrl, NSData * _Nullable signature, NSData * _Nullable salt, uint64_t timestamp, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKLocalPlayer loadDefaultLeaderboardCategoryIDWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515398-loaddefaultleaderboardcategoryid)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadDefaultLeaderboardCategoryIDWithCompletionHandler:(void (^)(NSString *categoryID, NSError *error))completionHandler ``` |
| To | ``` - (void)loadDefaultLeaderboardCategoryIDWithCompletionHandler:(void (^ _Nullable)(NSString * _Nullable categoryID, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKLocalPlayer loadDefaultLeaderboardIdentifierWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515404-loaddefaultleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadDefaultLeaderboardIdentifierWithCompletionHandler:(void (^)(NSString *leaderboardIdentifier, NSError *error))completionHandler ``` |
| To | ``` - (void)loadDefaultLeaderboardIdentifierWithCompletionHandler:(void (^ _Nullable)(NSString * _Nullable leaderboardIdentifier, NSError * _Nullable error))completionHandler ``` |

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

Modified [+[GKLocalPlayer localPlayer]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515401-localplayer)

|  | Declaration |
| --- | --- |
| From | ``` + (GKLocalPlayer *)localPlayer ``` |
| To | ``` + (GKLocalPlayer * _Nonnull)localPlayer ``` |

Modified [-[GKLocalPlayer registerListener:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515393-registerlistener)

|  | Declaration |
| --- | --- |
| From | ``` - (void)registerListener:(id<GKLocalPlayerListener>)listener ``` |
| To | ``` - (void)registerListener:(id<GKLocalPlayerListener> _Nonnull)listener ``` |

Modified [-[GKLocalPlayer setDefaultLeaderboardCategoryID:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515385-setdefaultleaderboardcategoryid)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDefaultLeaderboardCategoryID:(NSString *)categoryID completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)setDefaultLeaderboardCategoryID:(NSString * _Nullable)categoryID completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKLocalPlayer setDefaultLeaderboardIdentifier:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515408-setdefaultleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setDefaultLeaderboardIdentifier:(NSString *)leaderboardIdentifier completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)setDefaultLeaderboardIdentifier:(NSString * _Nonnull)leaderboardIdentifier completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKLocalPlayer unregisterListener:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515389-unregisterlistener)

|  | Declaration |
| --- | --- |
| From | ``` - (void)unregisterListener:(id<GKLocalPlayerListener>)listener ``` |
| To | ``` - (void)unregisterListener:(id<GKLocalPlayerListener> _Nonnull)listener ``` |

#### GKMatch.h

Added [-[GKMatchDelegate match:didReceiveData:forRecipient:fromRemotePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502034-match)Modified [-[GKMatch chooseBestHostingPlayerWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502072-choosebesthostingplayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)chooseBestHostingPlayerWithCompletionHandler:(void (^)(GKPlayer *player))completionHandler ``` |
| To | ``` - (void)chooseBestHostingPlayerWithCompletionHandler:(void (^ _Nonnull)(GKPlayer * _Nullable player))completionHandler ``` |

Modified [-[GKMatch chooseBestHostPlayerWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502044-choosebesthostplayerwithcompleti)

|  | Declaration |
| --- | --- |
| From | ``` - (void)chooseBestHostPlayerWithCompletionHandler:(void (^)(NSString *playerID))completionHandler ``` |
| To | ``` - (void)chooseBestHostPlayerWithCompletionHandler:(void (^ _Nonnull)(NSString * _Nullable playerID))completionHandler ``` |

Modified [GKMatch.delegate](https://developer.apple.com/documentation/gamekit/gkmatch/1502046-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<GKMatchDelegate> delegate ``` |
| To | ``` @property(nonatomic, assign, nullable) id<GKMatchDelegate> delegate ``` |

Modified [GKMatch.playerIDs](https://developer.apple.com/documentation/gamekit/gkmatch/1502064-playerids)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *playerIDs ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<NSString *> *playerIDs ``` |

Modified [GKMatch.players](https://developer.apple.com/documentation/gamekit/gkmatch/1502074-players)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly) NSArray *players ``` |
| To | ``` @property(nonatomic, readonly, nonnull) NSArray<GKPlayer *> *players ``` |

Modified [-[GKMatch rematchWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502042-rematch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rematchWithCompletionHandler:(void (^)(GKMatch *match, NSError *error))completionHandler ``` |
| To | ``` - (void)rematchWithCompletionHandler:(void (^ _Nullable)(GKMatch * _Nullable match, NSError * _Nullable error))completionHandler ``` |

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

Modified [-[GKMatch sendDataToAllPlayers:withDataMode:error:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502029-senddatatoallplayers)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendDataToAllPlayers:(NSData *)data withDataMode:(GKMatchSendDataMode)mode error:(NSError **)error ``` |
| To | ``` - (BOOL)sendDataToAllPlayers:(NSData * _Nonnull)data withDataMode:(GKMatchSendDataMode)mode error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[GKMatch voiceChatWithName:]](https://developer.apple.com/documentation/gamekit/gkmatch/1502066-voicechat)

|  | Declaration |
| --- | --- |
| From | ``` - (GKVoiceChat *)voiceChatWithName:(NSString *)name ``` |
| To | ``` - (GKVoiceChat * _Nullable)voiceChatWithName:(NSString * _Nonnull)name ``` |

Modified [-[GKMatchDelegate match:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502025-match)

|  | Declaration |
| --- | --- |
| From | ``` - (void)match:(GKMatch *)match didFailWithError:(NSError *)error ``` |
| To | ``` - (void)match:(GKMatch * _Nonnull)match didFailWithError:(NSError * _Nullable)error ``` |

Modified [-[GKMatchDelegate match:didReceiveData:fromPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502054-match)

|  | Declaration |
| --- | --- |
| From | ``` - (void)match:(GKMatch *)match didReceiveData:(NSData *)data fromPlayer:(NSString *)playerID ``` |
| To | ``` - (void)match:(GKMatch * _Nonnull)match didReceiveData:(NSData * _Nonnull)data fromPlayer:(NSString * _Nonnull)playerID ``` |

Modified [-[GKMatchDelegate match:didReceiveData:fromRemotePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502069-match)

|  | Declaration |
| --- | --- |
| From | ``` - (void)match:(GKMatch *)match didReceiveData:(NSData *)data fromRemotePlayer:(GKPlayer *)player ``` |
| To | ``` - (void)match:(GKMatch * _Nonnull)match didReceiveData:(NSData * _Nonnull)data fromRemotePlayer:(GKPlayer * _Nonnull)player ``` |

Modified [-[GKMatchDelegate match:player:didChangeConnectionState:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502048-match)

|  | Declaration |
| --- | --- |
| From | ``` - (void)match:(GKMatch *)match player:(GKPlayer *)player didChangeConnectionState:(GKPlayerConnectionState)state ``` |
| To | ``` - (void)match:(GKMatch * _Nonnull)match player:(GKPlayer * _Nonnull)player didChangeConnectionState:(GKPlayerConnectionState)state ``` |

Modified [-[GKMatchDelegate match:player:didChangeState:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502028-match)

|  | Declaration |
| --- | --- |
| From | ``` - (void)match:(GKMatch *)match player:(NSString *)playerID didChangeState:(GKPlayerConnectionState)state ``` |
| To | ``` - (void)match:(GKMatch * _Nonnull)match player:(NSString * _Nonnull)playerID didChangeState:(GKPlayerConnectionState)state ``` |

Modified [-[GKMatchDelegate match:shouldReinviteDisconnectedPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502038-match)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)match:(GKMatch *)match shouldReinviteDisconnectedPlayer:(GKPlayer *)player ``` |
| To | ``` - (BOOL)match:(GKMatch * _Nonnull)match shouldReinviteDisconnectedPlayer:(GKPlayer * _Nonnull)player ``` |

Modified [-[GKMatchDelegate match:shouldReinvitePlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502058-match)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)match:(GKMatch *)match shouldReinvitePlayer:(NSString *)playerID ``` |
| To | ``` - (BOOL)match:(GKMatch * _Nonnull)match shouldReinvitePlayer:(NSString * _Nonnull)playerID ``` |

#### GKMatchmaker.h

Modified [GKInvite.inviter](https://developer.apple.com/documentation/gamekit/gkinvite/1520959-inviter)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSString *inviter ``` |
| To | ``` @property(readonly, retain, atomic, nonnull) NSString *inviter ``` |

Modified [GKInvite.sender](https://developer.apple.com/documentation/gamekit/gkinvite/1521073-sender)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKPlayer *sender ``` |
| To | ``` @property(readonly, retain, atomic, nonnull) GKPlayer *sender ``` |

Modified [-[GKInviteEventListener player:didAcceptInvite:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520672-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didAcceptInvite:(GKInvite *)invite ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didAcceptInvite:(GKInvite * _Nonnull)invite ``` |

Modified [-[GKInviteEventListener player:didRequestMatchWithRecipients:]](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520894-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didRequestMatchWithRecipients:(NSArray *)recipientPlayers ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didRequestMatchWithRecipients:(NSArray<GKPlayer *> * _Nonnull)recipientPlayers ``` |

Modified [-[GKMatchmaker addPlayersToMatch:matchRequest:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520561-addplayerstomatch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addPlayersToMatch:(GKMatch *)match matchRequest:(GKMatchRequest *)matchRequest completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)addPlayersToMatch:(GKMatch * _Nonnull)match matchRequest:(GKMatchRequest * _Nonnull)matchRequest completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKMatchmaker cancelInviteToPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520576-cancelinvite)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelInviteToPlayer:(NSString *)playerID ``` |
| To | ``` - (void)cancelInviteToPlayer:(NSString * _Nonnull)playerID ``` |

Modified [-[GKMatchmaker cancelPendingInviteToPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520773-cancelpendinginvite)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelPendingInviteToPlayer:(GKPlayer *)player ``` |
| To | ``` - (void)cancelPendingInviteToPlayer:(GKPlayer * _Nonnull)player ``` |

Modified [-[GKMatchmaker findMatchForRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520777-findmatch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)findMatchForRequest:(GKMatchRequest *)request withCompletionHandler:(void (^)(GKMatch *match, NSError *error))completionHandler ``` |
| To | ``` - (void)findMatchForRequest:(GKMatchRequest * _Nonnull)request withCompletionHandler:(void (^ _Nullable)(GKMatch * _Nullable match, NSError * _Nullable error))completionHandler ``` |

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

Modified [-[GKMatchmaker finishMatchmakingForMatch:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520518-finishmatchmaking)

|  | Declaration |
| --- | --- |
| From | ``` - (void)finishMatchmakingForMatch:(GKMatch *)match ``` |
| To | ``` - (void)finishMatchmakingForMatch:(GKMatch * _Nonnull)match ``` |

Modified [GKMatchmaker.inviteHandler](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521060-invitehandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) void (^inviteHandler)(GKInvite *acceptedInvite, NSArray *playerIDsToInvite) ``` |
| To | ``` @property(nonatomic, copy, nullable) void (^inviteHandler)(GKInvite * _Nonnull acceptedInvite, NSArray * _Nullable playerIDsToInvite) ``` |

Modified [-[GKMatchmaker matchForInvite:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520847-match)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchForInvite:(GKInvite *)invite completionHandler:(void (^)(GKMatch *match, NSError *error))completionHandler ``` |
| To | ``` - (void)matchForInvite:(GKInvite * _Nonnull)invite completionHandler:(void (^ _Nullable)(GKMatch * _Nullable match, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKMatchmaker queryActivityWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520930-queryactivity)

|  | Declaration |
| --- | --- |
| From | ``` - (void)queryActivityWithCompletionHandler:(void (^)(NSInteger activity, NSError *error))completionHandler ``` |
| To | ``` - (void)queryActivityWithCompletionHandler:(void (^ _Nullable)(NSInteger activity, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKMatchmaker queryPlayerGroupActivity:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521189-queryplayergroupactivity)

|  | Declaration |
| --- | --- |
| From | ``` - (void)queryPlayerGroupActivity:(NSUInteger)playerGroup withCompletionHandler:(void (^)(NSInteger activity, NSError *error))completionHandler ``` |
| To | ``` - (void)queryPlayerGroupActivity:(NSUInteger)playerGroup withCompletionHandler:(void (^ _Nullable)(NSInteger activity, NSError * _Nullable error))completionHandler ``` |

Modified [+[GKMatchmaker sharedMatchmaker]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520781-sharedmatchmaker)

|  | Declaration |
| --- | --- |
| From | ``` + (GKMatchmaker *)sharedMatchmaker ``` |
| To | ``` + (GKMatchmaker * _Nonnull)sharedMatchmaker ``` |

Modified [-[GKMatchmaker startBrowsingForNearbyPlayersWithHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521043-startbrowsingfornearbyplayerswit)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startBrowsingForNearbyPlayersWithHandler:(void (^)(GKPlayer *player, BOOL reachable))reachableHandler ``` |
| To | ``` - (void)startBrowsingForNearbyPlayersWithHandler:(void (^ _Nullable)(GKPlayer * _Nonnull player, BOOL reachable))reachableHandler ``` |

Modified [-[GKMatchmaker startBrowsingForNearbyPlayersWithReachableHandler:]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521023-startbrowsingfornearbyplayerswit)

|  | Declaration |
| --- | --- |
| From | ``` - (void)startBrowsingForNearbyPlayersWithReachableHandler:(void (^)(NSString *playerID, BOOL reachable))reachableHandler ``` |
| To | ``` - (void)startBrowsingForNearbyPlayersWithReachableHandler:(void (^ _Nullable)(NSString * _Nonnull playerID, BOOL reachable))reachableHandler ``` |

Modified [GKMatchRequest.inviteeResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520511-inviteeresponsehandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) void (^inviteeResponseHandler)(NSString *playerID, GKInviteeResponse response) ``` |
| To | ``` @property(copy, nullable) void (^inviteeResponseHandler)(NSString * _Nonnull playerID, GKInviteeResponse response) ``` |

Modified [GKMatchRequest.inviteMessage](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521164-invitemessage)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) NSString *inviteMessage ``` |
| To | ``` @property(copy, nullable) NSString *inviteMessage ``` |

Modified [GKMatchRequest.playersToInvite](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520921-playerstoinvite)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSArray *playersToInvite ``` |
| To | ``` @property(retain, nullable) NSArray<NSString *> *playersToInvite ``` |

Modified [GKMatchRequest.recipientResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521004-recipientresponsehandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy) void (^recipientResponseHandler)(GKPlayer *player, GKInviteRecipientResponse response) ``` |
| To | ``` @property(copy, nullable) void (^recipientResponseHandler)(GKPlayer * _Nonnull player, GKInviteRecipientResponse response) ``` |

Modified [GKMatchRequest.recipients](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520800-recipients)

|  | Declaration |
| --- | --- |
| From | ``` @property(retain) NSArray *recipients ``` |
| To | ``` @property(retain, nullable) NSArray<GKPlayer *> *recipients ``` |

#### GKMatchmakerViewController.h

Modified [-[GKMatchmakerViewController addPlayersToMatch:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492425-addplayers)

|  | Declaration |
| --- | --- |
| From | ``` - (void)addPlayersToMatch:(GKMatch *)match ``` |
| To | ``` - (void)addPlayersToMatch:(GKMatch * _Nonnull)match ``` |

Modified [GKMatchmakerViewController.defaultInvitationMessage](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492409-defaultinvitationmessage)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, copy) NSString *defaultInvitationMessage ``` |
| To | ``` @property(nonatomic, copy, nullable) NSString *defaultInvitationMessage ``` |

Modified [-[GKMatchmakerViewController initWithInvite:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492434-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithInvite:(GKInvite *)invite ``` |
| To | ``` - (id _Nullable)initWithInvite:(GKInvite * _Nonnull)invite ``` |

Modified [-[GKMatchmakerViewController initWithMatchRequest:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492423-initwithmatchrequest)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMatchRequest:(GKMatchRequest *)request ``` |
| To | ``` - (id _Nullable)initWithMatchRequest:(GKMatchRequest * _Nonnull)request ``` |

Modified [GKMatchmakerViewController.matchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492426-matchmakerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, assign) id<GKMatchmakerViewControllerDelegate> matchmakerDelegate ``` |
| To | ``` @property(nonatomic, assign, nullable) id<GKMatchmakerViewControllerDelegate> matchmakerDelegate ``` |

Modified [GKMatchmakerViewController.matchRequest](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492410-matchrequest)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readonly, retain) GKMatchRequest *matchRequest ``` |
| To | ``` @property(nonatomic, readonly, retain, nonnull) GKMatchRequest *matchRequest ``` |

Modified [-[GKMatchmakerViewController setHostedPlayer:connected:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492418-sethostedplayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setHostedPlayer:(NSString *)playerID connected:(BOOL)connected ``` |
| To | ``` - (void)setHostedPlayer:(NSString * _Nonnull)playerID connected:(BOOL)connected ``` |

Modified [-[GKMatchmakerViewController setHostedPlayer:didConnect:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492406-sethostedplayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setHostedPlayer:(GKPlayer *)player didConnect:(BOOL)connected ``` |
| To | ``` - (void)setHostedPlayer:(GKPlayer * _Nonnull)player didConnect:(BOOL)connected ``` |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492419-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewController:(GKMatchmakerViewController *)viewController didFailWithError:(NSError *)error ``` |
| To | ``` - (void)matchmakerViewController:(GKMatchmakerViewController * _Nonnull)viewController didFailWithError:(NSError * _Nonnull)error ``` |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindHostedPlayers:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492421-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewController:(GKMatchmakerViewController *)viewController didFindHostedPlayers:(NSArray *)players ``` |
| To | ``` - (void)matchmakerViewController:(GKMatchmakerViewController * _Nonnull)viewController didFindHostedPlayers:(NSArray<GKPlayer *> * _Nonnull)players ``` |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindMatch:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492416-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewController:(GKMatchmakerViewController *)viewController didFindMatch:(GKMatch *)match ``` |
| To | ``` - (void)matchmakerViewController:(GKMatchmakerViewController * _Nonnull)viewController didFindMatch:(GKMatch * _Nonnull)match ``` |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didFindPlayers:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492428-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewController:(GKMatchmakerViewController *)viewController didFindPlayers:(NSArray *)playerIDs ``` |
| To | ``` - (void)matchmakerViewController:(GKMatchmakerViewController * _Nonnull)viewController didFindPlayers:(NSArray<NSString *> * _Nonnull)playerIDs ``` |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:didReceiveAcceptFromHostedPlayer:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492436-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewController:(GKMatchmakerViewController *)viewController didReceiveAcceptFromHostedPlayer:(NSString *)playerID ``` |
| To | ``` - (void)matchmakerViewController:(GKMatchmakerViewController * _Nonnull)viewController didReceiveAcceptFromHostedPlayer:(NSString * _Nonnull)playerID ``` |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewController:hostedPlayerDidAccept:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492412-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewController:(GKMatchmakerViewController *)viewController hostedPlayerDidAccept:(GKPlayer *)player ``` |
| To | ``` - (void)matchmakerViewController:(GKMatchmakerViewController * _Nonnull)viewController hostedPlayerDidAccept:(GKPlayer * _Nonnull)player ``` |

Modified [-[GKMatchmakerViewControllerDelegate matchmakerViewControllerWasCancelled:]](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492432-matchmakerviewcontrollerwascance)

|  | Declaration |
| --- | --- |
| From | ``` - (void)matchmakerViewControllerWasCancelled:(GKMatchmakerViewController *)viewController ``` |
| To | ``` - (void)matchmakerViewControllerWasCancelled:(GKMatchmakerViewController * _Nonnull)viewController ``` |

#### GKNotificationBanner.h

Modified [+[GKNotificationBanner showBannerWithTitle:message:completionHandler:]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515370-showbannerwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` + (void)showBannerWithTitle:(NSString *)title message:(NSString *)message completionHandler:(void (^)(void))completionHandler ``` |
| To | ``` + (void)showBannerWithTitle:(NSString * _Nullable)title message:(NSString * _Nullable)message completionHandler:(void (^ _Nullable)(void))completionHandler ``` |

Modified [+[GKNotificationBanner showBannerWithTitle:message:duration:completionHandler:]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515368-showbannerwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` + (void)showBannerWithTitle:(NSString *)title message:(NSString *)message duration:(NSTimeInterval)duration completionHandler:(void (^)(void))completionHandler ``` |
| To | ``` + (void)showBannerWithTitle:(NSString * _Nullable)title message:(NSString * _Nullable)message duration:(NSTimeInterval)duration completionHandler:(void (^ _Nullable)(void))completionHandler ``` |

#### GKPlayer.h

Added [+[GKPlayer anonymousGuestPlayerWithIdentifier:]](https://developer.apple.com/documentation/gamekit/gkplayer/1520559-anonymousguestplayerwithidentifi)Added [GKPlayer.guestIdentifier](https://developer.apple.com/documentation/gamekit/gkplayer/1520901-guestidentifier)Modified [GKPlayer.alias](https://developer.apple.com/documentation/gamekit/gkplayer/1520970-alias)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *alias ``` |
| To | ``` @property(readonly, copy, atomic, nullable) NSString *alias ``` |

Modified [GKPlayer.displayName](https://developer.apple.com/documentation/gamekit/gkplayer/1520695-displayname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *displayName ``` |
| To | ``` @property(readonly, atomic, nullable) NSString *displayName ``` |

Modified [-[GKPlayer loadPhotoForSize:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkplayer/1521176-loadphoto)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadPhotoForSize:(GKPhotoSize)size withCompletionHandler:(void (^)(NSImage *photo, NSError *error))completionHandler ``` |
| To | ``` - (void)loadPhotoForSize:(GKPhotoSize)size withCompletionHandler:(void (^ _Nullable)(NSImage * _Nullable photo, NSError * _Nullable error))completionHandler ``` |

Modified [+[GKPlayer loadPlayersForIdentifiers:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkplayer/1520723-loadplayersforidentifiers)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadPlayersForIdentifiers:(NSArray *)identifiers withCompletionHandler:(void (^)(NSArray *players, NSError *error))completionHandler ``` |
| To | ``` + (void)loadPlayersForIdentifiers:(NSArray<NSString *> * _Nonnull)identifiers withCompletionHandler:(void (^ _Nullable)(NSArray<GKPlayer *> * _Nullable players, NSError * _Nullable error))completionHandler ``` |

Modified [GKPlayer.playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSString *playerID ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSString *playerID ``` |

#### GKPublicConstants.h

Removed [GKVoiceChatServiceAudioUnavailableError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/audiounavailableerror)Removed [GKVoiceChatServiceClientMissingRequiredMethodsError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceclientmissingrequiredmethodserror)Removed [GKVoiceChatServiceInternalError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinternalerror)Removed [GKVoiceChatServiceInvalidCallIDError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinvalidcalliderror)Removed [GKVoiceChatServiceInvalidParameterError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceinvalidparametererror)Removed [GKVoiceChatServiceMethodCurrentlyInvalidError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatservicemethodcurrentlyinvaliderror)Removed [GKVoiceChatServiceNetworkConfigurationError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/networkconfigurationerror)Removed [GKVoiceChatServiceNoRemotePacketsError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/noremotepacketserror)Removed [GKVoiceChatServiceOutOfMemoryError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/outofmemoryerror)Removed [GKVoiceChatServiceRemoteParticipantBusyError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantbusyerror)Removed [GKVoiceChatServiceRemoteParticipantCancelledError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantcancellederror)Removed [GKVoiceChatServiceRemoteParticipantDeclinedInviteError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipantdeclinedinviteerror)Removed [GKVoiceChatServiceRemoteParticipantHangupError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code/remoteparticipanthanguperror)Removed [GKVoiceChatServiceRemoteParticipantResponseInvalidError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceremoteparticipantresponseinvaliderror)Removed [GKVoiceChatServiceUnableToConnectError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceunabletoconnecterror)Removed [GKVoiceChatServiceUninitializedClientError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceuninitializedclienterror)Removed [GKVoiceChatServiceUnsupportedRemoteVersionError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/gkvoicechatserviceunsupportedremoteversionerror)Added [GKVoiceChatServiceError](https://developer.apple.com/documentation/gamekit/gkvoicechatserviceerror/code)Modified [GKPeerConnectionState](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.8 | OS X 10.10 |
| To | OS X 10.10 | -- |

Modified [GKPeerStateAvailable](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/stateavailable)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKPeerStateConnected](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/gkpeerstateconnected)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKPeerStateConnecting](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/stateconnecting)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKPeerStateDisconnected](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/statedisconnected)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKPeerStateUnavailable](https://developer.apple.com/documentation/gamekit/gkpeerconnectionstate/gkpeerstateunavailable)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKSendDataMode](https://developer.apple.com/documentation/gamekit/gksenddatamode)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.8 | OS X 10.10 |
| To | OS X 10.10 | -- |

Modified [GKSendDataReliable](https://developer.apple.com/documentation/gamekit/gksenddatamode/reliable)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKSendDataUnreliable](https://developer.apple.com/documentation/gamekit/gksenddatamode/unreliable)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKSessionMode](https://developer.apple.com/documentation/gamekit/gksessionmode)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.8 | OS X 10.10 |
| To | OS X 10.10 | -- |

Modified [GKSessionModeClient](https://developer.apple.com/documentation/gamekit/gksessionmode/gksessionmodeclient)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKSessionModePeer](https://developer.apple.com/documentation/gamekit/gksessionmode/gksessionmodepeer)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

Modified [GKSessionModeServer](https://developer.apple.com/documentation/gamekit/gksessionmode/server)

|  | Introduction | Deprecation |
| --- | --- | --- |
| From | OS X 10.10 | -- |
| To | OS X 10.8 | OS X 10.10 |

#### GKPublicProtocols.h

Modified [-[GKSessionDelegate session:connectionWithPeerFailed:withError:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1521160-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(GKSession *)session connectionWithPeerFailed:(NSString *)peerID withError:(NSError *)error ``` |
| To | ``` - (void)session:(GKSession * _Nonnull)session connectionWithPeerFailed:(NSString * _Nonnull)peerID withError:(NSError * _Nonnull)error ``` |

Modified [-[GKSessionDelegate session:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520662-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(GKSession *)session didFailWithError:(NSError *)error ``` |
| To | ``` - (void)session:(GKSession * _Nonnull)session didFailWithError:(NSError * _Nonnull)error ``` |

Modified [-[GKSessionDelegate session:didReceiveConnectionRequestFromPeer:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520711-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(GKSession *)session didReceiveConnectionRequestFromPeer:(NSString *)peerID ``` |
| To | ``` - (void)session:(GKSession * _Nonnull)session didReceiveConnectionRequestFromPeer:(NSString * _Nonnull)peerID ``` |

Modified [-[GKSessionDelegate session:peer:didChangeState:]](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520885-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(GKSession *)session peer:(NSString *)peerID didChangeState:(GKPeerConnectionState)state ``` |
| To | ``` - (void)session:(GKSession * _Nonnull)session peer:(NSString * _Nonnull)peerID didChangeState:(GKPeerConnectionState)state ``` |

Modified [-[GKVoiceChatClient participantID]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520641-participantid)

|  | Declaration |
| --- | --- |
| From | ``` - (NSString *)participantID ``` |
| To | ``` - (NSString * _Nonnull)participantID ``` |

Modified [-[GKVoiceChatClient voiceChatService:didNotStartWithParticipantID:error:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521047-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)voiceChatService:(GKVoiceChatService *)voiceChatService didNotStartWithParticipantID:(NSString *)participantID error:(NSError *)error ``` |
| To | ``` - (void)voiceChatService:(GKVoiceChatService * _Nonnull)voiceChatService didNotStartWithParticipantID:(NSString * _Nonnull)participantID error:(NSError * _Nullable)error ``` |

Modified [-[GKVoiceChatClient voiceChatService:didReceiveInvitationFromParticipantID:callID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520997-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)voiceChatService:(GKVoiceChatService *)voiceChatService didReceiveInvitationFromParticipantID:(NSString *)participantID callID:(NSInteger)callID ``` |
| To | ``` - (void)voiceChatService:(GKVoiceChatService * _Nonnull)voiceChatService didReceiveInvitationFromParticipantID:(NSString * _Nonnull)participantID callID:(NSInteger)callID ``` |

Modified [-[GKVoiceChatClient voiceChatService:didStartWithParticipantID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520971-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)voiceChatService:(GKVoiceChatService *)voiceChatService didStartWithParticipantID:(NSString *)participantID ``` |
| To | ``` - (void)voiceChatService:(GKVoiceChatService * _Nonnull)voiceChatService didStartWithParticipantID:(NSString * _Nonnull)participantID ``` |

Modified [-[GKVoiceChatClient voiceChatService:didStopWithParticipantID:error:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520681-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)voiceChatService:(GKVoiceChatService *)voiceChatService didStopWithParticipantID:(NSString *)participantID error:(NSError *)error ``` |
| To | ``` - (void)voiceChatService:(GKVoiceChatService * _Nonnull)voiceChatService didStopWithParticipantID:(NSString * _Nonnull)participantID error:(NSError * _Nullable)error ``` |

Modified [-[GKVoiceChatClient voiceChatService:sendData:toParticipantID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521075-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)voiceChatService:(GKVoiceChatService *)voiceChatService sendData:(NSData *)data toParticipantID:(NSString *)participantID ``` |
| To | ``` - (void)voiceChatService:(GKVoiceChatService * _Nonnull)voiceChatService sendData:(NSData * _Nonnull)data toParticipantID:(NSString * _Nonnull)participantID ``` |

Modified [-[GKVoiceChatClient voiceChatService:sendRealTimeData:toParticipantID:]](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521009-voicechatservice)

|  | Declaration |
| --- | --- |
| From | ``` - (void)voiceChatService:(GKVoiceChatService *)voiceChatService sendRealTimeData:(NSData *)data toParticipantID:(NSString *)participantID ``` |
| To | ``` - (void)voiceChatService:(GKVoiceChatService * _Nonnull)voiceChatService sendRealTimeData:(NSData * _Nonnull)data toParticipantID:(NSString * _Nonnull)participantID ``` |

#### GKSavedGame.h

Modified [-[GKLocalPlayer deleteSavedGamesWithName:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520951-deletesavedgames)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deleteSavedGamesWithName:(NSString *)name completionHandler:(void (^)(NSError *error))handler ``` |
| To | ``` - (void)deleteSavedGamesWithName:(NSString * _Nonnull)name completionHandler:(void (^ _Nullable)(NSError * _Nullable error))handler ``` |

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

Modified [-[GKLocalPlayer saveGameData:withName:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520527-savegamedata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveGameData:(NSData *)data withName:(NSString *)name completionHandler:(void (^)(GKSavedGame *savedGame, NSError *error))handler ``` |
| To | ``` - (void)saveGameData:(NSData * _Nonnull)data withName:(NSString * _Nonnull)name completionHandler:(void (^ _Nullable)(GKSavedGame * _Nullable savedGame, NSError * _Nullable error))handler ``` |

Modified [GKSavedGame.deviceName](https://developer.apple.com/documentation/gamekit/gksavedgame/1520629-devicename)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, readonly) NSString *deviceName ``` |
| To | ``` @property(atomic, readonly, nullable) NSString *deviceName ``` |

Modified [-[GKSavedGame loadDataWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gksavedgame/1520754-loaddatawithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadDataWithCompletionHandler:(void (^)(NSData *data, NSError *error))handler ``` |
| To | ``` - (void)loadDataWithCompletionHandler:(void (^ _Nullable)(NSData * _Nullable data, NSError * _Nullable error))handler ``` |

Modified [GKSavedGame.modificationDate](https://developer.apple.com/documentation/gamekit/gksavedgame/1520829-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, readonly) NSDate *modificationDate ``` |
| To | ``` @property(atomic, readonly, nullable) NSDate *modificationDate ``` |

Modified [GKSavedGame.name](https://developer.apple.com/documentation/gamekit/gksavedgame/1520819-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(atomic, readonly) NSString *name ``` |
| To | ``` @property(atomic, readonly, nullable) NSString *name ``` |

#### GKSavedGameListener.h

Modified [-[GKSavedGameListener player:didModifySavedGame:]](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387328-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didModifySavedGame:(GKSavedGame *)savedGame ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didModifySavedGame:(GKSavedGame * _Nonnull)savedGame ``` |

Modified [-[GKSavedGameListener player:hasConflictingSavedGames:]](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387324-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player hasConflictingSavedGames:(NSArray *)savedGames ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player hasConflictingSavedGames:(NSArray<GKSavedGame *> * _Nonnull)savedGames ``` |

#### GKScore.h

Modified [GKScore.category](https://developer.apple.com/documentation/gamekit/gkscore/1399225-category)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *category ``` |
| To | ``` @property(copy, atomic, nullable) NSString *category ``` |

Modified [GKScore.date](https://developer.apple.com/documentation/gamekit/gkscore/1399234-date)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSDate *date ``` |
| To | ``` @property(readonly, retain, atomic, nonnull) NSDate *date ``` |

Modified [GKScore.formattedValue](https://developer.apple.com/documentation/gamekit/gkscore/1399221-formattedvalue)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *formattedValue ``` |
| To | ``` @property(readonly, copy, atomic, nullable) NSString *formattedValue ``` |

Modified [-[GKScore initWithCategory:]](https://developer.apple.com/documentation/gamekit/gkscore/1399242-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithCategory:(NSString *)category ``` |
| To | ``` - (instancetype _Nonnull)initWithCategory:(NSString * _Nullable)category ``` |

Modified [-[GKScore initWithLeaderboardIdentifier:]](https://developer.apple.com/documentation/gamekit/gkscore/1399240-initwithleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithLeaderboardIdentifier:(NSString *)identifier ``` |
| To | ``` - (instancetype _Nonnull)initWithLeaderboardIdentifier:(NSString * _Nonnull)identifier ``` |

Modified [-[GKScore initWithLeaderboardIdentifier:player:]](https://developer.apple.com/documentation/gamekit/gkscore/1399254-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithLeaderboardIdentifier:(NSString *)identifier player:(GKPlayer *)player ``` |
| To | ``` - (instancetype _Nonnull)initWithLeaderboardIdentifier:(NSString * _Nonnull)identifier player:(GKPlayer * _Nonnull)player ``` |

Modified [GKScore.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkscore/1399248-leaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) NSString *leaderboardIdentifier ``` |
| To | ``` @property(copy, atomic, nonnull) NSString *leaderboardIdentifier ``` |

Modified [GKScore.player](https://developer.apple.com/documentation/gamekit/gkscore/1399246-player)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKPlayer *player ``` |
| To | ``` @property(readonly, retain, atomic, nonnull) GKPlayer *player ``` |

Modified [GKScore.playerID](https://developer.apple.com/documentation/gamekit/gkscore/1399232-playerid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSString *playerID ``` |
| To | ``` @property(readonly, retain, atomic, nonnull) NSString *playerID ``` |

Modified [+[GKScore reportScores:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1399252-report)

|  | Declaration |
| --- | --- |
| From | ``` + (void)reportScores:(NSArray *)scores withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` + (void)reportScores:(NSArray<GKScore *> * _Nonnull)scores withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKScore reportScoreWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkscore/1399223-report)

|  | Declaration |
| --- | --- |
| From | ``` - (void)reportScoreWithCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)reportScoreWithCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

#### GKSessionError.h

Removed [GKSessionCancelledError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/cancellederror)Removed [GKSessionCannotEnableError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/cannotenableerror)Removed [GKSessionConnectionClosedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/connectionclosederror)Removed [GKSessionConnectionFailedError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionconnectionfailederror)Removed [GKSessionConnectivityError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionconnectivityerror)Removed [GKSessionDataTooBigError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessiondatatoobigerror)Removed [GKSessionDeclinedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/declinederror)Removed [GKSessionInProgressError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/inprogresserror)Removed [GKSessionInternalError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessioninternalerror)Removed [GKSessionInvalidParameterError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessioninvalidparametererror)Removed [GKSessionNotConnectedError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/notconnectederror)Removed [GKSessionPeerNotFoundError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/peernotfounderror)Removed [GKSessionSystemError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessionsystemerror)Removed [GKSessionTimedOutError](https://developer.apple.com/documentation/gamekit/gksessionerror/gksessiontimedouterror)Removed [GKSessionTransportError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/transporterror)Removed [GKSessionUnknownError](https://developer.apple.com/documentation/gamekit/gksessionerror/code/unknownerror)Added [GKSessionError](https://developer.apple.com/documentation/gamekit/gksessionerror)

#### GKTurnBasedMatch.h

Added [-[GKTurnBasedEventListener player:wantsToQuitMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520537-player)Modified [GKTurnBasedEventHandler.delegate](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521013-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) NSObject<GKTurnBasedEventHandlerDelegate> *delegate ``` |
| To | ``` @property(assign, atomic, nonnull) NSObject<GKTurnBasedEventHandlerDelegate> *delegate ``` |

Modified [+[GKTurnBasedEventHandler sharedTurnBasedEventHandler]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/1521211-sharedturnbasedeventhandler)

|  | Declaration |
| --- | --- |
| From | ``` + (GKTurnBasedEventHandler *)sharedTurnBasedEventHandler ``` |
| To | ``` + (GKTurnBasedEventHandler * _Nonnull)sharedTurnBasedEventHandler ``` |

Modified [-[GKTurnBasedEventHandlerDelegate handleInviteFromGameCenter:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1520926-handleinvite)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleInviteFromGameCenter:(NSArray *)playersToInvite ``` |
| To | ``` - (void)handleInviteFromGameCenter:(NSArray<GKPlayer *> * _Nonnull)playersToInvite ``` |

Modified [-[GKTurnBasedEventHandlerDelegate handleMatchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521053-handlematchended)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleMatchEnded:(GKTurnBasedMatch *)match ``` |
| To | ``` - (void)handleMatchEnded:(GKTurnBasedMatch * _Nonnull)match ``` |

Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1556899-handleturneventformatch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleTurnEventForMatch:(GKTurnBasedMatch *)match ``` |
| To | ``` - (void)handleTurnEventForMatch:(GKTurnBasedMatch * _Nonnull)match ``` |

Modified [-[GKTurnBasedEventHandlerDelegate handleTurnEventForMatch:didBecomeActive:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1521103-handleturnevent)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleTurnEventForMatch:(GKTurnBasedMatch *)match didBecomeActive:(BOOL)didBecomeActive ``` |
| To | ``` - (void)handleTurnEventForMatch:(GKTurnBasedMatch * _Nonnull)match didBecomeActive:(BOOL)didBecomeActive ``` |

Modified [-[GKTurnBasedEventListener player:didRequestMatchWithOtherPlayers:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520693-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player didRequestMatchWithOtherPlayers:(NSArray *)playersToInvite ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player didRequestMatchWithOtherPlayers:(NSArray<GKPlayer *> * _Nonnull)playersToInvite ``` |

Modified [-[GKTurnBasedEventListener player:matchEnded:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520554-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player matchEnded:(GKTurnBasedMatch *)match ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player matchEnded:(GKTurnBasedMatch * _Nonnull)match ``` |

Modified [-[GKTurnBasedEventListener player:receivedExchangeCancellation:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520649-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player receivedExchangeCancellation:(GKTurnBasedExchange *)exchange forMatch:(GKTurnBasedMatch *)match ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player receivedExchangeCancellation:(GKTurnBasedExchange * _Nonnull)exchange forMatch:(GKTurnBasedMatch * _Nonnull)match ``` |

Modified [-[GKTurnBasedEventListener player:receivedExchangeReplies:forCompletedExchange:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520827-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player receivedExchangeReplies:(NSArray *)replies forCompletedExchange:(GKTurnBasedExchange *)exchange forMatch:(GKTurnBasedMatch *)match ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player receivedExchangeReplies:(NSArray<GKTurnBasedExchangeReply *> * _Nonnull)replies forCompletedExchange:(GKTurnBasedExchange * _Nonnull)exchange forMatch:(GKTurnBasedMatch * _Nonnull)match ``` |

Modified [-[GKTurnBasedEventListener player:receivedExchangeRequest:forMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521209-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player receivedExchangeRequest:(GKTurnBasedExchange *)exchange forMatch:(GKTurnBasedMatch *)match ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player receivedExchangeRequest:(GKTurnBasedExchange * _Nonnull)exchange forMatch:(GKTurnBasedMatch * _Nonnull)match ``` |

Modified [-[GKTurnBasedEventListener player:receivedTurnEventForMatch:didBecomeActive:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521017-player)

|  | Declaration |
| --- | --- |
| From | ``` - (void)player:(GKPlayer *)player receivedTurnEventForMatch:(GKTurnBasedMatch *)match didBecomeActive:(BOOL)didBecomeActive ``` |
| To | ``` - (void)player:(GKPlayer * _Nonnull)player receivedTurnEventForMatch:(GKTurnBasedMatch * _Nonnull)match didBecomeActive:(BOOL)didBecomeActive ``` |

Modified [-[GKTurnBasedExchange cancelWithLocalizableMessageKey:arguments:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520779-cancel)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelWithLocalizableMessageKey:(NSString *)key arguments:(NSArray *)arguments completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)cancelWithLocalizableMessageKey:(NSString * _Nonnull)key arguments:(NSArray<NSString *> * _Nonnull)arguments completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedExchange.completionDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520994-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSDate *completionDate ``` |
| To | ``` @property(readonly, atomic, nullable) NSDate *completionDate ``` |

Modified [GKTurnBasedExchange.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521121-data)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSData *data ``` |
| To | ``` @property(readonly, atomic, nullable) NSData *data ``` |

Modified [GKTurnBasedExchange.exchangeID](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520666-exchangeid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *exchangeID ``` |
| To | ``` @property(readonly, atomic, nullable) NSString *exchangeID ``` |

Modified [GKTurnBasedExchange.message](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520633-message)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *message ``` |
| To | ``` @property(readonly, atomic, nullable) NSString *message ``` |

Modified [GKTurnBasedExchange.recipients](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520849-recipients)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *recipients ``` |
| To | ``` @property(readonly, atomic, nullable) NSArray<GKTurnBasedParticipant *> *recipients ``` |

Modified [GKTurnBasedExchange.replies](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520516-replies)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *replies ``` |
| To | ``` @property(readonly, atomic, nullable) NSArray<GKTurnBasedExchangeReply *> *replies ``` |

Modified [-[GKTurnBasedExchange replyWithLocalizableMessageKey:arguments:data:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520478-reply)

|  | Declaration |
| --- | --- |
| From | ``` - (void)replyWithLocalizableMessageKey:(NSString *)key arguments:(NSArray *)arguments data:(NSData *)data completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)replyWithLocalizableMessageKey:(NSString * _Nonnull)key arguments:(NSArray<NSString *> * _Nonnull)arguments data:(NSData * _Nonnull)data completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedExchange.sendDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521131-senddate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSDate *sendDate ``` |
| To | ``` @property(readonly, atomic, nullable) NSDate *sendDate ``` |

Modified [GKTurnBasedExchange.sender](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520936-sender)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) GKTurnBasedParticipant *sender ``` |
| To | ``` @property(readonly, atomic, nullable) GKTurnBasedParticipant *sender ``` |

Modified [GKTurnBasedExchange.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521105-timeoutdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSDate *timeoutDate ``` |
| To | ``` @property(readonly, atomic, nullable) NSDate *timeoutDate ``` |

Modified [GKTurnBasedExchangeReply.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520729-data)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSData *data ``` |
| To | ``` @property(readonly, atomic, nullable) NSData *data ``` |

Modified [GKTurnBasedExchangeReply.message](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520896-message)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *message ``` |
| To | ``` @property(readonly, atomic, nullable) NSString *message ``` |

Modified [GKTurnBasedExchangeReply.recipient](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1521025-recipient)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) GKTurnBasedParticipant *recipient ``` |
| To | ``` @property(readonly, atomic, nullable) GKTurnBasedParticipant *recipient ``` |

Modified [GKTurnBasedExchangeReply.replyDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520727-replydate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSDate *replyDate ``` |
| To | ``` @property(readonly, atomic, nullable) NSDate *replyDate ``` |

Modified [-[GKTurnBasedMatch acceptInviteWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520515-acceptinvite)

|  | Declaration |
| --- | --- |
| From | ``` - (void)acceptInviteWithCompletionHandler:(void (^)(GKTurnBasedMatch *match, NSError *error))completionHandler ``` |
| To | ``` - (void)acceptInviteWithCompletionHandler:(void (^ _Nullable)(GKTurnBasedMatch * _Nullable match, NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedMatch.activeExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520977-activeexchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSArray *activeExchanges ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSArray<GKTurnBasedExchange *> *activeExchanges ``` |

Modified [GKTurnBasedMatch.completedExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520918-completedexchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSArray *completedExchanges ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSArray<GKTurnBasedExchange *> *completedExchanges ``` |

Modified [GKTurnBasedMatch.creationDate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521168-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSDate *creationDate ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSDate *creationDate ``` |

Modified [GKTurnBasedMatch.currentParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520643-currentparticipant)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKTurnBasedParticipant *currentParticipant ``` |
| To | ``` @property(readonly, retain, atomic, nullable) GKTurnBasedParticipant *currentParticipant ``` |

Modified [-[GKTurnBasedMatch declineInviteWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520940-declineinvite)

|  | Declaration |
| --- | --- |
| From | ``` - (void)declineInviteWithCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)declineInviteWithCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch endMatchInTurnWithMatchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520907-endmatchinturn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)endMatchInTurnWithMatchData:(NSData *)matchData completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)endMatchInTurnWithMatchData:(NSData * _Nonnull)matchData completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch endMatchInTurnWithMatchData:scores:achievements:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521006-endmatchinturn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)endMatchInTurnWithMatchData:(NSData *)matchData scores:(NSArray *)scores achievements:(NSArray *)achievements completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)endMatchInTurnWithMatchData:(NSData * _Nonnull)matchData scores:(NSArray<GKScore *> * _Nullable)scores achievements:(NSArray<GKAchievement *> * _Nullable)achievements completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch endTurnWithNextParticipant:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1556897-endturn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)endTurnWithNextParticipant:(GKTurnBasedParticipant *)nextParticipant matchData:(NSData *)matchData completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)endTurnWithNextParticipant:(GKTurnBasedParticipant * _Nonnull)nextParticipant matchData:(NSData * _Nonnull)matchData completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch endTurnWithNextParticipants:turnTimeout:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520765-endturnwithnextparticipants)

|  | Declaration |
| --- | --- |
| From | ``` - (void)endTurnWithNextParticipants:(NSArray *)nextParticipants turnTimeout:(NSTimeInterval)timeout matchData:(NSData *)matchData completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)endTurnWithNextParticipants:(NSArray<GKTurnBasedParticipant *> * _Nonnull)nextParticipants turnTimeout:(NSTimeInterval)timeout matchData:(NSData * _Nonnull)matchData completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedMatch.exchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521224-exchanges)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSArray *exchanges ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSArray<GKTurnBasedExchange *> *exchanges ``` |

Modified [+[GKTurnBasedMatch findMatchForRequest:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521008-find)

|  | Declaration |
| --- | --- |
| From | ``` + (void)findMatchForRequest:(GKMatchRequest *)request withCompletionHandler:(void (^)(GKTurnBasedMatch *match, NSError *error))completionHandler ``` |
| To | ``` + (void)findMatchForRequest:(GKMatchRequest * _Nonnull)request withCompletionHandler:(void (^ _Nonnull)(GKTurnBasedMatch * _Nullable match, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch loadMatchDataWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521005-loadmatchdata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)loadMatchDataWithCompletionHandler:(void (^)(NSData *matchData, NSError *error))completionHandler ``` |
| To | ``` - (void)loadMatchDataWithCompletionHandler:(void (^ _Nullable)(NSData * _Nullable matchData, NSError * _Nullable error))completionHandler ``` |

Modified [+[GKTurnBasedMatch loadMatchesWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521207-loadmatcheswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadMatchesWithCompletionHandler:(void (^)(NSArray *matches, NSError *error))completionHandler ``` |
| To | ``` + (void)loadMatchesWithCompletionHandler:(void (^ _Nullable)(NSArray<GKTurnBasedMatch *> * _Nullable matches, NSError * _Nullable error))completionHandler ``` |

Modified [+[GKTurnBasedMatch loadMatchWithID:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521102-loadmatchwithid)

|  | Declaration |
| --- | --- |
| From | ``` + (void)loadMatchWithID:(NSString *)matchID withCompletionHandler:(void (^)(GKTurnBasedMatch *match, NSError *error))completionHandler ``` |
| To | ``` + (void)loadMatchWithID:(NSString * _Nonnull)matchID withCompletionHandler:(void (^ _Nullable)(GKTurnBasedMatch * _Nullable match, NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedMatch.matchData](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520991-matchdata)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSData *matchData ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSData *matchData ``` |

Modified [GKTurnBasedMatch.matchID](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520625-matchid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSString *matchID ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSString *matchID ``` |

Modified [GKTurnBasedMatch.message](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520721-message)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy, atomic) NSString *message ``` |
| To | ``` @property(readwrite, copy, atomic, nullable) NSString *message ``` |

Modified [-[GKTurnBasedMatch participantQuitInTurnWithOutcome:nextParticipant:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1556898-participantquitinturnwithoutcome)

|  | Declaration |
| --- | --- |
| From | ``` - (void)participantQuitInTurnWithOutcome:(GKTurnBasedMatchOutcome)matchOutcome nextParticipant:(GKTurnBasedParticipant *)nextParticipant matchData:(NSData *)matchData completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)participantQuitInTurnWithOutcome:(GKTurnBasedMatchOutcome)matchOutcome nextParticipant:(GKTurnBasedParticipant * _Nonnull)nextParticipant matchData:(NSData * _Nonnull)matchData completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch participantQuitInTurnWithOutcome:nextParticipants:turnTimeout:matchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520500-participantquitinturnwithoutcome)

|  | Declaration |
| --- | --- |
| From | ``` - (void)participantQuitInTurnWithOutcome:(GKTurnBasedMatchOutcome)matchOutcome nextParticipants:(NSArray *)nextParticipants turnTimeout:(NSTimeInterval)timeout matchData:(NSData *)matchData completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)participantQuitInTurnWithOutcome:(GKTurnBasedMatchOutcome)matchOutcome nextParticipants:(NSArray<GKTurnBasedParticipant *> * _Nonnull)nextParticipants turnTimeout:(NSTimeInterval)timeout matchData:(NSData * _Nonnull)matchData completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch participantQuitOutOfTurnWithOutcome:withCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521106-participantquitoutofturnwithoutc)

|  | Declaration |
| --- | --- |
| From | ``` - (void)participantQuitOutOfTurnWithOutcome:(GKTurnBasedMatchOutcome)matchOutcome withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)participantQuitOutOfTurnWithOutcome:(GKTurnBasedMatchOutcome)matchOutcome withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [GKTurnBasedMatch.participants](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520875-participants)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) NSArray *participants ``` |
| To | ``` @property(readonly, retain, atomic, nullable) NSArray<GKTurnBasedParticipant *> *participants ``` |

Modified [-[GKTurnBasedMatch rematchWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520794-rematch)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rematchWithCompletionHandler:(void (^)(GKTurnBasedMatch *match, NSError *error))completionHandler ``` |
| To | ``` - (void)rematchWithCompletionHandler:(void (^ _Nullable)(GKTurnBasedMatch * _Nullable match, NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch removeWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520651-remove)

|  | Declaration |
| --- | --- |
| From | ``` - (void)removeWithCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)removeWithCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[GKTurnBasedMatch saveCurrentTurnWithMatchData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520761-savecurrentturn)

|  | Declaration |
| --- | --- |
| From | ``` - (void)saveCurrentTurnWithMatchData:(NSData *)matchData completionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (void)saveCurrentTurnWithMatchData:(NSData * _Nonnull)matchData completionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

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

Modified [GKTurnBasedParticipant.lastTurnDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520941-lastturndate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSDate *lastTurnDate ``` |
| To | ``` @property(readonly, copy, atomic, nullable) NSDate *lastTurnDate ``` |

Modified [GKTurnBasedParticipant.player](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521037-player)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, retain, atomic) GKPlayer *player ``` |
| To | ``` @property(readonly, retain, atomic, nullable) GKPlayer *player ``` |

Modified [GKTurnBasedParticipant.playerID](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520474-playerid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *playerID ``` |
| To | ``` @property(readonly, copy, atomic, nullable) NSString *playerID ``` |

Modified [GKTurnBasedParticipant.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521187-timeoutdate)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSDate *timeoutDate ``` |
| To | ``` @property(readonly, copy, atomic, nullable) NSDate *timeoutDate ``` |

#### GKTurnBasedMatchmakerViewController.h

Modified [-[GKTurnBasedMatchmakerViewController initWithMatchRequest:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1521069-init)

|  | Declaration |
| --- | --- |
| From | ``` - (id)initWithMatchRequest:(GKMatchRequest *)request ``` |
| To | ``` - (id _Nonnull)initWithMatchRequest:(GKMatchRequest * _Nonnull)request ``` |

Modified [GKTurnBasedMatchmakerViewController.turnBasedMatchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1520697-turnbasedmatchmakerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(nonatomic, readwrite, assign) id<GKTurnBasedMatchmakerViewControllerDelegate> turnBasedMatchmakerDelegate ``` |
| To | ``` @property(nonatomic, readwrite, assign, nullable) id<GKTurnBasedMatchmakerViewControllerDelegate> turnBasedMatchmakerDelegate ``` |

Modified [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewController:didFailWithError:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1521028-turnbasedmatchmakerviewcontrolle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)turnBasedMatchmakerViewController:(GKTurnBasedMatchmakerViewController *)viewController didFailWithError:(NSError *)error ``` |
| To | ``` - (void)turnBasedMatchmakerViewController:(GKTurnBasedMatchmakerViewController * _Nonnull)viewController didFailWithError:(NSError * _Nonnull)error ``` |

Modified [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewController:didFindMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1520653-turnbasedmatchmakerviewcontrolle)

|  | Declaration | Deprecation | Optional |
| --- | --- | --- | --- |
| From | ``` - (void)turnBasedMatchmakerViewController:(GKTurnBasedMatchmakerViewController *)viewController didFindMatch:(GKTurnBasedMatch *)match ``` | -- | -- |
| To | ``` - (void)turnBasedMatchmakerViewController:(GKTurnBasedMatchmakerViewController * _Nonnull)viewController didFindMatch:(GKTurnBasedMatch * _Nonnull)match ``` | OS X 10.11 | yes |

Modified [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewController:playerQuitForMatch:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1520967-turnbasedmatchmakerviewcontrolle)

|  | Declaration | Deprecation | Optional |
| --- | --- | --- | --- |
| From | ``` - (void)turnBasedMatchmakerViewController:(GKTurnBasedMatchmakerViewController *)viewController playerQuitForMatch:(GKTurnBasedMatch *)match ``` | -- | -- |
| To | ``` - (void)turnBasedMatchmakerViewController:(GKTurnBasedMatchmakerViewController * _Nonnull)viewController playerQuitForMatch:(GKTurnBasedMatch * _Nonnull)match ``` | OS X 10.11 | yes |

Modified [-[GKTurnBasedMatchmakerViewControllerDelegate turnBasedMatchmakerViewControllerWasCancelled:]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1521000-turnbasedmatchmakerviewcontrolle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)turnBasedMatchmakerViewControllerWasCancelled:(GKTurnBasedMatchmakerViewController *)viewController ``` |
| To | ``` - (void)turnBasedMatchmakerViewControllerWasCancelled:(GKTurnBasedMatchmakerViewController * _Nonnull)viewController ``` |

#### GKVoiceChat.h

Modified [GKVoiceChat.name](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385707-name)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy, atomic) NSString *name ``` |
| To | ``` @property(readonly, copy, atomic, nonnull) NSString *name ``` |

Modified [GKVoiceChat.playerIDs](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385721-playerids)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *playerIDs ``` |
| To | ``` @property(readonly, atomic, nonnull) NSArray<NSString *> *playerIDs ``` |

Modified [GKVoiceChat.players](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385701-players)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *players ``` |
| To | ``` @property(readonly, atomic, nonnull) NSArray<GKPlayer *> *players ``` |

Modified [GKVoiceChat.playerStateUpdateHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385705-playerstateupdatehandler)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) void (^playerStateUpdateHandler)(NSString *playerID, GKVoiceChatPlayerState state) ``` |
| To | ``` @property(copy, atomic, nonnull) void (^playerStateUpdateHandler)(NSString * _Nonnull playerID, GKVoiceChatPlayerState state) ``` |

Modified [GKVoiceChat.playerVoiceChatStateDidChangeHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385713-playervoicechatstatedidchangehan)

|  | Declaration |
| --- | --- |
| From | ``` @property(copy, atomic) void (^playerVoiceChatStateDidChangeHandler)(GKPlayer *player, GKVoiceChatPlayerState state) ``` |
| To | ``` @property(copy, atomic, nonnull) void (^playerVoiceChatStateDidChangeHandler)(GKPlayer * _Nonnull player, GKVoiceChatPlayerState state) ``` |

Modified [-[GKVoiceChat setMute:forPlayer:]](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385711-setmute)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setMute:(BOOL)isMuted forPlayer:(NSString *)playerID ``` |
| To | ``` - (void)setMute:(BOOL)isMuted forPlayer:(NSString * _Nonnull)playerID ``` |

Modified [-[GKVoiceChat setPlayer:muted:]](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385717-setplayer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)setPlayer:(GKPlayer *)player muted:(BOOL)isMuted ``` |
| To | ``` - (void)setPlayer:(GKPlayer * _Nonnull)player muted:(BOOL)isMuted ``` |

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
