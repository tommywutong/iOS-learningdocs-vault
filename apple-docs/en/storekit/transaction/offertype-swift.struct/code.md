---
title: code
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offertype-swift.struct/code
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offertype-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offertype-swift.struct/code.json'
content_hash: 'sha256:5a0102761f8a89cc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [OfferType](../offertype-swift.struct.md)

# code

<sub>Type Property</sub>

An offer code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let code: Transaction.OfferType
```

## Discussion

You create and define offer codes in App Store Connect. Offer codes are available for any In-App Purchase product type.

For more information about offer codes, see [Set up offer codes](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-offer-codes).

The raw value of the [code](code.md) offer type is `3`.

## See Also

### Getting offer types

- [introductory](introductory.md) — An introductory offer for an auto-renewable subscription.
- [promotional](promotional.md) — A promotional offer for an auto-renewable subscription.
- [winBack](winback.md) — A win-back offer for an auto-renewable subscription.
