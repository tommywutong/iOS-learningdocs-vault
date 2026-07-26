---
title: 'updateAll(_:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/promotioninfo/updateall(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo/updateall(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo/updateall%28_%3A%29.json'
content_hash: 'sha256:1825ff6af7d422eb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PromotionInfo](../promotioninfo.md)

# updateAll(_:)

<sub>Type Method</sub>

Sets the order and visibility of all the promoted products and saves your changes.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static func updateAll(_ promotions: some Collection<Product.PromotionInfo>) async throws
```

## Parameters

- `promotions` — A collection of [PromotionInfo](../promotioninfo.md) objects that you list in the order they are to appear in the App Store on the user’s device. Use an empty collection to cancel previous changes.

## Discussion

Call this static method to set the order of promoted in-app purchases for the user. Calling this method overrides any previous order and visibility that you set for this user.

To remove a promoted in-app purchase so it doesn’t display for a user, there are two options:

- Don’t include it in the `promotions` collection.
- Change its [visibility](visibility-swift.property.md) value to [Product.PromotionInfo.Visibility.hidden](visibility-swift.enum/hidden.md).

To set the order of promoted in-app purchases using product identifiers instead of [PromotionInfo](../promotioninfo.md) objects, see [updateProductOrder(byID:)](<updateproductorder(byid_).md>).

### Cancel overrides

To cancel the order and visibility changes you make, send an empty collection in `promotions`. All in-app purchases then display in the default order.

## See Also

### Updating order and visibility

- [update()](<update().md>) — Saves your changes to the promoted product’s visibility.
