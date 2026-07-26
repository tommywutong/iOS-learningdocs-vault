---
title: CompactProductViewStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/compactproductviewstyle
source_url: 'https://developer.apple.com/documentation/storekit/compactproductviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/compactproductviewstyle.json'
content_hash: 'sha256:066fc773c69e4ede'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# CompactProductViewStyle

<sub>Structure</sub>

A style for a product view that’s suitable for layouts with less available space, or for displaying more items in a small amount of space.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@MainActor @preconcurrency struct CompactProductViewStyle
```

## Relationships

- **Conforms To**: [ProductViewStyle](productviewstyle.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the compact product view style

- [compact](productviewstyle/compact.md) — An product view style suitable for layouts where less space is available, or for displaying more items in a small amount of space.

### Creating the style

- [init()](<compactproductviewstyle/init().md>)

## See Also

### Supporting types

- [AutomaticProductViewStyle](automaticproductviewstyle.md)
- [RegularProductViewStyle](regularproductviewstyle.md) — A style for a product view that uses a standard, platform-appropriate layout.
- [LargeProductViewStyle](largeproductviewstyle.md) — A style for a product view that’s suitable for layouts where the in-app purchase content is prominent.
