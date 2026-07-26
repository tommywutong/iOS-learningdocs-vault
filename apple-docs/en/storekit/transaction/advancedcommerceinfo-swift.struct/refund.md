---
title: Transaction.AdvancedCommerceInfo.Refund
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund
source_url: 'https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund.json'
content_hash: 'sha256:46971576695ba74c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [AdvancedCommerceInfo](../advancedcommerceinfo-swift.struct.md)

# Transaction.AdvancedCommerceInfo.Refund

<sub>Structure</sub>

Information about refunds that were issued as part of this transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Refund
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Structures

- [Reason](refund/reason-swift.struct.md) — The reason for the refund.
- [RefundType](refund/refundtype.md) — The type of refund.

### Instance Properties

- [amount](refund/amount.md) — The amount of the refund.
- [date](refund/date.md) — The date the refund was granted.
- [reason](refund/reason-swift.property.md) — The reason for the refund.
- [type](refund/type.md) — The type of the refund.

## See Also

### Structures

- [Item](item.md) — The developer-defined product that was purchased.
- [Offer](offer.md) — Information about the offer that was redeemed as part of the purchase.
