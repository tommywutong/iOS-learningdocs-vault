---
title: 'updateProductOrder(byID:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/promotioninfo/updateproductorder(byid:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo/updateproductorder(byid:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo/updateproductorder%28byid%3A%29.json'
content_hash: 'sha256:e012b05f68b6efa3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PromotionInfo](../promotioninfo.md)

# updateProductOrder(byID:)

<sub>Type Method</sub>

Sets the display order of promoted in-app purchases in the App Store, using product identifiers.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func updateProductOrder(byID order: some Collection<String>) async throws
```

## Parameters

- `order` — A collection of product identifiers ([id](../id.md)) in the order that you want the promoted in-app purchases to appear, from first to last. Use an empty list to cancel previous changes.

## Discussion

Call this static method to override the default order of promoted in-app purchases on the current device. You provide the product identifiers of the promoted in-app purchases to set their order.

To hide a promoted in-app purchase so it doesn’t display in the App Store for the user, don’t include its product identifier when calling this method. You may want to do this, for example, if the user has already purchased the product, or if it isn’t relevant to them for some other reason.

To set the order using [PromotionInfo](../promotioninfo.md) objects instead of product identifiers, see [updateAll(_:)](<updateall(__).md>).

### Cancel overrides

To cancel the order and visibility changes you make, send an empty collection in the `order` parameter. All in-app purchases then display in the default order.

```swift
// Cancel overrides by using an empty collection.
do {
    try await Product.PromotionInfo.updateProductOrder(byID: [])
}
catch {
    <#Handle error.#>
}
```
