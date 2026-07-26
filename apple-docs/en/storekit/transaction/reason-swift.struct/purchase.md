---
title: purchase
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/reason-swift.struct/purchase
source_url: 'https://developer.apple.com/documentation/storekit/transaction/reason-swift.struct/purchase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/reason-swift.struct/purchase.json'
content_hash: 'sha256:d7f19209f25388b6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [Reason](../reason-swift.struct.md)

# purchase

<sub>Type Property</sub>

A transaction reason that indicates a purchase is initiated by a customer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let purchase: Transaction.Reason
```

## Discussion

The customer initiated the purchase, which may be for any in-app purchase type: consumable, non-consumable, non-renewing subscription, or auto-renewable subscription.

## See Also

### Transaction reasons

- [renewal](renewal.md) — A transaction reason that indicates the App Store server initiated a purchase transaction to renew an auto-renewable subscription.
