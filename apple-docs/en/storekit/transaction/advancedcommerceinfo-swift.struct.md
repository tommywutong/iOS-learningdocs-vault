---
title: Transaction.AdvancedCommerceInfo
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/advancedcommerceinfo-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/advancedcommerceinfo-swift.struct.json'
content_hash: 'sha256:c020866da0f42ef8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.AdvancedCommerceInfo

<sub>Structure</sub>

Metadata for transactions that use the Advanced Commerce API.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AdvancedCommerceInfo
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Structures

- [Item](advancedcommerceinfo-swift.struct/item.md) — The developer-defined product that was purchased.
- [Offer](advancedcommerceinfo-swift.struct/offer.md) — Information about the offer that was redeemed as part of the purchase.
- [Refund](advancedcommerceinfo-swift.struct/refund.md) — Information about refunds that were issued as part of this transaction.
- [Partner](advancedcommerceinfo-swift.struct/partner.md) _(beta)_

### Instance Properties

- [description](advancedcommerceinfo-swift.struct/description.md)
- [displayName](advancedcommerceinfo-swift.struct/displayname.md)
- [estimatedTax](advancedcommerceinfo-swift.struct/estimatedtax.md)
- [items](advancedcommerceinfo-swift.struct/items.md) — The items purchased as part of this transaction.
- [period](advancedcommerceinfo-swift.struct/period.md)
- [requestReferenceID](advancedcommerceinfo-swift.struct/requestreferenceid.md)
- [taxCode](advancedcommerceinfo-swift.struct/taxcode.md)
- [taxExclusivePrice](advancedcommerceinfo-swift.struct/taxexclusiveprice.md)
- [taxRate](advancedcommerceinfo-swift.struct/taxrate.md)

## See Also

### Advanced Commerce transaction data

- [advancedCommerceInfo](advancedcommerceinfo-swift.property.md) — Metadata for transactions that use the Advanced Commerce API.
