---
title: bundleProductID
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/bundleproductid
source_url: 'https://developer.apple.com/documentation/storekit/transaction/bundleproductid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/bundleproductid.json'
content_hash: 'sha256:f3a847dab2b2b12f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# bundleProductID

<sub>Instance Property</sub>

Identifies the bundle product the transaction is for. If this transaction is created as a result of a subscription bundle purchase or renewal, this field will be populated with the product ID of the bundle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: iOS 27.0, macOS 27.0, tvOS 27.0, watchOS 27.0, visionOS 27.0)
var bundleProductID: String? { get }
```
