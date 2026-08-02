---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/GameKit.html
archived_at: '2026-07-18T02:56:50.832088Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# GameKit Changes for Swift

### GameKit

Removed GKPeerPickerConnectionTypeRemoved GKPeerPickerConnectionTypeNearbyRemoved GKPeerPickerConnectionTypeOnlineRemoved GKPeerStateAvailableRemoved GKPeerStateConnectedRemoved GKPeerStateConnectingRemoved GKPeerStateDisconnectedRemoved GKPeerStateUnavailableRemoved GKSendDataReliableRemoved GKSendDataUnreliableRemoved GKSessionCancelledErrorRemoved GKSessionCannotEnableErrorRemoved GKSessionConnectionClosedErrorRemoved GKSessionConnectionFailedErrorRemoved GKSessionConnectivityErrorRemoved GKSessionDataTooBigErrorRemoved GKSessionDeclinedErrorRemoved GKSessionInProgressErrorRemoved GKSessionInternalErrorRemoved GKSessionInvalidParameterErrorRemoved GKSessionModeClientRemoved GKSessionModePeerRemoved GKSessionModeServerRemoved GKSessionNotConnectedErrorRemoved GKSessionPeerNotFoundErrorRemoved GKSessionSystemErrorRemoved GKSessionTimedOutErrorRemoved GKSessionTransportErrorRemoved GKSessionUnknownErrorRemoved GKTurnBasedExchangeStatusRemoved GKTurnBasedExchangeStatusActiveRemoved GKTurnBasedExchangeStatusCanceledRemoved GKTurnBasedExchangeStatusCompleteRemoved GKTurnBasedExchangeStatusResolvedRemoved GKTurnBasedExchangeStatusUnknownRemoved GKVoiceChatServiceAudioUnavailableErrorRemoved GKVoiceChatServiceClientMissingRequiredMethodsErrorRemoved GKVoiceChatServiceInternalErrorRemoved GKVoiceChatServiceInvalidCallIDErrorRemoved GKVoiceChatServiceInvalidParameterErrorRemoved GKVoiceChatServiceMethodCurrentlyInvalidErrorRemoved GKVoiceChatServiceNetworkConfigurationErrorRemoved GKVoiceChatServiceNoRemotePacketsErrorRemoved GKVoiceChatServiceOutOfMemoryErrorRemoved GKVoiceChatServiceRemoteParticipantBusyErrorRemoved GKVoiceChatServiceRemoteParticipantCancelledErrorRemoved GKVoiceChatServiceRemoteParticipantDeclinedInviteErrorRemoved GKVoiceChatServiceRemoteParticipantHangupErrorRemoved GKVoiceChatServiceRemoteParticipantResponseInvalidErrorRemoved GKVoiceChatServiceUnableToConnectErrorRemoved GKVoiceChatServiceUninitializedClientErrorRemoved GKVoiceChatServiceUnsupportedRemoteVersionErrorAdded [GKGameCenterViewController.leaderboardTimeScope](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520464-leaderboardtimescope)Added [GKInviteRecipientResponse.InviteeResponseAccepted](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponseaccepted)Added [GKInviteRecipientResponse.InviteeResponseDeclined](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/1520841-inviteeresponsedeclined)Added [GKInviteRecipientResponse.InviteeResponseFailed](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponsefailed)Added [GKInviteRecipientResponse.InviteeResponseIncompatible](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponseincompatible)Added [GKInviteRecipientResponse.InviteeResponseNoAnswer](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/1520715-inviteeresponsenoanswer)Added [GKInviteRecipientResponse.InviteeResponseUnableToConnect](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse/gkinviteeresponseunabletoconnect)Added [GKMatchDelegate.match(_: GKMatch, didReceiveData: NSData, forRecipient: GKPlayer, fromRemotePlayer: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502034-match)Added [GKPlayer.anonymousGuestPlayerWithIdentifier(_: String) -> Self [class]](https://developer.apple.com/documentation/gamekit/gkplayer/1520559-anonymousguestplayer)Added [GKPlayer.guestIdentifier](https://developer.apple.com/documentation/gamekit/gkplayer/1520901-guestidentifier)Added [GKTurnBasedEventListener.player(_: GKPlayer, wantsToQuitMatch: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520537-player)Added [GKTurnBasedExchangeStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus)Added [GKTurnBasedExchangeStatus.Active](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/active)Added [GKTurnBasedExchangeStatus.Canceled](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/gkturnbasedexchangestatuscanceled)Added [GKTurnBasedExchangeStatus.Complete](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/complete)Added [GKTurnBasedExchangeStatus.Resolved](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/resolved)Added [GKTurnBasedExchangeStatus.Unknown](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus/unknown)Modified [GKAchievement](https://developer.apple.com/documentation/gamekit/gkachievement)

|  | Declaration |
| --- | --- |
| From | ``` class GKAchievement : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     class func resetAchievementsWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     init!(identifier identifier: String!)     init!(identifier identifier: String!, player player: GKPlayer!)     class func reportAchievements(_ achievements: [AnyObject]!, withCompletionHandler completionHandler: ((NSError!) -> Void)!)     var identifier: String!     var percentComplete: Double     var completed: Bool { get }     @NSCopying var lastReportedDate: NSDate! { get }     var showsCompletionBanner: Bool     var player: GKPlayer! { get } } extension GKAchievement {     func reportAchievementWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     init!(identifier identifier: String!, forPlayer playerID: String!)     var hidden: Bool { get }     var playerID: String! { get } } extension GKAchievement {     func challengeComposeControllerWithMessage(_ message: String!, players players: [AnyObject]!, completionHandler completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController!     func selectChallengeablePlayers(_ players: [AnyObject]!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!)     class func reportAchievements(_ achievements: [AnyObject]!, withEligibleChallenges challenges: [AnyObject]!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) } extension GKAchievement {     func selectChallengeablePlayerIDs(_ playerIDs: [AnyObject]!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func issueChallengeToPlayers(_ playerIDs: [AnyObject]!, message message: String!)     func challengeComposeControllerWithPlayers(_ playerIDs: [AnyObject]!, message message: String!, completionHandler completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController! } ``` |
| To | ``` class GKAchievement : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementsWithCompletionHandler(_ completionHandler: (([GKAchievement]?, NSError?) -> Void)?)     class func resetAchievementsWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(identifier identifier: String?)     init(identifier identifier: String?, player player: GKPlayer)     class func reportAchievements(_ achievements: [GKAchievement], withCompletionHandler completionHandler: ((NSError?) -> Void)?)     var identifier: String?     var percentComplete: Double     var completed: Bool { get }     @NSCopying var lastReportedDate: NSDate { get }     var showsCompletionBanner: Bool     var player: GKPlayer { get } } extension GKAchievement {     func reportAchievementWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(identifier identifier: String?, forPlayer playerID: String)     var hidden: Bool { get }     var playerID: String { get } } extension GKAchievement {     func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer], completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController     func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     class func reportAchievements(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKAchievement {     func selectChallengeablePlayerIDs(_ playerIDs: [String]?, withCompletionHandler completionHandler: (([String]?, NSError?) -> Void)?)     func issueChallengeToPlayers(_ playerIDs: [String]?, message message: String?)     func challengeComposeControllerWithPlayers(_ playerIDs: [String]?, message message: String?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController? } ``` |

Modified [GKAchievement.challengeComposeControllerWithMessage(_: String?, players: [GKPlayer], completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](https://developer.apple.com/documentation/gamekit/gkachievement/1520805-challengecomposecontrollerwithme)

|  | Declaration |
| --- | --- |
| From | ``` func challengeComposeControllerWithMessage(_ message: String!, players players: [AnyObject]!, completionHandler completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController! ``` |
| To | ``` func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer], completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController ``` |

Modified [GKAchievement.challengeComposeControllerWithPlayers(_: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](https://developer.apple.com/documentation/gamekit/gkachievement/1623556-challengecomposecontroller)

|  | Declaration |
| --- | --- |
| From | ``` func challengeComposeControllerWithPlayers(_ playerIDs: [AnyObject]!, message message: String!, completionHandler completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController! ``` |
| To | ``` func challengeComposeControllerWithPlayers(_ playerIDs: [String]?, message message: String?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController? ``` |

Modified [GKAchievement.identifier](https://developer.apple.com/documentation/gamekit/gkachievement/1520631-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! ``` |
| To | ``` var identifier: String? ``` |

Modified [GKAchievement.init(identifier: String?)](https://developer.apple.com/documentation/gamekit/gkachievement/1520622-initwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(identifier identifier: String!) ``` |
| To | ``` init(identifier identifier: String?) ``` |

Modified [GKAchievement.init(identifier: String?, forPlayer: String)](https://developer.apple.com/documentation/gamekit/gkachievement/1625009-initwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(identifier identifier: String!, forPlayer playerID: String!) ``` |
| To | ``` init(identifier identifier: String?, forPlayer playerID: String) ``` |

Modified [GKAchievement.init(identifier: String?, player: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkachievement/1521092-initwithidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(identifier identifier: String!, player player: GKPlayer!) ``` |
| To | ``` init(identifier identifier: String?, player player: GKPlayer) ``` |

Modified [GKAchievement.lastReportedDate](https://developer.apple.com/documentation/gamekit/gkachievement/1520993-lastreporteddate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var lastReportedDate: NSDate! { get } ``` |
| To | ``` @NSCopying var lastReportedDate: NSDate { get } ``` |

Modified [GKAchievement.loadAchievementsWithCompletionHandler(_: (([GKAchievement]?, NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievement/1520748-loadachievements)

|  | Declaration |
| --- | --- |
| From | ``` class func loadAchievementsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` class func loadAchievementsWithCompletionHandler(_ completionHandler: (([GKAchievement]?, NSError?) -> Void)?) ``` |

Modified [GKAchievement.player](https://developer.apple.com/documentation/gamekit/gkachievement/1520943-player)

|  | Declaration |
| --- | --- |
| From | ``` var player: GKPlayer! { get } ``` |
| To | ``` var player: GKPlayer { get } ``` |

Modified [GKAchievement.playerID](https://developer.apple.com/documentation/gamekit/gkachievement/1625010-playerid)

|  | Declaration |
| --- | --- |
| From | ``` var playerID: String! { get } ``` |
| To | ``` var playerID: String { get } ``` |

Modified [GKAchievement.reportAchievements(_: [GKAchievement], withCompletionHandler: ((NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievement/1520509-reportachievements)

|  | Declaration |
| --- | --- |
| From | ``` class func reportAchievements(_ achievements: [AnyObject]!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` class func reportAchievements(_ achievements: [GKAchievement], withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKAchievement.reportAchievements(_: [GKAchievement], withEligibleChallenges: [GKChallenge], withCompletionHandler: ((NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievement/1520558-report)

|  | Declaration |
| --- | --- |
| From | ``` class func reportAchievements(_ achievements: [AnyObject]!, withEligibleChallenges challenges: [AnyObject]!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` class func reportAchievements(_ achievements: [GKAchievement], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKAchievement.resetAchievementsWithCompletionHandler(_: ((NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievement/1520717-resetachievementswithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` class func resetAchievementsWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` class func resetAchievementsWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKAchievement.selectChallengeablePlayerIDs(_: [String]?, withCompletionHandler: (([String]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkachievement/1521129-selectchallengeableplayerids)

|  | Declaration |
| --- | --- |
| From | ``` func selectChallengeablePlayerIDs(_ playerIDs: [AnyObject]!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func selectChallengeablePlayerIDs(_ playerIDs: [String]?, withCompletionHandler completionHandler: (([String]?, NSError?) -> Void)?) ``` |

Modified [GKAchievement.selectChallengeablePlayers(_: [GKPlayer], withCompletionHandler: (([GKPlayer]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkachievement/1520504-selectchallengeableplayers)

|  | Declaration |
| --- | --- |
| From | ``` func selectChallengeablePlayers(_ players: [AnyObject]!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func selectChallengeablePlayers(_ players: [GKPlayer], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?) ``` |

Modified [GKAchievementChallenge](https://developer.apple.com/documentation/gamekit/gkachievementchallenge)

|  | Declaration |
| --- | --- |
| From | ``` class GKAchievementChallenge : GKChallenge {     var achievement: GKAchievement! { get } } ``` |
| To | ``` class GKAchievementChallenge : GKChallenge {     var achievement: GKAchievement? { get } } ``` |

Modified [GKAchievementChallenge.achievement](https://developer.apple.com/documentation/gamekit/gkachievementchallenge/1520858-achievement)

|  | Declaration |
| --- | --- |
| From | ``` var achievement: GKAchievement! { get } ``` |
| To | ``` var achievement: GKAchievement? { get } ``` |

Modified [GKAchievementDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription)

|  | Declaration |
| --- | --- |
| From | ``` class GKAchievementDescription : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementDescriptionsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     var identifier: String! { get }     var groupIdentifier: String! { get }     var title: String! { get }     var achievedDescription: String! { get }     var unachievedDescription: String! { get }     var maximumPoints: Int { get }     var hidden: Bool { get }     var replayable: Bool { get } } extension GKAchievementDescription {     var image: UIImage! { get }     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage!, NSError!) -> Void)!)     class func incompleteAchievementImage() -> UIImage!     class func placeholderCompletedAchievementImage() -> UIImage! } ``` |
| To | ``` class GKAchievementDescription : NSObject, NSCoding, NSSecureCoding {     class func loadAchievementDescriptionsWithCompletionHandler(_ completionHandler: (([GKAchievementDescription]?, NSError?) -> Void)?)     var identifier: String? { get }     var groupIdentifier: String? { get }     var title: String? { get }     var achievedDescription: String? { get }     var unachievedDescription: String? { get }     var maximumPoints: Int { get }     var hidden: Bool { get }     var replayable: Bool { get } } extension GKAchievementDescription {     var image: UIImage? { get }     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?)     class func incompleteAchievementImage() -> UIImage     class func placeholderCompletedAchievementImage() -> UIImage } ``` |

Modified [GKAchievementDescription.achievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416598-achieveddescription)

|  | Declaration |
| --- | --- |
| From | ``` var achievedDescription: String! { get } ``` |
| To | ``` var achievedDescription: String? { get } ``` |

Modified [GKAchievementDescription.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416587-groupidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var groupIdentifier: String! { get } ``` |
| To | ``` var groupIdentifier: String? { get } ``` |

Modified [GKAchievementDescription.identifier](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416586-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! { get } ``` |
| To | ``` var identifier: String? { get } ``` |

Modified [GKAchievementDescription.incompleteAchievementImage() -> UIImage [class]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416600-incompleteachievementimage)

|  | Declaration |
| --- | --- |
| From | ``` class func incompleteAchievementImage() -> UIImage! ``` |
| To | ``` class func incompleteAchievementImage() -> UIImage ``` |

Modified [GKAchievementDescription.loadAchievementDescriptionsWithCompletionHandler(_: (([GKAchievementDescription]?, NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416601-loadachievementdescriptionswithc)

|  | Declaration |
| --- | --- |
| From | ``` class func loadAchievementDescriptionsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` class func loadAchievementDescriptionsWithCompletionHandler(_ completionHandler: (([GKAchievementDescription]?, NSError?) -> Void)?) ``` |

Modified [GKAchievementDescription.loadImageWithCompletionHandler(_: ((UIImage?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416596-loadimage)

|  | Declaration |
| --- | --- |
| From | ``` func loadImageWithCompletionHandler(_ completionHandler: ((UIImage!, NSError!) -> Void)!) ``` |
| To | ``` func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?) ``` |

Modified [GKAchievementDescription.placeholderCompletedAchievementImage() -> UIImage [class]](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416580-placeholdercompletedachievementi)

|  | Declaration |
| --- | --- |
| From | ``` class func placeholderCompletedAchievementImage() -> UIImage! ``` |
| To | ``` class func placeholderCompletedAchievementImage() -> UIImage ``` |

Modified [GKAchievementDescription.title](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416602-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified [GKAchievementDescription.unachievedDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription/1416584-unachieveddescription)

|  | Declaration |
| --- | --- |
| From | ``` var unachievedDescription: String! { get } ``` |
| To | ``` var unachievedDescription: String? { get } ``` |

Modified [GKChallenge](https://developer.apple.com/documentation/gamekit/gkchallenge)

|  | Declaration |
| --- | --- |
| From | ``` class GKChallenge : NSObject, NSCoding, NSSecureCoding {     class func loadReceivedChallengesWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func decline()     var issuingPlayerID: String! { get }     var receivingPlayerID: String! { get }     @NSCopying var issuingPlayer: GKPlayer! { get }     @NSCopying var receivingPlayer: GKPlayer! { get }     var state: GKChallengeState { get }     var issueDate: NSDate! { get }     var completionDate: NSDate! { get }     var message: String! { get } } ``` |
| To | ``` class GKChallenge : NSObject, NSCoding, NSSecureCoding {     class func loadReceivedChallengesWithCompletionHandler(_ completionHandler: (([GKChallenge]?, NSError?) -> Void)?)     func decline()     var issuingPlayerID: String? { get }     var receivingPlayerID: String? { get }     @NSCopying var issuingPlayer: GKPlayer? { get }     @NSCopying var receivingPlayer: GKPlayer? { get }     var state: GKChallengeState { get }     var issueDate: NSDate { get }     var completionDate: NSDate? { get }     var message: String? { get } } ``` |

Modified [GKChallenge.completionDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520928-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` var completionDate: NSDate! { get } ``` |
| To | ``` var completionDate: NSDate? { get } ``` |

Modified [GKChallenge.issueDate](https://developer.apple.com/documentation/gamekit/gkchallenge/1520803-issuedate)

|  | Declaration |
| --- | --- |
| From | ``` var issueDate: NSDate! { get } ``` |
| To | ``` var issueDate: NSDate { get } ``` |

Modified [GKChallenge.issuingPlayer](https://developer.apple.com/documentation/gamekit/gkchallenge/1521010-issuingplayer)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var issuingPlayer: GKPlayer! { get } ``` |
| To | ``` @NSCopying var issuingPlayer: GKPlayer? { get } ``` |

Modified [GKChallenge.issuingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521100-issuingplayerid)

|  | Declaration |
| --- | --- |
| From | ``` var issuingPlayerID: String! { get } ``` |
| To | ``` var issuingPlayerID: String? { get } ``` |

Modified [GKChallenge.loadReceivedChallengesWithCompletionHandler(_: (([GKChallenge]?, NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkchallenge/1520864-loadreceivedchallengeswithcomple)

|  | Declaration |
| --- | --- |
| From | ``` class func loadReceivedChallengesWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` class func loadReceivedChallengesWithCompletionHandler(_ completionHandler: (([GKChallenge]?, NSError?) -> Void)?) ``` |

Modified [GKChallenge.message](https://developer.apple.com/documentation/gamekit/gkchallenge/1520998-message)

|  | Declaration |
| --- | --- |
| From | ``` var message: String! { get } ``` |
| To | ``` var message: String? { get } ``` |

Modified [GKChallenge.receivingPlayer](https://developer.apple.com/documentation/gamekit/gkchallenge/1520570-receivingplayer)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var receivingPlayer: GKPlayer! { get } ``` |
| To | ``` @NSCopying var receivingPlayer: GKPlayer? { get } ``` |

Modified [GKChallenge.receivingPlayerID](https://developer.apple.com/documentation/gamekit/gkchallenge/1521113-receivingplayerid)

|  | Declaration |
| --- | --- |
| From | ``` var receivingPlayerID: String! { get } ``` |
| To | ``` var receivingPlayerID: String? { get } ``` |

Modified [GKChallengeListener](https://developer.apple.com/documentation/gamekit/gkchallengelistener)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKChallengeListener : NSObjectProtocol {     optional func player(_ player: GKPlayer!, wantsToPlayChallenge challenge: GKChallenge!)     optional func player(_ player: GKPlayer!, didReceiveChallenge challenge: GKChallenge!)     optional func player(_ player: GKPlayer!, didCompleteChallenge challenge: GKChallenge!, issuedByFriend friendPlayer: GKPlayer!)     optional func player(_ player: GKPlayer!, issuedChallengeWasCompleted challenge: GKChallenge!, byFriend friendPlayer: GKPlayer!) } ``` |
| To | ``` protocol GKChallengeListener : NSObjectProtocol {     optional func player(_ player: GKPlayer, wantsToPlayChallenge challenge: GKChallenge)     optional func player(_ player: GKPlayer, didReceiveChallenge challenge: GKChallenge)     optional func player(_ player: GKPlayer, didCompleteChallenge challenge: GKChallenge, issuedByFriend friendPlayer: GKPlayer)     optional func player(_ player: GKPlayer, issuedChallengeWasCompleted challenge: GKChallenge, byFriend friendPlayer: GKPlayer) } ``` |

Modified [GKChallengeListener.player(_: GKPlayer, didCompleteChallenge: GKChallenge, issuedByFriend: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494688-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, didCompleteChallenge challenge: GKChallenge!, issuedByFriend friendPlayer: GKPlayer!) ``` |
| To | ``` optional func player(_ player: GKPlayer, didCompleteChallenge challenge: GKChallenge, issuedByFriend friendPlayer: GKPlayer) ``` |

Modified [GKChallengeListener.player(_: GKPlayer, didReceiveChallenge: GKChallenge)](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494691-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, didReceiveChallenge challenge: GKChallenge!) ``` |
| To | ``` optional func player(_ player: GKPlayer, didReceiveChallenge challenge: GKChallenge) ``` |

Modified [GKChallengeListener.player(_: GKPlayer, issuedChallengeWasCompleted: GKChallenge, byFriend: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494686-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, issuedChallengeWasCompleted challenge: GKChallenge!, byFriend friendPlayer: GKPlayer!) ``` |
| To | ``` optional func player(_ player: GKPlayer, issuedChallengeWasCompleted challenge: GKChallenge, byFriend friendPlayer: GKPlayer) ``` |

Modified [GKChallengeListener.player(_: GKPlayer, wantsToPlayChallenge: GKChallenge)](https://developer.apple.com/documentation/gamekit/gkchallengelistener/1494684-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, wantsToPlayChallenge challenge: GKChallenge!) ``` |
| To | ``` optional func player(_ player: GKPlayer, wantsToPlayChallenge challenge: GKChallenge) ``` |

Modified [GKChallengeState [enum]](https://developer.apple.com/documentation/gamekit/gkchallengestate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKErrorCode [enum]](https://developer.apple.com/documentation/gamekit/gkerrorcode)

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum GKErrorCode : Int {     case Unknown     case Cancelled     case CommunicationsFailure     case UserDenied     case InvalidCredentials     case NotAuthenticated     case AuthenticationInProgress     case InvalidPlayer     case ScoreNotSet     case ParentalControlsBlocked     case PlayerStatusExceedsMaximumLength     case PlayerStatusInvalid     case MatchRequestInvalid     case Underage     case GameUnrecognized     case NotSupported     case InvalidParameter     case UnexpectedConnection     case ChallengeInvalid     case TurnBasedMatchDataTooLarge     case TurnBasedTooManySessions     case TurnBasedInvalidParticipant     case TurnBasedInvalidTurn     case TurnBasedInvalidState     case InvitationsDisabled     case PlayerPhotoFailure     case UbiquityContainerUnavailable } ``` | Equatable, Hashable, RawRepresentable | -- |
| To | ``` enum GKErrorCode : Int {     case Unknown     case Cancelled     case CommunicationsFailure     case UserDenied     case InvalidCredentials     case NotAuthenticated     case AuthenticationInProgress     case InvalidPlayer     case ScoreNotSet     case ParentalControlsBlocked     case PlayerStatusExceedsMaximumLength     case PlayerStatusInvalid     case MatchRequestInvalid     case Underage     case GameUnrecognized     case NotSupported     case InvalidParameter     case UnexpectedConnection     case ChallengeInvalid     case TurnBasedMatchDataTooLarge     case TurnBasedTooManySessions     case TurnBasedInvalidParticipant     case TurnBasedInvalidTurn     case TurnBasedInvalidState     case InvitationsDisabled     case PlayerPhotoFailure     case UbiquityContainerUnavailable } extension GKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension GKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable | Int |

Modified [GKFriendRequestComposeViewController](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GKFriendRequestComposeViewController : UINavigationController { } extension GKFriendRequestComposeViewController {     class func maxNumberOfRecipients() -> Int     func setMessage(_ message: String!)     func addRecipientPlayers(_ players: [AnyObject]!)     func addRecipientsWithPlayerIDs(_ playerIDs: [AnyObject]!)     func addRecipientsWithEmailAddresses(_ emailAddresses: [AnyObject]!)     unowned(unsafe) var composeViewDelegate: GKFriendRequestComposeViewControllerDelegate! } ``` |
| To | ``` class GKFriendRequestComposeViewController : UINavigationController { } extension GKFriendRequestComposeViewController {     class func maxNumberOfRecipients() -> Int     func setMessage(_ message: String?)     func addRecipientPlayers(_ players: [GKPlayer])     func addRecipientsWithPlayerIDs(_ playerIDs: [String])     func addRecipientsWithEmailAddresses(_ emailAddresses: [String])     unowned(unsafe) var composeViewDelegate: GKFriendRequestComposeViewControllerDelegate? } ``` |

Modified [GKFriendRequestComposeViewController.addRecipientPlayers(_: [GKPlayer])](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437199-addrecipientplayers)

|  | Declaration |
| --- | --- |
| From | ``` func addRecipientPlayers(_ players: [AnyObject]!) ``` |
| To | ``` func addRecipientPlayers(_ players: [GKPlayer]) ``` |

Modified [GKFriendRequestComposeViewController.addRecipientsWithEmailAddresses(_: [String])](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437190-addrecipientswithemailaddresses)

|  | Declaration |
| --- | --- |
| From | ``` func addRecipientsWithEmailAddresses(_ emailAddresses: [AnyObject]!) ``` |
| To | ``` func addRecipientsWithEmailAddresses(_ emailAddresses: [String]) ``` |

Modified [GKFriendRequestComposeViewController.addRecipientsWithPlayerIDs(_: [String])](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437188-addrecipientswithplayerids)

|  | Declaration |
| --- | --- |
| From | ``` func addRecipientsWithPlayerIDs(_ playerIDs: [AnyObject]!) ``` |
| To | ``` func addRecipientsWithPlayerIDs(_ playerIDs: [String]) ``` |

Modified [GKFriendRequestComposeViewController.composeViewDelegate](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437192-composeviewdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var composeViewDelegate: GKFriendRequestComposeViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var composeViewDelegate: GKFriendRequestComposeViewControllerDelegate? ``` |

Modified [GKFriendRequestComposeViewController.setMessage(_: String?)](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller/1437201-setmessage)

|  | Declaration |
| --- | --- |
| From | ``` func setMessage(_ message: String!) ``` |
| To | ``` func setMessage(_ message: String?) ``` |

Modified [GKFriendRequestComposeViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKFriendRequestComposeViewControllerDelegate {     func friendRequestComposeViewControllerDidFinish(_ viewController: GKFriendRequestComposeViewController!) } ``` |
| To | ``` protocol GKFriendRequestComposeViewControllerDelegate {     func friendRequestComposeViewControllerDidFinish(_ viewController: GKFriendRequestComposeViewController) } ``` |

Modified [GKFriendRequestComposeViewControllerDelegate.friendRequestComposeViewControllerDidFinish(_: GKFriendRequestComposeViewController)](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate/1437186-friendrequestcomposeviewcontroll)

|  | Declaration |
| --- | --- |
| From | ``` func friendRequestComposeViewControllerDidFinish(_ viewController: GKFriendRequestComposeViewController!) ``` |
| To | ``` func friendRequestComposeViewControllerDidFinish(_ viewController: GKFriendRequestComposeViewController) ``` |

Modified [GKGameCenterControllerDelegate](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKGameCenterControllerDelegate : NSObjectProtocol {     func gameCenterViewControllerDidFinish(_ gameCenterViewController: GKGameCenterViewController!) } ``` |
| To | ``` protocol GKGameCenterControllerDelegate : NSObjectProtocol {     func gameCenterViewControllerDidFinish(_ gameCenterViewController: GKGameCenterViewController) } ``` |

Modified [GKGameCenterControllerDelegate.gameCenterViewControllerDidFinish(_: GKGameCenterViewController)](https://developer.apple.com/documentation/gamekit/gkgamecentercontrollerdelegate/1520771-gamecenterviewcontrollerdidfinis)

|  | Declaration |
| --- | --- |
| From | ``` func gameCenterViewControllerDidFinish(_ gameCenterViewController: GKGameCenterViewController!) ``` |
| To | ``` func gameCenterViewControllerDidFinish(_ gameCenterViewController: GKGameCenterViewController) ``` |

Modified [GKGameCenterViewController](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GKGameCenterViewController : UINavigationController {     unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate!     var viewState: GKGameCenterViewControllerState } extension GKGameCenterViewController {     var leaderboardTimeScope: GKLeaderboardTimeScope     var leaderboardIdentifier: String!     var leaderboardCategory: String! } ``` |
| To | ``` class GKGameCenterViewController : UINavigationController {     unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate?     var viewState: GKGameCenterViewControllerState } extension GKGameCenterViewController {     var leaderboardTimeScope: GKLeaderboardTimeScope     var leaderboardIdentifier: String?     var leaderboardCategory: String? } ``` |

Modified [GKGameCenterViewController.gameCenterDelegate](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520845-gamecenterdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate! ``` |
| To | ``` unowned(unsafe) var gameCenterDelegate: GKGameCenterControllerDelegate? ``` |

Modified [GKGameCenterViewController.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520540-leaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var leaderboardIdentifier: String! ``` |
| To | ``` var leaderboardIdentifier: String? ``` |

Modified [GKGameCenterViewControllerState [enum]](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKInvite](https://developer.apple.com/documentation/gamekit/gkinvite)

|  | Declaration |
| --- | --- |
| From | ``` class GKInvite : NSObject {     var sender: GKPlayer! { get }     var inviter: String! { get }     var hosted: Bool { get }     var playerGroup: Int { get }     var playerAttributes: UInt32 { get } } ``` |
| To | ``` class GKInvite : NSObject {     var sender: GKPlayer { get }     var inviter: String { get }     var hosted: Bool { get }     var playerGroup: Int { get }     var playerAttributes: UInt32 { get } } ``` |

Modified [GKInvite.inviter](https://developer.apple.com/documentation/gamekit/gkinvite/1520959-inviter)

|  | Declaration |
| --- | --- |
| From | ``` var inviter: String! { get } ``` |
| To | ``` var inviter: String { get } ``` |

Modified [GKInvite.sender](https://developer.apple.com/documentation/gamekit/gkinvite/1521073-sender)

|  | Declaration |
| --- | --- |
| From | ``` var sender: GKPlayer! { get } ``` |
| To | ``` var sender: GKPlayer { get } ``` |

Modified [GKInviteEventListener](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKInviteEventListener {     optional func player(_ player: GKPlayer!, didAcceptInvite invite: GKInvite!)     optional func player(_ player: GKPlayer!, didRequestMatchWithRecipients recipientPlayers: [AnyObject]!)     optional func player(_ player: GKPlayer!, didRequestMatchWithPlayers playerIDsToInvite: [AnyObject]!) } ``` |
| To | ``` protocol GKInviteEventListener {     optional func player(_ player: GKPlayer, didAcceptInvite invite: GKInvite)     optional func player(_ player: GKPlayer, didRequestMatchWithRecipients recipientPlayers: [GKPlayer])     optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String]) } ``` |

Modified [GKInviteEventListener.player(_: GKPlayer, didAcceptInvite: GKInvite)](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520672-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, didAcceptInvite invite: GKInvite!) ``` |
| To | ``` optional func player(_ player: GKPlayer, didAcceptInvite invite: GKInvite) ``` |

Modified [GKInviteEventListener.player(_: GKPlayer, didRequestMatchWithPlayers: [String])](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1623695-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, didRequestMatchWithPlayers playerIDsToInvite: [AnyObject]!) ``` |
| To | ``` optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String]) ``` |

Modified [GKInviteEventListener.player(_: GKPlayer, didRequestMatchWithRecipients: [GKPlayer])](https://developer.apple.com/documentation/gamekit/gkinviteeventlistener/1520894-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, didRequestMatchWithRecipients recipientPlayers: [AnyObject]!) ``` |
| To | ``` optional func player(_ player: GKPlayer, didRequestMatchWithRecipients recipientPlayers: [GKPlayer]) ``` |

Modified [GKInviteRecipientResponse [enum]](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse)

|  | Declaration | Raw Value Type |
| --- | --- | --- |
| From | ``` enum GKInviteRecipientResponse : Int {     case InviteRecipientResponseAccepted     case InviteRecipientResponseDeclined     case InviteRecipientResponseFailed     case InviteRecipientResponseIncompatible     case InviteRecipientResponseUnableToConnect     case InviteRecipientResponseNoAnswer } ``` | -- |
| To | ``` enum GKInviteRecipientResponse : Int {     case InviteRecipientResponseAccepted     case InviteRecipientResponseDeclined     case InviteRecipientResponseFailed     case InviteRecipientResponseIncompatible     case InviteRecipientResponseUnableToConnect     case InviteRecipientResponseNoAnswer     static var InviteeResponseAccepted: GKInviteRecipientResponse { get }     static var InviteeResponseDeclined: GKInviteRecipientResponse { get }     static var InviteeResponseFailed: GKInviteRecipientResponse { get }     static var InviteeResponseIncompatible: GKInviteRecipientResponse { get }     static var InviteeResponseUnableToConnect: GKInviteRecipientResponse { get }     static var InviteeResponseNoAnswer: GKInviteRecipientResponse { get } } ``` | Int |

Modified [GKLeaderboard](https://developer.apple.com/documentation/gamekit/gkleaderboard)

|  | Declaration |
| --- | --- |
| From | ``` class GKLeaderboard : NSObject {     var timeScope: GKLeaderboardTimeScope     var playerScope: GKLeaderboardPlayerScope     var identifier: String!     var title: String! { get }     var range: NSRange     var scores: [AnyObject]! { get }     var maxRange: Int { get }     var localPlayerScore: GKScore! { get }     var loading: Bool { get }     var groupIdentifier: String! { get }     init!()     init!(players players: [AnyObject]!)     func loadScoresWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     class func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) } extension GKLeaderboard {     var category: String!     init!(playerIDs playerIDs: [AnyObject]!)     class func loadCategoriesWithCompletionHandler(_ completionHandler: (([AnyObject]!, [AnyObject]!, NSError!) -> Void)!)     class func setDefaultLeaderboard(_ leaderboardIdentifier: String!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) } extension GKLeaderboard {     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage!, NSError!) -> Void)!) } ``` |
| To | ``` class GKLeaderboard : NSObject {     var timeScope: GKLeaderboardTimeScope     var playerScope: GKLeaderboardPlayerScope     var identifier: String?     var title: String? { get }     var range: NSRange     var scores: [GKScore]? { get }     var maxRange: Int { get }     var localPlayerScore: GKScore? { get }     var loading: Bool { get }     var groupIdentifier: String? { get }     init()     init(players players: [GKPlayer])     func loadScoresWithCompletionHandler(_ completionHandler: (([GKScore]?, NSError?) -> Void)?)     class func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([GKLeaderboard]?, NSError?) -> Void)?) } extension GKLeaderboard {     var category: String?     init?(playerIDs playerIDs: [String]?)     class func loadCategoriesWithCompletionHandler(_ completionHandler: (([String]?, [String]?, NSError?) -> Void)?)     class func setDefaultLeaderboard(_ leaderboardIdentifier: String?, withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKLeaderboard {     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?) } ``` |

Modified [GKLeaderboard.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503135-groupidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var groupIdentifier: String! { get } ``` |
| To | ``` var groupIdentifier: String? { get } ``` |

Modified [GKLeaderboard.identifier](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503141-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! ``` |
| To | ``` var identifier: String? ``` |

Modified [GKLeaderboard.init()](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503125-init)

|  | Declaration |
| --- | --- |
| From | ``` init!() ``` |
| To | ``` init() ``` |

Modified [GKLeaderboard.init(playerIDs: [String]?)](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503132-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(playerIDs playerIDs: [AnyObject]!) ``` |
| To | ``` init?(playerIDs playerIDs: [String]?) ``` |

Modified [GKLeaderboard.init(players: [GKPlayer])](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503149-initwithplayers)

|  | Declaration |
| --- | --- |
| From | ``` init!(players players: [AnyObject]!) ``` |
| To | ``` init(players players: [GKPlayer]) ``` |

Modified [GKLeaderboard.loadImageWithCompletionHandler(_: ((UIImage?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503161-loadimage)

|  | Declaration |
| --- | --- |
| From | ``` func loadImageWithCompletionHandler(_ completionHandler: ((UIImage!, NSError!) -> Void)!) ``` |
| To | ``` func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?) ``` |

Modified [GKLeaderboard.loadLeaderboardsWithCompletionHandler(_: (([GKLeaderboard]?, NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503128-loadleaderboardswithcompletionha)

|  | Declaration |
| --- | --- |
| From | ``` class func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` class func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([GKLeaderboard]?, NSError?) -> Void)?) ``` |

Modified [GKLeaderboard.loadScoresWithCompletionHandler(_: (([GKScore]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503160-loadscores)

|  | Declaration |
| --- | --- |
| From | ``` func loadScoresWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func loadScoresWithCompletionHandler(_ completionHandler: (([GKScore]?, NSError?) -> Void)?) ``` |

Modified [GKLeaderboard.localPlayerScore](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503151-localplayerscore)

|  | Declaration |
| --- | --- |
| From | ``` var localPlayerScore: GKScore! { get } ``` |
| To | ``` var localPlayerScore: GKScore? { get } ``` |

Modified [GKLeaderboard.scores](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503159-scores)

|  | Declaration |
| --- | --- |
| From | ``` var scores: [AnyObject]! { get } ``` |
| To | ``` var scores: [GKScore]? { get } ``` |

Modified [GKLeaderboard.title](https://developer.apple.com/documentation/gamekit/gkleaderboard/1503139-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String? { get } ``` |

Modified [GKLeaderboardPlayerScope [enum]](https://developer.apple.com/documentation/gamekit/gkleaderboardplayerscope)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKLeaderboardSet](https://developer.apple.com/documentation/gamekit/gkleaderboardset)

|  | Declaration |
| --- | --- |
| From | ``` class GKLeaderboardSet : NSObject, NSCoding, NSSecureCoding {     var title: String! { get }     var groupIdentifier: String! { get }     var identifier: String!     class func loadLeaderboardSetsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) } extension GKLeaderboardSet {     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage!, NSError!) -> Void)!) } ``` |
| To | ``` class GKLeaderboardSet : NSObject, NSCoding, NSSecureCoding {     var title: String { get }     var groupIdentifier: String? { get }     var identifier: String?     class func loadLeaderboardSetsWithCompletionHandler(_ completionHandler: (([GKLeaderboardSet]?, NSError?) -> Void)?)     func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([GKLeaderboard]?, NSError?) -> Void)?) } extension GKLeaderboardSet {     func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?) } ``` |

Modified [GKLeaderboardSet.groupIdentifier](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451800-groupidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var groupIdentifier: String! { get } ``` |
| To | ``` var groupIdentifier: String? { get } ``` |

Modified [GKLeaderboardSet.identifier](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451802-identifier)

|  | Declaration |
| --- | --- |
| From | ``` var identifier: String! ``` |
| To | ``` var identifier: String? ``` |

Modified [GKLeaderboardSet.loadImageWithCompletionHandler(_: ((UIImage?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451812-loadimage)

|  | Declaration |
| --- | --- |
| From | ``` func loadImageWithCompletionHandler(_ completionHandler: ((UIImage!, NSError!) -> Void)!) ``` |
| To | ``` func loadImageWithCompletionHandler(_ completionHandler: ((UIImage?, NSError?) -> Void)?) ``` |

Modified [GKLeaderboardSet.loadLeaderboardSetsWithCompletionHandler(_: (([GKLeaderboardSet]?, NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451798-loadleaderboardsets)

|  | Declaration |
| --- | --- |
| From | ``` class func loadLeaderboardSetsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` class func loadLeaderboardSetsWithCompletionHandler(_ completionHandler: (([GKLeaderboardSet]?, NSError?) -> Void)?) ``` |

Modified [GKLeaderboardSet.loadLeaderboardsWithCompletionHandler(_: (([GKLeaderboard]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451810-loadleaderboardswithcompletionha)

|  | Declaration |
| --- | --- |
| From | ``` func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func loadLeaderboardsWithCompletionHandler(_ completionHandler: (([GKLeaderboard]?, NSError?) -> Void)?) ``` |

Modified [GKLeaderboardSet.title](https://developer.apple.com/documentation/gamekit/gkleaderboardset/1451804-title)

|  | Declaration |
| --- | --- |
| From | ``` var title: String! { get } ``` |
| To | ``` var title: String { get } ``` |

Modified [GKLeaderboardTimeScope [enum]](https://developer.apple.com/documentation/gamekit/gkleaderboardtimescope)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKLocalPlayer](https://developer.apple.com/documentation/gamekit/gklocalplayer)

|  | Declaration |
| --- | --- |
| From | ``` class GKLocalPlayer : GKPlayer {     class func localPlayer() -> GKLocalPlayer!     var authenticated: Bool { get }     var underage: Bool { get }     var authenticateHandler: ((UIViewController!, NSError!) -> Void)!     func loadFriendPlayersWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String!, completionHandler completionHandler: ((NSError!) -> Void)!)     func loadDefaultLeaderboardIdentifierWithCompletionHandler(_ completionHandler: ((String!, NSError!) -> Void)!)     func generateIdentityVerificationSignatureWithCompletionHandler(_ completionHandler: ((NSURL!, NSData!, NSData!, UInt64, NSError!) -> Void)!) } extension GKLocalPlayer {     func registerListener(_ listener: GKLocalPlayerListener!)     func unregisterListener(_ listener: GKLocalPlayerListener!)     func unregisterAllListeners() } extension GKLocalPlayer {     func setDefaultLeaderboardCategoryID(_ categoryID: String!, completionHandler completionHandler: ((NSError!) -> Void)!)     func loadDefaultLeaderboardCategoryIDWithCompletionHandler(_ completionHandler: ((String!, NSError!) -> Void)!)     func loadFriendsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func authenticateWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     var friends: [AnyObject]! { get } } extension GKLocalPlayer : GKSavedGameListener, NSObjectProtocol {     func fetchSavedGamesWithCompletionHandler(_ handler: (([AnyObject]!, NSError!) -> Void)!)     func saveGameData(_ data: NSData!, withName name: String!, completionHandler handler: ((GKSavedGame!, NSError!) -> Void)!)     func deleteSavedGamesWithName(_ name: String!, completionHandler handler: ((NSError!) -> Void)!)     func resolveConflictingSavedGames(_ conflictingSavedGames: [AnyObject]!, withData data: NSData!, completionHandler handler: (([AnyObject]!, NSError!) -> Void)!) } ``` |
| To | ``` class GKLocalPlayer : GKPlayer {     class func localPlayer() -> GKLocalPlayer     var authenticated: Bool { get }     var underage: Bool { get }     var authenticateHandler: ((UIViewController?, NSError?) -> Void)?     func loadFriendPlayersWithCompletionHandler(_ completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String, completionHandler completionHandler: ((NSError?) -> Void)?)     func loadDefaultLeaderboardIdentifierWithCompletionHandler(_ completionHandler: ((String?, NSError?) -> Void)?)     func generateIdentityVerificationSignatureWithCompletionHandler(_ completionHandler: ((NSURL?, NSData?, NSData?, UInt64, NSError?) -> Void)?) } extension GKLocalPlayer {     func registerListener(_ listener: GKLocalPlayerListener)     func unregisterListener(_ listener: GKLocalPlayerListener)     func unregisterAllListeners() } extension GKLocalPlayer {     func setDefaultLeaderboardCategoryID(_ categoryID: String?, completionHandler completionHandler: ((NSError?) -> Void)?)     func loadDefaultLeaderboardCategoryIDWithCompletionHandler(_ completionHandler: ((String?, NSError?) -> Void)?)     func loadFriendsWithCompletionHandler(_ completionHandler: (([String]?, NSError?) -> Void)?)     func authenticateWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     var friends: [String]? { get } } extension GKLocalPlayer : GKSavedGameListener {     func fetchSavedGamesWithCompletionHandler(_ handler: (([GKSavedGame]?, NSError?) -> Void)?)     func saveGameData(_ data: NSData, withName name: String, completionHandler handler: ((GKSavedGame?, NSError?) -> Void)?)     func deleteSavedGamesWithName(_ name: String, completionHandler handler: ((NSError?) -> Void)?)     func resolveConflictingSavedGames(_ conflictingSavedGames: [GKSavedGame], withData data: NSData, completionHandler handler: (([GKSavedGame]?, NSError?) -> Void)?) } ``` |

Modified [GKLocalPlayer.authenticateHandler](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515399-authenticatehandler)

|  | Declaration |
| --- | --- |
| From | ``` var authenticateHandler: ((UIViewController!, NSError!) -> Void)! ``` |
| To | ``` var authenticateHandler: ((UIViewController?, NSError?) -> Void)? ``` |

Modified [GKLocalPlayer.deleteSavedGamesWithName(_: String, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520951-deletesavedgames)

|  | Declaration |
| --- | --- |
| From | ``` func deleteSavedGamesWithName(_ name: String!, completionHandler handler: ((NSError!) -> Void)!) ``` |
| To | ``` func deleteSavedGamesWithName(_ name: String, completionHandler handler: ((NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.fetchSavedGamesWithCompletionHandler(_: (([GKSavedGame]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521086-fetchsavedgameswithcompletionhan)

|  | Declaration |
| --- | --- |
| From | ``` func fetchSavedGamesWithCompletionHandler(_ handler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func fetchSavedGamesWithCompletionHandler(_ handler: (([GKSavedGame]?, NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.friends](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515405-friends)

|  | Declaration |
| --- | --- |
| From | ``` var friends: [AnyObject]! { get } ``` |
| To | ``` var friends: [String]? { get } ``` |

Modified [GKLocalPlayer.generateIdentityVerificationSignatureWithCompletionHandler(_: ((NSURL?, NSData?, NSData?, UInt64, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515407-generateidentityverificationsign)

|  | Declaration |
| --- | --- |
| From | ``` func generateIdentityVerificationSignatureWithCompletionHandler(_ completionHandler: ((NSURL!, NSData!, NSData!, UInt64, NSError!) -> Void)!) ``` |
| To | ``` func generateIdentityVerificationSignatureWithCompletionHandler(_ completionHandler: ((NSURL?, NSData?, NSData?, UInt64, NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.loadDefaultLeaderboardIdentifierWithCompletionHandler(_: ((String?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515404-loaddefaultleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func loadDefaultLeaderboardIdentifierWithCompletionHandler(_ completionHandler: ((String!, NSError!) -> Void)!) ``` |
| To | ``` func loadDefaultLeaderboardIdentifierWithCompletionHandler(_ completionHandler: ((String?, NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.loadFriendPlayersWithCompletionHandler(_: (([GKPlayer]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515386-loadfriendplayerswithcompletionh)

|  | Declaration |
| --- | --- |
| From | ``` func loadFriendPlayersWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func loadFriendPlayersWithCompletionHandler(_ completionHandler: (([GKPlayer]?, NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.loadFriendsWithCompletionHandler(_: (([String]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515391-loadfriendswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func loadFriendsWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func loadFriendsWithCompletionHandler(_ completionHandler: (([String]?, NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.localPlayer() -> GKLocalPlayer [class]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515401-localplayer)

|  | Declaration |
| --- | --- |
| From | ``` class func localPlayer() -> GKLocalPlayer! ``` |
| To | ``` class func localPlayer() -> GKLocalPlayer ``` |

Modified [GKLocalPlayer.registerListener(_: GKLocalPlayerListener)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515393-register)

|  | Declaration |
| --- | --- |
| From | ``` func registerListener(_ listener: GKLocalPlayerListener!) ``` |
| To | ``` func registerListener(_ listener: GKLocalPlayerListener) ``` |

Modified [GKLocalPlayer.resolveConflictingSavedGames(_: [GKSavedGame], withData: NSData, completionHandler: (([GKSavedGame]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1521116-resolveconflictingsavedgames)

|  | Declaration |
| --- | --- |
| From | ``` func resolveConflictingSavedGames(_ conflictingSavedGames: [AnyObject]!, withData data: NSData!, completionHandler handler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func resolveConflictingSavedGames(_ conflictingSavedGames: [GKSavedGame], withData data: NSData, completionHandler handler: (([GKSavedGame]?, NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.saveGameData(_: NSData, withName: String, completionHandler: ((GKSavedGame?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1520527-savegamedata)

|  | Declaration |
| --- | --- |
| From | ``` func saveGameData(_ data: NSData!, withName name: String!, completionHandler handler: ((GKSavedGame!, NSError!) -> Void)!) ``` |
| To | ``` func saveGameData(_ data: NSData, withName name: String, completionHandler handler: ((GKSavedGame?, NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.setDefaultLeaderboardIdentifier(_: String, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515408-setdefaultleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func setDefaultLeaderboardIdentifier(_ leaderboardIdentifier: String, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKLocalPlayer.unregisterListener(_: GKLocalPlayerListener)](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515389-unregisterlistener)

|  | Declaration |
| --- | --- |
| From | ``` func unregisterListener(_ listener: GKLocalPlayerListener!) ``` |
| To | ``` func unregisterListener(_ listener: GKLocalPlayerListener) ``` |

Modified [GKMatch](https://developer.apple.com/documentation/gamekit/gkmatch)

|  | Declaration |
| --- | --- |
| From | ``` class GKMatch : NSObject {     var players: [AnyObject]! { get }     unowned(unsafe) var delegate: GKMatchDelegate!     var expectedPlayerCount: Int { get }     func sendData(_ data: NSData!, toPlayers players: [AnyObject]!, dataMode mode: GKMatchSendDataMode, error error: NSErrorPointer) -> Bool     func sendDataToAllPlayers(_ data: NSData!, withDataMode mode: GKMatchSendDataMode, error error: NSErrorPointer) -> Bool     func disconnect()     func voiceChatWithName(_ name: String!) -> GKVoiceChat!     func chooseBestHostingPlayerWithCompletionHandler(_ completionHandler: ((GKPlayer!) -> Void)!)     func rematchWithCompletionHandler(_ completionHandler: ((GKMatch!, NSError!) -> Void)!) } extension GKMatch {     func chooseBestHostPlayerWithCompletionHandler(_ completionHandler: ((String!) -> Void)!)     func sendData(_ data: NSData!, toPlayers playerIDs: [AnyObject]!, withDataMode mode: GKMatchSendDataMode, error error: NSErrorPointer) -> Bool     var playerIDs: [AnyObject]! { get } } ``` |
| To | ``` class GKMatch : NSObject {     var players: [GKPlayer] { get }     unowned(unsafe) var delegate: GKMatchDelegate?     var expectedPlayerCount: Int { get }     func sendData(_ data: NSData, toPlayers players: [GKPlayer], dataMode mode: GKMatchSendDataMode) throws     func sendDataToAllPlayers(_ data: NSData, withDataMode mode: GKMatchSendDataMode) throws     func disconnect()     func voiceChatWithName(_ name: String) -> GKVoiceChat?     func chooseBestHostingPlayerWithCompletionHandler(_ completionHandler: (GKPlayer?) -> Void)     func rematchWithCompletionHandler(_ completionHandler: ((GKMatch?, NSError?) -> Void)?) } extension GKMatch {     func chooseBestHostPlayerWithCompletionHandler(_ completionHandler: (String?) -> Void)     func sendData(_ data: NSData, toPlayers playerIDs: [String], withDataMode mode: GKMatchSendDataMode) throws     var playerIDs: [String] { get } } ``` |

Modified [GKMatch.chooseBestHostingPlayerWithCompletionHandler(_: (GKPlayer?) -> Void)](https://developer.apple.com/documentation/gamekit/gkmatch/1502072-choosebesthostingplayerwithcompl)

|  | Declaration |
| --- | --- |
| From | ``` func chooseBestHostingPlayerWithCompletionHandler(_ completionHandler: ((GKPlayer!) -> Void)!) ``` |
| To | ``` func chooseBestHostingPlayerWithCompletionHandler(_ completionHandler: (GKPlayer?) -> Void) ``` |

Modified [GKMatch.chooseBestHostPlayerWithCompletionHandler(_: (String?) -> Void)](https://developer.apple.com/documentation/gamekit/gkmatch/1502044-choosebesthostplayerwithcompleti)

|  | Declaration |
| --- | --- |
| From | ``` func chooseBestHostPlayerWithCompletionHandler(_ completionHandler: ((String!) -> Void)!) ``` |
| To | ``` func chooseBestHostPlayerWithCompletionHandler(_ completionHandler: (String?) -> Void) ``` |

Modified [GKMatch.delegate](https://developer.apple.com/documentation/gamekit/gkmatch/1502046-delegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var delegate: GKMatchDelegate! ``` |
| To | ``` unowned(unsafe) var delegate: GKMatchDelegate? ``` |

Modified [GKMatch.playerIDs](https://developer.apple.com/documentation/gamekit/gkmatch/1502064-playerids)

|  | Declaration |
| --- | --- |
| From | ``` var playerIDs: [AnyObject]! { get } ``` |
| To | ``` var playerIDs: [String] { get } ``` |

Modified [GKMatch.players](https://developer.apple.com/documentation/gamekit/gkmatch/1502074-players)

|  | Declaration |
| --- | --- |
| From | ``` var players: [AnyObject]! { get } ``` |
| To | ``` var players: [GKPlayer] { get } ``` |

Modified [GKMatch.rematchWithCompletionHandler(_: ((GKMatch?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatch/1502042-rematch)

|  | Declaration |
| --- | --- |
| From | ``` func rematchWithCompletionHandler(_ completionHandler: ((GKMatch!, NSError!) -> Void)!) ``` |
| To | ``` func rematchWithCompletionHandler(_ completionHandler: ((GKMatch?, NSError?) -> Void)?) ``` |

Modified [GKMatch.sendData(_: NSData, toPlayers: [GKPlayer], dataMode: GKMatchSendDataMode) throws](https://developer.apple.com/documentation/gamekit/gkmatch/1502056-senddata)

|  | Declaration |
| --- | --- |
| From | ``` func sendData(_ data: NSData!, toPlayers players: [AnyObject]!, dataMode mode: GKMatchSendDataMode, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func sendData(_ data: NSData, toPlayers players: [GKPlayer], dataMode mode: GKMatchSendDataMode) throws ``` |

Modified [GKMatch.sendData(_: NSData, toPlayers: [String], withDataMode: GKMatchSendDataMode) throws](https://developer.apple.com/documentation/gamekit/gkmatch/1502033-send)

|  | Declaration |
| --- | --- |
| From | ``` func sendData(_ data: NSData!, toPlayers playerIDs: [AnyObject]!, withDataMode mode: GKMatchSendDataMode, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func sendData(_ data: NSData, toPlayers playerIDs: [String], withDataMode mode: GKMatchSendDataMode) throws ``` |

Modified [GKMatch.sendDataToAllPlayers(_: NSData, withDataMode: GKMatchSendDataMode) throws](https://developer.apple.com/documentation/gamekit/gkmatch/1502029-senddata)

|  | Declaration |
| --- | --- |
| From | ``` func sendDataToAllPlayers(_ data: NSData!, withDataMode mode: GKMatchSendDataMode, error error: NSErrorPointer) -> Bool ``` |
| To | ``` func sendDataToAllPlayers(_ data: NSData, withDataMode mode: GKMatchSendDataMode) throws ``` |

Modified [GKMatch.voiceChatWithName(_: String) -> GKVoiceChat?](https://developer.apple.com/documentation/gamekit/gkmatch/1502066-voicechatwithname)

|  | Declaration |
| --- | --- |
| From | ``` func voiceChatWithName(_ name: String!) -> GKVoiceChat! ``` |
| To | ``` func voiceChatWithName(_ name: String) -> GKVoiceChat? ``` |

Modified [GKMatchDelegate](https://developer.apple.com/documentation/gamekit/gkmatchdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKMatchDelegate : NSObjectProtocol {     optional func match(_ match: GKMatch!, didReceiveData data: NSData!, fromRemotePlayer player: GKPlayer!)     optional func match(_ match: GKMatch!, didReceiveData data: NSData!, fromPlayer playerID: String!)     optional func match(_ match: GKMatch!, player player: GKPlayer!, didChangeConnectionState state: GKPlayerConnectionState)     optional func match(_ match: GKMatch!, player playerID: String!, didChangeState state: GKPlayerConnectionState)     optional func match(_ match: GKMatch!, didFailWithError error: NSError!)     optional func match(_ match: GKMatch!, shouldReinviteDisconnectedPlayer player: GKPlayer!) -> Bool     optional func match(_ match: GKMatch!, shouldReinvitePlayer playerID: String!) -> Bool } ``` |
| To | ``` protocol GKMatchDelegate : NSObjectProtocol {     optional func match(_ match: GKMatch, didReceiveData data: NSData, fromRemotePlayer player: GKPlayer)     optional func match(_ match: GKMatch, didReceiveData data: NSData, forRecipient recipient: GKPlayer, fromRemotePlayer player: GKPlayer)     optional func match(_ match: GKMatch, didReceiveData data: NSData, fromPlayer playerID: String)     optional func match(_ match: GKMatch, player player: GKPlayer, didChangeConnectionState state: GKPlayerConnectionState)     optional func match(_ match: GKMatch, player playerID: String, didChangeState state: GKPlayerConnectionState)     optional func match(_ match: GKMatch, didFailWithError error: NSError?)     optional func match(_ match: GKMatch, shouldReinviteDisconnectedPlayer player: GKPlayer) -> Bool     optional func match(_ match: GKMatch, shouldReinvitePlayer playerID: String) -> Bool } ``` |

Modified [GKMatchDelegate.match(_: GKMatch, didFailWithError: NSError?)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502025-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch!, didFailWithError error: NSError!) ``` |
| To | ``` optional func match(_ match: GKMatch, didFailWithError error: NSError?) ``` |

Modified [GKMatchDelegate.match(_: GKMatch, didReceiveData: NSData, fromPlayer: String)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502054-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch!, didReceiveData data: NSData!, fromPlayer playerID: String!) ``` |
| To | ``` optional func match(_ match: GKMatch, didReceiveData data: NSData, fromPlayer playerID: String) ``` |

Modified [GKMatchDelegate.match(_: GKMatch, didReceiveData: NSData, fromRemotePlayer: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502069-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch!, didReceiveData data: NSData!, fromRemotePlayer player: GKPlayer!) ``` |
| To | ``` optional func match(_ match: GKMatch, didReceiveData data: NSData, fromRemotePlayer player: GKPlayer) ``` |

Modified [GKMatchDelegate.match(_: GKMatch, player: GKPlayer, didChangeConnectionState: GKPlayerConnectionState)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502048-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch!, player player: GKPlayer!, didChangeConnectionState state: GKPlayerConnectionState) ``` |
| To | ``` optional func match(_ match: GKMatch, player player: GKPlayer, didChangeConnectionState state: GKPlayerConnectionState) ``` |

Modified [GKMatchDelegate.match(_: GKMatch, player: String, didChangeState: GKPlayerConnectionState)](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502028-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch!, player playerID: String!, didChangeState state: GKPlayerConnectionState) ``` |
| To | ``` optional func match(_ match: GKMatch, player playerID: String, didChangeState state: GKPlayerConnectionState) ``` |

Modified [GKMatchDelegate.match(_: GKMatch, shouldReinviteDisconnectedPlayer: GKPlayer) -> Bool](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502038-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch!, shouldReinviteDisconnectedPlayer player: GKPlayer!) -> Bool ``` |
| To | ``` optional func match(_ match: GKMatch, shouldReinviteDisconnectedPlayer player: GKPlayer) -> Bool ``` |

Modified [GKMatchDelegate.match(_: GKMatch, shouldReinvitePlayer: String) -> Bool](https://developer.apple.com/documentation/gamekit/gkmatchdelegate/1502058-match)

|  | Declaration |
| --- | --- |
| From | ``` optional func match(_ match: GKMatch!, shouldReinvitePlayer playerID: String!) -> Bool ``` |
| To | ``` optional func match(_ match: GKMatch, shouldReinvitePlayer playerID: String) -> Bool ``` |

Modified [GKMatchmaker](https://developer.apple.com/documentation/gamekit/gkmatchmaker)

|  | Declaration |
| --- | --- |
| From | ``` class GKMatchmaker : NSObject {     class func sharedMatchmaker() -> GKMatchmaker!     func matchForInvite(_ invite: GKInvite!, completionHandler completionHandler: ((GKMatch!, NSError!) -> Void)!)     func findMatchForRequest(_ request: GKMatchRequest!, withCompletionHandler completionHandler: ((GKMatch!, NSError!) -> Void)!)     func findPlayersForHostedRequest(_ request: GKMatchRequest!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!)     func addPlayersToMatch(_ match: GKMatch!, matchRequest matchRequest: GKMatchRequest!, completionHandler completionHandler: ((NSError!) -> Void)!)     func cancel()     func cancelPendingInviteToPlayer(_ player: GKPlayer!)     func finishMatchmakingForMatch(_ match: GKMatch!)     func queryPlayerGroupActivity(_ playerGroup: Int, withCompletionHandler completionHandler: ((Int, NSError!) -> Void)!)     func queryActivityWithCompletionHandler(_ completionHandler: ((Int, NSError!) -> Void)!)     func startBrowsingForNearbyPlayersWithHandler(_ reachableHandler: ((GKPlayer!, Bool) -> Void)!)     func stopBrowsingForNearbyPlayers() } extension GKMatchmaker {     var inviteHandler: ((GKInvite!, [AnyObject]!) -> Void)!     func startBrowsingForNearbyPlayersWithReachableHandler(_ reachableHandler: ((String!, Bool) -> Void)!)     func cancelInviteToPlayer(_ playerID: String!)     func findPlayersForHostedMatchRequest(_ request: GKMatchRequest!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!) } ``` |
| To | ``` class GKMatchmaker : NSObject {     class func sharedMatchmaker() -> GKMatchmaker     func matchForInvite(_ invite: GKInvite, completionHandler completionHandler: ((GKMatch?, NSError?) -> Void)?)     func findMatchForRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: ((GKMatch?, NSError?) -> Void)?)     func findPlayersForHostedRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     func addPlayersToMatch(_ match: GKMatch, matchRequest matchRequest: GKMatchRequest, completionHandler completionHandler: ((NSError?) -> Void)?)     func cancel()     func cancelPendingInviteToPlayer(_ player: GKPlayer)     func finishMatchmakingForMatch(_ match: GKMatch)     func queryPlayerGroupActivity(_ playerGroup: Int, withCompletionHandler completionHandler: ((Int, NSError?) -> Void)?)     func queryActivityWithCompletionHandler(_ completionHandler: ((Int, NSError?) -> Void)?)     func startBrowsingForNearbyPlayersWithHandler(_ reachableHandler: ((GKPlayer, Bool) -> Void)?)     func stopBrowsingForNearbyPlayers() } extension GKMatchmaker {     var inviteHandler: ((GKInvite, [AnyObject]?) -> Void)?     func startBrowsingForNearbyPlayersWithReachableHandler(_ reachableHandler: ((String, Bool) -> Void)?)     func cancelInviteToPlayer(_ playerID: String)     func findPlayersForHostedMatchRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (([String]?, NSError?) -> Void)?) } ``` |

Modified [GKMatchmaker.addPlayersToMatch(_: GKMatch, matchRequest: GKMatchRequest, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520561-addplayerstomatch)

|  | Declaration |
| --- | --- |
| From | ``` func addPlayersToMatch(_ match: GKMatch!, matchRequest matchRequest: GKMatchRequest!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func addPlayersToMatch(_ match: GKMatch, matchRequest matchRequest: GKMatchRequest, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKMatchmaker.cancelInviteToPlayer(_: String)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520576-cancelinvite)

|  | Declaration |
| --- | --- |
| From | ``` func cancelInviteToPlayer(_ playerID: String!) ``` |
| To | ``` func cancelInviteToPlayer(_ playerID: String) ``` |

Modified [GKMatchmaker.cancelPendingInviteToPlayer(_: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520773-cancelpendinginvitetoplayer)

|  | Declaration |
| --- | --- |
| From | ``` func cancelPendingInviteToPlayer(_ player: GKPlayer!) ``` |
| To | ``` func cancelPendingInviteToPlayer(_ player: GKPlayer) ``` |

Modified [GKMatchmaker.findMatchForRequest(_: GKMatchRequest, withCompletionHandler: ((GKMatch?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520777-findmatch)

|  | Declaration |
| --- | --- |
| From | ``` func findMatchForRequest(_ request: GKMatchRequest!, withCompletionHandler completionHandler: ((GKMatch!, NSError!) -> Void)!) ``` |
| To | ``` func findMatchForRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: ((GKMatch?, NSError?) -> Void)?) ``` |

Modified [GKMatchmaker.findPlayersForHostedMatchRequest(_: GKMatchRequest, withCompletionHandler: (([String]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520915-findplayersforhostedmatchrequest)

|  | Declaration |
| --- | --- |
| From | ``` func findPlayersForHostedMatchRequest(_ request: GKMatchRequest!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func findPlayersForHostedMatchRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (([String]?, NSError?) -> Void)?) ``` |

Modified [GKMatchmaker.findPlayersForHostedRequest(_: GKMatchRequest, withCompletionHandler: (([GKPlayer]?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520973-findplayersforhostedrequest)

|  | Declaration |
| --- | --- |
| From | ``` func findPlayersForHostedRequest(_ request: GKMatchRequest!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` func findPlayersForHostedRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?) ``` |

Modified [GKMatchmaker.finishMatchmakingForMatch(_: GKMatch)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520518-finishmatchmaking)

|  | Declaration |
| --- | --- |
| From | ``` func finishMatchmakingForMatch(_ match: GKMatch!) ``` |
| To | ``` func finishMatchmakingForMatch(_ match: GKMatch) ``` |

Modified [GKMatchmaker.matchForInvite(_: GKInvite, completionHandler: ((GKMatch?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520847-match)

|  | Declaration |
| --- | --- |
| From | ``` func matchForInvite(_ invite: GKInvite!, completionHandler completionHandler: ((GKMatch!, NSError!) -> Void)!) ``` |
| To | ``` func matchForInvite(_ invite: GKInvite, completionHandler completionHandler: ((GKMatch?, NSError?) -> Void)?) ``` |

Modified [GKMatchmaker.queryActivityWithCompletionHandler(_: ((Int, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520930-queryactivitywithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func queryActivityWithCompletionHandler(_ completionHandler: ((Int, NSError!) -> Void)!) ``` |
| To | ``` func queryActivityWithCompletionHandler(_ completionHandler: ((Int, NSError?) -> Void)?) ``` |

Modified [GKMatchmaker.queryPlayerGroupActivity(_: Int, withCompletionHandler: ((Int, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521189-queryplayergroupactivity)

|  | Declaration |
| --- | --- |
| From | ``` func queryPlayerGroupActivity(_ playerGroup: Int, withCompletionHandler completionHandler: ((Int, NSError!) -> Void)!) ``` |
| To | ``` func queryPlayerGroupActivity(_ playerGroup: Int, withCompletionHandler completionHandler: ((Int, NSError?) -> Void)?) ``` |

Modified [GKMatchmaker.sharedMatchmaker() -> GKMatchmaker [class]](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1520781-shared)

|  | Declaration |
| --- | --- |
| From | ``` class func sharedMatchmaker() -> GKMatchmaker! ``` |
| To | ``` class func sharedMatchmaker() -> GKMatchmaker ``` |

Modified [GKMatchmaker.startBrowsingForNearbyPlayersWithHandler(_: ((GKPlayer, Bool) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521043-startbrowsingfornearbyplayers)

|  | Declaration |
| --- | --- |
| From | ``` func startBrowsingForNearbyPlayersWithHandler(_ reachableHandler: ((GKPlayer!, Bool) -> Void)!) ``` |
| To | ``` func startBrowsingForNearbyPlayersWithHandler(_ reachableHandler: ((GKPlayer, Bool) -> Void)?) ``` |

Modified [GKMatchmaker.startBrowsingForNearbyPlayersWithReachableHandler(_: ((String, Bool) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkmatchmaker/1521023-startbrowsingfornearbyplayerswit)

|  | Declaration |
| --- | --- |
| From | ``` func startBrowsingForNearbyPlayersWithReachableHandler(_ reachableHandler: ((String!, Bool) -> Void)!) ``` |
| To | ``` func startBrowsingForNearbyPlayersWithReachableHandler(_ reachableHandler: ((String, Bool) -> Void)?) ``` |

Modified [GKMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GKMatchmakerViewController : UINavigationController {     unowned(unsafe) var matchmakerDelegate: GKMatchmakerViewControllerDelegate!     var matchRequest: GKMatchRequest! { get }     var hosted: Bool     init!(matchRequest request: GKMatchRequest!)     init!(invite invite: GKInvite!)     func addPlayersToMatch(_ match: GKMatch!)     func setHostedPlayer(_ playerID: String!, connected connected: Bool)     func setHostedPlayer(_ player: GKPlayer!, didConnect connected: Bool)     func setHostedPlayerReady(_ playerID: String!)     var defaultInvitationMessage: String! } ``` |
| To | ``` class GKMatchmakerViewController : UINavigationController {     unowned(unsafe) var matchmakerDelegate: GKMatchmakerViewControllerDelegate?     var matchRequest: GKMatchRequest { get }     var hosted: Bool     init?(matchRequest request: GKMatchRequest)     init?(invite invite: GKInvite)     func addPlayersToMatch(_ match: GKMatch)     func setHostedPlayer(_ playerID: String, connected connected: Bool)     func setHostedPlayer(_ player: GKPlayer, didConnect connected: Bool)     func setHostedPlayerReady(_ playerID: String)     var defaultInvitationMessage: String? } ``` |

Modified [GKMatchmakerViewController.addPlayersToMatch(_: GKMatch)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492425-addplayerstomatch)

|  | Declaration |
| --- | --- |
| From | ``` func addPlayersToMatch(_ match: GKMatch!) ``` |
| To | ``` func addPlayersToMatch(_ match: GKMatch) ``` |

Modified [GKMatchmakerViewController.init(invite: GKInvite)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492434-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(invite invite: GKInvite!) ``` |
| To | ``` init?(invite invite: GKInvite) ``` |

Modified [GKMatchmakerViewController.init(matchRequest: GKMatchRequest)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492423-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(matchRequest request: GKMatchRequest!) ``` |
| To | ``` init?(matchRequest request: GKMatchRequest) ``` |

Modified [GKMatchmakerViewController.matchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492426-matchmakerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var matchmakerDelegate: GKMatchmakerViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var matchmakerDelegate: GKMatchmakerViewControllerDelegate? ``` |

Modified [GKMatchmakerViewController.matchRequest](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492410-matchrequest)

|  | Declaration |
| --- | --- |
| From | ``` var matchRequest: GKMatchRequest! { get } ``` |
| To | ``` var matchRequest: GKMatchRequest { get } ``` |

Modified [GKMatchmakerViewController.setHostedPlayer(_: String, connected: Bool)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492418-sethostedplayer)

|  | Declaration |
| --- | --- |
| From | ``` func setHostedPlayer(_ playerID: String!, connected connected: Bool) ``` |
| To | ``` func setHostedPlayer(_ playerID: String, connected connected: Bool) ``` |

Modified [GKMatchmakerViewController.setHostedPlayer(_: GKPlayer, didConnect: Bool)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller/1492406-sethostedplayer)

|  | Declaration |
| --- | --- |
| From | ``` func setHostedPlayer(_ player: GKPlayer!, didConnect connected: Bool) ``` |
| To | ``` func setHostedPlayer(_ player: GKPlayer, didConnect connected: Bool) ``` |

Modified [GKMatchmakerViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKMatchmakerViewControllerDelegate : NSObjectProtocol {     func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController!)     func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didFailWithError error: NSError!)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didFindMatch match: GKMatch!)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didFindHostedPlayers players: [AnyObject]!)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didFindPlayers playerIDs: [AnyObject]!)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, hostedPlayerDidAccept player: GKPlayer!)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didReceiveAcceptFromHostedPlayer playerID: String!) } ``` |
| To | ``` protocol GKMatchmakerViewControllerDelegate : NSObjectProtocol {     func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController)     func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFailWithError error: NSError)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindMatch match: GKMatch)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindHostedPlayers players: [GKPlayer])     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindPlayers playerIDs: [String])     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, hostedPlayerDidAccept player: GKPlayer)     optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer playerID: String) } ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewController(_: GKMatchmakerViewController, didFailWithError: NSError)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492419-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didFailWithError error: NSError!) ``` |
| To | ``` func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFailWithError error: NSError) ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewController(_: GKMatchmakerViewController, didFindHostedPlayers: [GKPlayer])](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492421-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didFindHostedPlayers players: [AnyObject]!) ``` |
| To | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindHostedPlayers players: [GKPlayer]) ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewController(_: GKMatchmakerViewController, didFindMatch: GKMatch)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492416-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didFindMatch match: GKMatch!) ``` |
| To | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindMatch match: GKMatch) ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewController(_: GKMatchmakerViewController, didFindPlayers: [String])](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492428-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didFindPlayers playerIDs: [AnyObject]!) ``` |
| To | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didFindPlayers playerIDs: [String]) ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewController(_: GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer: String)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492436-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, didReceiveAcceptFromHostedPlayer playerID: String!) ``` |
| To | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, didReceiveAcceptFromHostedPlayer playerID: String) ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewController(_: GKMatchmakerViewController, hostedPlayerDidAccept: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492412-matchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController!, hostedPlayerDidAccept player: GKPlayer!) ``` |
| To | ``` optional func matchmakerViewController(_ viewController: GKMatchmakerViewController, hostedPlayerDidAccept player: GKPlayer) ``` |

Modified [GKMatchmakerViewControllerDelegate.matchmakerViewControllerWasCancelled(_: GKMatchmakerViewController)](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontrollerdelegate/1492432-matchmakerviewcontrollerwascance)

|  | Declaration |
| --- | --- |
| From | ``` func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController!) ``` |
| To | ``` func matchmakerViewControllerWasCancelled(_ viewController: GKMatchmakerViewController) ``` |

Modified [GKMatchRequest](https://developer.apple.com/documentation/gamekit/gkmatchrequest)

|  | Declaration |
| --- | --- |
| From | ``` class GKMatchRequest : NSObject {     var minPlayers: Int     var maxPlayers: Int     var playerGroup: Int     var playerAttributes: UInt32     var recipients: [AnyObject]!     var playersToInvite: [AnyObject]!     var inviteMessage: String!     var defaultNumberOfPlayers: Int     var recipientResponseHandler: ((GKPlayer!, GKInviteRecipientResponse) -> Void)!     var inviteeResponseHandler: ((String!, GKInviteeResponse) -> Void)!     class func maxPlayersAllowedForMatchOfType(_ matchType: GKMatchType) -> Int } ``` |
| To | ``` class GKMatchRequest : NSObject {     var minPlayers: Int     var maxPlayers: Int     var playerGroup: Int     var playerAttributes: UInt32     var recipients: [GKPlayer]?     var playersToInvite: [String]?     var inviteMessage: String?     var defaultNumberOfPlayers: Int     var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Void)?     var inviteeResponseHandler: ((String, GKInviteeResponse) -> Void)?     class func maxPlayersAllowedForMatchOfType(_ matchType: GKMatchType) -> Int } ``` |

Modified [GKMatchRequest.inviteeResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520511-inviteeresponsehandler)

|  | Declaration |
| --- | --- |
| From | ``` var inviteeResponseHandler: ((String!, GKInviteeResponse) -> Void)! ``` |
| To | ``` var inviteeResponseHandler: ((String, GKInviteeResponse) -> Void)? ``` |

Modified [GKMatchRequest.inviteMessage](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521164-invitemessage)

|  | Declaration |
| --- | --- |
| From | ``` var inviteMessage: String! ``` |
| To | ``` var inviteMessage: String? ``` |

Modified [GKMatchRequest.playersToInvite](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520921-playerstoinvite)

|  | Declaration |
| --- | --- |
| From | ``` var playersToInvite: [AnyObject]! ``` |
| To | ``` var playersToInvite: [String]? ``` |

Modified [GKMatchRequest.recipientResponseHandler](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1521004-recipientresponsehandler)

|  | Declaration |
| --- | --- |
| From | ``` var recipientResponseHandler: ((GKPlayer!, GKInviteRecipientResponse) -> Void)! ``` |
| To | ``` var recipientResponseHandler: ((GKPlayer, GKInviteRecipientResponse) -> Void)? ``` |

Modified [GKMatchRequest.recipients](https://developer.apple.com/documentation/gamekit/gkmatchrequest/1520800-recipients)

|  | Declaration |
| --- | --- |
| From | ``` var recipients: [AnyObject]! ``` |
| To | ``` var recipients: [GKPlayer]? ``` |

Modified [GKMatchSendDataMode [enum]](https://developer.apple.com/documentation/gamekit/gkmatchsenddatamode)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKMatchType [enum]](https://developer.apple.com/documentation/gamekit/gkmatchtype)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | UInt |

Modified [GKNotificationBanner](https://developer.apple.com/documentation/gamekit/gknotificationbanner)

|  | Declaration |
| --- | --- |
| From | ``` class GKNotificationBanner : NSObject {     class func showBannerWithTitle(_ title: String!, message message: String!, completionHandler completionHandler: (() -> Void)!)     class func showBannerWithTitle(_ title: String!, message message: String!, duration duration: NSTimeInterval, completionHandler completionHandler: (() -> Void)!) } ``` |
| To | ``` class GKNotificationBanner : NSObject {     class func showBannerWithTitle(_ title: String?, message message: String?, completionHandler completionHandler: (() -> Void)?)     class func showBannerWithTitle(_ title: String?, message message: String?, duration duration: NSTimeInterval, completionHandler completionHandler: (() -> Void)?) } ``` |

Modified [GKNotificationBanner.showBannerWithTitle(_: String?, message: String?, completionHandler: (() -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515370-showbannerwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` class func showBannerWithTitle(_ title: String!, message message: String!, completionHandler completionHandler: (() -> Void)!) ``` |
| To | ``` class func showBannerWithTitle(_ title: String?, message message: String?, completionHandler completionHandler: (() -> Void)?) ``` |

Modified [GKNotificationBanner.showBannerWithTitle(_: String?, message: String?, duration: NSTimeInterval, completionHandler: (() -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gknotificationbanner/1515368-showbannerwithtitle)

|  | Declaration |
| --- | --- |
| From | ``` class func showBannerWithTitle(_ title: String!, message message: String!, duration duration: NSTimeInterval, completionHandler completionHandler: (() -> Void)!) ``` |
| To | ``` class func showBannerWithTitle(_ title: String?, message message: String?, duration duration: NSTimeInterval, completionHandler completionHandler: (() -> Void)?) ``` |

Modified [GKPeerPickerControllerDelegate](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKPeerPickerControllerDelegate : NSObjectProtocol {     optional func peerPickerController(_ picker: GKPeerPickerController!, didSelectConnectionType type: GKPeerPickerConnectionType)     optional func peerPickerController(_ picker: GKPeerPickerController!, sessionForConnectionType type: GKPeerPickerConnectionType) -> GKSession!     optional func peerPickerController(_ picker: GKPeerPickerController!, didConnectPeer peerID: String!, toSession session: GKSession!)     optional func peerPickerControllerDidCancel(_ picker: GKPeerPickerController!) } ``` |
| To | ``` protocol GKPeerPickerControllerDelegate : NSObjectProtocol {     optional func peerPickerController(_ picker: GKPeerPickerController, didSelectConnectionType type: GKPeerPickerConnectionType)     optional func peerPickerController(_ picker: GKPeerPickerController, sessionForConnectionType type: GKPeerPickerConnectionType) -> GKSession     optional func peerPickerController(_ picker: GKPeerPickerController, didConnectPeer peerID: String, toSession session: GKSession)     optional func peerPickerControllerDidCancel(_ picker: GKPeerPickerController) } ``` |

Modified [GKPeerPickerControllerDelegate.peerPickerController(_: GKPeerPickerController, didConnectPeer: String, toSession: GKSession)](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/1622153-peerpickercontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peerPickerController(_ picker: GKPeerPickerController!, didConnectPeer peerID: String!, toSession session: GKSession!) ``` | iOS 8.0 |
| To | ``` optional func peerPickerController(_ picker: GKPeerPickerController, didConnectPeer peerID: String, toSession session: GKSession) ``` | iOS 3.0 |

Modified [GKPeerPickerControllerDelegate.peerPickerController(_: GKPeerPickerController, didSelectConnectionType: GKPeerPickerConnectionType)](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/1622163-peerpickercontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peerPickerController(_ picker: GKPeerPickerController!, didSelectConnectionType type: GKPeerPickerConnectionType) ``` | iOS 8.0 |
| To | ``` optional func peerPickerController(_ picker: GKPeerPickerController, didSelectConnectionType type: GKPeerPickerConnectionType) ``` | iOS 3.0 |

Modified [GKPeerPickerControllerDelegate.peerPickerController(_: GKPeerPickerController, sessionForConnectionType: GKPeerPickerConnectionType) -> GKSession](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/1622156-peerpickercontroller)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peerPickerController(_ picker: GKPeerPickerController!, sessionForConnectionType type: GKPeerPickerConnectionType) -> GKSession! ``` | iOS 8.0 |
| To | ``` optional func peerPickerController(_ picker: GKPeerPickerController, sessionForConnectionType type: GKPeerPickerConnectionType) -> GKSession ``` | iOS 3.0 |

Modified [GKPeerPickerControllerDelegate.peerPickerControllerDidCancel(_: GKPeerPickerController)](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/1622161-peerpickercontrollerdidcancel)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func peerPickerControllerDidCancel(_ picker: GKPeerPickerController!) ``` | iOS 8.0 |
| To | ``` optional func peerPickerControllerDidCancel(_ picker: GKPeerPickerController) ``` | iOS 3.0 |

Modified [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer)

|  | Declaration |
| --- | --- |
| From | ``` class GKPlayer : NSObject {     class func loadPlayersForIdentifiers(_ identifiers: [AnyObject]!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!)     var playerID: String! { get }     var displayName: String! { get }     var alias: String! { get } } extension GKPlayer {     func loadPhotoForSize(_ size: GKPhotoSize, withCompletionHandler completionHandler: ((UIImage!, NSError!) -> Void)!) } extension GKPlayer {     var isFriend: Bool { get } } ``` |
| To | ``` class GKPlayer : NSObject {     class func loadPlayersForIdentifiers(_ identifiers: [String], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?)     var playerID: String? { get }     var displayName: String? { get }     var alias: String? { get }     class func anonymousGuestPlayerWithIdentifier(_ guestIdentifier: String) -> Self     var guestIdentifier: String? { get } } extension GKPlayer {     func loadPhotoForSize(_ size: GKPhotoSize, withCompletionHandler completionHandler: ((UIImage?, NSError?) -> Void)?) } extension GKPlayer {     var isFriend: Bool { get } } ``` |

Modified [GKPlayer.alias](https://developer.apple.com/documentation/gamekit/gkplayer/1520970-alias)

|  | Declaration |
| --- | --- |
| From | ``` var alias: String! { get } ``` |
| To | ``` var alias: String? { get } ``` |

Modified [GKPlayer.displayName](https://developer.apple.com/documentation/gamekit/gkplayer/1520695-displayname)

|  | Declaration |
| --- | --- |
| From | ``` var displayName: String! { get } ``` |
| To | ``` var displayName: String? { get } ``` |

Modified [GKPlayer.loadPhotoForSize(_: GKPhotoSize, withCompletionHandler: ((UIImage?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkplayer/1521176-loadphoto)

|  | Declaration |
| --- | --- |
| From | ``` func loadPhotoForSize(_ size: GKPhotoSize, withCompletionHandler completionHandler: ((UIImage!, NSError!) -> Void)!) ``` |
| To | ``` func loadPhotoForSize(_ size: GKPhotoSize, withCompletionHandler completionHandler: ((UIImage?, NSError?) -> Void)?) ``` |

Modified [GKPlayer.loadPlayersForIdentifiers(_: [String], withCompletionHandler: (([GKPlayer]?, NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkplayer/1520723-loadplayers)

|  | Declaration |
| --- | --- |
| From | ``` class func loadPlayersForIdentifiers(_ identifiers: [AnyObject]!, withCompletionHandler completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` class func loadPlayersForIdentifiers(_ identifiers: [String], withCompletionHandler completionHandler: (([GKPlayer]?, NSError?) -> Void)?) ``` |

Modified [GKPlayer.playerID](https://developer.apple.com/documentation/gamekit/gkplayer/1521127-playerid)

|  | Declaration |
| --- | --- |
| From | ``` var playerID: String! { get } ``` |
| To | ``` var playerID: String? { get } ``` |

Modified [GKPlayerConnectionState [enum]](https://developer.apple.com/documentation/gamekit/gkplayerconnectionstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame)

|  | Declaration |
| --- | --- |
| From | ``` class GKSavedGame : NSObject, NSCopying {     var name: String! { get }     var deviceName: String! { get }     var modificationDate: NSDate! { get }     func loadDataWithCompletionHandler(_ handler: ((NSData!, NSError!) -> Void)!) } ``` |
| To | ``` class GKSavedGame : NSObject, NSCopying {     var name: String? { get }     var deviceName: String? { get }     var modificationDate: NSDate? { get }     func loadDataWithCompletionHandler(_ handler: ((NSData?, NSError?) -> Void)?) } ``` |

Modified [GKSavedGame.deviceName](https://developer.apple.com/documentation/gamekit/gksavedgame/1520629-devicename)

|  | Declaration |
| --- | --- |
| From | ``` var deviceName: String! { get } ``` |
| To | ``` var deviceName: String? { get } ``` |

Modified [GKSavedGame.loadDataWithCompletionHandler(_: ((NSData?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gksavedgame/1520754-loaddata)

|  | Declaration |
| --- | --- |
| From | ``` func loadDataWithCompletionHandler(_ handler: ((NSData!, NSError!) -> Void)!) ``` |
| To | ``` func loadDataWithCompletionHandler(_ handler: ((NSData?, NSError?) -> Void)?) ``` |

Modified [GKSavedGame.modificationDate](https://developer.apple.com/documentation/gamekit/gksavedgame/1520829-modificationdate)

|  | Declaration |
| --- | --- |
| From | ``` var modificationDate: NSDate! { get } ``` |
| To | ``` var modificationDate: NSDate? { get } ``` |

Modified [GKSavedGame.name](https://developer.apple.com/documentation/gamekit/gksavedgame/1520819-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String? { get } ``` |

Modified [GKSavedGameListener](https://developer.apple.com/documentation/gamekit/gksavedgamelistener)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKSavedGameListener : NSObjectProtocol {     optional func player(_ player: GKPlayer!, didModifySavedGame savedGame: GKSavedGame!)     optional func player(_ player: GKPlayer!, hasConflictingSavedGames savedGames: [AnyObject]!) } ``` |
| To | ``` protocol GKSavedGameListener : NSObjectProtocol {     optional func player(_ player: GKPlayer, didModifySavedGame savedGame: GKSavedGame)     optional func player(_ player: GKPlayer, hasConflictingSavedGames savedGames: [GKSavedGame]) } ``` |

Modified [GKSavedGameListener.player(_: GKPlayer, didModifySavedGame: GKSavedGame)](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387328-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, didModifySavedGame savedGame: GKSavedGame!) ``` |
| To | ``` optional func player(_ player: GKPlayer, didModifySavedGame savedGame: GKSavedGame) ``` |

Modified [GKSavedGameListener.player(_: GKPlayer, hasConflictingSavedGames: [GKSavedGame])](https://developer.apple.com/documentation/gamekit/gksavedgamelistener/1387324-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, hasConflictingSavedGames savedGames: [AnyObject]!) ``` |
| To | ``` optional func player(_ player: GKPlayer, hasConflictingSavedGames savedGames: [GKSavedGame]) ``` |

Modified [GKScore](https://developer.apple.com/documentation/gamekit/gkscore)

|  | Declaration |
| --- | --- |
| From | ``` class GKScore : NSObject, NSCoding, NSSecureCoding {     init!(leaderboardIdentifier identifier: String!)     init!(leaderboardIdentifier identifier: String!, player player: GKPlayer!)     var value: Int64     var formattedValue: String! { get }     var leaderboardIdentifier: String!     var context: UInt64     var date: NSDate! { get }     var player: GKPlayer! { get }     var rank: Int { get }     var shouldSetDefaultLeaderboard: Bool     class func reportScores(_ scores: [AnyObject]!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) } extension GKScore {     func challengeComposeControllerWithMessage(_ message: String!, players players: [AnyObject]!, completionHandler completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController!     func issueChallengeToPlayers(_ playerIDs: [AnyObject]!, message message: String!)     class func reportScores(_ scores: [AnyObject]!, withEligibleChallenges challenges: [AnyObject]!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) } extension GKScore {     func challengeComposeControllerWithPlayers(_ playerIDs: [AnyObject]!, message message: String!, completionHandler completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController! } extension GKScore {     init!(leaderboardIdentifier identifier: String!, forPlayer playerID: String!)     func reportScoreWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     init!(category category: String!)     var playerID: String! { get }     var category: String! } ``` |
| To | ``` class GKScore : NSObject, NSCoding, NSSecureCoding {     init(leaderboardIdentifier identifier: String)     init(leaderboardIdentifier identifier: String, player player: GKPlayer)     var value: Int64     var formattedValue: String? { get }     var leaderboardIdentifier: String     var context: UInt64     var date: NSDate { get }     var player: GKPlayer { get }     var rank: Int { get }     var shouldSetDefaultLeaderboard: Bool     class func reportScores(_ scores: [GKScore], withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKScore {     func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer]?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController     func issueChallengeToPlayers(_ playerIDs: [String]?, message message: String?)     class func reportScores(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) } extension GKScore {     func challengeComposeControllerWithPlayers(_ playerIDs: [String]?, message message: String?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController? } extension GKScore {     init(leaderboardIdentifier identifier: String, forPlayer playerID: String)     func reportScoreWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     init(category category: String?)     var playerID: String { get }     var category: String? } ``` |

Modified [GKScore.challengeComposeControllerWithMessage(_: String?, players: [GKPlayer]?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController](https://developer.apple.com/documentation/gamekit/gkscore/1521227-challengecomposecontroller)

|  | Declaration |
| --- | --- |
| From | ``` func challengeComposeControllerWithMessage(_ message: String!, players players: [AnyObject]!, completionHandler completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController! ``` |
| To | ``` func challengeComposeControllerWithMessage(_ message: String?, players players: [GKPlayer]?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController ``` |

Modified [GKScore.challengeComposeControllerWithPlayers(_: [String]?, message: String?, completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController?](https://developer.apple.com/documentation/gamekit/gkscore/1623555-challengecomposecontroller)

|  | Declaration |
| --- | --- |
| From | ``` func challengeComposeControllerWithPlayers(_ playerIDs: [AnyObject]!, message message: String!, completionHandler completionHandler: GKChallengeComposeCompletionBlock!) -> UIViewController! ``` |
| To | ``` func challengeComposeControllerWithPlayers(_ playerIDs: [String]?, message message: String?, completionHandler completionHandler: GKChallengeComposeCompletionBlock?) -> UIViewController? ``` |

Modified [GKScore.date](https://developer.apple.com/documentation/gamekit/gkscore/1399234-date)

|  | Declaration |
| --- | --- |
| From | ``` var date: NSDate! { get } ``` |
| To | ``` var date: NSDate { get } ``` |

Modified [GKScore.formattedValue](https://developer.apple.com/documentation/gamekit/gkscore/1399221-formattedvalue)

|  | Declaration |
| --- | --- |
| From | ``` var formattedValue: String! { get } ``` |
| To | ``` var formattedValue: String? { get } ``` |

Modified [GKScore.init(leaderboardIdentifier: String)](https://developer.apple.com/documentation/gamekit/gkscore/1399240-initwithleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(leaderboardIdentifier identifier: String!) ``` |
| To | ``` init(leaderboardIdentifier identifier: String) ``` |

Modified [GKScore.init(leaderboardIdentifier: String, forPlayer: String)](https://developer.apple.com/documentation/gamekit/gkscore/1620733-initwithleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(leaderboardIdentifier identifier: String!, forPlayer playerID: String!) ``` |
| To | ``` init(leaderboardIdentifier identifier: String, forPlayer playerID: String) ``` |

Modified [GKScore.init(leaderboardIdentifier: String, player: GKPlayer)](https://developer.apple.com/documentation/gamekit/gkscore/1399254-initwithleaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` init!(leaderboardIdentifier identifier: String!, player player: GKPlayer!) ``` |
| To | ``` init(leaderboardIdentifier identifier: String, player player: GKPlayer) ``` |

Modified [GKScore.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkscore/1399248-leaderboardidentifier)

|  | Declaration |
| --- | --- |
| From | ``` var leaderboardIdentifier: String! ``` |
| To | ``` var leaderboardIdentifier: String ``` |

Modified [GKScore.player](https://developer.apple.com/documentation/gamekit/gkscore/1399246-player)

|  | Declaration |
| --- | --- |
| From | ``` var player: GKPlayer! { get } ``` |
| To | ``` var player: GKPlayer { get } ``` |

Modified [GKScore.playerID](https://developer.apple.com/documentation/gamekit/gkscore/1399232-playerid)

|  | Declaration |
| --- | --- |
| From | ``` var playerID: String! { get } ``` |
| To | ``` var playerID: String { get } ``` |

Modified [GKScore.reportScores(_: [GKScore], withCompletionHandler: ((NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkscore/1399252-reportscores)

|  | Declaration |
| --- | --- |
| From | ``` class func reportScores(_ scores: [AnyObject]!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` class func reportScores(_ scores: [GKScore], withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKScore.reportScores(_: [GKScore], withEligibleChallenges: [GKChallenge], withCompletionHandler: ((NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkscore/1520627-report)

|  | Declaration |
| --- | --- |
| From | ``` class func reportScores(_ scores: [AnyObject]!, withEligibleChallenges challenges: [AnyObject]!, withCompletionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` class func reportScores(_ scores: [GKScore], withEligibleChallenges challenges: [GKChallenge], withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKScoreChallenge](https://developer.apple.com/documentation/gamekit/gkscorechallenge)

|  | Declaration |
| --- | --- |
| From | ``` class GKScoreChallenge : GKChallenge {     var score: GKScore! { get } } ``` |
| To | ``` class GKScoreChallenge : GKChallenge {     var score: GKScore? { get } } ``` |

Modified [GKScoreChallenge.score](https://developer.apple.com/documentation/gamekit/gkscorechallenge/1521014-score)

|  | Declaration |
| --- | --- |
| From | ``` var score: GKScore! { get } ``` |
| To | ``` var score: GKScore? { get } ``` |

Modified [GKSessionDelegate](https://developer.apple.com/documentation/gamekit/gksessiondelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKSessionDelegate : NSObjectProtocol {     optional func session(_ session: GKSession!, peer peerID: String!, didChangeState state: GKPeerConnectionState)     optional func session(_ session: GKSession!, didReceiveConnectionRequestFromPeer peerID: String!)     optional func session(_ session: GKSession!, connectionWithPeerFailed peerID: String!, withError error: NSError!)     optional func session(_ session: GKSession!, didFailWithError error: NSError!) } ``` |
| To | ``` protocol GKSessionDelegate : NSObjectProtocol {     optional func session(_ session: GKSession, peer peerID: String, didChangeState state: GKPeerConnectionState)     optional func session(_ session: GKSession, didReceiveConnectionRequestFromPeer peerID: String)     optional func session(_ session: GKSession, connectionWithPeerFailed peerID: String, withError error: NSError)     optional func session(_ session: GKSession, didFailWithError error: NSError) } ``` |

Modified [GKSessionDelegate.session(_: GKSession, connectionWithPeerFailed: String, withError: NSError)](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1521160-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func session(_ session: GKSession!, connectionWithPeerFailed peerID: String!, withError error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func session(_ session: GKSession, connectionWithPeerFailed peerID: String, withError error: NSError) ``` | iOS 3.0 |

Modified [GKSessionDelegate.session(_: GKSession, didFailWithError: NSError)](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520662-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func session(_ session: GKSession!, didFailWithError error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func session(_ session: GKSession, didFailWithError error: NSError) ``` | iOS 3.0 |

Modified [GKSessionDelegate.session(_: GKSession, didReceiveConnectionRequestFromPeer: String)](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520711-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func session(_ session: GKSession!, didReceiveConnectionRequestFromPeer peerID: String!) ``` | iOS 8.0 |
| To | ``` optional func session(_ session: GKSession, didReceiveConnectionRequestFromPeer peerID: String) ``` | iOS 3.0 |

Modified [GKSessionDelegate.session(_: GKSession, peer: String, didChangeState: GKPeerConnectionState)](https://developer.apple.com/documentation/gamekit/gksessiondelegate/1520885-session)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func session(_ session: GKSession!, peer peerID: String!, didChangeState state: GKPeerConnectionState) ``` | iOS 8.0 |
| To | ``` optional func session(_ session: GKSession, peer peerID: String, didChangeState state: GKPeerConnectionState) ``` | iOS 3.0 |

Modified [GKTurnBasedEventListener](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKTurnBasedEventListener {     optional func player(_ player: GKPlayer!, didRequestMatchWithOtherPlayers playersToInvite: [AnyObject]!)     optional func player(_ player: GKPlayer!, receivedTurnEventForMatch match: GKTurnBasedMatch!, didBecomeActive didBecomeActive: Bool)     optional func player(_ player: GKPlayer!, matchEnded match: GKTurnBasedMatch!)     optional func player(_ player: GKPlayer!, receivedExchangeRequest exchange: GKTurnBasedExchange!, forMatch match: GKTurnBasedMatch!)     optional func player(_ player: GKPlayer!, receivedExchangeCancellation exchange: GKTurnBasedExchange!, forMatch match: GKTurnBasedMatch!)     optional func player(_ player: GKPlayer!, receivedExchangeReplies replies: [AnyObject]!, forCompletedExchange exchange: GKTurnBasedExchange!, forMatch match: GKTurnBasedMatch!)     optional func player(_ player: GKPlayer!, didRequestMatchWithPlayers playerIDsToInvite: [AnyObject]!) } ``` |
| To | ``` protocol GKTurnBasedEventListener {     optional func player(_ player: GKPlayer, didRequestMatchWithOtherPlayers playersToInvite: [GKPlayer])     optional func player(_ player: GKPlayer, receivedTurnEventForMatch match: GKTurnBasedMatch, didBecomeActive didBecomeActive: Bool)     optional func player(_ player: GKPlayer, matchEnded match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeRequest exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeCancellation exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, receivedExchangeReplies replies: [GKTurnBasedExchangeReply], forCompletedExchange exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, wantsToQuitMatch match: GKTurnBasedMatch)     optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String]) } ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, didRequestMatchWithOtherPlayers: [GKPlayer])](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520693-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, didRequestMatchWithOtherPlayers playersToInvite: [AnyObject]!) ``` |
| To | ``` optional func player(_ player: GKPlayer, didRequestMatchWithOtherPlayers playersToInvite: [GKPlayer]) ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, didRequestMatchWithPlayers: [String])](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1624268-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, didRequestMatchWithPlayers playerIDsToInvite: [AnyObject]!) ``` |
| To | ``` optional func player(_ player: GKPlayer, didRequestMatchWithPlayers playerIDsToInvite: [String]) ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, matchEnded: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520554-player)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, matchEnded match: GKTurnBasedMatch!) ``` | iOS 8.0 |
| To | ``` optional func player(_ player: GKPlayer, matchEnded match: GKTurnBasedMatch) ``` | iOS 5.0 |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, receivedExchangeCancellation: GKTurnBasedExchange, forMatch: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520649-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, receivedExchangeCancellation exchange: GKTurnBasedExchange!, forMatch match: GKTurnBasedMatch!) ``` |
| To | ``` optional func player(_ player: GKPlayer, receivedExchangeCancellation exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch) ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, receivedExchangeReplies: [GKTurnBasedExchangeReply], forCompletedExchange: GKTurnBasedExchange, forMatch: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1520827-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, receivedExchangeReplies replies: [AnyObject]!, forCompletedExchange exchange: GKTurnBasedExchange!, forMatch match: GKTurnBasedMatch!) ``` |
| To | ``` optional func player(_ player: GKPlayer, receivedExchangeReplies replies: [GKTurnBasedExchangeReply], forCompletedExchange exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch) ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, receivedExchangeRequest: GKTurnBasedExchange, forMatch: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521209-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, receivedExchangeRequest exchange: GKTurnBasedExchange!, forMatch match: GKTurnBasedMatch!) ``` |
| To | ``` optional func player(_ player: GKPlayer, receivedExchangeRequest exchange: GKTurnBasedExchange, forMatch match: GKTurnBasedMatch) ``` |

Modified [GKTurnBasedEventListener.player(_: GKPlayer, receivedTurnEventForMatch: GKTurnBasedMatch, didBecomeActive: Bool)](https://developer.apple.com/documentation/gamekit/gkturnbasedeventlistener/1521017-player)

|  | Declaration |
| --- | --- |
| From | ``` optional func player(_ player: GKPlayer!, receivedTurnEventForMatch match: GKTurnBasedMatch!, didBecomeActive didBecomeActive: Bool) ``` |
| To | ``` optional func player(_ player: GKPlayer, receivedTurnEventForMatch match: GKTurnBasedMatch, didBecomeActive didBecomeActive: Bool) ``` |

Modified [GKTurnBasedExchange](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange)

|  | Declaration |
| --- | --- |
| From | ``` class GKTurnBasedExchange : NSObject {     var exchangeID: String! { get }     var sender: GKTurnBasedParticipant! { get }     var recipients: [AnyObject]! { get }     var status: GKTurnBasedExchangeStatus { get }     var message: String! { get }     var data: NSData! { get }     var sendDate: NSDate! { get }     var timeoutDate: NSDate! { get }     var completionDate: NSDate! { get }     var replies: [AnyObject]! { get }     func cancelWithLocalizableMessageKey(_ key: String!, arguments arguments: [AnyObject]!, completionHandler completionHandler: ((NSError!) -> Void)!)     func replyWithLocalizableMessageKey(_ key: String!, arguments arguments: [AnyObject]!, data data: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!) } ``` |
| To | ``` class GKTurnBasedExchange : NSObject {     var exchangeID: String? { get }     var sender: GKTurnBasedParticipant? { get }     var recipients: [GKTurnBasedParticipant]? { get }     var status: GKTurnBasedExchangeStatus { get }     var message: String? { get }     var data: NSData? { get }     var sendDate: NSDate? { get }     var timeoutDate: NSDate? { get }     var completionDate: NSDate? { get }     var replies: [GKTurnBasedExchangeReply]? { get }     func cancelWithLocalizableMessageKey(_ key: String, arguments arguments: [String], completionHandler completionHandler: ((NSError?) -> Void)?)     func replyWithLocalizableMessageKey(_ key: String, arguments arguments: [String], data data: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) } ``` |

Modified [GKTurnBasedExchange.cancelWithLocalizableMessageKey(_: String, arguments: [String], completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520779-cancel)

|  | Declaration |
| --- | --- |
| From | ``` func cancelWithLocalizableMessageKey(_ key: String!, arguments arguments: [AnyObject]!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func cancelWithLocalizableMessageKey(_ key: String, arguments arguments: [String], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedExchange.completionDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520994-completiondate)

|  | Declaration |
| --- | --- |
| From | ``` var completionDate: NSDate! { get } ``` |
| To | ``` var completionDate: NSDate? { get } ``` |

Modified [GKTurnBasedExchange.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521121-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` var data: NSData? { get } ``` |

Modified [GKTurnBasedExchange.exchangeID](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520666-exchangeid)

|  | Declaration |
| --- | --- |
| From | ``` var exchangeID: String! { get } ``` |
| To | ``` var exchangeID: String? { get } ``` |

Modified [GKTurnBasedExchange.message](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520633-message)

|  | Declaration |
| --- | --- |
| From | ``` var message: String! { get } ``` |
| To | ``` var message: String? { get } ``` |

Modified [GKTurnBasedExchange.recipients](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520849-recipients)

|  | Declaration |
| --- | --- |
| From | ``` var recipients: [AnyObject]! { get } ``` |
| To | ``` var recipients: [GKTurnBasedParticipant]? { get } ``` |

Modified [GKTurnBasedExchange.replies](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520516-replies)

|  | Declaration |
| --- | --- |
| From | ``` var replies: [AnyObject]! { get } ``` |
| To | ``` var replies: [GKTurnBasedExchangeReply]? { get } ``` |

Modified [GKTurnBasedExchange.replyWithLocalizableMessageKey(_: String, arguments: [String], data: NSData, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520478-reply)

|  | Declaration |
| --- | --- |
| From | ``` func replyWithLocalizableMessageKey(_ key: String!, arguments arguments: [AnyObject]!, data data: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func replyWithLocalizableMessageKey(_ key: String, arguments arguments: [String], data data: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedExchange.sendDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521131-senddate)

|  | Declaration |
| --- | --- |
| From | ``` var sendDate: NSDate! { get } ``` |
| To | ``` var sendDate: NSDate? { get } ``` |

Modified [GKTurnBasedExchange.sender](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1520936-sender)

|  | Declaration |
| --- | --- |
| From | ``` var sender: GKTurnBasedParticipant! { get } ``` |
| To | ``` var sender: GKTurnBasedParticipant? { get } ``` |

Modified [GKTurnBasedExchange.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange/1521105-timeoutdate)

|  | Declaration |
| --- | --- |
| From | ``` var timeoutDate: NSDate! { get } ``` |
| To | ``` var timeoutDate: NSDate? { get } ``` |

Modified [GKTurnBasedExchangeReply](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply)

|  | Declaration |
| --- | --- |
| From | ``` class GKTurnBasedExchangeReply : NSObject {     var recipient: GKTurnBasedParticipant! { get }     var message: String! { get }     var data: NSData! { get }     var replyDate: NSDate! { get } } ``` |
| To | ``` class GKTurnBasedExchangeReply : NSObject {     var recipient: GKTurnBasedParticipant? { get }     var message: String? { get }     var data: NSData? { get }     var replyDate: NSDate? { get } } ``` |

Modified [GKTurnBasedExchangeReply.data](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520729-data)

|  | Declaration |
| --- | --- |
| From | ``` var data: NSData! { get } ``` |
| To | ``` var data: NSData? { get } ``` |

Modified [GKTurnBasedExchangeReply.message](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520896-message)

|  | Declaration |
| --- | --- |
| From | ``` var message: String! { get } ``` |
| To | ``` var message: String? { get } ``` |

Modified [GKTurnBasedExchangeReply.recipient](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1521025-recipient)

|  | Declaration |
| --- | --- |
| From | ``` var recipient: GKTurnBasedParticipant! { get } ``` |
| To | ``` var recipient: GKTurnBasedParticipant? { get } ``` |

Modified [GKTurnBasedExchangeReply.replyDate](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply/1520727-replydate)

|  | Declaration |
| --- | --- |
| From | ``` var replyDate: NSDate! { get } ``` |
| To | ``` var replyDate: NSDate? { get } ``` |

Modified [GKTurnBasedMatch](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch)

|  | Declaration |
| --- | --- |
| From | ``` class GKTurnBasedMatch : NSObject {     var matchID: String! { get }     var creationDate: NSDate! { get }     var participants: [AnyObject]! { get }     var status: GKTurnBasedMatchStatus { get }     var currentParticipant: GKTurnBasedParticipant! { get }     var matchData: NSData! { get }     func setLocalizableMessageWithKey(_ key: String!, arguments arguments: [AnyObject]!)     var message: String!     var matchDataMaximumSize: Int { get }     var exchanges: [AnyObject]! { get }     var activeExchanges: [AnyObject]! { get }     var completedExchanges: [AnyObject]! { get }     var exchangeDataMaximumSize: Int { get }     var exchangeMaxInitiatedExchangesPerPlayer: Int { get }     class func findMatchForRequest(_ request: GKMatchRequest!, withCompletionHandler completionHandler: ((GKTurnBasedMatch!, NSError!) -> Void)!)     class func loadMatchesWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!)     class func loadMatchWithID(_ matchID: String!, withCompletionHandler completionHandler: ((GKTurnBasedMatch!, NSError!) -> Void)!)     func rematchWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch!, NSError!) -> Void)!)     func acceptInviteWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch!, NSError!) -> Void)!)     func declineInviteWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     func removeWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!)     func loadMatchDataWithCompletionHandler(_ completionHandler: ((NSData!, NSError!) -> Void)!)     func endTurnWithNextParticipants(_ nextParticipants: [AnyObject]!, turnTimeout timeout: NSTimeInterval, matchData matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!)     func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipants nextParticipants: [AnyObject]!, turnTimeout timeout: NSTimeInterval, matchData matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!)     func participantQuitOutOfTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, withCompletionHandler completionHandler: ((NSError!) -> Void)!)     func endMatchInTurnWithMatchData(_ matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!)     func endMatchInTurnWithMatchData(_ matchData: NSData!, scores scores: [AnyObject]!, achievements achievements: [AnyObject]!, completionHandler completionHandler: ((NSError!) -> Void)!)     func saveCurrentTurnWithMatchData(_ matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!)     func saveMergedMatchData(_ matchData: NSData!, withResolvedExchanges exchanges: [AnyObject]!, completionHandler completionHandler: ((NSError!) -> Void)!)     func sendExchangeToParticipants(_ participants: [AnyObject]!, data data: NSData!, localizableMessageKey key: String!, arguments arguments: [AnyObject]!, timeout timeout: NSTimeInterval, completionHandler completionHandler: ((GKTurnBasedExchange!, NSError!) -> Void)!)     func sendReminderToParticipants(_ participants: [AnyObject]!, localizableMessageKey key: String!, arguments arguments: [AnyObject]!, completionHandler completionHandler: ((NSError!) -> Void)!)     func endTurnWithNextParticipant(_ nextParticipant: GKTurnBasedParticipant!, matchData matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!)     func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipant nextParticipant: GKTurnBasedParticipant!, matchData matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!) } ``` |
| To | ``` class GKTurnBasedMatch : NSObject {     var matchID: String? { get }     var creationDate: NSDate? { get }     var participants: [GKTurnBasedParticipant]? { get }     var status: GKTurnBasedMatchStatus { get }     var currentParticipant: GKTurnBasedParticipant? { get }     var matchData: NSData? { get }     func setLocalizableMessageWithKey(_ key: String, arguments arguments: [String]?)     var message: String?     var matchDataMaximumSize: Int { get }     var exchanges: [GKTurnBasedExchange]? { get }     var activeExchanges: [GKTurnBasedExchange]? { get }     var completedExchanges: [GKTurnBasedExchange]? { get }     var exchangeDataMaximumSize: Int { get }     var exchangeMaxInitiatedExchangesPerPlayer: Int { get }     class func findMatchForRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (GKTurnBasedMatch?, NSError?) -> Void)     class func loadMatchesWithCompletionHandler(_ completionHandler: (([GKTurnBasedMatch]?, NSError?) -> Void)?)     class func loadMatchWithID(_ matchID: String, withCompletionHandler completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?)     func rematchWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?)     func acceptInviteWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?)     func declineInviteWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     func removeWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?)     func loadMatchDataWithCompletionHandler(_ completionHandler: ((NSData?, NSError?) -> Void)?)     func endTurnWithNextParticipants(_ nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: NSTimeInterval, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: NSTimeInterval, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func participantQuitOutOfTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, withCompletionHandler completionHandler: ((NSError?) -> Void)?)     func endMatchInTurnWithMatchData(_ matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func endMatchInTurnWithMatchData(_ matchData: NSData, scores scores: [GKScore]?, achievements achievements: [GKAchievement]?, completionHandler completionHandler: ((NSError?) -> Void)?)     func saveCurrentTurnWithMatchData(_ matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func saveMergedMatchData(_ matchData: NSData, withResolvedExchanges exchanges: [GKTurnBasedExchange], completionHandler completionHandler: ((NSError?) -> Void)?)     func sendExchangeToParticipants(_ participants: [GKTurnBasedParticipant], data data: NSData, localizableMessageKey key: String, arguments arguments: [String], timeout timeout: NSTimeInterval, completionHandler completionHandler: ((GKTurnBasedExchange, NSError) -> Void)?)     func sendReminderToParticipants(_ participants: [GKTurnBasedParticipant], localizableMessageKey key: String, arguments arguments: [String], completionHandler completionHandler: ((NSError?) -> Void)?)     func endTurnWithNextParticipant(_ nextParticipant: GKTurnBasedParticipant, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?)     func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipant nextParticipant: GKTurnBasedParticipant, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) } ``` |

Modified [GKTurnBasedMatch.acceptInviteWithCompletionHandler(_: ((GKTurnBasedMatch?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520515-acceptinvitewithcompletionhandle)

|  | Declaration |
| --- | --- |
| From | ``` func acceptInviteWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch!, NSError!) -> Void)!) ``` |
| To | ``` func acceptInviteWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.activeExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520977-activeexchanges)

|  | Declaration |
| --- | --- |
| From | ``` var activeExchanges: [AnyObject]! { get } ``` |
| To | ``` var activeExchanges: [GKTurnBasedExchange]? { get } ``` |

Modified [GKTurnBasedMatch.completedExchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520918-completedexchanges)

|  | Declaration |
| --- | --- |
| From | ``` var completedExchanges: [AnyObject]! { get } ``` |
| To | ``` var completedExchanges: [GKTurnBasedExchange]? { get } ``` |

Modified [GKTurnBasedMatch.creationDate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521168-creationdate)

|  | Declaration |
| --- | --- |
| From | ``` var creationDate: NSDate! { get } ``` |
| To | ``` var creationDate: NSDate? { get } ``` |

Modified [GKTurnBasedMatch.currentParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520643-currentparticipant)

|  | Declaration |
| --- | --- |
| From | ``` var currentParticipant: GKTurnBasedParticipant! { get } ``` |
| To | ``` var currentParticipant: GKTurnBasedParticipant? { get } ``` |

Modified [GKTurnBasedMatch.declineInviteWithCompletionHandler(_: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520940-declineinvitewithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func declineInviteWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func declineInviteWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.endMatchInTurnWithMatchData(_: NSData, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520907-endmatchinturnwithmatchdata)

|  | Declaration |
| --- | --- |
| From | ``` func endMatchInTurnWithMatchData(_ matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func endMatchInTurnWithMatchData(_ matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.endMatchInTurnWithMatchData(_: NSData, scores: [GKScore]?, achievements: [GKAchievement]?, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521006-endmatchinturn)

|  | Declaration |
| --- | --- |
| From | ``` func endMatchInTurnWithMatchData(_ matchData: NSData!, scores scores: [AnyObject]!, achievements achievements: [AnyObject]!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func endMatchInTurnWithMatchData(_ matchData: NSData, scores scores: [GKScore]?, achievements achievements: [GKAchievement]?, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.endTurnWithNextParticipants(_: [GKTurnBasedParticipant], turnTimeout: NSTimeInterval, matchData: NSData, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520765-endturnwithnextparticipants)

|  | Declaration |
| --- | --- |
| From | ``` func endTurnWithNextParticipants(_ nextParticipants: [AnyObject]!, turnTimeout timeout: NSTimeInterval, matchData matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func endTurnWithNextParticipants(_ nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: NSTimeInterval, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.exchanges](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521224-exchanges)

|  | Declaration |
| --- | --- |
| From | ``` var exchanges: [AnyObject]! { get } ``` |
| To | ``` var exchanges: [GKTurnBasedExchange]? { get } ``` |

Modified [GKTurnBasedMatch.findMatchForRequest(_: GKMatchRequest, withCompletionHandler: (GKTurnBasedMatch?, NSError?) -> Void) [class]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521008-findmatchforrequest)

|  | Declaration |
| --- | --- |
| From | ``` class func findMatchForRequest(_ request: GKMatchRequest!, withCompletionHandler completionHandler: ((GKTurnBasedMatch!, NSError!) -> Void)!) ``` |
| To | ``` class func findMatchForRequest(_ request: GKMatchRequest, withCompletionHandler completionHandler: (GKTurnBasedMatch?, NSError?) -> Void) ``` |

Modified [GKTurnBasedMatch.loadMatchDataWithCompletionHandler(_: ((NSData?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521005-loadmatchdatawithcompletionhandl)

|  | Declaration |
| --- | --- |
| From | ``` func loadMatchDataWithCompletionHandler(_ completionHandler: ((NSData!, NSError!) -> Void)!) ``` |
| To | ``` func loadMatchDataWithCompletionHandler(_ completionHandler: ((NSData?, NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.loadMatchesWithCompletionHandler(_: (([GKTurnBasedMatch]?, NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521207-loadmatcheswithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` class func loadMatchesWithCompletionHandler(_ completionHandler: (([AnyObject]!, NSError!) -> Void)!) ``` |
| To | ``` class func loadMatchesWithCompletionHandler(_ completionHandler: (([GKTurnBasedMatch]?, NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.loadMatchWithID(_: String, withCompletionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?) [class]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521102-load)

|  | Declaration |
| --- | --- |
| From | ``` class func loadMatchWithID(_ matchID: String!, withCompletionHandler completionHandler: ((GKTurnBasedMatch!, NSError!) -> Void)!) ``` |
| To | ``` class func loadMatchWithID(_ matchID: String, withCompletionHandler completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.matchData](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520991-matchdata)

|  | Declaration |
| --- | --- |
| From | ``` var matchData: NSData! { get } ``` |
| To | ``` var matchData: NSData? { get } ``` |

Modified [GKTurnBasedMatch.matchID](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520625-matchid)

|  | Declaration |
| --- | --- |
| From | ``` var matchID: String! { get } ``` |
| To | ``` var matchID: String? { get } ``` |

Modified [GKTurnBasedMatch.message](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520721-message)

|  | Declaration |
| --- | --- |
| From | ``` var message: String! ``` |
| To | ``` var message: String? ``` |

Modified [GKTurnBasedMatch.participantQuitInTurnWithOutcome(_: GKTurnBasedMatchOutcome, nextParticipants: [GKTurnBasedParticipant], turnTimeout: NSTimeInterval, matchData: NSData, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520500-participantquitinturn)

|  | Declaration |
| --- | --- |
| From | ``` func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipants nextParticipants: [AnyObject]!, turnTimeout timeout: NSTimeInterval, matchData matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func participantQuitInTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, nextParticipants nextParticipants: [GKTurnBasedParticipant], turnTimeout timeout: NSTimeInterval, matchData matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.participantQuitOutOfTurnWithOutcome(_: GKTurnBasedMatchOutcome, withCompletionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521106-participantquitoutofturn)

|  | Declaration |
| --- | --- |
| From | ``` func participantQuitOutOfTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, withCompletionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func participantQuitOutOfTurnWithOutcome(_ matchOutcome: GKTurnBasedMatchOutcome, withCompletionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.participants](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520875-participants)

|  | Declaration |
| --- | --- |
| From | ``` var participants: [AnyObject]! { get } ``` |
| To | ``` var participants: [GKTurnBasedParticipant]? { get } ``` |

Modified [GKTurnBasedMatch.rematchWithCompletionHandler(_: ((GKTurnBasedMatch?, NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520794-rematchwithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func rematchWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch!, NSError!) -> Void)!) ``` |
| To | ``` func rematchWithCompletionHandler(_ completionHandler: ((GKTurnBasedMatch?, NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.removeWithCompletionHandler(_: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520651-removewithcompletionhandler)

|  | Declaration |
| --- | --- |
| From | ``` func removeWithCompletionHandler(_ completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func removeWithCompletionHandler(_ completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.saveCurrentTurnWithMatchData(_: NSData, completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520761-savecurrentturnwithmatchdata)

|  | Declaration |
| --- | --- |
| From | ``` func saveCurrentTurnWithMatchData(_ matchData: NSData!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func saveCurrentTurnWithMatchData(_ matchData: NSData, completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.saveMergedMatchData(_: NSData, withResolvedExchanges: [GKTurnBasedExchange], completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1521154-savemergedmatch)

|  | Declaration |
| --- | --- |
| From | ``` func saveMergedMatchData(_ matchData: NSData!, withResolvedExchanges exchanges: [AnyObject]!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func saveMergedMatchData(_ matchData: NSData, withResolvedExchanges exchanges: [GKTurnBasedExchange], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.sendExchangeToParticipants(_: [GKTurnBasedParticipant], data: NSData, localizableMessageKey: String, arguments: [String], timeout: NSTimeInterval, completionHandler: ((GKTurnBasedExchange, NSError) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520451-sendexchangetoparticipants)

|  | Declaration |
| --- | --- |
| From | ``` func sendExchangeToParticipants(_ participants: [AnyObject]!, data data: NSData!, localizableMessageKey key: String!, arguments arguments: [AnyObject]!, timeout timeout: NSTimeInterval, completionHandler completionHandler: ((GKTurnBasedExchange!, NSError!) -> Void)!) ``` |
| To | ``` func sendExchangeToParticipants(_ participants: [GKTurnBasedParticipant], data data: NSData, localizableMessageKey key: String, arguments arguments: [String], timeout timeout: NSTimeInterval, completionHandler completionHandler: ((GKTurnBasedExchange, NSError) -> Void)?) ``` |

Modified [GKTurnBasedMatch.sendReminderToParticipants(_: [GKTurnBasedParticipant], localizableMessageKey: String, arguments: [String], completionHandler: ((NSError?) -> Void)?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520947-sendremindertoparticipants)

|  | Declaration |
| --- | --- |
| From | ``` func sendReminderToParticipants(_ participants: [AnyObject]!, localizableMessageKey key: String!, arguments arguments: [AnyObject]!, completionHandler completionHandler: ((NSError!) -> Void)!) ``` |
| To | ``` func sendReminderToParticipants(_ participants: [GKTurnBasedParticipant], localizableMessageKey key: String, arguments arguments: [String], completionHandler completionHandler: ((NSError?) -> Void)?) ``` |

Modified [GKTurnBasedMatch.setLocalizableMessageWithKey(_: String, arguments: [String]?)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch/1520510-setlocalizablemessagewithkey)

|  | Declaration |
| --- | --- |
| From | ``` func setLocalizableMessageWithKey(_ key: String!, arguments arguments: [AnyObject]!) ``` |
| To | ``` func setLocalizableMessageWithKey(_ key: String, arguments arguments: [String]?) ``` |

Modified [GKTurnBasedMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` class GKTurnBasedMatchmakerViewController : UINavigationController { } extension GKTurnBasedMatchmakerViewController {     unowned(unsafe) var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate!     var showExistingMatches: Bool     init!(matchRequest request: GKMatchRequest!) } ``` |
| To | ``` class GKTurnBasedMatchmakerViewController : UINavigationController { } extension GKTurnBasedMatchmakerViewController {     unowned(unsafe) var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate?     var showExistingMatches: Bool     init(matchRequest request: GKMatchRequest) } ``` |

Modified [GKTurnBasedMatchmakerViewController.init(matchRequest: GKMatchRequest)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1521069-init)

|  | Declaration |
| --- | --- |
| From | ``` init!(matchRequest request: GKMatchRequest!) ``` |
| To | ``` init(matchRequest request: GKMatchRequest) ``` |

Modified [GKTurnBasedMatchmakerViewController.turnBasedMatchmakerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller/1520697-turnbasedmatchmakerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` unowned(unsafe) var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate! ``` |
| To | ``` unowned(unsafe) var turnBasedMatchmakerDelegate: GKTurnBasedMatchmakerViewControllerDelegate? ``` |

Modified [GKTurnBasedMatchmakerViewControllerDelegate](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKTurnBasedMatchmakerViewControllerDelegate : NSObjectProtocol {     func turnBasedMatchmakerViewControllerWasCancelled(_ viewController: GKTurnBasedMatchmakerViewController!)     func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController!, didFailWithError error: NSError!)     func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController!, didFindMatch match: GKTurnBasedMatch!)     func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController!, playerQuitForMatch match: GKTurnBasedMatch!) } ``` |
| To | ``` protocol GKTurnBasedMatchmakerViewControllerDelegate : NSObjectProtocol {     func turnBasedMatchmakerViewControllerWasCancelled(_ viewController: GKTurnBasedMatchmakerViewController)     func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFailWithError error: NSError)     optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFindMatch match: GKTurnBasedMatch)     optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, playerQuitForMatch match: GKTurnBasedMatch) } ``` |

Modified [GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(_: GKTurnBasedMatchmakerViewController, didFailWithError: NSError)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1521028-turnbasedmatchmakerviewcontrolle)

|  | Declaration |
| --- | --- |
| From | ``` func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController!, didFailWithError error: NSError!) ``` |
| To | ``` func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFailWithError error: NSError) ``` |

Modified [GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(_: GKTurnBasedMatchmakerViewController, didFindMatch: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1520653-turnbasedmatchmakerviewcontrolle)

|  | Declaration | Deprecation | Optional |
| --- | --- | --- | --- |
| From | ``` func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController!, didFindMatch match: GKTurnBasedMatch!) ``` | -- | -- |
| To | ``` optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, didFindMatch match: GKTurnBasedMatch) ``` | iOS 9.0 | yes |

Modified [GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewController(_: GKTurnBasedMatchmakerViewController, playerQuitForMatch: GKTurnBasedMatch)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1520967-turnbasedmatchmakerviewcontrolle)

|  | Declaration | Deprecation | Optional |
| --- | --- | --- | --- |
| From | ``` func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController!, playerQuitForMatch match: GKTurnBasedMatch!) ``` | -- | -- |
| To | ``` optional func turnBasedMatchmakerViewController(_ viewController: GKTurnBasedMatchmakerViewController, playerQuitForMatch match: GKTurnBasedMatch) ``` | iOS 9.0 | yes |

Modified [GKTurnBasedMatchmakerViewControllerDelegate.turnBasedMatchmakerViewControllerWasCancelled(_: GKTurnBasedMatchmakerViewController)](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontrollerdelegate/1521000-turnbasedmatchmakerviewcontrolle)

|  | Declaration |
| --- | --- |
| From | ``` func turnBasedMatchmakerViewControllerWasCancelled(_ viewController: GKTurnBasedMatchmakerViewController!) ``` |
| To | ``` func turnBasedMatchmakerViewControllerWasCancelled(_ viewController: GKTurnBasedMatchmakerViewController) ``` |

Modified [GKTurnBasedMatchOutcome [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKTurnBasedMatchStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKTurnBasedParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant)

|  | Declaration |
| --- | --- |
| From | ``` class GKTurnBasedParticipant : NSObject {     var player: GKPlayer! { get }     @NSCopying var lastTurnDate: NSDate! { get }     var status: GKTurnBasedParticipantStatus { get }     var matchOutcome: GKTurnBasedMatchOutcome     @NSCopying var timeoutDate: NSDate! { get }     var playerID: String! { get } } ``` |
| To | ``` class GKTurnBasedParticipant : NSObject {     var player: GKPlayer? { get }     @NSCopying var lastTurnDate: NSDate? { get }     var status: GKTurnBasedParticipantStatus { get }     var matchOutcome: GKTurnBasedMatchOutcome     @NSCopying var timeoutDate: NSDate? { get }     var playerID: String? { get } } ``` |

Modified [GKTurnBasedParticipant.lastTurnDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520941-lastturndate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var lastTurnDate: NSDate! { get } ``` |
| To | ``` @NSCopying var lastTurnDate: NSDate? { get } ``` |

Modified [GKTurnBasedParticipant.player](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521037-player)

|  | Declaration |
| --- | --- |
| From | ``` var player: GKPlayer! { get } ``` |
| To | ``` var player: GKPlayer? { get } ``` |

Modified [GKTurnBasedParticipant.playerID](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1520474-playerid)

|  | Declaration |
| --- | --- |
| From | ``` var playerID: String! { get } ``` |
| To | ``` var playerID: String? { get } ``` |

Modified [GKTurnBasedParticipant.timeoutDate](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant/1521187-timeoutdate)

|  | Declaration |
| --- | --- |
| From | ``` @NSCopying var timeoutDate: NSDate! { get } ``` |
| To | ``` @NSCopying var timeoutDate: NSDate? { get } ``` |

Modified [GKTurnBasedParticipantStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKVoiceChat](https://developer.apple.com/documentation/gamekit/gkvoicechat)

|  | Declaration |
| --- | --- |
| From | ``` class GKVoiceChat : NSObject {     func start()     func stop()     func setPlayer(_ player: GKPlayer!, muted isMuted: Bool)     var playerVoiceChatStateDidChangeHandler: ((GKPlayer!, GKVoiceChatPlayerState) -> Void)!     var name: String! { get }     var active: Bool     var volume: Float     var players: [AnyObject]! { get }     class func isVoIPAllowed() -> Bool } extension GKVoiceChat {     var playerIDs: [AnyObject]! { get }     var playerStateUpdateHandler: ((String!, GKVoiceChatPlayerState) -> Void)!     func setMute(_ isMuted: Bool, forPlayer playerID: String!) } ``` |
| To | ``` class GKVoiceChat : NSObject {     func start()     func stop()     func setPlayer(_ player: GKPlayer, muted isMuted: Bool)     var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChatPlayerState) -> Void     var name: String { get }     var active: Bool     var volume: Float     var players: [GKPlayer] { get }     class func isVoIPAllowed() -> Bool } extension GKVoiceChat {     var playerIDs: [String] { get }     var playerStateUpdateHandler: (String, GKVoiceChatPlayerState) -> Void     func setMute(_ isMuted: Bool, forPlayer playerID: String) } ``` |

Modified [GKVoiceChat.name](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385707-name)

|  | Declaration |
| --- | --- |
| From | ``` var name: String! { get } ``` |
| To | ``` var name: String { get } ``` |

Modified [GKVoiceChat.playerIDs](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385721-playerids)

|  | Declaration |
| --- | --- |
| From | ``` var playerIDs: [AnyObject]! { get } ``` |
| To | ``` var playerIDs: [String] { get } ``` |

Modified [GKVoiceChat.players](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385701-players)

|  | Declaration |
| --- | --- |
| From | ``` var players: [AnyObject]! { get } ``` |
| To | ``` var players: [GKPlayer] { get } ``` |

Modified [GKVoiceChat.playerStateUpdateHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385705-playerstateupdatehandler)

|  | Declaration |
| --- | --- |
| From | ``` var playerStateUpdateHandler: ((String!, GKVoiceChatPlayerState) -> Void)! ``` |
| To | ``` var playerStateUpdateHandler: (String, GKVoiceChatPlayerState) -> Void ``` |

Modified [GKVoiceChat.playerVoiceChatStateDidChangeHandler](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385713-playervoicechatstatedidchangehan)

|  | Declaration |
| --- | --- |
| From | ``` var playerVoiceChatStateDidChangeHandler: ((GKPlayer!, GKVoiceChatPlayerState) -> Void)! ``` |
| To | ``` var playerVoiceChatStateDidChangeHandler: (GKPlayer, GKVoiceChatPlayerState) -> Void ``` |

Modified [GKVoiceChat.setMute(_: Bool, forPlayer: String)](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385711-setmute)

|  | Declaration |
| --- | --- |
| From | ``` func setMute(_ isMuted: Bool, forPlayer playerID: String!) ``` |
| To | ``` func setMute(_ isMuted: Bool, forPlayer playerID: String) ``` |

Modified [GKVoiceChat.setPlayer(_: GKPlayer, muted: Bool)](https://developer.apple.com/documentation/gamekit/gkvoicechat/1385717-setplayer)

|  | Declaration |
| --- | --- |
| From | ``` func setPlayer(_ player: GKPlayer!, muted isMuted: Bool) ``` |
| To | ``` func setPlayer(_ player: GKPlayer, muted isMuted: Bool) ``` |

Modified [GKVoiceChatClient](https://developer.apple.com/documentation/gamekit/gkvoicechatclient)

|  | Declaration |
| --- | --- |
| From | ``` protocol GKVoiceChatClient : NSObjectProtocol {     func voiceChatService(_ voiceChatService: GKVoiceChatService!, sendData data: NSData!, toParticipantID participantID: String!)     func participantID() -> String!     optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, sendRealTimeData data: NSData!, toParticipantID participantID: String!)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, didStartWithParticipantID participantID: String!)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, didNotStartWithParticipantID participantID: String!, error error: NSError!)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, didStopWithParticipantID participantID: String!, error error: NSError!)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, didReceiveInvitationFromParticipantID participantID: String!, callID callID: Int) } ``` |
| To | ``` protocol GKVoiceChatClient : NSObjectProtocol {     func voiceChatService(_ voiceChatService: GKVoiceChatService, sendData data: NSData, toParticipantID participantID: String)     func participantID() -> String     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, sendRealTimeData data: NSData, toParticipantID participantID: String)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStartWithParticipantID participantID: String)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didNotStartWithParticipantID participantID: String, error error: NSError?)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStopWithParticipantID participantID: String, error error: NSError?)     optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didReceiveInvitationFromParticipantID participantID: String, callID callID: Int) } ``` |

Modified [GKVoiceChatClient.participantID() -> String](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520641-participantid)

|  | Declaration |
| --- | --- |
| From | ``` func participantID() -> String! ``` |
| To | ``` func participantID() -> String ``` |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, didNotStartWithParticipantID: String, error: NSError?)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521047-voicechatservice)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, didNotStartWithParticipantID participantID: String!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didNotStartWithParticipantID participantID: String, error error: NSError?) ``` | iOS 3.0 |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, didReceiveInvitationFromParticipantID: String, callID: Int)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520997-voicechatservice)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, didReceiveInvitationFromParticipantID participantID: String!, callID callID: Int) ``` | iOS 8.0 |
| To | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didReceiveInvitationFromParticipantID participantID: String, callID callID: Int) ``` | iOS 3.0 |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, didStartWithParticipantID: String)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520971-voicechatservice)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, didStartWithParticipantID participantID: String!) ``` | iOS 8.0 |
| To | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStartWithParticipantID participantID: String) ``` | iOS 3.0 |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, didStopWithParticipantID: String, error: NSError?)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1520681-voicechatservice)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, didStopWithParticipantID participantID: String!, error error: NSError!) ``` | iOS 8.0 |
| To | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, didStopWithParticipantID participantID: String, error error: NSError?) ``` | iOS 3.0 |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, sendData: NSData, toParticipantID: String)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521075-voicechatservice)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func voiceChatService(_ voiceChatService: GKVoiceChatService!, sendData data: NSData!, toParticipantID participantID: String!) ``` | iOS 8.0 |
| To | ``` func voiceChatService(_ voiceChatService: GKVoiceChatService, sendData data: NSData, toParticipantID participantID: String) ``` | iOS 3.0 |

Modified [GKVoiceChatClient.voiceChatService(_: GKVoiceChatService, sendRealTimeData: NSData, toParticipantID: String)](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/1521009-voicechatservice)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService!, sendRealTimeData data: NSData!, toParticipantID participantID: String!) ``` | iOS 8.0 |
| To | ``` optional func voiceChatService(_ voiceChatService: GKVoiceChatService, sendRealTimeData data: NSData, toParticipantID participantID: String) ``` | iOS 3.0 |

Modified [GKVoiceChatPlayerState [enum]](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate)

|  | Raw Value Type |
| --- | --- |
| From | -- |
| To | Int |

Modified [GKChallengeComposeCompletionBlock](https://developer.apple.com/documentation/gamekit/gkchallengecomposecompletionblock)

|  | Declaration |
| --- | --- |
| From | ``` typealias GKChallengeComposeCompletionBlock = (UIViewController!, Bool, [AnyObject]!) -> Void ``` |
| To | ``` typealias GKChallengeComposeCompletionBlock = (UIViewController, Bool, [String]?) -> Void ``` |

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
