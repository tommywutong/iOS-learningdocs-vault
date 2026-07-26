---
title: offer
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.2+, iPadOS 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offer-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offer-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offer-swift.property.json'
content_hash: 'sha256:798783573265cc56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# offer

<sub>Instance Property</sub>

The offer that applies to the transaction, including its offer type, payment mode, and ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let offer: Transaction.Offer?
```

## Discussion

This value is `nil` if the transaction doesn’t include an offer.

You set up offers for auto-renewable subscriptions and other In-App Purchase product types in App Store Connect. If a customer redeems an offer, this property contains the offer details, including its [type](offer-swift.struct/type.md), [paymentMode](offer-swift.struct/paymentmode-swift.property.md), and [id](id.md). For more information, see [Offer](offer-swift.struct.md).

## See Also

### Identifying offers

- [Offer](offer-swift.struct.md) — Discounts or promotions that apply to a transaction.
