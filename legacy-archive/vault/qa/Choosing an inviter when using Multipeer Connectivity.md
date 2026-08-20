---
title: Choosing an inviter when using Multipeer Connectivity
apple_id: DTS40014788
resource_type: QA
platform: iOS
topic: null
technology: MultipeerConnectivity
published: '2014-08-05'
source_url: https://developer.apple.com/library/archive/qa/qa1869/_index.html
archived_at: '2026-07-18T02:35:09.529018Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1869

# Choosing an inviter when using Multipeer Connectivity

## Q:  I'm trying to implement automatic invites using Multipeer connectivity. What's the best way to handle this?

A: iOS 7 handles invites slightly differently than iOS 8, so if you want to support iOS 7 you'll need to use a slightly different approach.

Starting in iOS 8, all devices can simply invite any peer they detect while browsing. Multipeer Connectivity will automatically process both invites so that both peers join the same MCSession.

In iOS 7, sending simultaneous invites can cause both invites to fail, leaving both peers unable to communicate with each other. Apps can work around this by programmatically selecting one of the peers to send the invite. Many approaches are possible for selecting the inviting peer, but the simplest is to compare the hash values of the two MCPeerID and select the highest as shown in Listing 1

__Listing 1__  Choosing which MCPeerID will invite

```objc
- (void)browser: (MCNearbyServiceBrowser*) browser
                 foundPeer: (MCPeerID*) nearbyPeerID
                 withDiscoveryInfo: (NSDictionary *) info
{
   // Compare the hash values of the 2 peers IDs
   if ((uint32_t)myPeerID.hash > (uint32_t)nearbyPeerID.hash)
   {
      [self.browser invitePeer:nearbyPeerID
                           toSession:session
                           withContext:nil
                           timeout:15];
   }
   else
   {
      // NSLog(@"Skipping invite on: %@", [myPeerID description]);
   }
}
```


---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-05 | New document that describes how apps should select an inviting device when using Multipeer Connectivity |

