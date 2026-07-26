---
title: 'simulatesAskToBuyInSandbox(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/simulatesasktobuyinsandbox(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/simulatesasktobuyinsandbox(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/simulatesasktobuyinsandbox%28_%3A%29.json'
content_hash: 'sha256:18278e8e27c48bb5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# simulatesAskToBuyInSandbox(_:)

<sub>Type Method</sub>

Simulates an Ask to Buy scenario when testing your app in the sandbox environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func simulatesAskToBuyInSandbox(_ simulateAskToBuy: Bool) -> Product.PurchaseOption
```

## Parameters

- `simulateAskToBuy` — Set to `true` to simulate a child’s account asking permission to make a purchase.

## Return Value

An instance of [PurchaseOption](../purchaseoption.md) to use in [purchase(options:)](<../purchase(options_).md>).

## Discussion

For information about testing Ask to Buy scenarios, see [Testing at all stages of development with Xcode and the sandbox](../../testing-at-all-stages-of-development-with-xcode-and-the-sandbox.md).

For information about purchases made using Ask to Buy, see [Approve what kids buy with Ask to Buy](https://support.apple.com/en-us/HT201089).
