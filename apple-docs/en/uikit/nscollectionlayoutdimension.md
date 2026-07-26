---
title: NSCollectionLayoutDimension
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutdimension
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutdimension'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutdimension.json'
content_hash: 'sha256:ea865210647c44f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutDimension

<sub>Class</sub>

An individual dimension representing an item’s width or height in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSCollectionLayoutDimension
```

## Overview

Each item in a collection view has an explicit width dimension and height dimension, which combine to define the item’s size ([NSCollectionLayoutSize](nscollectionlayoutsize.md)).

You can express an item’s dimensions using an absolute, estimated, or fractional value.

Use an _absolute value_ to specify exact dimensions, like a 44 x 44 point square:

**Swift**

```swift
let absoluteSize = NSCollectionLayoutSize(widthDimension: .absolute(44),
                                         heightDimension: .absolute(44))
```

**Objective-C**

```objc
NSCollectionLayoutSize *absoluteSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension absoluteDimension:44.0] heightDimension:[NSCollectionLayoutDimension absoluteDimension:44.0]];
```

Use an _estimated value_ if the size of your content might change at runtime, such as when data is loaded or in response to a change in system font size. You provide an initial estimated size and the system computes the actual value later.

**Swift**

```swift
let estimatedSize = NSCollectionLayoutSize(widthDimension: .estimated(200),
                                          heightDimension: .estimated(100))
```

**Objective-C**

```objc
NSCollectionLayoutSize *estimatedSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension estimatedDimension:200.0] heightDimension:[NSCollectionLayoutDimension estimatedDimension:100.0]];
```

Use a _fractional value_ to define a value that’s relative to a dimension of the item’s container. This option simplifies specifying aspect ratios. For example, the following item has a width and a height that are both equal to 20% of its container’s width, creating a square that grows and shrinks as the size of its container changes.

**Swift**

```swift
let fractionalSize = NSCollectionLayoutSize(widthDimension: .fractionalWidth(0.2),
                                           heightDimension: .fractionalWidth(0.2))
```

**Objective-C**

```objc
NSCollectionLayoutSize *fractionalSize = [NSCollectionLayoutSize sizeWithWidthDimension:[NSCollectionLayoutDimension fractionalWidthDimension:0.2] heightDimension:[NSCollectionLayoutDimension fractionalWidthDimension:0.2]];
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating a dimension

- [+ absoluteDimension:](<nscollectionlayoutdimension/absolute(__).md>) — Creates a dimension with an absolute point value.
- [+ estimatedDimension:](<nscollectionlayoutdimension/estimated(__).md>) — Creates a dimension with an estimated point value.
- [+ fractionalHeightDimension:](<nscollectionlayoutdimension/fractionalheight(__).md>) — Creates a dimension that is computed as a fraction of the height of the containing group.
- [+ fractionalWidthDimension:](<nscollectionlayoutdimension/fractionalwidth(__).md>) — Creates a dimension that is computed as a fraction of the width of the containing group.
- [+ uniformAcrossSiblingsWithEstimate:](<nscollectionlayoutdimension/uniformacrosssiblings(estimate_).md>) — Creates a dimension in which each item receives as much room as it requires and grows to match the dimension of its largest sibling.

### Getting the dimension value

- [dimension](nscollectionlayoutdimension/dimension.md) — The floating-point value of the dimension.

### Getting the dimension type

- [isAbsolute](nscollectionlayoutdimension/isabsolute.md) — A Boolean value that indicates whether the dimension is expressed as an absolute value.
- [isEstimated](nscollectionlayoutdimension/isestimated.md) — A Boolean value that indicates whether the dimension is expressed as an estimated value.
- [isFractionalHeight](nscollectionlayoutdimension/isfractionalheight.md) — A Boolean value that indicates whether the dimension is expressed as a fraction of its container’s height.
- [isFractionalWidth](nscollectionlayoutdimension/isfractionalwidth.md) — A Boolean value that indicates whether the dimension is expressed as a fraction of its container’s width.
- [isUniformAcrossSiblings](nscollectionlayoutdimension/isuniformacrosssiblings.md) — A Boolean value that indicates whether the dimension grows to match the dimension of its largest sibling.

## See Also

### Size and spacing

- [NSCollectionLayoutSize](nscollectionlayoutsize.md) — The width and the height of an item in a collection view.
- [NSCollectionLayoutSpacing](nscollectionlayoutspacing.md) — An object that defines the space between or around items in a collection view.
- [NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md) — An object that defines the space around the edges of items in a collection view.
- [NSCollectionLayoutContainer](nscollectionlayoutcontainer.md) — A protocol used to provide information about the size and content insets of a layout’s container.
