---
title: ProductViewStyleConfiguration
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/productviewstyleconfiguration
source_url: 'https://developer.apple.com/documentation/storekit/productviewstyleconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productviewstyleconfiguration.json'
content_hash: 'sha256:a566511c71548c2a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# ProductViewStyleConfiguration

<sub>Structure</sub>

The properties of an In-App Purchase product for use by custom product view styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ProductViewStyleConfiguration
```

## Overview

Use the `ProductViewStyleConfiguration` to create a custom [ProductViewStyle](productviewstyle.md).

## Topics

### Getting a product’s information

- [product](productviewstyleconfiguration/product.md) — The in-app purchase product to merchandise.
- [state](productviewstyleconfiguration/state.md) — The product task state that indicates the product’s loading phase.
- [hasCurrentEntitlement](productviewstyleconfiguration/hascurrententitlement.md) — A Boolean value that indicates whether an in-app purchase transaction exists for the product.

### Getting a product view’s icon

- [icon](productviewstyleconfiguration/icon-swift.property.md) — A decorative view for merchandising the product.
- [Icon](productviewstyleconfiguration/icon-swift.struct.md) — A type-erased icon of an in-app purchase product.

### Getting a product’s description visibility

- [descriptionVisibility](productviewstyleconfiguration/descriptionvisibility.md) — The visibility of product descriptions.

### Initiating a purchase

- [purchase()](<productviewstyleconfiguration/purchase().md>) — Initiates a purchase action for the product.

## See Also

### Styling product views

- [productViewStyle(_:)](<../swiftui/view/productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productIconBorder()](<../swiftui/view/producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [ProductViewStyle](productviewstyle.md) — A type that specifies the appearance and interaction of In-App Purchase products within the view hierarchy.
