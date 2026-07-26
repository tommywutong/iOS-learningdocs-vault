---
title: bounds
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicoordinatespace/bounds
source_url: 'https://developer.apple.com/documentation/uikit/uicoordinatespace/bounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicoordinatespace/bounds.json'
content_hash: 'sha256:cc0168ec5b747bc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICoordinateSpace](../uicoordinatespace.md)

# bounds

<sub>Instance Property</sub>

The bounds rectangle describing the item’s location and size in its own coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var bounds: CGRect { get }
```

## Discussion

The rectangle in this property always matches the app’s interface orientation. For apps that support all interface orientations, the value in this property can change when the user rotates the device between portrait and landscape modes.
