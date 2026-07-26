---
title: isUpgraded
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/isupgraded
source_url: 'https://developer.apple.com/documentation/storekit/transaction/isupgraded'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/isupgraded.json'
content_hash: 'sha256:6ecb9c628673c5b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# isUpgraded

<sub>Instance Property</sub>

A Boolean that indicates whether the user upgraded to another subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let isUpgraded: Bool
```

## Discussion

If [isUpgraded](isupgraded.md) is `true`, the user has upgraded the subscription represented by this transaction to another subscription. This value appears in the transaction only when the value is `true`. To determine the service that the customer is entitled to, look for another transaction that has a subscription with a higher level of service.

## See Also

### Getting purchase details

- [ownershipType](ownershiptype-swift.property.md) — A value that indicates whether the transaction was purchased by the user, or is made available to them through Family Sharing.
- [OwnershipType](ownershiptype-swift.struct.md) — The types the system uses to describe whether the user purchased the product or it’s available to them through Family Sharing.
- [purchasedQuantity](purchasedquantity.md) — The number of consumable products purchased.
