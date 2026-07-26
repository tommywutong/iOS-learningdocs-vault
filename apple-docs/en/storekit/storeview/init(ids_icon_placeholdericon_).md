---
title: 'init(ids:icon:placeholderIcon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storeview/init(ids:icon:placeholdericon:)'
source_url: 'https://developer.apple.com/documentation/storekit/storeview/init(ids:icon:placeholdericon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storeview/init%28ids%3Aicon%3Aplaceholdericon%3A%29.json'
content_hash: 'sha256:9b6b2ebf8eb728f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreView](../storeview.md)

# init(ids:icon:placeholderIcon:)

<sub>Initializer</sub>

Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using their promotional images and a custom placeholder icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(ids productIDs: some Collection<String>, @ViewBuilder icon: @escaping (Product, ProductIconPhase) -> Icon, @ViewBuilder placeholderIcon: () -> PlaceholderIcon)
```

## Parameters

- `productIDs` — The product identifiers to load from the App Store.

- `icon` — A closure that receives a [Product](../product.md) and a [ProductIconPhase](../producticonphase.md) as input. The [ProductIconPhase](../producticonphase.md) indicates the state of the loading operation of the product’s promotional image. The closure returns the view to display for the given product and phase value.

- `placeholderIcon` — A closure that returns the view that the store view uses while the products are loading. The store view uses the same placeholder image for all the products.

## Discussion

The store view shows the custom `placeholderIcon` until all products finish loading. After the products finish loading, the view asynchronously loads and displays each product’s promotional image.

Use the [ProductIconPhase](../producticonphase.md) to monitor the current loading state of a product’s promotional image, and provide a view for each phase. Consider returning the view provided in the `placeholderIcon` closure for during the [ProductIconPhase.loading](../producticonphase/loading.md) phase. For more information, see [ProductIconPhase](../producticonphase.md).

If a product is unavailable, the store view uses the view that the `placeholderIcon` closure provides as a fallback.

## See Also

### Creating store views that load products

- [init(ids:prefersPromotionalIcon:)](<init(ids_preferspromotionalicon_).md>) — Creates a view to load and merchandise a collection of products from the App Store using product identifiers.
- [init(ids:prefersPromotionalIcon:icon:)](<init(ids_preferspromotionalicon_icon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using a custom image.
- [init(ids:prefersPromotionalIcon:icon:placeholderIcon:)](<init(ids_preferspromotionalicon_icon_placeholdericon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using an image and a custom placeholder icon.
