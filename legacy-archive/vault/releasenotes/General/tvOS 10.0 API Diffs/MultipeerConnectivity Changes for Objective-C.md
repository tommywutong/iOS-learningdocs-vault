---
title: tvOS 10.0 API Diffs
apple_id: TP40017336
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS10APIDiffs/Objective-C/MultipeerConnectivity.html
archived_at: '2026-07-18T02:57:27.344401Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 10.0 API Diffs](tvOS%209.2%20to%20tvOS%2010.0%20API%20Diffs.md)


# MultipeerConnectivity Changes for Objective-C

### MultipeerConnectivity (Added)

#### MCAdvertiserAssistant.h (Added)

Added [MCAdvertiserAssistant](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant)Added [MCAdvertiserAssistant.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407041-delegate)Added [MCAdvertiserAssistant.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406952-discoveryinfo)Added [-[MCAdvertiserAssistant initWithServiceType:discoveryInfo:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406990-init)Added [MCAdvertiserAssistant.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407062-servicetype)Added [MCAdvertiserAssistant.session](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406924-session)Added [-[MCAdvertiserAssistant start]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407085-start)Added [-[MCAdvertiserAssistant stop]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406986-stop)Added [MCAdvertiserAssistantDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate)Added [-[MCAdvertiserAssistantDelegate advertiserAssistantDidDismissInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406922-advertiserassistantdiddismissinv)Added [-[MCAdvertiserAssistantDelegate advertiserAssistantWillPresentInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406978-advertiserassistantwillpresentin)

#### MCBrowserViewController.h (Added)

Added [MCBrowserViewController](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller)Added [MCBrowserViewController.browser](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406969-browser)Added [MCBrowserViewController.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406982-delegate)Added [-[MCBrowserViewController initWithBrowser:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406963-init)Added [-[MCBrowserViewController initWithServiceType:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406915-init)Added [MCBrowserViewController.maximumNumberOfPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406954-maximumnumberofpeers)Added [MCBrowserViewController.minimumNumberOfPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1407043-minimumnumberofpeers)Added [MCBrowserViewController.session](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406976-session)Added [MCBrowserViewControllerDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate)Added [-[MCBrowserViewControllerDelegate browserViewController:shouldPresentNearbyPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407039-browserviewcontroller)Added [-[MCBrowserViewControllerDelegate browserViewControllerDidFinish:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407002-browserviewcontrollerdidfinish)Added [-[MCBrowserViewControllerDelegate browserViewControllerWasCancelled:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1406942-browserviewcontrollerwascancelle)

#### MCError.h (Added)

Added #def MC_EXTERNAdded #def MC_EXTERN_CLASSAdded #def MC_EXTERN_WEAKAdded [MCErrorCancelled](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrorcancelled)Added [MCErrorCode](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode)Added [MCErrorDomain](https://developer.apple.com/documentation/multipeerconnectivity/mcerrordomain)Added [MCErrorInvalidParameter](https://developer.apple.com/documentation/multipeerconnectivity/mcerror/code/invalidparameter)Added [MCErrorNotConnected](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrornotconnected)Added [MCErrorTimedOut](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrortimedout)Added [MCErrorUnavailable](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrorunavailable)Added [MCErrorUnknown](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrorunknown)Added [MCErrorUnsupported](https://developer.apple.com/documentation/multipeerconnectivity/mcerrorcode/mcerrorunsupported)

#### MCNearbyServiceAdvertiser.h (Added)

Added [MCNearbyServiceAdvertiser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser)Added [MCNearbyServiceAdvertiser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407031-delegate)Added [MCNearbyServiceAdvertiser.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1406967-discoveryinfo)Added [-[MCNearbyServiceAdvertiser initWithPeer:discoveryInfo:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407102-initwithpeer)Added [MCNearbyServiceAdvertiser.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407022-mypeerid)Added [MCNearbyServiceAdvertiser.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407108-servicetype)Added [-[MCNearbyServiceAdvertiser startAdvertisingPeer]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407006-startadvertisingpeer)Added [-[MCNearbyServiceAdvertiser stopAdvertisingPeer]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407010-stopadvertisingpeer)Added [MCNearbyServiceAdvertiserDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate)Added [-[MCNearbyServiceAdvertiserDelegate advertiser:didNotStartAdvertisingPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1407100-advertiser)Added [-[MCNearbyServiceAdvertiserDelegate advertiser:didReceiveInvitationFromPeer:withContext:invitationHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1406971-advertiser)

#### MCNearbyServiceBrowser.h (Added)

Added [MCNearbyServiceBrowser](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser)Added [MCNearbyServiceBrowser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407079-delegate)Added [-[MCNearbyServiceBrowser initWithPeer:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407094-init)Added [-[MCNearbyServiceBrowser invitePeer:toSession:withContext:timeout:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1406944-invitepeer)Added [MCNearbyServiceBrowser.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407050-mypeerid)Added [MCNearbyServiceBrowser.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407110-servicetype)Added [-[MCNearbyServiceBrowser startBrowsingForPeers]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1406956-startbrowsingforpeers)Added [-[MCNearbyServiceBrowser stopBrowsingForPeers]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407033-stopbrowsingforpeers)Added [MCNearbyServiceBrowserDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate)Added [-[MCNearbyServiceBrowserDelegate browser:didNotStartBrowsingForPeers:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406913-browser)Added [-[MCNearbyServiceBrowserDelegate browser:foundPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406926-browser)Added [-[MCNearbyServiceBrowserDelegate browser:lostPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1407014-browser)

#### MCPeerID.h (Added)

Added [MCPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid)Added [MCPeerID.displayName](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407077-displayname)Added [-[MCPeerID initWithDisplayName:]](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407089-init)

#### MCSession.h (Added)

Added [MCSession](https://developer.apple.com/documentation/multipeerconnectivity/mcsession)Added [-[MCSession cancelConnectPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407106-cancelconnectpeer)Added [MCSession.connectedPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406911-connectedpeers)Added [-[MCSession connectPeer:withNearbyConnectionData:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407054-connectpeer)Added [MCSession.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407112-delegate)Added [-[MCSession disconnect]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407004-disconnect)Added [MCSession.encryptionPreference](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407081-encryptionpreference)Added [-[MCSession initWithPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407000-initwithpeer)Added [-[MCSession initWithPeer:securityIdentity:encryptionPreference:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407025-init)Added [MCSession.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406992-mypeerid)Added [-[MCSession nearbyConnectionDataForPeer:withCompletionHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407060-nearbyconnectiondata)Added [MCSession.securityIdentity](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406980-securityidentity)Added [-[MCSession sendData:toPeers:withMode:error:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406997-send)Added [-[MCSession sendResourceAtURL:withName:toPeer:withCompletionHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407056-sendresourceaturl)Added [-[MCSession startStreamWithName:toPeer:error:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407071-startstream)Added [MCSessionDelegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate)Added [-[MCSessionDelegate session:didFinishReceivingResourceWithName:fromPeer:atURL:withError:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406984-session)Added [-[MCSessionDelegate session:didReceiveCertificate:fromPeer:certificateHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1407067-session)Added [-[MCSessionDelegate session:didReceiveData:fromPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406934-session)Added [-[MCSessionDelegate session:didReceiveStream:withName:fromPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406917-session)Added [-[MCSessionDelegate session:didStartReceivingResourceWithName:fromPeer:withProgress:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406965-session)Added [-[MCSessionDelegate session:peer:didChangeState:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406958-session)Added [kMCSessionMaximumNumberOfPeers](https://developer.apple.com/documentation/multipeerconnectivity/kmcsessionmaximumnumberofpeers)Added [kMCSessionMinimumNumberOfPeers](https://developer.apple.com/documentation/multipeerconnectivity/kmcsessionminimumnumberofpeers)Added [MCEncryptionNone](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference/mcencryptionnone)Added [MCEncryptionOptional](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference/mcencryptionoptional)Added [MCEncryptionPreference](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference)Added [MCEncryptionRequired](https://developer.apple.com/documentation/multipeerconnectivity/mcencryptionpreference/mcencryptionrequired)Added MCSession(MCSessionCustomDiscovery)Added [MCSessionSendDataMode](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode)Added [MCSessionSendDataReliable](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode/mcsessionsenddatareliable)Added [MCSessionSendDataUnreliable](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionsenddatamode/mcsessionsenddataunreliable)Added [MCSessionState](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate)Added [MCSessionStateConnected](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate/mcsessionstateconnected)Added [MCSessionStateConnecting](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate/mcsessionstateconnecting)Added [MCSessionStateNotConnected](https://developer.apple.com/documentation/multipeerconnectivity/mcsessionstate/mcsessionstatenotconnected)

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
