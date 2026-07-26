---
title: 'onStorefrontChange(shouldContinuePurchase:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/onstorefrontchange(shouldcontinuepurchase:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/onstorefrontchange(shouldcontinuepurchase:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/onstorefrontchange%28shouldcontinuepurchase%3A%29.json'
content_hash: 'sha256:e5e1c63754dc8a65'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# onStorefrontChange(shouldContinuePurchase:)

<sub>Type Method</sub>

Indicates whether a transaction needs to continue if the App Store storefront changes on the device during the transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency static func onStorefrontChange(shouldContinuePurchase: @escaping @Sendable (Storefront) -> Bool) -> Product.PurchaseOption
```

## Parameters

- `shouldContinuePurchase` — A closure that returns a Boolean value to indicate whether the purchase needs to continue when the App Store storefront changes to the [storefront](../../transaction/storefront.md) value during a transaction.

## Return Value

[PurchaseOption](../purchaseoption.md)

## Discussion

The default value is `true` if this option isn’t added to the purchase.
