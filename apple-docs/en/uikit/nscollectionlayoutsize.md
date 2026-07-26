---
title: NSCollectionLayoutSize
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutsize
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutsize.json'
content_hash: 'sha256:b784ac0a27cc1537'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutSize

<sub>Class</sub>

The width and the height of an item in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSCollectionLayoutSize
```

## Overview

A size is a pair of dimensions ([NSCollectionLayoutDimension](nscollectionlayoutdimension.md)): a width dimension and a height dimension. Every component of a collection view layout has an explicit size.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a layout size

- [+ sizeWithWidthDimension:heightDimension:](<nscollectionlayoutsize/init(widthdimension_heightdimension_).md>) — Creates a size with the specified width and height dimensions.

### Getting the width and height

- [widthDimension](nscollectionlayoutsize/widthdimension.md) — The width dimension of an item in a collection view layout.
- [heightDimension](nscollectionlayoutsize/heightdimension.md) — The height dimension of an item in a collection view layout.

## See Also

### Size and spacing

- [NSCollectionLayoutDimension](nscollectionlayoutdimension.md) — An individual dimension representing an item’s width or height in a collection view.
- [NSCollectionLayoutSpacing](nscollectionlayoutspacing.md) — An object that defines the space between or around items in a collection view.
- [NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md) — An object that defines the space around the edges of items in a collection view.
- [NSCollectionLayoutContainer](nscollectionlayoutcontainer.md) — A protocol used to provide information about the size and content insets of a layout’s container.
