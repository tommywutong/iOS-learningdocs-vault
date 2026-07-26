---
title: previousOriginalTransactionID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/previousoriginaltransactionid
source_url: 'https://developer.apple.com/documentation/storekit/transaction/previousoriginaltransactionid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/previousoriginaltransactionid.json'
content_hash: 'sha256:6b9e2eaa6c5b763e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# previousOriginalTransactionID

<sub>Instance Property</sub>

The original transaction ID of the subscription this one replaced when a customer switched between a standalone auto-renewable subscription and a subscription bundle (in either direction).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
var previousOriginalTransactionID: UInt64? { get }
```

## Discussion

For a bundle transaction, this is the standalone subscription’s original transaction ID, while for a standalone transaction, this is the bundle’s original transaction ID. This field is `nil` if no such switch occurred.
