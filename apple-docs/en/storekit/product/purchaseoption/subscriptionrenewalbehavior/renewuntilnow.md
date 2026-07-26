---
title: Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior/renewuntilnow
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior/renewuntilnow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior/renewuntilnow.json'
content_hash: 'sha256:6763a507697cf0dd'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [PurchaseOption](../../purchaseoption.md) · [SubscriptionRenewalBehavior](../subscriptionrenewalbehavior.md)

# Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow

<sub>Case</sub>

A subscription-renewal behavior in the testing environment that allows the subscription to renew continuously, up to the current date.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case renewUntilNow
```

## Discussion

Choose this option to create test cases that require an auto-renewable subscription that continues to renew. If you set the purchase date in [purchaseDate(_:renewalBehavior:)](<../purchasedate(__renewalbehavior_).md>)to the past, the testing environment generates transactions for all the subscription renewals up to the current date.

## See Also

### Renewal behaviors in the testing environment

- [Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately](cancelimmediately.md) — A subscription-renewal behavior in the testing environment that cancels the subscription, resulting in only one subscription period.
