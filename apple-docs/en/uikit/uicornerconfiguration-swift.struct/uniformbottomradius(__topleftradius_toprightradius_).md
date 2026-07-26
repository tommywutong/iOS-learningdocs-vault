---
title: 'uniformBottomRadius(_:topLeftRadius:topRightRadius:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicornerconfiguration-swift.struct/uniformbottomradius(_:topleftradius:toprightradius:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct/uniformbottomradius(_:topleftradius:toprightradius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerconfiguration-swift.struct/uniformbottomradius%28_%3Atopleftradius%3Atoprightradius%3A%29.json'
content_hash: 'sha256:c759ecc3caf18304'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICornerConfiguration](../uicornerconfiguration-swift.struct.md)

# uniformBottomRadius(_:topLeftRadius:topRightRadius:)

<sub>Type Method</sub>

A configuration that applies the radius you provide to the bottom corners, with optional independent radii for the top corners.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func uniformBottomRadius(_ bottomRadius: UICornerRadius, topLeftRadius: UICornerRadius? = nil, topRightRadius: UICornerRadius? = nil) -> UICornerConfiguration
```

## Parameters

- `bottomRadius` — A [UICornerRadius](../uicornerradius-swift.struct.md) that represents the radius to use for the bottom-left and bottom-right corners.

- `topLeftRadius` — An optional [UICornerRadius](../uicornerradius-swift.struct.md) that represents the radius to use for the top-left corner.

- `topRightRadius` — An optional [UICornerRadius](../uicornerradius-swift.struct.md) that represents the radius to use for the top-right corner.

## See Also

### Configuring uniform corners

- [uniformCorners(radius:)](<uniformcorners(radius_).md>) — A configuration that applies the given radius uniformly to all corners.
- [uniformEdges(leftRadius:rightRadius:)](<uniformedges(leftradius_rightradius_).md>) — A configuration that applies the left radius you provide to the left corners, and the right radius you provide to the right corners.
- [uniformEdges(topRadius:bottomRadius:)](<uniformedges(topradius_bottomradius_).md>) — A configuration that applies the top radius to the top corners, and the bottom radius you provide to the bottom corners.
- [uniformLeftRadius(_:topRightRadius:bottomRightRadius:)](<uniformleftradius(__toprightradius_bottomrightradius_).md>) — A configuration that applies the left radius to the left corners, with optional independent radii for the right corners.
- [uniformRightRadius(_:topLeftRadius:bottomLeftRadius:)](<uniformrightradius(__topleftradius_bottomleftradius_).md>) — A configuration that applies the right radius you provide to the right corners, with optional independent radii for the left corners.
- [uniformTopRadius(_:bottomLeftRadius:bottomRightRadius:)](<uniformtopradius(__bottomleftradius_bottomrightradius_).md>) — A configuration that applies the top radius you provide to the top corners, with optional independent radii for the bottom corners.
