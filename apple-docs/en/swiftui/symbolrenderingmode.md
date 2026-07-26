---
title: SymbolRenderingMode
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolrenderingmode
source_url: 'https://developer.apple.com/documentation/swiftui/symbolrenderingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolrenderingmode.json'
content_hash: 'sha256:e94724efc4076a84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SymbolRenderingMode

<sub>Structure</sub>

A symbol rendering mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SymbolRenderingMode
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting symbol rendering modes

- [hierarchical](symbolrenderingmode/hierarchical.md) — A mode that renders symbols as multiple layers, with different opacities applied to the foreground style.
- [monochrome](symbolrenderingmode/monochrome.md) — A mode that renders symbols as a single layer filled with the foreground style.
- [multicolor](symbolrenderingmode/multicolor.md) — A mode that renders symbols as multiple layers with their inherit styles.
- [palette](symbolrenderingmode/palette.md) — A mode that renders symbols as multiple layers, with different styles applied to the layers.

## See Also

### Setting symbol rendering modes

- [symbolRenderingMode(_:)](<view/symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [symbolRenderingMode](environmentvalues/symbolrenderingmode.md) — The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [SymbolColorRenderingMode](symbolcolorrenderingmode.md) — A method of filling a layer in a symbol image.
- [SymbolVariableValueMode](symbolvariablevaluemode.md) — A method of rendering the variable value of a symbol image.
