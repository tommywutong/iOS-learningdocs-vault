---
title: 'init(_:icon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/productview/init(_:icon:)'
source_url: 'https://developer.apple.com/documentation/storekit/productview/init(_:icon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productview/init%28_%3Aicon%3A%29.json'
content_hash: 'sha256:c84460693fc7f6ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductView](../productview.md)

# init(_:icon:)

<sub>Initializer</sub>

Creates a view to display a product that the system already loaded from the App Store, and merchandise it using its promotional image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ product: Product, @ViewBuilder icon: @escaping (ProductIconPhase) -> Icon) where PlaceholderIcon == EmptyView
```

## Parameters

- `product` — The product to merchandise.

- `icon` — A closure that receives a [ProductIconPhase](../producticonphase.md) as an input, which indicates the state of the loading operation of the product’s promoted image, and returns the view to display for the specified phase.

## Discussion

The product view asynchronously loads and displays the product’s promotional image.

The [ProductIconPhase](../producticonphase.md) value indicates whether the promotional image is loading, unavailable, or whether it succeeded or failed to load. Use the [ProductIconPhase](../producticonphase.md) to monitor current loading phase, and to decide the image to return in the `icon` closure.

## See Also

### Creating product views with preloaded products

- [init(_:prefersPromotionalIcon:icon:)](<init(__preferspromotionalicon_icon_).md>) — Creates a view to merchandise an individual product using a custom icon.
- [init(_:prefersPromotionalIcon:)](<init(__preferspromotionalicon_).md>) — Creates a view to merchandise an individual product.
