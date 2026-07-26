---
title: periodCount
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptionoffer/periodcount
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer/periodcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer/periodcount.json'
content_hash: 'sha256:d61eb35f71e3eb52'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionOffer](../subscriptionoffer.md)

# periodCount

<sub>Instance Property</sub>

The number of periods that the subscription offer renews for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let periodCount: Int
```

## Discussion

If the payment mode is [payAsYouGo](paymentmode-swift.struct/payasyougo.md), the period count represents the number of periods the subscription renews at the discounted [price](price.md).

The period count is 1 for offers with payment modes [freeTrial](paymentmode-swift.struct/freetrial.md) and [payUpFront](paymentmode-swift.struct/payupfront.md).

## See Also

### Getting the subscription duration

- [period](period.md) — The subscription period for the subscription offer.
