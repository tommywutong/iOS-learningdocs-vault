---
title: 'init(ids:prefersPromotionalIcon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storeview/init(ids:preferspromotionalicon:)'
source_url: 'https://developer.apple.com/documentation/storekit/storeview/init(ids:preferspromotionalicon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storeview/init%28ids%3Apreferspromotionalicon%3A%29.json'
content_hash: 'sha256:5e98d6bfcf4f502c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreView](../storeview.md)

# init(ids:prefersPromotionalIcon:)

<sub>Initializer</sub>

Creates a view to load and merchandise a collection of products from the App Store using product identifiers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(ids productIDs: some Collection<String>, prefersPromotionalIcon: Bool = false) where Icon == EmptyView, PlaceholderIcon == EmptyView
```

## Parameters

- `productIDs` — The product identifiers to load from the App Store.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use promotional images from the App Store, if they’re available. If this parameter is `false`, the system ignores promotional images.

## See Also

### Creating store views that load products

- [init(ids:prefersPromotionalIcon:icon:)](<init(ids_preferspromotionalicon_icon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using a custom image.
- [init(ids:prefersPromotionalIcon:icon:placeholderIcon:)](<init(ids_preferspromotionalicon_icon_placeholdericon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using an image and a custom placeholder icon.
- [init(ids:icon:placeholderIcon:)](<init(ids_icon_placeholdericon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using their promotional images and a custom placeholder icon.
