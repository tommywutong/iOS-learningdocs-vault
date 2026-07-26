---
title: 'init(ids:prefersPromotionalIcon:icon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storeview/init(ids:preferspromotionalicon:icon:)'
source_url: 'https://developer.apple.com/documentation/storekit/storeview/init(ids:preferspromotionalicon:icon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storeview/init%28ids%3Apreferspromotionalicon%3Aicon%3A%29.json'
content_hash: 'sha256:a0c44abea9ce9419'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreView](../storeview.md)

# init(ids:prefersPromotionalIcon:icon:)

<sub>Initializer</sub>

Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using a custom image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(ids productIDs: some Collection<String>, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: @escaping (Product) -> Icon) where PlaceholderIcon == AutomaticProductPlaceholderIcon
```

## Parameters

- `productIDs` — The product identifiers to load from the App Store.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use promotional images from the App Store, if they’re available. If this parameter is `false`, the system ignores promotional images.

- `icon` — A closure that returns the image the view displays when the products finish loading from the App Store.

## Discussion

The store view shows a placeholder icon until all products finish loading. Then, the view uses the image that you provide in `icon`, by default. If you set `prefersPromotionalIcon` to `true`, the view uses the promotional image instead of the `icon` for any products that have promotional images available.

## See Also

### Creating store views that load products

- [init(ids:prefersPromotionalIcon:)](<init(ids_preferspromotionalicon_).md>) — Creates a view to load and merchandise a collection of products from the App Store using product identifiers.
- [init(ids:prefersPromotionalIcon:icon:placeholderIcon:)](<init(ids_preferspromotionalicon_icon_placeholdericon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using an image and a custom placeholder icon.
- [init(ids:icon:placeholderIcon:)](<init(ids_icon_placeholdericon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using their promotional images and a custom placeholder icon.
