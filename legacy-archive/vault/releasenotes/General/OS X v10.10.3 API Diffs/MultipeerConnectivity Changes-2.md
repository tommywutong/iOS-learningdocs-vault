---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/MultipeerConnectivity.html
archived_at: '2026-07-18T02:52:33.931600Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# MultipeerConnectivity Changes

## MultipeerConnectivity

Modified MCAdvertiserAssistant.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: MCAdvertiserAssistantDelegate! ``` |
| To | ``` weak var delegate: MCAdvertiserAssistantDelegate! ``` |

Modified MCAdvertiserAssistant.init(serviceType: String!, discoveryInfo:[NSObject: AnyObject]!, session: MCSession!)

|  | Declaration |
| --- | --- |
| From | ``` init(serviceType serviceType: String!, discoveryInfo info: [NSObject : AnyObject]!, session session: MCSession!) ``` |
| To | ``` init!(serviceType serviceType: String!, discoveryInfo info: [NSObject : AnyObject]!, session session: MCSession!) ``` |

Modified MCAdvertiserAssistantDelegate.advertiserAssistantDidDismissInvitation(MCAdvertiserAssistant!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MCAdvertiserAssistantDelegate.advertiserAssistantWillPresentInvitation(MCAdvertiserAssistant!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MCBrowserViewController.init(browser: MCNearbyServiceBrowser!, session: MCSession!)

|  | Declaration |
| --- | --- |
| From | ``` init(browser browser: MCNearbyServiceBrowser!, session session: MCSession!) ``` |
| To | ``` init!(browser browser: MCNearbyServiceBrowser!, session session: MCSession!) ``` |

Modified MCBrowserViewController.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: MCBrowserViewControllerDelegate! ``` |
| To | ``` weak var delegate: MCBrowserViewControllerDelegate! ``` |

Modified MCBrowserViewController.init(serviceType: String!, session: MCSession!)

|  | Declaration |
| --- | --- |
| From | ``` convenience init(serviceType serviceType: String!, session session: MCSession!) ``` |
| To | ``` convenience init!(serviceType serviceType: String!, session session: MCSession!) ``` |

Modified MCBrowserViewControllerDelegate.browserViewController(MCBrowserViewController!, shouldPresentNearbyPeer: MCPeerID!, withDiscoveryInfo:[NSObject: AnyObject]!) -> Bool

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MCNearbyServiceAdvertiser.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: MCNearbyServiceAdvertiserDelegate! ``` |
| To | ``` weak var delegate: MCNearbyServiceAdvertiserDelegate! ``` |

Modified MCNearbyServiceAdvertiser.init(peer: MCPeerID!, discoveryInfo:[NSObject: AnyObject]!, serviceType: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(peer myPeerID: MCPeerID!, discoveryInfo info: [NSObject : AnyObject]!, serviceType serviceType: String!) ``` |
| To | ``` init!(peer myPeerID: MCPeerID!, discoveryInfo info: [NSObject : AnyObject]!, serviceType serviceType: String!) ``` |

Modified MCNearbyServiceAdvertiserDelegate.advertiser(MCNearbyServiceAdvertiser!, didNotStartAdvertisingPeer: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MCNearbyServiceBrowser.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: MCNearbyServiceBrowserDelegate! ``` |
| To | ``` weak var delegate: MCNearbyServiceBrowserDelegate! ``` |

Modified MCNearbyServiceBrowser.init(peer: MCPeerID!, serviceType: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(peer myPeerID: MCPeerID!, serviceType serviceType: String!) ``` |
| To | ``` init!(peer myPeerID: MCPeerID!, serviceType serviceType: String!) ``` |

Modified MCNearbyServiceBrowserDelegate.browser(MCNearbyServiceBrowser!, didNotStartBrowsingForPeers: NSError!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MCPeerID.init(displayName: String!)

|  | Declaration |
| --- | --- |
| From | ``` init(displayName myDisplayName: String!) ``` |
| To | ``` init!(displayName myDisplayName: String!) ``` |

Modified MCSession.delegate

|  | Declaration |
| --- | --- |
| From | ``` var delegate: MCSessionDelegate! ``` |
| To | ``` weak var delegate: MCSessionDelegate! ``` |

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

Modified MCSessionDelegate.session(MCSession!, didReceiveCertificate:[AnyObject]!, fromPeer: MCPeerID!, certificateHandler:((Bool) -> Void)!)

|  | Optional |
| --- | --- |
| From | -- |
| To | yes |

Modified MCErrorDomain

|  | Declaration |
| --- | --- |
| From | ``` let MCErrorDomain: NSString! ``` |
| To | ``` let MCErrorDomain: String ``` |

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
