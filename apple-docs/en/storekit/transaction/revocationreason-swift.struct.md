---
title: Transaction.RevocationReason
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/revocationreason-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/transaction/revocationreason-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/revocationreason-swift.struct.json'
content_hash: 'sha256:256487c3f96c4046'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# Transaction.RevocationReason

<sub>Structure</sub>

Reasons that describe why the App Store may refund a transaction or revoke it from Family Sharing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RevocationReason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Revocation reasons

- [developerIssue](revocationreason-swift.struct/developerissue.md) — The value that indicates a customer canceled the transaction due to an actual or perceived issue within your app.
- [other](revocationreason-swift.struct/other.md) — The value that indicates a customer canceled the transaction for other reasons.

### Getting a localized description

- [localizedDescription](revocationreason-swift.struct/localizeddescription.md) — The localized text that describes the revocation reason.

### Type Properties

- [upgradedToBundle](revocationreason-swift.struct/upgradedtobundle.md) — The transaction was revoked because the customer switched to a subscription bundle.

## See Also

### Getting revocation status

- [revocationDate](revocationdate.md) — The date that the App Store refunded the transaction or revoked it from Family Sharing.
- [revocationReason](revocationreason-swift.property.md) — The reason that the App Store refunded the transaction or revoked it from Family Sharing.
