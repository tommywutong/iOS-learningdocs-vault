---
title: symbolRenderingMode
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/symbolrenderingmode
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/symbolrenderingmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/symbolrenderingmode.json'
content_hash: 'sha256:3d797f10dbcb5a76'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# symbolRenderingMode

<sub>Instance Property</sub>

The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var symbolRenderingMode: SymbolRenderingMode? { get set }
```

## See Also

### Setting symbol rendering modes

- [symbolRenderingMode(_:)](<../view/symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [SymbolRenderingMode](../symbolrenderingmode.md) — A symbol rendering mode.
- [SymbolColorRenderingMode](../symbolcolorrenderingmode.md) — A method of filling a layer in a symbol image.
- [SymbolVariableValueMode](../symbolvariablevaluemode.md) — A method of rendering the variable value of a symbol image.
