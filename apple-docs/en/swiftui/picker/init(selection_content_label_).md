---
title: 'init(selection:content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(selection:content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(selection:content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28selection%3Acontent%3Alabel%3A%29.json'
content_hash: 'sha256:67237c08ba5df9e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(selection:content:label:)

<sub>Initializer</sub>

Creates a picker that displays a custom label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `selection` — A binding to a property that determines the currently-selected option.

- `content` — A view that contains the set of options.

- `label` — A view that describes the purpose of selecting an option.

## See Also

### Creating a picker

- [init(_:selection:content:)](<init(__selection_content_).md>) — Creates a picker that generates its label from a localized string resource.
