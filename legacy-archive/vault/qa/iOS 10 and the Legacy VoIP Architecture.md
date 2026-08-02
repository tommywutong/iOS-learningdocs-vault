---
title: iOS 10 and the Legacy VoIP Architecture
apple_id: DTS40017564
resource_type: QA
platform: iOS
topic: null
technology: PushKit
published: '2016-10-20'
source_url: https://developer.apple.com/library/archive/qa/qa1938/_index.html
archived_at: '2026-07-18T02:37:25.017471Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1938

# iOS 10 and the Legacy VoIP Architecture

## Q:  My VoIP app still uses the legacy VoIP architecture (`NSStreamNetworkServiceTypeVoIP` and so on). Why, when I build it with Xcode 8 and run it on iOS 10, does it no longer receive calls when in the background?

A: The legacy VoIP architecture was replaced by a new PushKit-based architecture in iOS 8. It was then formally deprecated with the iOS 9 SDK. In iOS 10 it is only available as a compatibility measure; it continues to work (as well as it ever did) if your app is linked with an old SDK, but is disabled if you link with the iOS 10 SDK.

For the moment you can work around this by building your app with Xcode 7. However, this is not a good long-term solution because:

- Our experience is that PushKit-based VoIP apps are more reliable and more power efficient than those using the legacy VoIP architecture.
- Apple always recommends that you use the latest version of Xcode because it combines the best features and the best compatibility.
- Specifically, we encourage VoIP apps to take advantage of CallKit, a new framework in the iOS 10 SDK that radically improves the user experience for VoIP apps. Xcode 8 is the only supported way to use CallKit.
- Also, be aware that Xcode 7 is not supported on macOS 10.12 Sierra.
- At some point support for the legacy VoIP architecture will be removed, whereupon all VoIP apps will have to move to the new PushKit-based VoIP architecture. It’s better to start this work sooner rather than later.

Some VoIP apps are specifically designed to work in special networks, ones that don’t provide access to the wider Internet. To use PushKit in such an environment you must configure the network to allow iOS devices to access the Apple Push Notification Service. See [TCP and UDP ports used by Apple software products](https://support.apple.com/en-us/HT202944) for information on how to do this.

For more information about PushKit, see:

- [PushKit API reference](https://developer.apple.com/reference/pushkit)
- WWDC 2014 Session 712 [Writing Energy Efficient Code, Part 2](https://developer.apple.com/videos/play/wwdc2014/712/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-10-20 | First Version |

