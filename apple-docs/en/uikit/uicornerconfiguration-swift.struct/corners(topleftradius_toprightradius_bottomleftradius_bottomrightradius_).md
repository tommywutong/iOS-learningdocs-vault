---
title: 'corners(topLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicornerconfiguration-swift.struct/corners(topleftradius:toprightradius:bottomleftradius:bottomrightradius:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicornerconfiguration-swift.struct/corners(topleftradius:toprightradius:bottomleftradius:bottomrightradius:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicornerconfiguration-swift.struct/corners%28topleftradius%3Atoprightradius%3Abottomleftradius%3Abottomrightradius%3A%29.json'
content_hash: 'sha256:3eb55165db933d67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICornerConfiguration](../uicornerconfiguration-swift.struct.md)

# corners(topLeftRadius:topRightRadius:bottomLeftRadius:bottomRightRadius:)

<sub>Type Method</sub>

A configuration with independent radii for each corner.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static func corners(topLeftRadius: UICornerRadius?, topRightRadius: UICornerRadius?, bottomLeftRadius: UICornerRadius?, bottomRightRadius: UICornerRadius?) -> UICornerConfiguration
```

## Parameters

- `topLeftRadius` — A [UICornerRadius](../uicornerradius-swift.struct.md) that represents the radius to use for the top-left corner.

- `topRightRadius` — A [UICornerRadius](../uicornerradius-swift.struct.md) that represents the radius to use for the top-right corner.

- `bottomLeftRadius` — A [UICornerRadius](../uicornerradius-swift.struct.md) that represents the radius to use for the bottom-left corner.

- `bottomRightRadius` — A [UICornerRadius](../uicornerradius-swift.struct.md) that represents the radius to use for the bottom-right corner.

## See Also

### Configuring independent corners

- [corners(radius:)](<corners(radius_).md>) — A configuration that applies the given radius independently to all corners.
