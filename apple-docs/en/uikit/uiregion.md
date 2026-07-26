---
title: UIRegion
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiregion
source_url: 'https://developer.apple.com/documentation/uikit/uiregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiregion.json'
content_hash: 'sha256:89d26d3e2b99331f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIRegion

<sub>Class</sub>

A shape for use in UIKit Dynamics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIRegion
```

## Overview

When creating animations, you use regions to define the effective area of a field behavior such as a magnetic or gravitational force. Most regions are rectangular or elliptical in shape, but you can use the methods of this class to create more complex shapes by adding, subtracting, and intersecting other regions.

When creating a new region, you specify only the size of the corresponding rectangle or circle. The origin of a newly created region is at the center of the specified area, and any mathematical manipulations you make to the region occur relative to that origin point.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Creating and initializing regions

- [infiniteRegion](uiregion/infinite.md) — Returns the region that encloses all points.
- [- initWithSize:](<uiregion/init(size_).md>) — Initializes and returns a rectangular region of the specified size.
- [- initWithRadius:](<uiregion/init(radius_).md>) — Initializes and returns a region with a circular shape of the specified radius.

### Creating complex regions

- [- inverseRegion](<uiregion/inverse().md>) — Returns a new region that’s the mathematical inverse of the current region.
- [- regionByDifferenceFromRegion:](<uiregion/bydifference(from_).md>) — Returns a new region created by subtracting the specified region from the current region.
- [- regionByIntersectionWithRegion:](<uiregion/byintersection(with_).md>) — Returns a new region containing only the area occupied by both the specified region and current region.
- [- regionByUnionWithRegion:](<uiregion/byunion(with_).md>) — Returns a new region containing the combined areas of the specified region and the current region.

### Interacting with a region

- [- containsPoint:](<uiregion/contains(__).md>) — Returns a Boolean indicating whether the specified point is inside of the current region.

### Initializers

- [init(coder:)](<uiregion/init(coder_).md>)
