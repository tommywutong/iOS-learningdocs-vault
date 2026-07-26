---
title: custom
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/paletteselectioneffect/custom
source_url: 'https://developer.apple.com/documentation/swiftui/paletteselectioneffect/custom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/paletteselectioneffect/custom.json'
content_hash: 'sha256:f7eede1e390d999c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PaletteSelectionEffect](../paletteselectioneffect.md)

# custom

<sub>Type Property</sub>

Does not apply any system effect when selected.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let custom: PaletteSelectionEffect
```

## Discussion

> [!note] Note
> Make sure to manually implement a way to indicate selection when using this case. For example, you could dynamically resolve the item’s image based on the selection state.

## See Also

### Getting palette selection effects

- [automatic](automatic.md) — Applies the system’s default effect when selected.
- [symbolVariant(_:)](<symbolvariant(__).md>) — Applies the specified symbol variant when selected.
