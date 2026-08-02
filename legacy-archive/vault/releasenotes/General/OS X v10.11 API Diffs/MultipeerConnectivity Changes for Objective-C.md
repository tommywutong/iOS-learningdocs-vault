---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/MultipeerConnectivity.html
archived_at: '2026-07-18T02:53:10.706772Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# MultipeerConnectivity Changes for Objective-C

### MultipeerConnectivity

#### MCAdvertiserAssistant.h

Modified [MCAdvertiserAssistant.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407041-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, atomic) id<MCAdvertiserAssistantDelegate> delegate ``` |
| To | ``` @property(weak, atomic, nullable) id<MCAdvertiserAssistantDelegate> delegate ``` |

Modified [MCAdvertiserAssistant.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406952-discoveryinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSDictionary *discoveryInfo ``` |
| To | ``` @property(readonly, atomic, nullable) NSDictionary<NSString *,NSString *> *discoveryInfo ``` |

Modified [-[MCAdvertiserAssistant initWithServiceType:discoveryInfo:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406990-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithServiceType:(NSString *)serviceType discoveryInfo:(NSDictionary *)info session:(MCSession *)session ``` |
| To | ``` - (instancetype _Nonnull)initWithServiceType:(NSString * _Nonnull)serviceType discoveryInfo:(NSDictionary<NSString *,NSString *> * _Nullable)info session:(MCSession * _Nonnull)session ``` |

Modified [MCAdvertiserAssistant.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407062-servicetype)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *serviceType ``` |
| To | ``` @property(readonly, atomic, nonnull) NSString *serviceType ``` |

Modified [MCAdvertiserAssistant.session](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406924-session)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) MCSession *session ``` |
| To | ``` @property(readonly, atomic, nonnull) MCSession *session ``` |

Modified [-[MCAdvertiserAssistantDelegate advertiserAssistantDidDismissInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406922-advertiserassistantdiddismissinv)

|  | Declaration |
| --- | --- |
| From | ``` - (void)advertiserAssistantDidDismissInvitation:(MCAdvertiserAssistant *)advertiserAssistant ``` |
| To | ``` - (void)advertiserAssistantDidDismissInvitation:(MCAdvertiserAssistant * _Nonnull)advertiserAssistant ``` |

Modified [-[MCAdvertiserAssistantDelegate advertiserAssistantWillPresentInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406978-advertiserassistantwillpresentin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)advertiserAssistantWillPresentInvitation:(MCAdvertiserAssistant *)advertiserAssistant ``` |
| To | ``` - (void)advertiserAssistantWillPresentInvitation:(MCAdvertiserAssistant * _Nonnull)advertiserAssistant ``` |

#### MCBrowserViewController.h

Modified [MCBrowserViewController.browser](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406969-browser)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) MCNearbyServiceBrowser *browser ``` |
| To | ``` @property(readonly, atomic, nonnull) MCNearbyServiceBrowser *browser ``` |

Modified [MCBrowserViewController.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406982-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, atomic) id<MCBrowserViewControllerDelegate> delegate ``` |
| To | ``` @property(weak, atomic, nullable) id<MCBrowserViewControllerDelegate> delegate ``` |

Modified [-[MCBrowserViewController initWithBrowser:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406963-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithBrowser:(MCNearbyServiceBrowser *)browser session:(MCSession *)session ``` |
| To | ``` - (instancetype _Nonnull)initWithBrowser:(MCNearbyServiceBrowser * _Nonnull)browser session:(MCSession * _Nonnull)session ``` |

Modified [-[MCBrowserViewController initWithServiceType:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406915-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithServiceType:(NSString *)serviceType session:(MCSession *)session ``` |
| To | ``` - (instancetype _Nonnull)initWithServiceType:(NSString * _Nonnull)serviceType session:(MCSession * _Nonnull)session ``` |

Modified [MCBrowserViewController.session](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406976-session)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) MCSession *session ``` |
| To | ``` @property(readonly, atomic, nonnull) MCSession *session ``` |

Modified [-[MCBrowserViewControllerDelegate browserViewController:shouldPresentNearbyPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407039-browserviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)browserViewController:(MCBrowserViewController *)browserViewController shouldPresentNearbyPeer:(MCPeerID *)peerID withDiscoveryInfo:(NSDictionary *)info ``` |
| To | ``` - (BOOL)browserViewController:(MCBrowserViewController * _Nonnull)browserViewController shouldPresentNearbyPeer:(MCPeerID * _Nonnull)peerID withDiscoveryInfo:(NSDictionary<NSString *,NSString *> * _Nullable)info ``` |

Modified [-[MCBrowserViewControllerDelegate browserViewControllerDidFinish:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407002-browserviewcontrollerdidfinish)

|  | Declaration |
| --- | --- |
| From | ``` - (void)browserViewControllerDidFinish:(MCBrowserViewController *)browserViewController ``` |
| To | ``` - (void)browserViewControllerDidFinish:(MCBrowserViewController * _Nonnull)browserViewController ``` |

Modified [-[MCBrowserViewControllerDelegate browserViewControllerWasCancelled:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1406942-browserviewcontrollerwascancelle)

|  | Declaration |
| --- | --- |
| From | ``` - (void)browserViewControllerWasCancelled:(MCBrowserViewController *)browserViewController ``` |
| To | ``` - (void)browserViewControllerWasCancelled:(MCBrowserViewController * _Nonnull)browserViewController ``` |

#### MCNearbyServiceAdvertiser.h

Modified [MCNearbyServiceAdvertiser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407031-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, atomic) id<MCNearbyServiceAdvertiserDelegate> delegate ``` |
| To | ``` @property(weak, atomic, nullable) id<MCNearbyServiceAdvertiserDelegate> delegate ``` |

Modified [MCNearbyServiceAdvertiser.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1406967-discoveryinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSDictionary *discoveryInfo ``` |
| To | ``` @property(readonly, atomic, nullable) NSDictionary<NSString *,NSString *> *discoveryInfo ``` |

Modified [-[MCNearbyServiceAdvertiser initWithPeer:discoveryInfo:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407102-initwithpeer)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPeer:(MCPeerID *)myPeerID discoveryInfo:(NSDictionary *)info serviceType:(NSString *)serviceType ``` |
| To | ``` - (instancetype _Nonnull)initWithPeer:(MCPeerID * _Nonnull)myPeerID discoveryInfo:(NSDictionary<NSString *,NSString *> * _Nullable)info serviceType:(NSString * _Nonnull)serviceType ``` |

Modified [MCNearbyServiceAdvertiser.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407022-mypeerid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) MCPeerID *myPeerID ``` |
| To | ``` @property(readonly, atomic, nonnull) MCPeerID *myPeerID ``` |

Modified [MCNearbyServiceAdvertiser.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407108-servicetype)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *serviceType ``` |
| To | ``` @property(readonly, atomic, nonnull) NSString *serviceType ``` |

Modified [-[MCNearbyServiceAdvertiserDelegate advertiser:didNotStartAdvertisingPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1407100-advertiser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)advertiser:(MCNearbyServiceAdvertiser *)advertiser didNotStartAdvertisingPeer:(NSError *)error ``` |
| To | ``` - (void)advertiser:(MCNearbyServiceAdvertiser * _Nonnull)advertiser didNotStartAdvertisingPeer:(NSError * _Nonnull)error ``` |

Modified [-[MCNearbyServiceAdvertiserDelegate advertiser:didReceiveInvitationFromPeer:withContext:invitationHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1406971-advertiser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)advertiser:(MCNearbyServiceAdvertiser *)advertiser didReceiveInvitationFromPeer:(MCPeerID *)peerID withContext:(NSData *)context invitationHandler:(void (^)(BOOL accept, MCSession *session))invitationHandler ``` |
| To | ``` - (void)advertiser:(MCNearbyServiceAdvertiser * _Nonnull)advertiser didReceiveInvitationFromPeer:(MCPeerID * _Nonnull)peerID withContext:(NSData * _Nullable)context invitationHandler:(void (^ _Nonnull)(BOOL accept, MCSession * _Nonnull session))invitationHandler ``` |

#### MCNearbyServiceBrowser.h

Modified [MCNearbyServiceBrowser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407079-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, atomic) id<MCNearbyServiceBrowserDelegate> delegate ``` |
| To | ``` @property(weak, atomic, nullable) id<MCNearbyServiceBrowserDelegate> delegate ``` |

Modified [-[MCNearbyServiceBrowser initWithPeer:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407094-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPeer:(MCPeerID *)myPeerID serviceType:(NSString *)serviceType ``` |
| To | ``` - (instancetype _Nonnull)initWithPeer:(MCPeerID * _Nonnull)myPeerID serviceType:(NSString * _Nonnull)serviceType ``` |

Modified [-[MCNearbyServiceBrowser invitePeer:toSession:withContext:timeout:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1406944-invitepeer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)invitePeer:(MCPeerID *)peerID toSession:(MCSession *)session withContext:(NSData *)context timeout:(NSTimeInterval)timeout ``` |
| To | ``` - (void)invitePeer:(MCPeerID * _Nonnull)peerID toSession:(MCSession * _Nonnull)session withContext:(NSData * _Nullable)context timeout:(NSTimeInterval)timeout ``` |

Modified [MCNearbyServiceBrowser.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407050-mypeerid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) MCPeerID *myPeerID ``` |
| To | ``` @property(readonly, atomic, nonnull) MCPeerID *myPeerID ``` |

Modified [MCNearbyServiceBrowser.serviceType](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407110-servicetype)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *serviceType ``` |
| To | ``` @property(readonly, atomic, nonnull) NSString *serviceType ``` |

Modified [-[MCNearbyServiceBrowserDelegate browser:didNotStartBrowsingForPeers:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406913-browser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)browser:(MCNearbyServiceBrowser *)browser didNotStartBrowsingForPeers:(NSError *)error ``` |
| To | ``` - (void)browser:(MCNearbyServiceBrowser * _Nonnull)browser didNotStartBrowsingForPeers:(NSError * _Nonnull)error ``` |

Modified [-[MCNearbyServiceBrowserDelegate browser:foundPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406926-browser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)browser:(MCNearbyServiceBrowser *)browser foundPeer:(MCPeerID *)peerID withDiscoveryInfo:(NSDictionary *)info ``` |
| To | ``` - (void)browser:(MCNearbyServiceBrowser * _Nonnull)browser foundPeer:(MCPeerID * _Nonnull)peerID withDiscoveryInfo:(NSDictionary<NSString *,NSString *> * _Nullable)info ``` |

Modified [-[MCNearbyServiceBrowserDelegate browser:lostPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1407014-browser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)browser:(MCNearbyServiceBrowser *)browser lostPeer:(MCPeerID *)peerID ``` |
| To | ``` - (void)browser:(MCNearbyServiceBrowser * _Nonnull)browser lostPeer:(MCPeerID * _Nonnull)peerID ``` |

#### MCPeerID.h

Modified [MCPeerID.displayName](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407077-displayname)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSString *displayName ``` |
| To | ``` @property(readonly, atomic, nonnull) NSString *displayName ``` |

Modified [-[MCPeerID initWithDisplayName:]](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407089-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithDisplayName:(NSString *)myDisplayName ``` |
| To | ``` - (instancetype _Nonnull)initWithDisplayName:(NSString * _Nonnull)myDisplayName ``` |

#### MCSession.h

Modified [-[MCSession cancelConnectPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407106-cancelconnectpeer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)cancelConnectPeer:(MCPeerID *)peerID ``` |
| To | ``` - (void)cancelConnectPeer:(MCPeerID * _Nonnull)peerID ``` |

Modified [MCSession.connectedPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406911-connectedpeers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *connectedPeers ``` |
| To | ``` @property(readonly, atomic, nonnull) NSArray<MCPeerID *> *connectedPeers ``` |

Modified [-[MCSession connectPeer:withNearbyConnectionData:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407054-connectpeer)

|  | Declaration |
| --- | --- |
| From | ``` - (void)connectPeer:(MCPeerID *)peerID withNearbyConnectionData:(NSData *)data ``` |
| To | ``` - (void)connectPeer:(MCPeerID * _Nonnull)peerID withNearbyConnectionData:(NSData * _Nonnull)data ``` |

Modified [MCSession.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407112-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(weak, atomic) id<MCSessionDelegate> delegate ``` |
| To | ``` @property(weak, atomic, nullable) id<MCSessionDelegate> delegate ``` |

Modified [-[MCSession initWithPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407000-initwithpeer)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPeer:(MCPeerID *)myPeerID ``` |
| To | ``` - (instancetype _Nonnull)initWithPeer:(MCPeerID * _Nonnull)myPeerID ``` |

Modified [-[MCSession initWithPeer:securityIdentity:encryptionPreference:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407025-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPeer:(MCPeerID *)myPeerID securityIdentity:(NSArray *)identity encryptionPreference:(MCEncryptionPreference)encryptionPreference ``` |
| To | ``` - (instancetype _Nonnull)initWithPeer:(MCPeerID * _Nonnull)myPeerID securityIdentity:(NSArray * _Nullable)identity encryptionPreference:(MCEncryptionPreference)encryptionPreference ``` |

Modified [MCSession.myPeerID](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406992-mypeerid)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) MCPeerID *myPeerID ``` |
| To | ``` @property(readonly, atomic, nonnull) MCPeerID *myPeerID ``` |

Modified [-[MCSession nearbyConnectionDataForPeer:withCompletionHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407060-nearbyconnectiondata)

|  | Declaration |
| --- | --- |
| From | ``` - (void)nearbyConnectionDataForPeer:(MCPeerID *)peerID withCompletionHandler:(void (^)(NSData *connectionData, NSError *error))completionHandler ``` |
| To | ``` - (void)nearbyConnectionDataForPeer:(MCPeerID * _Nonnull)peerID withCompletionHandler:(void (^ _Nonnull)(NSData * _Nonnull connectionData, NSError * _Nullable error))completionHandler ``` |

Modified [MCSession.securityIdentity](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406980-securityidentity)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, atomic) NSArray *securityIdentity ``` |
| To | ``` @property(readonly, atomic, nullable) NSArray *securityIdentity ``` |

Modified [-[MCSession sendData:toPeers:withMode:error:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406997-send)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendData:(NSData *)data toPeers:(NSArray *)peerIDs withMode:(MCSessionSendDataMode)mode error:(NSError **)error ``` |
| To | ``` - (BOOL)sendData:(NSData * _Nonnull)data toPeers:(NSArray<MCPeerID *> * _Nonnull)peerIDs withMode:(MCSessionSendDataMode)mode error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[MCSession sendResourceAtURL:withName:toPeer:withCompletionHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407056-sendresourceaturl)

|  | Declaration |
| --- | --- |
| From | ``` - (NSProgress *)sendResourceAtURL:(NSURL *)resourceURL withName:(NSString *)resourceName toPeer:(MCPeerID *)peerID withCompletionHandler:(void (^)(NSError *error))completionHandler ``` |
| To | ``` - (NSProgress * _Nullable)sendResourceAtURL:(NSURL * _Nonnull)resourceURL withName:(NSString * _Nonnull)resourceName toPeer:(MCPeerID * _Nonnull)peerID withCompletionHandler:(void (^ _Nullable)(NSError * _Nullable error))completionHandler ``` |

Modified [-[MCSession startStreamWithName:toPeer:error:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407071-startstream)

|  | Declaration |
| --- | --- |
| From | ``` - (NSOutputStream *)startStreamWithName:(NSString *)streamName toPeer:(MCPeerID *)peerID error:(NSError **)error ``` |
| To | ``` - (NSOutputStream * _Nullable)startStreamWithName:(NSString * _Nonnull)streamName toPeer:(MCPeerID * _Nonnull)peerID error:(NSError * _Nullable * _Nullable)error ``` |

Modified [-[MCSessionDelegate session:didFinishReceivingResourceWithName:fromPeer:atURL:withError:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406984-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(MCSession *)session didFinishReceivingResourceWithName:(NSString *)resourceName fromPeer:(MCPeerID *)peerID atURL:(NSURL *)localURL withError:(NSError *)error ``` |
| To | ``` - (void)session:(MCSession * _Nonnull)session didFinishReceivingResourceWithName:(NSString * _Nonnull)resourceName fromPeer:(MCPeerID * _Nonnull)peerID atURL:(NSURL * _Nonnull)localURL withError:(NSError * _Nullable)error ``` |

Modified [-[MCSessionDelegate session:didReceiveCertificate:fromPeer:certificateHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1407067-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(MCSession *)session didReceiveCertificate:(NSArray *)certificate fromPeer:(MCPeerID *)peerID certificateHandler:(void (^)(BOOL accept))certificateHandler ``` |
| To | ``` - (void)session:(MCSession * _Nonnull)session didReceiveCertificate:(NSArray * _Nullable)certificate fromPeer:(MCPeerID * _Nonnull)peerID certificateHandler:(void (^ _Nonnull)(BOOL accept))certificateHandler ``` |

Modified [-[MCSessionDelegate session:didReceiveData:fromPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406934-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(MCSession *)session didReceiveData:(NSData *)data fromPeer:(MCPeerID *)peerID ``` |
| To | ``` - (void)session:(MCSession * _Nonnull)session didReceiveData:(NSData * _Nonnull)data fromPeer:(MCPeerID * _Nonnull)peerID ``` |

Modified [-[MCSessionDelegate session:didReceiveStream:withName:fromPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406917-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(MCSession *)session didReceiveStream:(NSInputStream *)stream withName:(NSString *)streamName fromPeer:(MCPeerID *)peerID ``` |
| To | ``` - (void)session:(MCSession * _Nonnull)session didReceiveStream:(NSInputStream * _Nonnull)stream withName:(NSString * _Nonnull)streamName fromPeer:(MCPeerID * _Nonnull)peerID ``` |

Modified [-[MCSessionDelegate session:didStartReceivingResourceWithName:fromPeer:withProgress:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406965-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(MCSession *)session didStartReceivingResourceWithName:(NSString *)resourceName fromPeer:(MCPeerID *)peerID withProgress:(NSProgress *)progress ``` |
| To | ``` - (void)session:(MCSession * _Nonnull)session didStartReceivingResourceWithName:(NSString * _Nonnull)resourceName fromPeer:(MCPeerID * _Nonnull)peerID withProgress:(NSProgress * _Nonnull)progress ``` |

Modified [-[MCSessionDelegate session:peer:didChangeState:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1406958-session)

|  | Declaration |
| --- | --- |
| From | ``` - (void)session:(MCSession *)session peer:(MCPeerID *)peerID didChangeState:(MCSessionState)state ``` |
| To | ``` - (void)session:(MCSession * _Nonnull)session peer:(MCPeerID * _Nonnull)peerID didChangeState:(MCSessionState)state ``` |

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
