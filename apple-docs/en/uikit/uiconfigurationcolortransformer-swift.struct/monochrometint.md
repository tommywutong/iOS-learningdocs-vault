---
title: monochromeTint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationcolortransformer-swift.struct/monochrometint
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/monochrometint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationcolortransformer-swift.struct/monochrometint.json'
content_hash: 'sha256:af229f66040b776b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationColorTransformer](../uiconfigurationcolortransformer-swift.struct.md)

# monochromeTint

<sub>Type Property</sub>

A color transformer that returns the color with a monochrome tint.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let monochromeTint: UIConfigurationColorTransformer
```

## Discussion

Use this color transformer to deemphasize a tinted item. The tinted item remains monochrome regardless of the system accent color.

## See Also

### Creating a color transformer

- [init(_:)](<init(__).md>) — Creates a color transformer with the specified closure.
- [grayscale](grayscale.md) — Creates a color transformer that generates a grayscale version of the color.
- [preferredTint](preferredtint.md) — A color transformer that returns the preferred system accent color.
