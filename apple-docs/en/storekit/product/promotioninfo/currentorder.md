---
title: currentOrder
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/promotioninfo/currentorder
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo/currentorder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo/currentorder.json'
content_hash: 'sha256:e3814998df3a4f72'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PromotionInfo](../promotioninfo.md)

# currentOrder

<sub>Type Property</sub>

Gets the customized order of the promotion info objects the represent promoted products.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static var currentOrder: [Product.PromotionInfo] { get async throws }
```

## Discussion

This asynchronous array returns a list of [PromotionInfo](../promotioninfo.md) objects in the custom order they appear in on the device.

> [!note] Note
> This list is empty if you don’t override the order, and the App Store displays the products in their default order.

For information about setting the default order using App Store Connect, see [Promote in-app purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/promote-in-app-purchases).
