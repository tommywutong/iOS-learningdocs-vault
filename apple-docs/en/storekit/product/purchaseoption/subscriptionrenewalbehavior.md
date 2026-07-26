---
title: Product.PurchaseOption.SubscriptionRenewalBehavior
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior.json'
content_hash: 'sha256:02ed9a6f9e02b4db'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# Product.PurchaseOption.SubscriptionRenewalBehavior

<sub>Enumeration</sub>

Renewal options for auto-renewable subscriptions that you purchase in the testing environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SubscriptionRenewalBehavior
```

## Overview

Use the subscription renewal behavior values when you use the [purchaseDate](../../../storekittest/sktesttransaction/purchasedate.md) option to test your app in Xcode using [StoreKit Test](../../../storekittest.md).

## Relationships

- **Conforms To**: [Decodable](../../../swift/decodable.md), [Encodable](../../../swift/encodable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Renewal behaviors in the testing environment

- [Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately](subscriptionrenewalbehavior/cancelimmediately.md) — A subscription-renewal behavior in the testing environment that cancels the subscription, resulting in only one subscription period.
- [Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow](subscriptionrenewalbehavior/renewuntilnow.md) — A subscription-renewal behavior in the testing environment that allows the subscription to renew continuously, up to the current date.

## See Also

### Setting options for StoreKit Testing in Xcode

- [purchaseDate(_:renewalBehavior:)](<purchasedate(__renewalbehavior_).md>) — Sets the purchase date for the transaction in the testing environment, and indicates the renewal behavior for an auto-renewable subscription.
- [codeOffer(referenceName:)](<codeoffer(referencename_).md>) — Sets an offer code for the transaction in the testing environment.
- [promotionalOffer(id:)](<promotionaloffer(id_).md>) — Sets a promotional offer for the transaction in the testing environment.
