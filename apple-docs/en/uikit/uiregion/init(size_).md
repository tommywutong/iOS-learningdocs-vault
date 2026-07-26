---
title: 'init(size:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiregion/init(size:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiregion/init(size:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiregion/init%28size%3A%29.json'
content_hash: 'sha256:159d4a7d1f159a16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIRegion](../uiregion.md)

# init(size:)

<sub>Initializer</sub>

Initializes and returns a rectangular region of the specified size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(size: CGSize)
```

## Parameters

- `size` — The size of the region, specified in points.

## Return Value

A rectangular region of the specified size.

## Discussion

The center of the rectangle is the origin of the region’s coordinate system.

## See Also

### Creating and initializing regions

- [infiniteRegion](infinite.md) — Returns the region that encloses all points.
- [- initWithRadius:](<init(radius_).md>) — Initializes and returns a region with a circular shape of the specified radius.
