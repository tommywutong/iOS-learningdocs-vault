---
title: 'init(products:prefersPromotionalIcon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storeview/init(products:preferspromotionalicon:)'
source_url: 'https://developer.apple.com/documentation/storekit/storeview/init(products:preferspromotionalicon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storeview/init%28products%3Apreferspromotionalicon%3A%29.json'
content_hash: 'sha256:c6f40064d9b0e056'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreView](../storeview.md)

# init(products:prefersPromotionalIcon:)

<sub>Initializer</sub>

Creates a view to load and merchandise a collection of products from the App Store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(products: some Collection<Product>, prefersPromotionalIcon: Bool = false) where Icon == EmptyView, PlaceholderIcon == EmptyView
```

## Parameters

- `products` — The products to merchandise.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use promotional images from the App Store, if they’re available. If this parameter is `false`, the system ignores promotional images.

## Discussion

By default, the store view doesn’t show promotional images. If you set `prefersPromotionalIcon` to `true`, the store view uses each product’s promotional image as its icon.

## See Also

### Creating store views with preloaded products

- [init(products:prefersPromotionalIcon:icon:)](<init(products_preferspromotionalicon_icon_).md>) — Creates a view to merchandise a collection of products using a custom icon.
- [init(products:icon:)](<init(products_icon_).md>) — Creates a view to merchandise a collection of products with promotional images.
