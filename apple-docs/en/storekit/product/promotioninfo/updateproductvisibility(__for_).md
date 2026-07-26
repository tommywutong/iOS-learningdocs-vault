---
title: 'updateProductVisibility(_:for:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/promotioninfo/updateproductvisibility(_:for:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo/updateproductvisibility(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo/updateproductvisibility%28_%3Afor%3A%29.json'
content_hash: 'sha256:8622db03c1e4a05f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PromotionInfo](../promotioninfo.md)

# updateProductVisibility(_:for:)

<sub>Type Method</sub>

Updates a value that indicates whether a promoted in-app purchase appears in the App Store on the user’s device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func updateProductVisibility(_ visibility: Product.PromotionInfo.Visibility, for productID: Product.ID) async throws
```

## Parameters

- `visibility` — A visibility value of [Visibility](visibility-swift.enum.md) that determines whether a promoted in-app purchase appears in the App Store on the user’s device.

- `productID` — The product identifier of the promoted in-app purchase.

## Discussion

Call this method to change the visibility setting for a promoted in-app purchase. Changes take effect after you call this method.

The following code example updates a promoted product’s visibility after the user purchases it. The purchased product is hidden to avoid showing it again on the device.

```swift
// Update visibility to hide a promoted product after the user purchases it.
let purchasedProductIdentifier = "com.example.ExampleApp.product1"

do {
  try await Product.PromotionInfo.updateProductVisibility(.hidden, for: purchasedProductIdentifier)
}
catch {
  <#Handle Error#>
}
```

## See Also

### Managing promotion visibility

- [visibility](visibility-swift.property.md) — A value that indicates whether the promoted in-app purchase is visible or hidden on the user’s device.
- [Visibility](visibility-swift.enum.md) — The visibility states for product promotion information.
