---
title: 'makeBody(configuration:)'
framework: StoreKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/storekit/productviewstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/storekit/productviewstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/productviewstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:33dc04e31bd0be26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [ProductViewStyle](../productviewstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Creates a view that represents the body of a product view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@ViewBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of a product view style.

## See Also

### Creating custom product views

- [Configuration](configuration.md) — A type that represents the properties of a product view style.
- [Body](body.md) — A view that represents the body of a product view.
