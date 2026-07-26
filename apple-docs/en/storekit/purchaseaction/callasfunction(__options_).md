---
title: 'callAsFunction(_:options:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/purchaseaction/callasfunction(_:options:)'
source_url: 'https://developer.apple.com/documentation/storekit/purchaseaction/callasfunction(_:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/purchaseaction/callasfunction%28_%3Aoptions%3A%29.json'
content_hash: 'sha256:c333315bd5b783f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [PurchaseAction](../purchaseaction.md)

# callAsFunction(_:options:)

<sub>Instance Method</sub>

Starts an in-app purchase for the indicated product and purchase options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func callAsFunction(_ product: Product, options: Set<Product.PurchaseOption> = []) async throws -> Product.PurchaseResult
```

## Parameters

- `product` — The in-app purchase [Product](../product.md) the customer is purchasing.

- `options` — A set of options you may associate with the purchase ([PurchaseOption](../product/purchaseoption.md)).

## Return Value

The result of the purchase, [PurchaseResult](../product/purchaseresult.md).

## Discussion

Don’t call this method directly. SwiftUI calls it when you call the [PurchaseAction](../purchaseaction.md) structure with the `product` and `options` as arguments.

This method may throw a [PurchaseError](../product/purchaseerror.md) or [StoreKitError](../storekiterror.md).

For information about how Swift uses the [callAsFunction(_:options:)](<callasfunction(__options_).md>) method to simplify call site syntax, see [Methods with Special Names](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations/#Methods-with-Special-Names) in _The Swift Programming Language_.
