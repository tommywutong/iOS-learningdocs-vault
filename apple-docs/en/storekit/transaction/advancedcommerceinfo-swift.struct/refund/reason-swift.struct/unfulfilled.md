---
title: unfulfilled
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund/reason-swift.struct/unfulfilled
source_url: 'https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund/reason-swift.struct/unfulfilled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund/reason-swift.struct/unfulfilled.json'
content_hash: 'sha256:75cd66d07277a080'
translated: false
---

> Navigation: [Technologies](../../../../../technologies.md) · [StoreKit](../../../../../storekit.md) · [Transaction](../../../../transaction.md) · [AdvancedCommerceInfo](../../../advancedcommerceinfo-swift.struct.md) · [Refund](../../refund.md) · [Reason](../reason-swift.struct.md)

# unfulfilled

<sub>Type Property</sub>

The customer had issues with receiving or using the in-app purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let unfulfilled: Transaction.AdvancedCommerceInfo.Refund.Reason
```

## See Also

### Type Properties

- [legal](legal.md) — The customer requested a refund based on a legal reason.
- [modifyItems](modifyitems.md)
- [other](other.md) — The customer requested a refund for other reasons.
- [unintended](unintended.md) — The customer didn’t intend to make the in-app purchase.
- [unsatisfied](unsatisfied.md) — The customer wasn’t satisfied with the in-app purchase.
