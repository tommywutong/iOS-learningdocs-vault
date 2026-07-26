---
title: fixedCoordinateSpace
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscreen/fixedcoordinatespace
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/fixedcoordinatespace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/fixedcoordinatespace.json'
content_hash: 'sha256:ca9b33af6ed579cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# fixedCoordinateSpace

<sub>Instance Property</sub>

The fixed coordinate space of the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var fixedCoordinateSpace: any UICoordinateSpace { get }
```

## Discussion

The bounds of this coordinate space always reflect the screen dimensions of the device in a portrait-up orientation. You can use this coordinate space in places where you need a fixed frame of reference. For example, if your app saves screen coordinate values to disk, convert those values to the fixed coordinate space before doing so. Saving them in the fixed coordinate space ensures that when your app reads the values later, it can convert them to the current coordinate space correctly.

## See Also

### Getting the coordinate space

- [coordinateSpace](coordinatespace.md) — The current coordinate space of the screen.
