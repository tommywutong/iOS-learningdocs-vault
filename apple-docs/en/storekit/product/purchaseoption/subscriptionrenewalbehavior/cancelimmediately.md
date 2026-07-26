---
title: Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior/cancelimmediately
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior/cancelimmediately'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/subscriptionrenewalbehavior/cancelimmediately.json'
content_hash: 'sha256:895c9c709e0b1544'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [PurchaseOption](../../purchaseoption.md) · [SubscriptionRenewalBehavior](../subscriptionrenewalbehavior.md)

# Product.PurchaseOption.SubscriptionRenewalBehavior.cancelImmediately

<sub>Case</sub>

A subscription-renewal behavior in the testing environment that cancels the subscription, resulting in only one subscription period.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cancelImmediately
```

## Discussion

Choose this option for test cases that require an auto-renewable subscription that won’t renew.

## See Also

### Renewal behaviors in the testing environment

- [Product.PurchaseOption.SubscriptionRenewalBehavior.renewUntilNow](renewuntilnow.md) — A subscription-renewal behavior in the testing environment that allows the subscription to renew continuously, up to the current date.
