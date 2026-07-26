---
title: 'init(_:prefersPromotionalIcon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/productview/init(_:preferspromotionalicon:)'
source_url: 'https://developer.apple.com/documentation/storekit/productview/init(_:preferspromotionalicon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productview/init%28_%3Apreferspromotionalicon%3A%29.json'
content_hash: 'sha256:6592e1b92be70630'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductView](../productview.md)

# init(_:prefersPromotionalIcon:)

<sub>Initializer</sub>

Creates a view to merchandise an individual product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ product: Product, prefersPromotionalIcon: Bool = true) where Icon == EmptyView, PlaceholderIcon == EmptyView
```

## Parameters

- `product` — The product to merchandise.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use the promotional image from the App Store, if it’s available. If this value is `true` and a promotional image for the product is available, the view displays it.

## Discussion

If the product has a promotional image available, the view displays it. Otherwise, the view doesn’t show an image.

If you set the `prefersPromotionalIcon` parameter to `false`, the view doesn’t show an image even if the product has a promotional image available.

> [!tip] Tip
> To gain more control over the image that decorates this view, use the [init(_:icon:)](<init(__icon_).md>) initializer. It receives a [ProductIconPhase](../producticonphase.md), which enables you to supply an image for each phase of the image-loading process.

## See Also

### Creating product views with preloaded products

- [init(_:prefersPromotionalIcon:icon:)](<init(__preferspromotionalicon_icon_).md>) — Creates a view to merchandise an individual product using a custom icon.
- [init(_:icon:)](<init(__icon_).md>) — Creates a view to display a product that the system already loaded from the App Store, and merchandise it using its promotional image.
