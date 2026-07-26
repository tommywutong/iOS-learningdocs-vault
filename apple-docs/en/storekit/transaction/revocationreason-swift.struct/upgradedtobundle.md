---
title: upgradedToBundle
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/revocationreason-swift.struct/upgradedtobundle
source_url: 'https://developer.apple.com/documentation/storekit/transaction/revocationreason-swift.struct/upgradedtobundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/revocationreason-swift.struct/upgradedtobundle.json'
content_hash: 'sha256:9a1c12f37b960b90'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Transaction](../../transaction.md) · [RevocationReason](../revocationreason-swift.struct.md)

# upgradedToBundle

<sub>Type Property</sub>

The transaction was revoked because the customer switched to a subscription bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
static var upgradedToBundle: Transaction.RevocationReason { get }
```
