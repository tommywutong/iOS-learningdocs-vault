---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/GameKit.html
archived_at: '2026-07-18T02:57:08.701372Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# GameKit Changes for Swift

### GameKit

Modified [GKAchievement](https://developer.apple.com/documentation/gamekit/gkachievement)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSSecureCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKAchievementChallenge](https://developer.apple.com/documentation/gamekit/gkachievementchallenge)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKAchievementDescription](https://developer.apple.com/documentation/gamekit/gkachievementdescription)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSSecureCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKChallenge](https://developer.apple.com/documentation/gamekit/gkchallenge)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSSecureCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKChallengeState [enum]](https://developer.apple.com/documentation/gamekit/gkchallengestate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKErrorCode [enum]](https://developer.apple.com/documentation/gamekit/gkerrorcode)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum GKErrorCode : Int {     case Unknown     case Cancelled     case CommunicationsFailure     case UserDenied     case InvalidCredentials     case NotAuthenticated     case AuthenticationInProgress     case InvalidPlayer     case ScoreNotSet     case ParentalControlsBlocked     case PlayerStatusExceedsMaximumLength     case PlayerStatusInvalid     case MatchRequestInvalid     case Underage     case GameUnrecognized     case NotSupported     case InvalidParameter     case UnexpectedConnection     case ChallengeInvalid     case TurnBasedMatchDataTooLarge     case TurnBasedTooManySessions     case TurnBasedInvalidParticipant     case TurnBasedInvalidTurn     case TurnBasedInvalidState     case InvitationsDisabled     case PlayerPhotoFailure     case UbiquityContainerUnavailable } extension GKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } extension GKErrorCode : Hashable, Equatable, __BridgedNSError, ErrorType, RawRepresentable, _ObjectiveCBridgeableErrorType, _BridgedNSError { } ``` | Equatable, ErrorType, Hashable, RawRepresentable |
| To | ``` enum GKErrorCode : Int {     case Unknown     case Cancelled     case CommunicationsFailure     case UserDenied     case InvalidCredentials     case NotAuthenticated     case AuthenticationInProgress     case InvalidPlayer     case ScoreNotSet     case ParentalControlsBlocked     case PlayerStatusExceedsMaximumLength     case PlayerStatusInvalid     case MatchRequestInvalid     case Underage     case GameUnrecognized     case NotSupported     case InvalidParameter     case UnexpectedConnection     case ChallengeInvalid     case TurnBasedMatchDataTooLarge     case TurnBasedTooManySessions     case TurnBasedInvalidParticipant     case TurnBasedInvalidTurn     case TurnBasedInvalidState     case InvitationsDisabled     case PlayerPhotoFailure     case UbiquityContainerUnavailable } extension GKErrorCode : _BridgedNSError { } extension GKErrorCode : _BridgedNSError { } ``` | -- |

Modified [GKFriendRequestComposeViewController](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKGameCenterViewController](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKGameCenterViewControllerState [enum]](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontrollerstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKInvite](https://developer.apple.com/documentation/gamekit/gkinvite)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKInviteRecipientResponse [enum]](https://developer.apple.com/documentation/gamekit/gkinviterecipientresponse)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKLeaderboard](https://developer.apple.com/documentation/gamekit/gkleaderboard)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKLeaderboardPlayerScope [enum]](https://developer.apple.com/documentation/gamekit/gkleaderboardplayerscope)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKLeaderboardSet](https://developer.apple.com/documentation/gamekit/gkleaderboardset)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSSecureCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKLeaderboardTimeScope [enum]](https://developer.apple.com/documentation/gamekit/gkleaderboardtimescope)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKLocalPlayer](https://developer.apple.com/documentation/gamekit/gklocalplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject, GKSavedGameListener, NSObjectProtocol |
| To | GKSavedGameListener |

Modified [GKLocalPlayerListener](https://developer.apple.com/documentation/gamekit/gklocalplayerlistener)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol GKLocalPlayerListener : GKChallengeListener, NSObjectProtocol, GKInviteEventListener, GKTurnBasedEventListener, GKSavedGameListener { } ``` | GKChallengeListener, GKInviteEventListener, GKSavedGameListener, GKTurnBasedEventListener, NSObjectProtocol |
| To | ``` protocol GKLocalPlayerListener : GKChallengeListener, GKInviteEventListener, GKTurnBasedEventListener, GKSavedGameListener { } ``` | GKChallengeListener, GKInviteEventListener, GKSavedGameListener, GKTurnBasedEventListener |

Modified [GKMatch](https://developer.apple.com/documentation/gamekit/gkmatch)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKMatchmaker](https://developer.apple.com/documentation/gamekit/gkmatchmaker)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkmatchmakerviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKMatchRequest](https://developer.apple.com/documentation/gamekit/gkmatchrequest)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKMatchSendDataMode [enum]](https://developer.apple.com/documentation/gamekit/gkmatchsenddatamode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKMatchType [enum]](https://developer.apple.com/documentation/gamekit/gkmatchtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKNotificationBanner](https://developer.apple.com/documentation/gamekit/gknotificationbanner)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKPlayerConnectionState [enum]](https://developer.apple.com/documentation/gamekit/gkplayerconnectionstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKSavedGame](https://developer.apple.com/documentation/gamekit/gksavedgame)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCopying |
| To | NSCopying |

Modified [GKScore](https://developer.apple.com/documentation/gamekit/gkscore)

|  | Protocols |
| --- | --- |
| From | AnyObject, NSCoding, NSSecureCoding |
| To | NSCoding, NSSecureCoding |

Modified [GKScoreChallenge](https://developer.apple.com/documentation/gamekit/gkscorechallenge)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKTurnBasedExchange](https://developer.apple.com/documentation/gamekit/gkturnbasedexchange)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKTurnBasedExchangeReply](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangereply)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKTurnBasedExchangeStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedexchangestatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKTurnBasedMatch](https://developer.apple.com/documentation/gamekit/gkturnbasedmatch)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKTurnBasedMatchmakerViewController](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchmakerviewcontroller)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKTurnBasedMatchOutcome [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchoutcome)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKTurnBasedMatchStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedmatchstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKTurnBasedParticipant](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipant)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKTurnBasedParticipantStatus [enum]](https://developer.apple.com/documentation/gamekit/gkturnbasedparticipantstatus)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [GKVoiceChat](https://developer.apple.com/documentation/gamekit/gkvoicechat)

|  | Protocols |
| --- | --- |
| From | AnyObject |
| To | -- |

Modified [GKVoiceChatPlayerState [enum]](https://developer.apple.com/documentation/gamekit/gkvoicechatplayerstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

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
