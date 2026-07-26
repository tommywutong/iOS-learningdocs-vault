---
title: SymbolColorRenderingMode
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolcolorrenderingmode
source_url: 'https://developer.apple.com/documentation/swiftui/symbolcolorrenderingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolcolorrenderingmode.json'
content_hash: 'sha256:33a6e3b745b61bfb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SymbolColorRenderingMode

<sub>Structure</sub>

A method of filling a layer in a symbol image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SymbolColorRenderingMode
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [flat](symbolcolorrenderingmode/flat.md) — The symbol image layer should be filled with a solid color.
- [gradient](symbolcolorrenderingmode/gradient.md) — The symbol image layer should be filled with an axial gradient.

## See Also

### Setting symbol rendering modes

- [symbolRenderingMode(_:)](<view/symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [symbolRenderingMode](environmentvalues/symbolrenderingmode.md) — The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [SymbolRenderingMode](symbolrenderingmode.md) — A symbol rendering mode.
- [SymbolVariableValueMode](symbolvariablevaluemode.md) — A method of rendering the variable value of a symbol image.
