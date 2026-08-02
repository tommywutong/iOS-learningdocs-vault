---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/GameKit.html
archived_at: '2026-07-18T02:50:39.286947Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# GameKit Changes for Objective-C

### GameKit

#### GKBasePlayer.h (Added)

Added [GKBasePlayer](https://developer.apple.com/documentation/gamekit/gkbaseplayer)Added [GKBasePlayer.displayName](https://developer.apple.com/documentation/gamekit/gkbaseplayer/1641907-displayname)Added [GKBasePlayer.playerID](https://developer.apple.com/documentation/gamekit/gkbaseplayer/1641912-playerid)

#### GKCloudPlayer.h (Added)

Added [GKCloudPlayer](https://developer.apple.com/documentation/gamekit/gkcloudplayer)Added [+[GKCloudPlayer getCurrentSignedInPlayerForContainer:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkcloudplayer/2172413-getcurrentsignedinplayer)

#### GKError.h

Added [GKErrorGameSessionRequestInvalid](https://developer.apple.com/documentation/gamekit/gkerrorcode/gkerrorgamesessionrequestinvalid)Added [GKErrorMatchNotConnected](https://developer.apple.com/documentation/gamekit/gkerror/code/matchnotconnected)

#### GKFriendRequestComposeViewController.h

Modified [GKFriendRequestComposeViewController](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontroller)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

Modified [-[GKFriendRequestComposeViewControllerDelegate friendRequestComposeViewControllerDidFinish:]](https://developer.apple.com/documentation/gamekit/gkfriendrequestcomposeviewcontrollerdelegate/1437186-friendrequestcomposeviewcontroll)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### GKGameSession.h (Added)

Added [GKGameSession](https://developer.apple.com/documentation/gamekit/gkgamesession)Added [GKGameSession.badgedPlayers](https://developer.apple.com/documentation/gamekit/gkgamesession/1641884-badgedplayers)Added [-[GKGameSession clearBadgeForPlayers:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641900-clearbadge)Added [+[GKGameSession createSessionInContainer:withTitle:maxConnectedPlayers:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641863-createsessionincontainer)Added [-[GKGameSession getShareURLWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641893-getshareurl)Added [GKGameSession.identifier](https://developer.apple.com/documentation/gamekit/gkgamesession/1641891-identifier)Added [GKGameSession.lastModifiedDate](https://developer.apple.com/documentation/gamekit/gkgamesession/1641854-lastmodifieddate)Added [GKGameSession.lastModifiedPlayer](https://developer.apple.com/documentation/gamekit/gkgamesession/1641882-lastmodifiedplayer)Added [-[GKGameSession loadDataWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641899-loaddatawithcompletionhandler)Added [+[GKGameSession loadSessionsInContainer:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641908-loadsessions)Added [+[GKGameSession loadSessionWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641894-loadsessionwithidentifier)Added [GKGameSession.maxNumberOfConnectedPlayers](https://developer.apple.com/documentation/gamekit/gkgamesession/1641876-maxnumberofconnectedplayers)Added [GKGameSession.owner](https://developer.apple.com/documentation/gamekit/gkgamesession/1641896-owner)Added [GKGameSession.players](https://developer.apple.com/documentation/gamekit/gkgamesession/1641906-players)Added [-[GKGameSession playersWithConnectionState:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641877-playerswithconnectionstate)Added [+[GKGameSession removeSessionWithIdentifier:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641875-remove)Added [-[GKGameSession saveData:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641903-save)Added [-[GKGameSession sendData:withTransportType:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641880-send)Added [-[GKGameSession sendMessageWithLocalizedFormatKey:arguments:data:toPlayers:badgePlayers:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641868-sendmessage)Added [-[GKGameSession setConnectionState:completionHandler:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641885-setconnectionstate)Added [GKGameSession.title](https://developer.apple.com/documentation/gamekit/gkgamesession/1641910-title)Added [GKConnectionState](https://developer.apple.com/documentation/gamekit/gkconnectionstate)Added [GKConnectionStateConnected](https://developer.apple.com/documentation/gamekit/gkconnectionstate/gkconnectionstateconnected)Added [GKConnectionStateNotConnected](https://developer.apple.com/documentation/gamekit/gkconnectionstate/gkconnectionstatenotconnected)Added [GKTransportType](https://developer.apple.com/documentation/gamekit/gktransporttype)Added [GKTransportTypeReliable](https://developer.apple.com/documentation/gamekit/gktransporttype/gktransporttypereliable)Added [GKTransportTypeUnreliable](https://developer.apple.com/documentation/gamekit/gktransporttype/unreliable)

#### GKGameSessionError.h (Added)

Added [GKGameSessionErrorBadContainer](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorbadcontainer)Added [GKGameSessionErrorCloudDriveDisabled](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorclouddrivedisabled)Added [GKGameSessionErrorCloudQuotaExceeded](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorcloudquotaexceeded)Added [GKGameSessionErrorCode](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode)Added [GKGameSessionErrorConnectionCancelledByUser](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/connectioncancelledbyuser)Added [GKGameSessionErrorConnectionFailed](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/connectionfailed)Added [GKGameSessionErrorDomain](https://developer.apple.com/documentation/gamekit/gkgamesessionerrordomain)Added [GKGameSessionErrorInvalidSession](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorinvalidsession)Added [GKGameSessionErrorNetworkFailure](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/networkfailure)Added [GKGameSessionErrorNotAuthenticated](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/notauthenticated)Added [GKGameSessionErrorSendDataNoRecipients](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsenddatanorecipients)Added [GKGameSessionErrorSendDataNotConnected](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsenddatanotconnected)Added [GKGameSessionErrorSendDataNotReachable](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsenddatanotreachable)Added [GKGameSessionErrorSendRateLimitReached](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsendratelimitreached)Added [GKGameSessionErrorSessionConflict](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/sessionconflict)Added [GKGameSessionErrorSessionHasMaxConnectedPlayers](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsessionhasmaxconnectedplayers)Added [GKGameSessionErrorSessionNotShared](https://developer.apple.com/documentation/gamekit/gkgamesessionerrorcode/gkgamesessionerrorsessionnotshared)Added [GKGameSessionErrorUnknown](https://developer.apple.com/documentation/gamekit/gkgamesessionerror/code/unknown)

#### GKGameSessionEventListener.h (Added)

Added [+[GKGameSession addEventListener:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641889-addeventlistener)Added [+[GKGameSession removeEventListener:]](https://developer.apple.com/documentation/gamekit/gkgamesession/1641886-removeeventlistener)Added [GKGameSessionEventListener](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener)Added [-[GKGameSessionEventListener session:didAddPlayer:]](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641867-session)Added [-[GKGameSessionEventListener session:didReceiveData:fromPlayer:]](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641857-session)Added [-[GKGameSessionEventListener session:didReceiveMessage:withData:fromPlayer:]](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641879-session)Added [-[GKGameSessionEventListener session:didRemovePlayer:]](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641881-session)Added [-[GKGameSessionEventListener session:player:didChangeConnectionState:]](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641861-session)Added [-[GKGameSessionEventListener session:player:didSaveData:]](https://developer.apple.com/documentation/gamekit/gkgamesessioneventlistener/1641888-session)Added GKGameSession(GKGameSessionEventListener)

#### GKLocalPlayer.h

Added [-[GKLocalPlayer loadRecentPlayersWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1833711-loadrecentplayerswithcompletionh)Modified [-[GKLocalPlayer loadFriendPlayersWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515386-loadfriendplayers)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.12 |

#### GKPlayer.h

Modified [GKPlayer](https://developer.apple.com/documentation/gamekit/gkplayer)

|  | Superclasses |
| --- | --- |
| From | NSObject |
| To | GKBasePlayer |

#### GKTurnBasedMatch.h

Modified [-[GKTurnBasedEventHandlerDelegate handleInviteFromGameCenter:]](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandlerdelegate/1520926-handleinvite)

|  | Declaration |
| --- | --- |
| From | ``` - (void)handleInviteFromGameCenter:(NSArray<GKPlayer *> *)playersToInvite ``` |
| To | ``` - (void)handleInviteFromGameCenter:(NSArray<NSString *> *)playersToInvite ``` |

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
