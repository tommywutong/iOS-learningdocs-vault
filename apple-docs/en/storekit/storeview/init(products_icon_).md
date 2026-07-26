---
title: 'init(products:icon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storeview/init(products:icon:)'
source_url: 'https://developer.apple.com/documentation/storekit/storeview/init(products:icon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storeview/init%28products%3Aicon%3A%29.json'
content_hash: 'sha256:1be6b84f0d7acdb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreView](../storeview.md)

# init(products:icon:)

<sub>Initializer</sub>

Creates a view to merchandise a collection of products with promotional images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(products: some Collection<Product>, @ViewBuilder icon: @escaping (Product, ProductIconPhase) -> Icon) where PlaceholderIcon == EmptyView
```

## Parameters

- `products` — The products to merchandise.

- `icon` — A closure that receives a [Product](../product.md) and a [ProductIconPhase](../producticonphase.md) as input. The [ProductIconPhase](../producticonphase.md) indicates the state of the loading operation of the product’s promotional image. The closure returns the view to display for the given product and phase value.

## Discussion

The store view asynchronously loads and displays each product’s promotional image. Use the [ProductIconPhase](../producticonphase.md) to monitor the current loading phase of the product’s promotional image, and provide an image for each phase. For more information about the loading phases, see [ProductIconPhase](../producticonphase.md).

## See Also

### Creating store views with preloaded products

- [init(products:prefersPromotionalIcon:)](<init(products_preferspromotionalicon_).md>) — Creates a view to load and merchandise a collection of products from the App Store.
- [init(products:prefersPromotionalIcon:icon:)](<init(products_preferspromotionalicon_icon_).md>) — Creates a view to merchandise a collection of products using a custom icon.
