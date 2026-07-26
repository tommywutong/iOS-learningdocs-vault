---
title: visibility
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/promotioninfo/visibility-swift.property
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo/visibility-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo/visibility-swift.property.json'
content_hash: 'sha256:5d19f388cb42cd99'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PromotionInfo](../promotioninfo.md)

# visibility

<sub>Instance Property</sub>

A value that indicates whether the promoted in-app purchase is visible or hidden on the user’s device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var visibility: Product.PromotionInfo.Visibility
```

## Discussion

To override the visibility of a promoted in-app purchase, set the [visibility](visibility-swift.property.md) value and then call [update()](<update().md>) to save the change. You can also call [updateProductVisibility(_:for:)](<updateproductvisibility(__for_).md>) to set the visibility.

The default value is [Product.PromotionInfo.Visibility.appStoreConnectDefault](visibility-swift.enum/appstoreconnectdefault.md).

## See Also

### Managing promotion visibility

- [Visibility](visibility-swift.enum.md) — The visibility states for product promotion information.
- [updateProductVisibility(_:for:)](<updateproductvisibility(__for_).md>) — Updates a value that indicates whether a promoted in-app purchase appears in the App Store on the user’s device.
