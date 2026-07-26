---
title: update()
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.4+, iPadOS 16.4+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/product/promotioninfo/update()
source_url: 'https://developer.apple.com/documentation/storekit/product/promotioninfo/update()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/promotioninfo/update%28%29.json'
content_hash: 'sha256:c6a24c9731265fe0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PromotionInfo](../promotioninfo.md)

# update()

<sub>Instance Method</sub>

Saves your changes to the promoted product’s visibility.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func update() async throws
```

## Discussion

If you change the [visibility](visibility-swift.property.md) value by setting it directly, call [update()](<update().md>) to save your changes to the App Store server. Changes take effect after you call [update()](<update().md>) or [updateAll(_:)](<updateall(__).md>).

## See Also

### Updating order and visibility

- [updateAll(_:)](<updateall(__).md>) — Sets the order and visibility of all the promoted products and saves your changes.
