---
title: 'init(_:selection:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(_:selection:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(_:selection:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28_%3Aselection%3Acontent%3A%29.json'
content_hash: 'sha256:a76f7d8489bdb6bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(_:selection:content:)

<sub>Initializer</sub>

Creates a picker that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — A localized string resource that describes the purpose of selecting an option.

- `selection` — A binding to a property that determines the currently-selected option.

- `content` — A view that contains the set of options.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a picker

- [init(selection:content:label:)](<init(selection_content_label_).md>) — Creates a picker that displays a custom label.
