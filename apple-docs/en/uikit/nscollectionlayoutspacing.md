---
title: NSCollectionLayoutSpacing
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutspacing
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutspacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutspacing.json'
content_hash: 'sha256:2ee4fd77d35fddf7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutSpacing

<sub>Class</sub>

An object that defines the space between or around items in a collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class NSCollectionLayoutSpacing
```

## Overview

In a collection view layout, you use a spacing object to specify both the amount of space and the way in which it’s calculated.

You can express spacing using fixed or flexible spacing.

Use _fixed spacing_ to provide an exact amount of space. For example, the following code creates exactly 200 points of space between the items in the group.

**Swift**

```swift
group.interItemSpacing = .fixed(200.0)
```

**Objective-C**

```objc
[group setInterItemSpacing: [NSCollectionLayoutSpacing fixedSpacing:200.0]];
```

Use _flexible spacing_ to provide a minimum amount of space that can grow as more space becomes available. For example, the following code creates at least 200 points of space between the items in the group. As more space becomes available, items are respaced evenly in the additional space.

**Swift**

```swift
group.interItemSpacing = .flexible(200.0)
```

**Objective-C**

```objc
[group setInterItemSpacing: [NSCollectionLayoutSpacing flexibleSpacing:200.0]];
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating spacing

- [+ fixedSpacing:](<nscollectionlayoutspacing/fixed(__).md>) — Creates a space equivalent to the specified number of points.
- [+ flexibleSpacing:](<nscollectionlayoutspacing/flexible(__).md>) — Creates a space equivalent to or greater than the specified number of points, depending on the available space.

### Getting the spacing value

- [spacing](nscollectionlayoutspacing/spacing.md) — The floating-point value of the space.

### Getting the spacing type

- [isFixedSpacing](nscollectionlayoutspacing/isfixed.md) — A Boolean value that indicates whether the space is fixed to a specific number of points.
- [isFlexibleSpacing](nscollectionlayoutspacing/isflexible.md) — A Boolean value that indicates whether the space is flexible.

## See Also

### Size and spacing

- [NSCollectionLayoutDimension](nscollectionlayoutdimension.md) — An individual dimension representing an item’s width or height in a collection view.
- [NSCollectionLayoutSize](nscollectionlayoutsize.md) — The width and the height of an item in a collection view.
- [NSCollectionLayoutEdgeSpacing](nscollectionlayoutedgespacing.md) — An object that defines the space around the edges of items in a collection view.
- [NSCollectionLayoutContainer](nscollectionlayoutcontainer.md) — A protocol used to provide information about the size and content insets of a layout’s container.
