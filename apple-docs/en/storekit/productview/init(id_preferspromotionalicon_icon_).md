---
title: 'init(id:prefersPromotionalIcon:icon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/productview/init(id:preferspromotionalicon:icon:)'
source_url: 'https://developer.apple.com/documentation/storekit/productview/init(id:preferspromotionalicon:icon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productview/init%28id%3Apreferspromotionalicon%3Aicon%3A%29.json'
content_hash: 'sha256:829abb99b790aed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductView](../productview.md)

# init(id:prefersPromotionalIcon:icon:)

<sub>Initializer</sub>

Creates a view to load an individual product from the App Store and merchandise it using a custom icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(id productID: Product.ID, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: () -> Icon) where PlaceholderIcon == AutomaticProductPlaceholderIcon
```

## Parameters

- `productID` — The product identifier to load from the App Store.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use the promotional image from the App Store, if it’s available. If this value is `true` and a promotional image for the product is available, the view displays it instead of the view you provide in the `icon` parameter.

- `icon` — A closure that returns the image the view displays when the system finishes loading the product from the App Store.

## Discussion

The product view displays a placeholder icon until the system finishes loading the product. After the product loads, the system uses the view you provide in the `icon` parameter, by default. If `prefersPromotionalIcon` is `true` and the product has a promotional image, the view displays the promotional image as its icon instead of the provided view.

> [!tip] Tip
> To gain more control over the image that decorates this view, use the [init(id:icon:placeholderIcon:)](<init(id_icon_placeholdericon_).md>) initializer. It receives a [ProductIconPhase](../producticonphase.md), which enables you to supply an image for each phase of the image-loading process.

## See Also

### Creating product views that load products

- [init(id:prefersPromotionalIcon:)](<init(id_preferspromotionalicon_).md>) — Creates a view to load and merchandise an individual product from the App Store.
- [init(id:prefersPromotionalIcon:icon:placeholderIcon:)](<init(id_preferspromotionalicon_icon_placeholdericon_).md>) — Creates a view to load an individual product from the App Store and merchandise it using an image and a custom placeholder icon.
- [init(id:icon:placeholderIcon:)](<init(id_icon_placeholdericon_).md>) — Creates a view to load an individual product from the App Store, and merchandise it using its promotional image and a custom placeholder icon.
