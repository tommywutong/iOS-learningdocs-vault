---
title: 'corners(radius:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicornerconfiguration-swift.struct/corners(radius:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct/corners(radius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerconfiguration-swift.struct/corners%28radius%3A%29.json'
content_hash: 'sha256:b429cc4df1f999e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICornerConfiguration](../uicornerconfiguration-swift.struct.md)

# corners(radius:)

<sub>Type Method</sub>

A configuration that applies the given radius independently to all corners.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func corners(radius: UICornerRadius) -> UICornerConfiguration
```

## Parameters

- `radius` — A [UICornerRadius](../uicornerradius-swift.struct.md) that represents a radius to apply to each corner.

## Discussion

Use a container concentric radius to allow each individual corner to resolve to different radii.

## See Also

### Configuring independent corners

- [corners(topLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:)](<corners(topleftradius_toprightradius_bottomleftradius_bottomrightradius_).md>) — A configuration with independent radii for each corner.
