---
title: 'init(ids:prefersPromotionalIcon:icon:placeholderIcon:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/storeview/init(ids:preferspromotionalicon:icon:placeholdericon:)'
source_url: 'https://developer.apple.com/documentation/storekit/storeview/init(ids:preferspromotionalicon:icon:placeholdericon:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/storeview/init%28ids%3Apreferspromotionalicon%3Aicon%3Aplaceholdericon%3A%29.json'
content_hash: 'sha256:a74c510774ab66e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [StoreView](../storeview.md)

# init(ids:prefersPromotionalIcon:icon:placeholderIcon:)

<sub>Initializer</sub>

Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using an image and a custom placeholder icon.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(ids productIDs: some Collection<String>, prefersPromotionalIcon: Bool = false, @ViewBuilder icon: @escaping (Product) -> Icon, @ViewBuilder placeholderIcon: () -> PlaceholderIcon)
```

## Parameters

- `productIDs` — The product identifiers to load from the App Store.

- `prefersPromotionalIcon` — A Boolean value that indicates whether to use a promotional image from the App Store, if it’s available. If this parameter is `false`, the system ignores promotional images.

- `icon` — A closure that returns the image the view displays when the products finish loading from the App Store.

- `placeholderIcon` — A closure that returns the image that the view uses while the products are loading. The view uses the same placeholder image for all the products.

## Discussion

The store view shows the custom placeholder icon until all products finish loading. After the view finishes loading the products, it uses the image you provide, by default. If you set `prefersPromotionalIcon` to `true`, any products that have an available promotional image use the promotional image instead.

The following example shows how to create a store view using an icon and a custom placeholder icon:

```swift
StoreView(ids: [
    "com.example.product1",
    "com.example.product2"
]) { product in
     Image(systemName: "star.fill")
         .foregroundStyle(.yellow)
 } placeholderIcon: {
      Image(systemName: "star.fill")
         .foregroundStyle(.gray)
 }
```

## See Also

### Creating store views that load products

- [init(ids:prefersPromotionalIcon:)](<init(ids_preferspromotionalicon_).md>) — Creates a view to load and merchandise a collection of products from the App Store using product identifiers.
- [init(ids:prefersPromotionalIcon:icon:)](<init(ids_preferspromotionalicon_icon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using a custom image.
- [init(ids:icon:placeholderIcon:)](<init(ids_icon_placeholdericon_).md>) — Creates a view to load a collection of products from the App Store using product identifiers, and merchandise them using their promotional images and a custom placeholder icon.
