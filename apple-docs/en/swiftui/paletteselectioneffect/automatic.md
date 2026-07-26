---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/paletteselectioneffect/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/paletteselectioneffect/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/paletteselectioneffect/automatic.json'
content_hash: 'sha256:09f7ed04394b9517'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PaletteSelectionEffect](../paletteselectioneffect.md)

# automatic

<sub>Type Property</sub>

Applies the system’s default effect when selected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let automatic: PaletteSelectionEffect
```

## Discussion

When using un-tinted SF Symbols or template images, the current tint color is applied to the selected items’ image. If the provided SF Symbols have custom tints, a stroke is drawn around selected items.

## See Also

### Getting palette selection effects

- [custom](custom.md) — Does not apply any system effect when selected.
- [symbolVariant(_:)](<symbolvariant(__).md>) — Applies the specified symbol variant when selected.
