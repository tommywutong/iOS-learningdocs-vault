---
title: 'init(_:prefersPromotionalIcon:icon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/productview/init(_:preferspromotionalicon:icon:)'
source_url: 'https://developer.apple.com/documentation/storekit/productview/init(_:preferspromotionalicon:icon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productview/init%28_%3Apreferspromotionalicon%3Aicon%3A%29.json'
content_hash: 'sha256:b9095637d7901288'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductView](../productview.md)

# init(_:prefersPromotionalIcon:icon:)

<sub>Initializer</sub>

Creates a view to merchandise an individual product using a custom icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ product: Product, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: () -> Icon) where PlaceholderIcon == EmptyView
```

## Parameters

- `product` — The product to merchandise.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use the promotional image from the App Store, if it’s available. If this value is `true` and a promotional image for the product is available, the view displays it instead of the view you provide in the `icon` parameter.

- `icon` — A closure that returns the image to use for decorating the in-app purchase product.

## Discussion

If `prefersPromotionalIcon` is `true` and the product has a promotional image, the view displays the promotional image instead of the view you provide in `icon`.

The following example shows how to create a product view using a custom icon:

```swift
ProductView(product) {
    Image(systemName: "star.fill")
        .foregroundStyle(.yellow)
}
```

> [!tip] Tip
> To gain more control over the image that decorates this view, use the [init(_:icon:)](<init(__icon_).md>) initializer. It receives a [ProductIconPhase](../producticonphase.md), which enables you to supply an image for each phase of the image-loading process.

## See Also

### Creating product views with preloaded products

- [init(_:prefersPromotionalIcon:)](<init(__preferspromotionalicon_).md>) — Creates a view to merchandise an individual product.
- [init(_:icon:)](<init(__icon_).md>) — Creates a view to display a product that the system already loaded from the App Store, and merchandise it using its promotional image.
