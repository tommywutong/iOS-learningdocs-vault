---
title: 'init(_:systemImage:selection:content:currentValueLabel:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(_:systemimage:selection:content:currentvaluelabel:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:selection:content:currentvaluelabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28_%3Asystemimage%3Aselection%3Acontent%3Acurrentvaluelabel%3A%29.json'
content_hash: 'sha256:8d5d38079d7007a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(_:systemImage:selection:content:currentValueLabel:)

<sub>Initializer</sub>

Creates a picker that accepts a custom current value label and generates its label from a localized string key and system image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

## Parameters

- `titleKey` — A localized string key that describes the purpose of selecting an option.

- `systemImage` — The name of the image resource to lookup.

- `selection` — A binding to a property that determines the currently-selected option.

- `content` — A view that contains the set of options.

- `currentValueLabel` — A view that represents the current value of the picker.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See [Text](../text.md) for more information about localizing strings.
