---
title: 'all(for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/transaction/all(for:)'
source_url: 'https://developer.apple.com/documentation/storekit/transaction/all(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/all%28for%3A%29.json'
content_hash: 'sha256:f12a8163f665a67f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# all(for:)

<sub>Type Method</sub>

Gets all the transactions associated with this product ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func all(for productID: String) -> Transaction.Transactions
```

## Parameters

- `productID` — Identifies the product to filter the transaction cache against.

## Return Value

A sequence containing all transactions for the given product.
