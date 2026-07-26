---
title: 'init(_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiconfigurationcolortransformer-swift.struct/init(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationcolortransformer-swift.struct/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationcolortransformer-swift.struct/init%28_%3A%29.json'
content_hash: 'sha256:4a871eca40bac155'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConfigurationColorTransformer](../uiconfigurationcolortransformer-swift.struct.md)

# init(_:)

<sub>Initializer</sub>

Creates a color transformer with the specified closure.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(_ transform: @escaping (UIColor) -> UIColor)
```

## See Also

### Creating a color transformer

- [grayscale](grayscale.md) — Creates a color transformer that generates a grayscale version of the color.
- [preferredTint](preferredtint.md) — A color transformer that returns the preferred system accent color.
- [monochromeTint](monochrometint.md) — A color transformer that returns the color with a monochrome tint.
