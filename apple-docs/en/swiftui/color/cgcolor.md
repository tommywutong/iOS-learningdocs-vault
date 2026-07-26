---
title: cgColor
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 7.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/color/cgcolor
source_url: 'https://developer.apple.com/documentation/swiftui/color/cgcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/color/cgcolor.json'
content_hash: 'sha256:03d5bdb551ec7830'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Color](../color.md)

# cgColor

<sub>Instance Property</sub>

A Core Graphics representation of the color, if available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var cgColor: CGColor? { get }
```

## Discussion

You can get a [CGColor](../../coregraphics/cgcolor.md) instance from a constant SwiftUI color. This includes colors you create from a Core Graphics color, from RGB or HSB components, or from constant UIKit and AppKit colors.

For a dynamic color, like one you load from an Asset Catalog using [init(_:bundle:)](<init(__bundle_).md>), or one you create from a dynamic UIKit or AppKit color, this property is `nil`. To evaluate all types of colors, use the `resolve(in:)` method.
