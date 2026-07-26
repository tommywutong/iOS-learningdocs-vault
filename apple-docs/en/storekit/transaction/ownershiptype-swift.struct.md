---
title: Transaction.OwnershipType
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/ownershiptype-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/transaction/ownershiptype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/ownershiptype-swift.struct.json'
content_hash: 'sha256:6afea4f78ebbc651'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.OwnershipType

<sub>Structure</sub>

The types the system uses to describe whether the user purchased the product or it’s available to them through Family Sharing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct OwnershipType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting ownership types

- [familyShared](ownershiptype-swift.struct/familyshared.md) — The transaction belongs to a family member who benefits from the service.
- [purchased](ownershiptype-swift.struct/purchased.md) — The transaction belongs to the purchaser.

### Getting a localized description

- [localizedDescription](ownershiptype-swift.struct/localizeddescription.md) — The localized text that describes the ownership type.

### Type Properties

- [assigned](ownershiptype-swift.struct/assigned.md) — The user has access to this transaction through an organization.

## See Also

### Getting purchase details

- [isUpgraded](isupgraded.md) — A Boolean that indicates whether the user upgraded to another subscription.
- [ownershipType](ownershiptype-swift.property.md) — A value that indicates whether the transaction was purchased by the user, or is made available to them through Family Sharing.
- [purchasedQuantity](purchasedquantity.md) — The number of consumable products purchased.
