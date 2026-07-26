---
title: coordinateSpace
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/coordinatespace
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/coordinatespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/coordinatespace.json'
content_hash: 'sha256:8612fd90fefb520a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# coordinateSpace

<sub>Instance Property</sub>

The current coordinate space of the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var coordinateSpace: any UICoordinateSpace { get }
```

## Discussion

The screen’s current coordinate space always reflects any interface orientations applied to the device. Therefore, the bounds of this coordinate space match the [bounds](bounds.md) property of the screen itself.

## See Also

### Getting the coordinate space

- [fixedCoordinateSpace](fixedcoordinatespace.md) — The fixed coordinate space of the screen.
