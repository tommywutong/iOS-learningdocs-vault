---
title: revocationType
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.4+, iPadOS 26.4+, macOS 26.4+, tvOS 26.4+, visionOS 26.4+, watchOS 26.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/revocationtype-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/transaction/revocationtype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/revocationtype-swift.property.json'
content_hash: 'sha256:58632b43c1d69095'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# revocationType

<sub>Instance Property</sub>

The type of refund or revocation that applies to the transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let revocationType: Transaction.RevocationType?
```

## Discussion

This property indicates whether the transaction has a full refund, a prorated refund, or is revoked from Family Sharing. This property is `nil` for transactions that are not revoked.

> [!note] Note
> This property is not present for Advanced Commerce transactions, which use [refunds](advancedcommerceinfo-swift.struct/item/refunds.md) instead.
