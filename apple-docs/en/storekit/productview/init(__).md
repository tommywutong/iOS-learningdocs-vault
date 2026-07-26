---
title: 'init(_:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/productview/init(_:)'
source_url: 'https://developer.apple.com/documentation/storekit/productview/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productview/init%28_%3A%29.json'
content_hash: 'sha256:ef0cb13f5f82977e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductView](../productview.md)

# init(_:)

<sub>Initializer</sub>

Creates a view to merchandise an individual product using a configuration for product view style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ configuration: ProductViewStyleConfiguration) where Icon == ProductViewStyleConfiguration.Icon, PlaceholderIcon == ProductViewStyleConfiguration.Icon
```

## Parameters

- `configuration` — A configuration for a product view style.

## Discussion

Use this initializer within the [makeBody(configuration:)](<../productviewstyle/makebody(configuration_).md>) method of a [ProductViewStyle](../productviewstyle.md) to create an instance of the product view you want to style. This is useful for custom product view styles that modify the current style, rather than implementing a new style.

The following code example shows how to create and use custom styles by composing standard styles:

```swift
struct SpinnerWhenLoadingStyle: ProductViewStyle {
    public func makeBody(configuration: Configuration) -> some View {
        switch configuration.state {
        case .loading:
            ProgressView()
                .progressView(.circular)
        default:
            ProductView(configuration)
        }
    }
}
// Use the following elsewhere in the code.
ProductView(id: "com.example.product")
    .productViewStyle(SpinnerWhenLoadingStyle())
```
