---
title: dithersColor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/shader/ditherscolor
source_url: 'https://developer.apple.com/documentation/swiftui/shader/ditherscolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/shader/ditherscolor.json'
content_hash: 'sha256:6e4b10298ff60e2c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Shader](../shader.md)

# dithersColor

<sub>Instance Property</sub>

For shader functions that return color values, whether the returned color has dither noise added to it, or is simply rounded to the output bit-depth. For shaders generating smooth gradients, dithering is usually necessary to prevent visible banding in the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var dithersColor: Bool { get set }
```
