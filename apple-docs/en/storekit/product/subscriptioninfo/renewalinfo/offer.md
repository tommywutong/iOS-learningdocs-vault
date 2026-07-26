---
title: offer
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/subscriptioninfo/renewalinfo/offer
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/offer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptioninfo/renewalinfo/offer.json'
content_hash: 'sha256:986414b1b1bf984c'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionInfo](../../subscriptioninfo.md) · [RenewalInfo](../renewalinfo.md)

# offer

<sub>Instance Property</sub>

A subscription offer that applies to the transaction at the next renewal period.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let offer: Transaction.Offer?
```

## Discussion

This value is populated if a customer redeems a subscription offer that applies to more than one subscription period.

This value is `nil` if there’s no subscription offer.

## See Also

### Getting offers

- [Offer](../../../transaction/offer-swift.struct.md) — Discounts or promotions that apply to a transaction.
- [eligibleWinBackOfferIDs](eligiblewinbackofferids.md) — An array of strings that represent identifiers of win-back offers that the customer is eligible to redeem, sorted with the best offers first.
