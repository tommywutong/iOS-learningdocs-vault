---
title: SymbolVariableValueMode
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/symbolvariablevaluemode
source_url: 'https://developer.apple.com/documentation/swiftui/symbolvariablevaluemode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/symbolvariablevaluemode.json'
content_hash: 'sha256:3471ea236459f571'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# SymbolVariableValueMode

<sub>Structure</sub>

A method of rendering the variable value of a symbol image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SymbolVariableValueMode
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [color](symbolvariablevaluemode/color.md) — The “color” variable value mode. Sets the opacity of each variable layer to either on or off depending on how its threshold compared to the current value.
- [draw](symbolvariablevaluemode/draw.md) — The “draw” variable value mode. Changes the drawn length of each variable layer to either based on how its range relates to the current value.

## See Also

### Setting symbol rendering modes

- [symbolRenderingMode(_:)](<view/symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [symbolRenderingMode](environmentvalues/symbolrenderingmode.md) — The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [SymbolRenderingMode](symbolrenderingmode.md) — A symbol rendering mode.
- [SymbolColorRenderingMode](symbolcolorrenderingmode.md) — A method of filling a layer in a symbol image.
