---
title: revocationDate
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/revocationdate
source_url: 'https://developer.apple.com/documentation/storekit/transaction/revocationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/revocationdate.json'
content_hash: 'sha256:59b4f853f39e4599'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# revocationDate

<sub>Instance Property</sub>

The date that the App Store refunded the transaction or revoked it from Family Sharing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let revocationDate: Date?
```

## See Also

### Getting revocation status

- [revocationReason](revocationreason-swift.property.md) — The reason that the App Store refunded the transaction or revoked it from Family Sharing.
- [RevocationReason](revocationreason-swift.struct.md) — Reasons that describe why the App Store may refund a transaction or revoke it from Family Sharing.
