---
title: 'symbolColorRenderingMode(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/symbolcolorrenderingmode(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/symbolcolorrenderingmode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/symbolcolorrenderingmode%28_%3A%29.json'
content_hash: 'sha256:e5f0bbc71471788e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# symbolColorRenderingMode(_:)

<sub>Instance Method</sub>

Sets the color rendering mode for symbol images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func symbolColorRenderingMode(_ mode: SymbolColorRenderingMode?) -> some View

```

## Parameters

- `mode` — The color rendering mode, or nil to use the default mode.

## Return Value

A view that specifies the color rendering mode for symbol images.

## See Also

### Symbol appearance

- [symbolRenderingMode(_:)](<symbolrenderingmode(__).md>) — Sets the rendering mode for symbol images within this view.
- [symbolVariableValueMode(_:)](<symbolvariablevaluemode(__).md>) — Sets the variable value mode mode for symbol images within this view.
- [symbolVariant(_:)](<symbolvariant(__).md>) — Makes symbols within the view show a particular variant.
