---
title: 'symbolRenderingMode(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/symbolrenderingmode(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/symbolrenderingmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/symbolrenderingmode%28_%3A%29.json'
content_hash: 'sha256:c9c0ce69881990a7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# symbolRenderingMode(_:)

<sub>Instance Method</sub>

Sets the rendering mode for symbol images within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func symbolRenderingMode(_ mode: SymbolRenderingMode?) -> some View

```

## Parameters

- `mode` — The symbol rendering mode to use.

## Return Value

A view that uses the rendering mode you supply.

## See Also

### Setting symbol rendering modes

- [symbolRenderingMode](../environmentvalues/symbolrenderingmode.md) — The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.
- [SymbolRenderingMode](../symbolrenderingmode.md) — A symbol rendering mode.
- [SymbolColorRenderingMode](../symbolcolorrenderingmode.md) — A method of filling a layer in a symbol image.
- [SymbolVariableValueMode](../symbolvariablevaluemode.md) — A method of rendering the variable value of a symbol image.
