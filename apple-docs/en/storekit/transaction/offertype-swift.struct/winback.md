---
title: winBack
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/offertype-swift.struct/winback
source_url: 'https://developer.apple.com/documentation/storekit/transaction/offertype-swift.struct/winback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/offertype-swift.struct/winback.json'
content_hash: 'sha256:275e762580701417'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [OfferType](../offertype-swift.struct.md)

# winBack

<sub>Type Property</sub>

A win-back offer for an auto-renewable subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 18.0, macOS 15.0, tvOS 18.0, watchOS 11.0, visionOS 2.0)
static var winBack: Transaction.OfferType { get }
```

## Discussion

For more information about win-back offers, see [Set up win-back offers](https://developer.apple.com/help/app-store-connect/manage-subscriptions/set-up-win-back-offers).

The raw value of the [winBack](winback.md) offer type is `4`.

## See Also

### Getting offer types

- [introductory](introductory.md) — An introductory offer for an auto-renewable subscription.
- [promotional](promotional.md) — A promotional offer for an auto-renewable subscription.
- [code](code.md) — An offer code.
