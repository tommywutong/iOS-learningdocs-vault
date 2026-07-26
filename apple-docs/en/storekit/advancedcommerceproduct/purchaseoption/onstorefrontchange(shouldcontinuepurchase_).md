---
title: 'onStorefrontChange(shouldContinuePurchase:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 18.4+, iPadOS 18.4+, macOS 15.4+, tvOS 18.4+, visionOS 2.4+, watchOS 11.4+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/advancedcommerceproduct/purchaseoption/onstorefrontchange(shouldcontinuepurchase:)'
source_url: 'https://developer.apple.com/documentation/storekit/advancedcommerceproduct/purchaseoption/onstorefrontchange(shouldcontinuepurchase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/advancedcommerceproduct/purchaseoption/onstorefrontchange%28shouldcontinuepurchase%3A%29.json'
content_hash: 'sha256:23fb6a04e0c1c0de'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [AdvancedCommerceProduct](../../advancedcommerceproduct.md) · [PurchaseOption](../purchaseoption.md)

# onStorefrontChange(shouldContinuePurchase:)

<sub>Type Method</sub>

A closure that determines whether the transaction continues if the device’s App Store storefront changes during a transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func onStorefrontChange(shouldContinuePurchase: @escaping @Sendable (Storefront) -> Bool) -> AdvancedCommerceProduct.PurchaseOption
```

## Parameters

- `shouldContinuePurchase` — A closure that returns a Boolean value that determines whether the purchase continues when the storefront changes to `Storefront` during the purchase process.

## Discussion

The default is `true` if you don’t include this option in the purchase options.
