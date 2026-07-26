---
title: 'init(radius:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiregion/init(radius:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiregion/init(radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiregion/init%28radius%3A%29.json'
content_hash: 'sha256:e6b211ccfa684338'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRegion](../uiregion.md)

# init(radius:)

<sub>Initializer</sub>

Initializes and returns a region with a circular shape of the specified radius.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(radius: CGFloat)
```

## Parameters

- `radius` — The radius of the circular area, specified in points.

## Return Value

A circular region with the specified radius.

## Discussion

The center of the circle is the origin of the region’s coordinate system.

## See Also

### Creating and initializing regions

- [infiniteRegion](infinite.md) — Returns the region that encloses all points.
- [- initWithSize:](<init(size_).md>) — Initializes and returns a rectangular region of the specified size.
