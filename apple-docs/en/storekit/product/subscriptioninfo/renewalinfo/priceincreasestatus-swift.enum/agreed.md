---
title: Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/agreed
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/agreed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/priceincreasestatus-swift.enum/agreed.json'
content_hash: 'sha256:5121875bfebdae2a'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [StoreKit](../../../../../storekit.md) · [Product](../../../../product.md) · [SubscriptionInfo](../../../subscriptioninfo.md) · [RenewalInfo](../../renewalinfo.md) · [PriceIncreaseStatus](../priceincreasestatus-swift.enum.md)

# Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.agreed

<sub>Case</sub>

The auto-renewable subscription is subject to a price increase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case agreed
```

## Discussion

There are two types of price increases for auto-renewable subscriptions: those that require customer consent, and those that don’t require customer consent. For a price increase that requires customer consent, this value indicates that the customer consented to the price increase. For a price increase that doesn’t require customer consent, this value indicates that the App Store informed the customer of the price increase and the subscription is subject to the price increase.

For more information about this value, see [Managing Price Increases for Auto-Renewable Subscriptions](../../../../managing-price-increases-for-auto-renewable-subscriptions.md).

## See Also

### Getting Price Increase Status

- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.noIncreasePending](noincreasepending.md) — There’s no pending price increase for the auto-renewable subscription.
- [Product.SubscriptionInfo.RenewalInfo.PriceIncreaseStatus.pending](pending.md) — The customer hasn’t yet responded to an auto-renewable subscription price increase that requires customer consent.
