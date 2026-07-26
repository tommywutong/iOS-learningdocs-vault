---
title: ProductViewStyle
framework: StoreKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/productviewstyle
source_url: 'https://developer.apple.com/documentation/storekit/productviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productviewstyle.json'
content_hash: 'sha256:24064b8a13bf251b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# ProductViewStyle

<sub>Protocol</sub>

A type that specifies the appearance and interaction of In-App Purchase products within the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol ProductViewStyle
```

## Overview

To configure the in-app purchase product style for a view hierarchy, use the [productViewStyle(_:)](<../swiftui/view/productviewstyle(__).md>) modifier.

To create a custom style, declare a type that conforms to the `ProductViewStyle` protocol. Implement the [makeBody(configuration:)](<productviewstyle/makebody(configuration_).md>) method to return a view that composes the elements of the configuration that the system provides to your method. The following code example shows how to create a custom product view style:

```swift
struct CustomProductViewStyle: ProductViewStyle {
    func makeBody(configuration: Configuration) -> some View {
        switch configuration.state {
        // Add other cases here.
        case .success(let product):
            VStack(alignment: .center) {
                configuration.icon
                Text(product.displayName)
                Button(product.displayPrice) {}
            }
        }
    }
}

ProductView(id: "com.example.product")
    .productViewStyle(CustomProductViewStyle())
    // Add your code here.
```

## Relationships

- **Conforming Types**: [AutomaticProductViewStyle](automaticproductviewstyle.md), [CompactProductViewStyle](compactproductviewstyle.md), [LargeProductViewStyle](largeproductviewstyle.md), [RegularProductViewStyle](regularproductviewstyle.md)

## Topics

### Getting built-in product view styles

- [automatic](productviewstyle/automatic.md)
- [compact](productviewstyle/compact.md) — An product view style suitable for layouts where less space is available, or for displaying more items in a small amount of space.
- [large](productviewstyle/large.md) — A product view style suitable for layouts where the in-app purchase content is prominent.
- [regular](productviewstyle/regular.md) — A product view style that uses a standard, platform-appropriate layout.

### Creating custom product views

- [makeBody(configuration:)](<productviewstyle/makebody(configuration_).md>) — Creates a view that represents the body of a product view.
- [Configuration](productviewstyle/configuration.md) — A type that represents the properties of a product view style.
- [Body](productviewstyle/body.md) — A view that represents the body of a product view.

### Supporting types

- [AutomaticProductViewStyle](automaticproductviewstyle.md)
- [CompactProductViewStyle](compactproductviewstyle.md) — A style for a product view that’s suitable for layouts with less available space, or for displaying more items in a small amount of space.
- [RegularProductViewStyle](regularproductviewstyle.md) — A style for a product view that uses a standard, platform-appropriate layout.
- [LargeProductViewStyle](largeproductviewstyle.md) — A style for a product view that’s suitable for layouts where the in-app purchase content is prominent.

## See Also

### Styling product views

- [productViewStyle(_:)](<../swiftui/view/productviewstyle(__).md>) — Sets the style for In-App Purchase product views within a view.
- [productIconBorder()](<../swiftui/view/producticonborder().md>) — Adds a standard border to an in-app purchase product’s icon .
- [ProductViewStyleConfiguration](productviewstyleconfiguration.md) — The properties of an In-App Purchase product for use by custom product view styles.
