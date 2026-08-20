---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/MultipeerConnectivity.html
archived_at: '2026-07-18T02:51:50.154674Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# MultipeerConnectivity Changes

## MultipeerConnectivity

MCAdvertiserAssistant.hModified [MCAdvertiserAssistant.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1407041-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) id<MCAdvertiserAssistantDelegate> delegate ``` |
| To | ``` @property(weak, atomic) id<MCAdvertiserAssistantDelegate> delegate ``` |

Modified [-[MCAdvertiserAssistant initWithServiceType:discoveryInfo:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant/1406990-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

MCBrowserViewController.hModified [MCBrowserViewController.delegate](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406982-delegate)

|  | Declaration |
| --- | --- |
| From | ``` @property(assign, atomic) id<MCBrowserViewControllerDelegate> delegate ``` |
| To | ``` @property(weak, atomic) id<MCBrowserViewControllerDelegate> delegate ``` |

Modified [-[MCBrowserViewController initWithBrowser:session:]](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontroller/1406963-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

MCNearbyServiceAdvertiser.hModified [-[MCNearbyServiceAdvertiser initWithPeer:discoveryInfo:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser/1407102-initwithpeer)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

MCNearbyServiceBrowser.hModified [-[MCNearbyServiceBrowser initWithPeer:serviceType:]](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/1407094-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

MCPeerID.hModified [-[MCPeerID initWithDisplayName:]](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid/1407089-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

MCSession.hModified [-[MCSession initWithPeer:securityIdentity:encryptionPreference:]](https://developer.apple.com/documentation/multipeerconnectivity/mcsession/1407025-init)

|  | Designated Initializer |
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
