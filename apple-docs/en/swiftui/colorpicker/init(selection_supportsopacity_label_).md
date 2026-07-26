---
title: 'init(selection:supportsOpacity:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/colorpicker/init(selection:supportsopacity:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/colorpicker/init(selection:supportsopacity:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/colorpicker/init%28selection%3Asupportsopacity%3Alabel%3A%29.json'
content_hash: 'sha256:51c90fd27477b55d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ColorPicker](../colorpicker.md)

# init(selection:supportsOpacity:label:)

<sub>Initializer</sub>

Creates an instance that selects a color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(selection: Binding<CGColor>, supportsOpacity: Bool = true, @ContentBuilder label: () -> Label)
```

## Parameters

- `selection` — A [Binding](../binding.md) to the variable that displays the selected `CGColor`.

- `supportsOpacity` — A Boolean value that indicates whether the color picker allows adjusting the selected color’s opacity; the default is `true`.

- `label` — A view that describes the use of the selected color. The system color picker UI sets it’s title using the text from this view.

## See Also

### Creating a color picker

- [init(_:selection:supportsOpacity:)](<init(__selection_supportsopacity_).md>) — Creates a color picker with a text label generated from a title string resource.
