---
title: disablesSubpixelQuantization
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/text/layout/drawingoptions/disablessubpixelquantization
source_url: 'https://developer.apple.com/documentation/swiftui/text/layout/drawingoptions/disablessubpixelquantization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/layout/drawingoptions/disablessubpixelquantization.json'
content_hash: 'sha256:a790dce61b6c20a9'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [SwiftUI](../../../../swiftui.md) · [Text](../../../text.md) · [Layout](../../layout.md) · [DrawingOptions](../drawingoptions.md)

# disablesSubpixelQuantization

<sub>Type Property</sub>

If set, subpixel quantization requested by the text engine is disabled. This can be useful for text that will be animated to prevent it jittering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) static var disablesSubpixelQuantization: Text.Layout.DrawingOptions { get }
```
