---
title: iOS 8.0 API Diffs
apple_id: TP40014455
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS80APIDiffs/frameworks/MultipeerConnectivity.html
archived_at: '2026-07-18T02:55:59.383748Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.0 API Diffs](iOS%207.1%20to%20iOS%208.0%20API%20Differences.md)


# MultipeerConnectivity Changes

## MultipeerConnectivity

MCAdvertiserAssistant.hRemoved [-[MCAdvertiserAssistantDelegate advertiserAssitantWillPresentInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1809093-advertiserassitantwillpresentinv)Added [-[MCAdvertiserAssistantDelegate advertiserAssistantWillPresentInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406978-advertiserassistantwillpresentin)Modified [MCAdvertiserAssistant.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407041-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<MCAdvertiserAssistantDelegate> delegate ``` |
| To | ``` @property(weak, nonatomic) id<MCAdvertiserAssistantDelegate> delegate ``` |

Modified [-[MCAdvertiserAssistantDelegate advertiserAssistantDidDismissInvitation:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistantdelegate/1406922-advertiserassistantdiddismissinv)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MCBrowserViewController.hModified [MCBrowserViewController.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406982-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<MCBrowserViewControllerDelegate> delegate ``` |
| To | ``` @property(weak, nonatomic) id<MCBrowserViewControllerDelegate> delegate ``` |

Modified [-[MCBrowserViewControllerDelegate browserViewController:shouldPresentNearbyPeer:withDiscoveryInfo:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate/1407039-browserviewcontroller)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MCNearbyServiceAdvertiser.hModified [MCNearbyServiceAdvertiser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407031-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<MCNearbyServiceAdvertiserDelegate> delegate ``` |
| To | ``` @property(weak, nonatomic) id<MCNearbyServiceAdvertiserDelegate> delegate ``` |

Modified [-[MCNearbyServiceAdvertiserDelegate advertiser:didNotStartAdvertisingPeer:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiserdelegate/1407100-advertiser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MCNearbyServiceBrowser.hModified [MCNearbyServiceBrowser.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407079-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<MCNearbyServiceBrowserDelegate> delegate ``` |
| To | ``` @property(weak, nonatomic) id<MCNearbyServiceBrowserDelegate> delegate ``` |

Modified [-[MCNearbyServiceBrowserDelegate browser:didNotStartBrowsingForPeers:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/1406913-browser)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

MCSession.hModified [MCSession.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407112-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, nonatomic) id<MCSessionDelegate> delegate ``` |
| To | ``` @property(weak, nonatomic) id<MCSessionDelegate> delegate ``` |

Modified [-[MCSessionDelegate session:didReceiveCertificate:fromPeer:certificateHandler:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate/1407067-session)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

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
