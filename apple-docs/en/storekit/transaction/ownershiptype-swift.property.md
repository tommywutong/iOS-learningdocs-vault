---
title: ownershipType
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/ownershiptype-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/transaction/ownershiptype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/ownershiptype-swift.property.json'
content_hash: 'sha256:8694e0ae372fe40b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# ownershipType

<sub>Instance Property</sub>

A value that indicates whether the transaction was purchased by the user, or is made available to them through Family Sharing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let ownershipType: Transaction.OwnershipType
```

## See Also

### Getting purchase details

- [isUpgraded](isupgraded.md) — A Boolean that indicates whether the user upgraded to another subscription.
- [OwnershipType](ownershiptype-swift.struct.md) — The types the system uses to describe whether the user purchased the product or it’s available to them through Family Sharing.
- [purchasedQuantity](purchasedquantity.md) — The number of consumable products purchased.
