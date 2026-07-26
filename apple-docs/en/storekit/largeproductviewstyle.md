---
title: LargeProductViewStyle
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/largeproductviewstyle
source_url: 'https://developer.apple.com/documentation/storekit/largeproductviewstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/largeproductviewstyle.json'
content_hash: 'sha256:3c09965b3e09164f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# LargeProductViewStyle

<sub>Structure</sub>

A style for a product view that’s suitable for layouts where the in-app purchase content is prominent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @preconcurrency struct LargeProductViewStyle
```

## Relationships

- **Conforms To**: [ProductViewStyle](productviewstyle.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the large product view style

- [large](productviewstyle/large.md) — A product view style suitable for layouts where the in-app purchase content is prominent.

### Creating the style

- [init()](<largeproductviewstyle/init().md>)

## See Also

### Supporting types

- [AutomaticProductViewStyle](automaticproductviewstyle.md)
- [CompactProductViewStyle](compactproductviewstyle.md) — A style for a product view that’s suitable for layouts with less available space, or for displaying more items in a small amount of space.
- [RegularProductViewStyle](regularproductviewstyle.md) — A style for a product view that uses a standard, platform-appropriate layout.
