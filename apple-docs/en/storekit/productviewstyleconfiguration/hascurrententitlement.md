---
title: hasCurrentEntitlement
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/productviewstyleconfiguration/hascurrententitlement
source_url: 'https://developer.apple.com/documentation/storekit/productviewstyleconfiguration/hascurrententitlement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productviewstyleconfiguration/hascurrententitlement.json'
content_hash: 'sha256:adac4dcfc3504cfb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductViewStyleConfiguration](../productviewstyleconfiguration.md)

# hasCurrentEntitlement

<sub>Instance Property</sub>

A Boolean value that indicates whether an in-app purchase transaction exists for the product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let hasCurrentEntitlement: Bool
```

## Discussion

Use the [hasCurrentEntitlement](hascurrententitlement.md) property to determine whether a purchase may succeed, for a porduct that people can purchase only once. For example, if hasCurrentEntitlement is false, you may choose not to display a purchase button for the product, because the person has already purchased it.

> [!important] Important
> Don’t use this value to determine whether to enable access to the product; check the in-app purchase transaction information instead ([Transaction](../transaction.md)).

## See Also

### Getting a product’s information

- [product](product.md) — The in-app purchase product to merchandise.
- [state](state.md) — The product task state that indicates the product’s loading phase.
