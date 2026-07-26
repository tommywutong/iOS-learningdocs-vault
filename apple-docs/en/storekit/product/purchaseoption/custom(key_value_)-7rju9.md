---
title: 'custom(key:value:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/product/purchaseoption/custom(key:value:)-7rju9'
source_url: 'https://developer.apple.com/documentation/storekit/product/purchaseoption/custom(key:value:)-7rju9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/purchaseoption/custom%28key%3Avalue%3A%29-7rju9.json'
content_hash: 'sha256:feea239d6392623e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [PurchaseOption](../purchaseoption.md)

# custom(key:value:)

<sub>Type Method</sub>

Adds a number for a custom key to a purchase.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func custom(key: String, value: Double) -> Product.PurchaseOption
```

## Parameters

- `key` — The key for this custom option.

- `value` — The numerical value you assign to this custom option.

## Discussion

This custom purchase option doesn’t have any effect.

## See Also

### Setting custom purchase options

- [custom(key:value:)](<custom(key_value_)-80cvh.md>) — Adds data for a custom key to a purchase.
- [custom(key:value:)](<custom(key_value_)-3g3nc.md>) — Adds a string for a custom key to a purchase.
- [custom(key:value:)](<custom(key_value_)-8tjim.md>) — Adds a Boolean value for a custom key to a purchase.
