---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/MultipeerConnectivity.html
archived_at: '2026-07-18T02:56:14.945098Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# MultipeerConnectivity Changes

## MultipeerConnectivity

Modified MCAdvertiserAssistant

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCAdvertiserAssistant.init(serviceType: String!, discoveryInfo:[NSObject: AnyObject]!, session: MCSession!)

|  | Declaration |
| --- | --- |
| From | ``` init(serviceType serviceType: String!, discoveryInfo info: [NSObject : AnyObject]!, session session: MCSession!) ``` |
| To | ``` init!(serviceType serviceType: String!, discoveryInfo info: [NSObject : AnyObject]!, session session: MCSession!) ``` |

Modified MCBrowserViewController

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCBrowserViewController.init(browser: MCNearbyServiceBrowser!, session: MCSession!)

|  | Declaration |
| --- | --- |
| From | ``` init(browser browser: MCNearbyServiceBrowser!, session session: MCSession!) ``` |
| To | ``` init!(browser browser: MCNearbyServiceBrowser!, session session: MCSession!) ``` |

Modified MCBrowserViewController.init(serviceType: String!, session: MCSession!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(serviceType serviceType: String!, session session: MCSession!) ``` |
| To | ``` convenience init!(serviceType serviceType: String!, session session: MCSession!) ``` |

Modified MCEncryptionPreference [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCErrorCode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCNearbyServiceAdvertiser

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCNearbyServiceAdvertiser.init(peer: MCPeerID!, discoveryInfo:[NSObject: AnyObject]!, serviceType: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(peer myPeerID: MCPeerID!, discoveryInfo info: [NSObject : AnyObject]!, serviceType serviceType: String!) ``` |
| To | ``` init!(peer myPeerID: MCPeerID!, discoveryInfo info: [NSObject : AnyObject]!, serviceType serviceType: String!) ``` |

Modified MCNearbyServiceBrowser

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCNearbyServiceBrowser.init(peer: MCPeerID!, serviceType: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(peer myPeerID: MCPeerID!, serviceType serviceType: String!) ``` |
| To | ``` init!(peer myPeerID: MCPeerID!, serviceType serviceType: String!) ``` |

Modified MCPeerID

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCPeerID.init(displayName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(displayName myDisplayName: String!) ``` |
| To | ``` init!(displayName myDisplayName: String!) ``` |

Modified MCSession

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCSession.init(peer: MCPeerID!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(peer myPeerID: MCPeerID!) ``` |
| To | ``` convenience init!(peer myPeerID: MCPeerID!) ``` |

Modified MCSession.init(peer: MCPeerID!, securityIdentity:[AnyObject]!, encryptionPreference: MCEncryptionPreference)

|  | Declaration |
| --- | --- |
| From | ``` init(peer myPeerID: MCPeerID!, securityIdentity identity: [AnyObject]!, encryptionPreference encryptionPreference: MCEncryptionPreference) ``` |
| To | ``` init!(peer myPeerID: MCPeerID!, securityIdentity identity: [AnyObject]!, encryptionPreference encryptionPreference: MCEncryptionPreference) ``` |

Modified MCSessionSendDataMode [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified MCSessionState [enum]

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kMCSessionMaximumNumberOfPeers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

Modified kMCSessionMinimumNumberOfPeers

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 7.0 |

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
