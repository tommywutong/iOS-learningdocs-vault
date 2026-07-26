---
title: coordinateSpace
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+（26.0 起废弃）, iPadOS 13.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, tvOS 13.0+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiwindowscene/coordinatespace
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/coordinatespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/coordinatespace.json'
content_hash: 'sha256:07f84ffbfdfe9629'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowScene](../uiwindowscene.md)

# coordinateSpace

<sub>Instance Property</sub>

The coordinate space occupied by the scene.

> [!warning] Deprecated
> Use effectiveGeometry.coordinateSpace instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var coordinateSpace: any UICoordinateSpace { get }
```

## Discussion

Use the provided coordinate space to get the bounds of the scene’s bounds rectangle and to convert points and rectangles to and from other coordinate spaces. For example, use [coordinateSpace](coordinatespace.md) to convert a point in the scene to the screen coordinate space.

## See Also

### Deprecated symbols

- [interfaceOrientation](interfaceorientation.md) — The orientation to use when displaying content in your windows. _(deprecated)_
