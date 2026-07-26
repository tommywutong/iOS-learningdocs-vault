---
title: 'init(selection:label:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/picker/init(selection:label:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(selection:label:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28selection%3Alabel%3Acontent%3A%29.json'
content_hash: 'sha256:135320c568711f5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(selection:label:content:)

<sub>Initializer</sub>

Creates a picker that displays a custom label.

> [!warning] Deprecated
> Use [init(selection:content:label:)](<init(selection_content_label_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(selection: Binding<SelectionValue>, label: Label, @ContentBuilder content: () -> Content)
```

## Parameters

- `selection` — A binding to a property that determines the currently-selected option.

- `label` — A view that describes the purpose of selecting an option.

- `content` — A view that contains the set of options.
