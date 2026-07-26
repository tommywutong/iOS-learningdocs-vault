---
title: Transaction.AdvancedCommerceInfo.Refund.Reason
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund/reason-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund/reason-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund/reason-swift.struct.json'
content_hash: 'sha256:70ddab685242b09e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Transaction](../../../transaction.md) · [AdvancedCommerceInfo](../../advancedcommerceinfo-swift.struct.md) · [Refund](../refund.md)

# Transaction.AdvancedCommerceInfo.Refund.Reason

<sub>Structure</sub>

The reason for the refund.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Reason
```

## Relationships

- **Conforms To**: [Equatable](../../../../swift/equatable.md), [Hashable](../../../../swift/hashable.md), [RawRepresentable](../../../../swift/rawrepresentable.md), [Sendable](../../../../swift/sendable.md), [SendableMetatype](../../../../swift/sendablemetatype.md)

## Topics

### Type Properties

- [legal](reason-swift.struct/legal.md) — The customer requested a refund based on a legal reason.
- [modifyItems](reason-swift.struct/modifyitems.md)
- [other](reason-swift.struct/other.md) — The customer requested a refund for other reasons.
- [unfulfilled](reason-swift.struct/unfulfilled.md) — The customer had issues with receiving or using the in-app purchase.
- [unintended](reason-swift.struct/unintended.md) — The customer didn’t intend to make the in-app purchase.
- [unsatisfied](reason-swift.struct/unsatisfied.md) — The customer wasn’t satisfied with the in-app purchase.

## See Also

### Structures

- [RefundType](refundtype.md) — The type of refund.
