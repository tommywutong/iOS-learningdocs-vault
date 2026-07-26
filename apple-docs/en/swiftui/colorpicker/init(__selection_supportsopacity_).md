---
title: 'init(_:selection:supportsOpacity:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/colorpicker/init(_:selection:supportsopacity:)'
source_url: 'https://developer.apple.com/documentation/swiftui/colorpicker/init(_:selection:supportsopacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/colorpicker/init%28_%3Aselection%3Asupportsopacity%3A%29.json'
content_hash: 'sha256:cd46288c01c799e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ColorPicker](../colorpicker.md)

# init(_:selection:supportsOpacity:)

<sub>Initializer</sub>

Creates a color picker with a text label generated from a title string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<CGColor>, supportsOpacity: Bool = true)
```

## Parameters

- `titleResource` — The localized title of the picker.

- `selection` — A [Binding](../binding.md) to the variable that displays the selected `CGColor`.

- `supportsOpacity` — A Boolean value that indicates whether the color picker allows adjustments to the selected color’s opacity; the default is `true`.

## See Also

### Creating a color picker

- [init(selection:supportsOpacity:label:)](<init(selection_supportsopacity_label_).md>) — Creates an instance that selects a color.
