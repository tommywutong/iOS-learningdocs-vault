---
title: 'init(id:prefersPromotionalIcon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/productview/init(id:preferspromotionalicon:)'
source_url: 'https://developer.apple.com/documentation/storekit/productview/init(id:preferspromotionalicon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productview/init%28id%3Apreferspromotionalicon%3A%29.json'
content_hash: 'sha256:26cca27074de1212'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductView](../productview.md)

# init(id:prefersPromotionalIcon:)

<sub>Initializer</sub>

Creates a view to load and merchandise an individual product from the App Store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(id productID: Product.ID, prefersPromotionalIcon: Bool = false) where Icon == EmptyView, PlaceholderIcon == EmptyView
```

## Parameters

- `productID` — The product identifier to load from the App Store.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use the promotional image from the App Store, if it’s available. If this parameter is `false`, the system ignores any promotional images.

## Discussion

By default, the view doesn’t show an icon. If you set the `prefersPromotionalIcon` parameter to `true`, the view displays a placeholder icon while loading, and replaces the placeholder with the promotional image for the product.

> [!tip] Tip
> To gain more control over the image that decorates this view, use the [init(id:icon:placeholderIcon:)](<init(id_icon_placeholdericon_).md>) initializer. It receives a [ProductIconPhase](../producticonphase.md), which enables you to supply an image for each phase of the image-loading process.

## See Also

### Creating product views that load products

- [init(id:prefersPromotionalIcon:icon:)](<init(id_preferspromotionalicon_icon_).md>) — Creates a view to load an individual product from the App Store and merchandise it using a custom icon.
- [init(id:prefersPromotionalIcon:icon:placeholderIcon:)](<init(id_preferspromotionalicon_icon_placeholdericon_).md>) — Creates a view to load an individual product from the App Store and merchandise it using an image and a custom placeholder icon.
- [init(id:icon:placeholderIcon:)](<init(id_icon_placeholdericon_).md>) — Creates a view to load an individual product from the App Store, and merchandise it using its promotional image and a custom placeholder icon.
