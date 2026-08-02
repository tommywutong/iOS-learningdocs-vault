---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/MultipeerConnectivity.html
archived_at: '2026-07-15T07:34:56.112694Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# MultipeerConnectivity Changes

## MultipeerConnectivity (Added)

Added MCAdvertiserAssistantAdded MCAdvertiserAssistant.delegateAdded MCAdvertiserAssistant.discoveryInfoAdded MCAdvertiserAssistant.serviceTypeAdded MCAdvertiserAssistant.init(serviceType: String!, discoveryInfo:[NSObject: AnyObject]!, session: MCSession!)Added MCAdvertiserAssistant.sessionAdded MCAdvertiserAssistant.start()Added MCAdvertiserAssistant.stop()Added MCAdvertiserAssistantDelegateAdded MCAdvertiserAssistantDelegate.advertiserAssistantDidDismissInvitation(MCAdvertiserAssistant!)Added MCAdvertiserAssistantDelegate.advertiserAssistantWillPresentInvitation(MCAdvertiserAssistant!)Added MCBrowserViewControllerAdded MCBrowserViewController.browserAdded MCBrowserViewController.init(browser: MCNearbyServiceBrowser!, session: MCSession!)Added MCBrowserViewController.delegateAdded MCBrowserViewController.maximumNumberOfPeersAdded MCBrowserViewController.minimumNumberOfPeersAdded MCBrowserViewController.init(serviceType: String!, session: MCSession!)Added MCBrowserViewController.sessionAdded MCBrowserViewControllerDelegateAdded MCBrowserViewControllerDelegate.browserViewController(MCBrowserViewController!, shouldPresentNearbyPeer: MCPeerID!, withDiscoveryInfo:[NSObject: AnyObject]!) -> BoolAdded MCBrowserViewControllerDelegate.browserViewControllerDidFinish(MCBrowserViewController!)Added MCBrowserViewControllerDelegate.browserViewControllerWasCancelled(MCBrowserViewController!)Added MCEncryptionPreference [enum]Added MCEncryptionPreference.NoneAdded MCEncryptionPreference.OptionalAdded MCEncryptionPreference.RequiredAdded MCErrorCode [enum]Added MCErrorCode.CancelledAdded MCErrorCode.InvalidParameterAdded MCErrorCode.NotConnectedAdded MCErrorCode.TimedOutAdded MCErrorCode.UnavailableAdded MCErrorCode.UnknownAdded MCErrorCode.UnsupportedAdded MCNearbyServiceAdvertiserAdded MCNearbyServiceAdvertiser.delegateAdded MCNearbyServiceAdvertiser.discoveryInfoAdded MCNearbyServiceAdvertiser.myPeerIDAdded MCNearbyServiceAdvertiser.init(peer: MCPeerID!, discoveryInfo:[NSObject: AnyObject]!, serviceType: String!)Added MCNearbyServiceAdvertiser.serviceTypeAdded MCNearbyServiceAdvertiser.startAdvertisingPeer()Added MCNearbyServiceAdvertiser.stopAdvertisingPeer()Added MCNearbyServiceAdvertiserDelegateAdded MCNearbyServiceAdvertiserDelegate.advertiser(MCNearbyServiceAdvertiser!, didNotStartAdvertisingPeer: NSError!)Added MCNearbyServiceAdvertiserDelegate.advertiser(MCNearbyServiceAdvertiser!, didReceiveInvitationFromPeer: MCPeerID!, withContext: NSData!, invitationHandler:((Bool, MCSession!) -> Void)!)Added MCNearbyServiceBrowserAdded MCNearbyServiceBrowser.delegateAdded MCNearbyServiceBrowser.invitePeer(MCPeerID!, toSession: MCSession!, withContext: NSData!, timeout: NSTimeInterval)Added MCNearbyServiceBrowser.myPeerIDAdded MCNearbyServiceBrowser.init(peer: MCPeerID!, serviceType: String!)Added MCNearbyServiceBrowser.serviceTypeAdded MCNearbyServiceBrowser.startBrowsingForPeers()Added MCNearbyServiceBrowser.stopBrowsingForPeers()Added MCNearbyServiceBrowserDelegateAdded MCNearbyServiceBrowserDelegate.browser(MCNearbyServiceBrowser!, didNotStartBrowsingForPeers: NSError!)Added MCNearbyServiceBrowserDelegate.browser(MCNearbyServiceBrowser!, foundPeer: MCPeerID!, withDiscoveryInfo:[NSObject: AnyObject]!)Added MCNearbyServiceBrowserDelegate.browser(MCNearbyServiceBrowser!, lostPeer: MCPeerID!)Added MCPeerIDAdded MCPeerID.displayNameAdded MCPeerID.init(displayName: String!)Added MCSessionAdded MCSession.cancelConnectPeer(MCPeerID!)Added MCSession.connectPeer(MCPeerID!, withNearbyConnectionData: NSData!)Added MCSession.connectedPeersAdded MCSession.delegateAdded MCSession.disconnect()Added MCSession.encryptionPreferenceAdded MCSession.myPeerIDAdded MCSession.nearbyConnectionDataForPeer(MCPeerID!, withCompletionHandler:((NSData!, NSError!) -> Void)!)Added MCSession.init(peer: MCPeerID!)Added MCSession.init(peer: MCPeerID!, securityIdentity:[AnyObject]!, encryptionPreference: MCEncryptionPreference)Added MCSession.securityIdentityAdded MCSession.sendData(NSData!, toPeers:[AnyObject]!, withMode: MCSessionSendDataMode, error: NSErrorPointer) -> BoolAdded MCSession.sendResourceAtURL(NSURL!, withName: String!, toPeer: MCPeerID!, withCompletionHandler:((NSError!) -> Void)!) -> NSProgress!Added MCSession.startStreamWithName(String!, toPeer: MCPeerID!, error: NSErrorPointer) -> NSOutputStream!Added MCSessionDelegateAdded MCSessionDelegate.session(MCSession!, didFinishReceivingResourceWithName: String!, fromPeer: MCPeerID!, atURL: NSURL!, withError: NSError!)Added MCSessionDelegate.session(MCSession!, didReceiveCertificate:[AnyObject]!, fromPeer: MCPeerID!, certificateHandler:((Bool) -> Void)!)Added MCSessionDelegate.session(MCSession!, didReceiveData: NSData!, fromPeer: MCPeerID!)Added MCSessionDelegate.session(MCSession!, didReceiveStream: NSInputStream!, withName: String!, fromPeer: MCPeerID!)Added MCSessionDelegate.session(MCSession!, didStartReceivingResourceWithName: String!, fromPeer: MCPeerID!, withProgress: NSProgress!)Added MCSessionDelegate.session(MCSession!, peer: MCPeerID!, didChangeState: MCSessionState)Added MCSessionSendDataMode [enum]Added MCSessionSendDataMode.ReliableAdded MCSessionSendDataMode.UnreliableAdded MCSessionState [enum]Added MCSessionState.ConnectedAdded MCSessionState.ConnectingAdded MCSessionState.NotConnectedAdded MCErrorDomainAdded kMCSessionMaximumNumberOfPeersAdded kMCSessionMinimumNumberOfPeers

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
