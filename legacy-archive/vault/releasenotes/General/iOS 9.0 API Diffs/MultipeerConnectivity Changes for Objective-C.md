---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Objective-C/MultipeerConnectivity.html
archived_at: '2026-07-18T02:56:35.650552Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# MultipeerConnectivity Changes for Objective-C

### MultipeerConnectivity

#### MCAdvertiserAssistant.h

Modified [MCAdvertiserAssistant.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406952-discoveryinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSDictionary *discoveryInfo ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSDictionary<NSString *,NSString *> *discoveryInfo ``` |

Modified [-[MCAdvertiserAssistant initWithServiceType:discoveryInfo:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406990-init)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithServiceType:(NSString *)serviceType discoveryInfo:(NSDictionary *)info session:(MCSession *)session ``` |
| To | ``` - (instancetype _Nonnull)initWithServiceType:(NSString * _Nonnull)serviceType discoveryInfo:(NSDictionary<NSString *,NSString *> * _Nullable)info session:(MCSession * _Nonnull)session ``` |

#### MCBrowserViewController.h

Modified [-[MCBrowserViewControllerDelegate browserViewController:shouldPresentNearbyPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407039-browserviewcontroller)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)browserViewController:(MCBrowserViewController *)browserViewController shouldPresentNearbyPeer:(MCPeerID *)peerID withDiscoveryInfo:(NSDictionary *)info ``` |
| To | ``` - (BOOL)browserViewController:(MCBrowserViewController * _Nonnull)browserViewController shouldPresentNearbyPeer:(MCPeerID * _Nonnull)peerID withDiscoveryInfo:(NSDictionary<NSString *,NSString *> * _Nullable)info ``` |

#### MCNearbyServiceAdvertiser.h

Modified [MCNearbyServiceAdvertiser.discoveryInfo](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1406967-discoveryinfo)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSDictionary *discoveryInfo ``` |
| To | ``` @property(readonly, nonatomic, nullable) NSDictionary<NSString *,NSString *> *discoveryInfo ``` |

Modified [-[MCNearbyServiceAdvertiser initWithPeer:discoveryInfo:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407102-initwithpeer)

|  | Declaration |
| --- | --- |
| From | ``` - (instancetype)initWithPeer:(MCPeerID *)myPeerID discoveryInfo:(NSDictionary *)info serviceType:(NSString *)serviceType ``` |
| To | ``` - (instancetype _Nonnull)initWithPeer:(MCPeerID * _Nonnull)myPeerID discoveryInfo:(NSDictionary<NSString *,NSString *> * _Nullable)info serviceType:(NSString * _Nonnull)serviceType ``` |

#### MCNearbyServiceBrowser.h

Modified [-[MCNearbyServiceBrowserDelegate browser:foundPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406926-browser)

|  | Declaration |
| --- | --- |
| From | ``` - (void)browser:(MCNearbyServiceBrowser *)browser foundPeer:(MCPeerID *)peerID withDiscoveryInfo:(NSDictionary *)info ``` |
| To | ``` - (void)browser:(MCNearbyServiceBrowser * _Nonnull)browser foundPeer:(MCPeerID * _Nonnull)peerID withDiscoveryInfo:(NSDictionary<NSString *,NSString *> * _Nullable)info ``` |

#### MCSession.h

Modified [MCSession.connectedPeers](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406911-connectedpeers)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, nonatomic) NSArray *connectedPeers ``` |
| To | ``` @property(readonly, nonatomic, nonnull) NSArray<MCPeerID *> *connectedPeers ``` |

Modified [-[MCSession sendData:toPeers:withMode:error:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1406997-send)

|  | Declaration |
| --- | --- |
| From | ``` - (BOOL)sendData:(NSData *)data toPeers:(NSArray *)peerIDs withMode:(MCSessionSendDataMode)mode error:(NSError **)error ``` |
| To | ``` - (BOOL)sendData:(NSData * _Nonnull)data toPeers:(NSArray<MCPeerID *> * _Nonnull)peerIDs withMode:(MCSessionSendDataMode)mode error:(NSError * _Nullable * _Nullable)error ``` |

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
