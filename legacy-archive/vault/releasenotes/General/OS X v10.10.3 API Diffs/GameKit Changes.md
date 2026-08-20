---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/GameKit.html
archived_at: '2026-07-18T02:51:49.394723Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# GameKit Changes

## GameKit

GKAchievementViewController.hModified [-[GKAchievementViewControllerDelegate achievementViewControllerDidFinish:]](https://developer.apple.com/documentation/gamekit/gkachievementviewcontrollerdelegate/1521156-achievementviewcontrollerdidfini)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

GKChallengeEventHandler.hModified [-[GKChallengeEventHandlerDelegate localPlayerDidCompleteChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1521031-localplayerdidcompletechallenge)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKChallengeEventHandlerDelegate localPlayerDidReceiveChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520987-localplayerdidreceive)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKChallengeEventHandlerDelegate localPlayerDidSelectChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520995-localplayerdidselectchallenge)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKChallengeEventHandlerDelegate remotePlayerDidCompleteChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520880-remoteplayerdidcomplete)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKChallengeEventHandlerDelegate shouldShowBannerForLocallyCompletedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520924-shouldshowbanner)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKChallengeEventHandlerDelegate shouldShowBannerForLocallyReceivedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1521055-shouldshowbanner)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKChallengeEventHandlerDelegate shouldShowBannerForRemotelyCompletedChallenge:]](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandlerdelegate/1520499-shouldshowbanner)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

GKChallengesViewController.hModified [GKChallengesViewController.challengeDelegate](https://developer.apple.com/documentation/gamekit/gkchallengesviewcontroller/1470742-challengedelegate)

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
| From | ``` @property(assign) NSWindow *parentWindow ``` |
| To | ``` @property(assign) IBOutlet NSWindow *parentWindow ``` |

GKGameCenterViewController.hModified [GKGameCenterViewController.leaderboardIdentifier](https://developer.apple.com/documentation/gamekit/gkgamecenterviewcontroller/1520540-leaderboardidentifier)

|  | Introduction |
| --- | --- |
| From | OS X 10.9 |
| To | OS X 10.10 |

GKLeaderboardViewController.hModified [-[GKLeaderboardViewControllerDelegate leaderboardViewControllerDidFinish:]](https://developer.apple.com/documentation/gamekit/gkleaderboardviewcontrollerdelegate/1521097-leaderboardviewcontrollerdidfini)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

GKLocalPlayer.hModified [-[GKLocalPlayer loadDefaultLeaderboardIdentifierWithCompletionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515404-loaddefaultleaderboardidentifier)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.10 |

Modified [-[GKLocalPlayer setDefaultLeaderboardIdentifier:completionHandler:]](https://developer.apple.com/documentation/gamekit/gklocalplayer/1515408-setdefaultleaderboardidentifier)

|  | Introduction |
| --- | --- |
| From | OS X 10.8 |
| To | OS X 10.10 |

GKSession.hModified [-[GKSession acceptConnectionFromPeer:error:]](https://developer.apple.com/documentation/gamekit/gksession/1520935-acceptconnection)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKSession.available](https://developer.apple.com/documentation/gamekit/gksession/1520566-isavailable)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKSession cancelConnectToPeer:]](https://developer.apple.com/documentation/gamekit/gksession/1520823-cancelconnecttopeer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKSession connectToPeer:withTimeout:]](https://developer.apple.com/documentation/gamekit/gksession/1520572-connect)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKSession.delegate](https://developer.apple.com/documentation/gamekit/gksession/1520491-delegate)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKSession denyConnectionFromPeer:]](https://developer.apple.com/documentation/gamekit/gksession/1521117-denyconnectionfrompeer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKSession disconnectFromAllPeers]](https://developer.apple.com/documentation/gamekit/gksession/1521120-disconnectfromallpeers)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKSession disconnectPeerFromAllPeers:]](https://developer.apple.com/documentation/gamekit/gksession/1520534-disconnectpeer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKSession.disconnectTimeout](https://developer.apple.com/documentation/gamekit/gksession/1521193-disconnecttimeout)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKSession.displayName](https://developer.apple.com/documentation/gamekit/gksession/1520904-displayname)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKSession displayNameForPeer:]](https://developer.apple.com/documentation/gamekit/gksession/1520606-displaynameforpeer)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKSession.peerID](https://developer.apple.com/documentation/gamekit/gksession/1520703-peerid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [GKSession.sessionID](https://developer.apple.com/documentation/gamekit/gksession/1520620-sessionid)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

Modified [-[GKSession setDataReceiveHandler:withContext:]](https://developer.apple.com/documentation/gamekit/gksession/1520831-setdatareceivehandler)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.10 |

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
