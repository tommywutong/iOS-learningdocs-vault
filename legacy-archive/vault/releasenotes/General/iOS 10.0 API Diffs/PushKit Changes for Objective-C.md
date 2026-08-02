---
title: iOS 10.0 API Diffs
apple_id: TP40017327
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS10APIDiffs/Objective-C/PushKit.html
archived_at: '2026-07-18T02:54:58.170810Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 10.0 API Diffs](iOS%209.3%20to%20iOS%2010.0%20API%20Differences.md)


# PushKit Changes for Objective-C

### PushKit

#### PKDefines.h

Added [PKPushType](https://developer.apple.com/documentation/pushkit/pkpushtype)

#### PKPushCredentials.h

Modified [PKPushCredentials.type](https://developer.apple.com/documentation/pushkit/pkpushcredentials/1614484-type)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *type ``` |
| To | ``` @property(readonly, copy) PKPushType type ``` |

#### PKPushPayload.h

Modified [PKPushPayload.type](https://developer.apple.com/documentation/pushkit/pkpushpayload/1614476-type)

|  | Declaration |
| --- | --- |
| From | ``` @property(readonly, copy) NSString *type ``` |
| To | ``` @property(readonly, copy) PKPushType type ``` |

#### PKPushRegistry.h

Modified [PKPushRegistry.desiredPushTypes](https://developer.apple.com/documentation/pushkit/pkpushregistry/1614479-desiredpushtypes)

|  | Declaration |
| --- | --- |
| From | ``` @property(readwrite, copy) NSSet *desiredPushTypes ``` |
| To | ``` @property(readwrite, copy) NSSet<PKPushType> *desiredPushTypes ``` |

Modified [-[PKPushRegistry initWithQueue:]](https://developer.apple.com/documentation/pushkit/pkpushregistry/1614494-init)

|  | Designated Initializer |
| --- | --- |
| From | -- |
| To | yes |

Modified [-[PKPushRegistry pushTokenForType:]](https://developer.apple.com/documentation/pushkit/pkpushregistry/1614472-pushtokenfortype)

|  | Declaration |
| --- | --- |
| From | ``` - (NSData *)pushTokenForType:(NSString *)type ``` |
| To | ``` - (NSData *)pushTokenForType:(PKPushType)type ``` |

Modified [-[PKPushRegistryDelegate pushRegistry:didInvalidatePushTokenForType:]](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/1614490-pushregistry)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pushRegistry:(PKPushRegistry *)registry didInvalidatePushTokenForType:(NSString *)type ``` |
| To | ``` - (void)pushRegistry:(PKPushRegistry *)registry didInvalidatePushTokenForType:(PKPushType)type ``` |

Modified [-[PKPushRegistryDelegate pushRegistry:didReceiveIncomingPushWithPayload:forType:]](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/1614492-pushregistry)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pushRegistry:(PKPushRegistry *)registry didReceiveIncomingPushWithPayload:(PKPushPayload *)payload forType:(NSString *)type ``` |
| To | ``` - (void)pushRegistry:(PKPushRegistry *)registry didReceiveIncomingPushWithPayload:(PKPushPayload *)payload forType:(PKPushType)type ``` |

Modified [-[PKPushRegistryDelegate pushRegistry:didUpdatePushCredentials:forType:]](https://developer.apple.com/documentation/pushkit/pkpushregistrydelegate/1614470-pushregistry)

|  | Declaration |
| --- | --- |
| From | ``` - (void)pushRegistry:(PKPushRegistry *)registry didUpdatePushCredentials:(PKPushCredentials *)credentials forType:(NSString *)type ``` |
| To | ``` - (void)pushRegistry:(PKPushRegistry *)registry didUpdatePushCredentials:(PKPushCredentials *)credentials forType:(PKPushType)type ``` |

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
