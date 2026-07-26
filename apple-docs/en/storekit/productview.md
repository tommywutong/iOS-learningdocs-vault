---
title: ProductView
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/productview
source_url: 'https://developer.apple.com/documentation/storekit/productview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productview.json'
content_hash: 'sha256:577a041f92fe2146'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# ProductView

<sub>Structure</sub>

A view that merchandises an individual In-App Purchase product.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct ProductView<Icon, PlaceholderIcon> where Icon : View, PlaceholderIcon : View
```

## Overview

A `ProductView` shows information about an in-app purchase product, including its localized name, description, and price, and displays a purchase button.

You create a product view by providing a product identifier to load from the App Store, or a [Product](product.md) value you previously loaded. If you provide a product identifier, the view loads the product’s information from the App Store automatically, and updates the view when the product is available.

You can customize the view by providing a view to use as an icon, or image, for the in-app purchase product. If you provide a product identifier, you can optionally provide a placeholder icon for the system to use instead of the automatic placeholder icon. If you set up promoted images for your products in App Store Connect, you can choose to use those images as the icon.

You can customize the product view’s appearance using the standard styles, including the [CompactProductViewStyle](compactproductviewstyle.md), [RegularProductViewStyle](regularproductviewstyle.md), and [LargeProductViewStyle](largeproductviewstyle.md) styles. Apply the style using the [productViewStyle(_:)](<../swiftui/view/productviewstyle(__).md>) view modifier.

You can also create your own custom styles by creating styles that conform to the [ProductViewStyle](productviewstyle.md) protocol.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Creating product views that load products

- [init(id:prefersPromotionalIcon:)](<productview/init(id_preferspromotionalicon_).md>) — Creates a view to load and merchandise an individual product from the App Store.
- [init(id:prefersPromotionalIcon:icon:)](<productview/init(id_preferspromotionalicon_icon_).md>) — Creates a view to load an individual product from the App Store and merchandise it using a custom icon.
- [init(id:prefersPromotionalIcon:icon:placeholderIcon:)](<productview/init(id_preferspromotionalicon_icon_placeholdericon_).md>) — Creates a view to load an individual product from the App Store and merchandise it using an image and a custom placeholder icon.
- [init(id:icon:placeholderIcon:)](<productview/init(id_icon_placeholdericon_).md>) — Creates a view to load an individual product from the App Store, and merchandise it using its promotional image and a custom placeholder icon.

### Creating product views with preloaded products

- [init(_:prefersPromotionalIcon:icon:)](<productview/init(__preferspromotionalicon_icon_).md>) — Creates a view to merchandise an individual product using a custom icon.
- [init(_:prefersPromotionalIcon:)](<productview/init(__preferspromotionalicon_).md>) — Creates a view to merchandise an individual product.
- [init(_:icon:)](<productview/init(__icon_).md>) — Creates a view to display a product that the system already loaded from the App Store, and merchandise it using its promotional image.

### Creating product views with a configuration

- [init(_:)](<productview/init(__).md>) — Creates a view to merchandise an individual product using a configuration for product view style.

### Loading promotional images

- [ProductIconPhase](producticonphase.md) — The current phase of the asynchronous loading operation of a product’s promotional image.

### Supporting types

- [AutomaticProductPlaceholderIcon](automaticproductplaceholdericon.md) — A view that represents the default placeholder icon for an in-app store product.

## See Also

### Merchandising In-App Purchases, subscriptions, and offers

- [StoreView](storeview.md) — A view that merchandises a collection of In-App Purchase products.
- [SubscriptionStoreView](subscriptionstoreview.md) — A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.
- [SubscriptionOfferView](subscriptionofferview.md)
- [Backyard Birds: Building an app with SwiftData and widgets](../swiftui/backyard-birds-sample.md) — Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
