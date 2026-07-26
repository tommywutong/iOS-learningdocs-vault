---
title: 'init(_:systemImage:sources:selection:content:currentValueLabel:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:currentvaluelabel:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:currentvaluelabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28_%3Asystemimage%3Asources%3Aselection%3Acontent%3Acurrentvaluelabel%3A%29.json'
content_hash: 'sha256:83c852986e4612e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(_:systemImage:sources:selection:content:currentValueLabel:)

<sub>Initializer</sub>

Creates a picker bound to a collection of bindings that accepts a custom current value label and generates its label from a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<C, S>(_ title: S, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>
```

## Parameters

- `title` — A string that describes the purpose of selecting an option.

- `systemImage` — The name of the image resource to lookup.

- `sources` — A collection of values used as the source for displaying the Picker’s selection.

- `selection` — The key path of the values that determines the currently-selected options. When a user selects an option from the picker, the values at the key path of all items in the `sources` collection are updated with the selected option.

- `content` — A view that contains the set of options.

- `currentValueLabel` — A view that represents the current value of the picker.
