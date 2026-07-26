---
title: Transaction.AdvancedCommerceInfo.Offer
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/advancedcommerceinfo-swift.struct/offer
source_url: 'https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/offer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/offer.json'
content_hash: 'sha256:cba5e85955a3d8f3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [AdvancedCommerceInfo](../advancedcommerceinfo-swift.struct.md)

# Transaction.AdvancedCommerceInfo.Offer

<sub>Structure</sub>

Information about the offer that was redeemed as part of the purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Offer
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Structures

- [Reason](offer/reason-swift.struct.md) — The reasons why subscription offers are applied to the purchase of auto-renewable subscriptions.

### Instance Properties

- [period](offer/period.md) — The duration of the offer.
- [periodCount](offer/periodcount.md) — The number of periods the system applies the offer.
- [price](offer/price.md) — The discounted price under the offer.
- [reason](offer/reason-swift.property.md) — The reason the offer was applied.

## See Also

### Structures

- [Item](item.md) — The developer-defined product that was purchased.
- [Refund](refund.md) — Information about refunds that were issued as part of this transaction.
