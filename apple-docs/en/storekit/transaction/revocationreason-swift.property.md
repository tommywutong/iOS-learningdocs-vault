---
title: revocationReason
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/revocationreason-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/transaction/revocationreason-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/revocationreason-swift.property.json'
content_hash: 'sha256:99eaedc490f4750c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# revocationReason

<sub>Instance Property</sub>

The reason that the App Store refunded the transaction or revoked it from Family Sharing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let revocationReason: Transaction.RevocationReason?
```

## See Also

### Getting revocation status

- [revocationDate](revocationdate.md) — The date that the App Store refunded the transaction or revoked it from Family Sharing.
- [RevocationReason](revocationreason-swift.struct.md) — Reasons that describe why the App Store may refund a transaction or revoke it from Family Sharing.
