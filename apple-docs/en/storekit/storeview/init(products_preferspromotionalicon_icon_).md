---
title: 'init(products:prefersPromotionalIcon:icon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storeview/init(products:preferspromotionalicon:icon:)'
source_url: 'https://developer.apple.com/documentation/storekit/storeview/init(products:preferspromotionalicon:icon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storeview/init%28products%3Apreferspromotionalicon%3Aicon%3A%29.json'
content_hash: 'sha256:599f6e0bfadaea24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreView](../storeview.md)

# init(products:prefersPromotionalIcon:icon:)

<sub>Initializer</sub>

Creates a view to merchandise a collection of products using a custom icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(products: some Collection<Product>, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: @escaping (Product) -> Icon) where PlaceholderIcon == EmptyView
```

## Parameters

- `products` — The products to merchandise.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use promotional images from the App Store, if they’re available. If this parameter is `false`, the system ignores promotional images.

- `icon` — A closure that returns the image the view displays when the products finish loading from the App Store.

## Discussion

If you set `prefersPromotionalIcon` to `true`, the view uses promotional images for products that have a promotional image available.

The following code example shows how to create a store view using a custom icon:

```swift
StoreView(products: [
          product1,
          product2,
          // Add products as needed.
 ]) { product in
    Image(systemName: "star.fill")
        .foregroundStyle(.yellow)
    }  
```

## See Also

### Creating store views with preloaded products

- [init(products:prefersPromotionalIcon:)](<init(products_preferspromotionalicon_).md>) — Creates a view to load and merchandise a collection of products from the App Store.
- [init(products:icon:)](<init(products_icon_).md>) — Creates a view to merchandise a collection of products with promotional images.
