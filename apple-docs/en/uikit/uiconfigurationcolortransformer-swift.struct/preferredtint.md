---
title: preferredTint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationcolortransformer-swift.struct/preferredtint
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/preferredtint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationcolortransformer-swift.struct/preferredtint.json'
content_hash: 'sha256:02f6d9772ad3ae08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationColorTransformer](../uiconfigurationcolortransformer-swift.struct.md)

# preferredTint

<sub>Type Property</sub>

A color transformer that returns the preferred system accent color.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let preferredTint: UIConfigurationColorTransformer
```

## Discussion

This color transformer returns the original color on platforms without a system accent color, or when the system accent color is set to Multicolor. When the system accent color is set to any other color, this color transformer returns that system accent color.

## See Also

### Creating a color transformer

- [init(_:)](<init(__).md>) — Creates a color transformer with the specified closure.
- [grayscale](grayscale.md) — Creates a color transformer that generates a grayscale version of the color.
- [monochromeTint](monochrometint.md) — A color transformer that returns the color with a monochrome tint.
