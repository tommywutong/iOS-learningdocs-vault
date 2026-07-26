---
title: Transaction.Reason
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/reason-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/transaction/reason-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/reason-swift.struct.json'
content_hash: 'sha256:ce3dc97f03e16d64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.Reason

<sub>Structure</sub>

A cause of a purchase transaction, indicating whether it’s a customer’s purchase or an auto-renewable subscription renewal that the system initiates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Reason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Transaction reasons

- [purchase](reason-swift.struct/purchase.md) — A transaction reason that indicates a purchase is initiated by a customer.
- [renewal](reason-swift.struct/renewal.md) — A transaction reason that indicates the App Store server initiated a purchase transaction to renew an auto-renewable subscription.

## See Also

### Getting transaction reason

- [reason](reason-swift.property.md) — The cause of the purchase transaction, whether it’s a customer’s purchase or an auto-renewable subscription renewal that the system initiates.
