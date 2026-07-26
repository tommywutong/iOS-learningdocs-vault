---
title: appAccountToken
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/appaccounttoken
source_url: 'https://developer.apple.com/documentation/storekit/transaction/appaccounttoken'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/appaccounttoken.json'
content_hash: 'sha256:d3b37e76ae2d5c80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# appAccountToken

<sub>Instance Property</sub>

A UUID that associates the transaction with a user on your own service.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let appAccountToken: UUID?
```

## Discussion

You create an [appAccountToken(_:)](<../product/purchaseoption/appaccounttoken(__).md>) and send it to the App Store when a customer initiates an in-app purchase. The App Store returns the same value in [appAccountToken](appaccounttoken.md) in the transaction information after the customer completes the purchase.
