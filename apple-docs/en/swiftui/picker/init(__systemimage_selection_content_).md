---
title: 'init(_:systemImage:selection:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(_:systemimage:selection:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:selection:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28_%3Asystemimage%3Aselection%3Acontent%3A%29.json'
content_hash: 'sha256:4ccaeb80c77733d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(_:systemImage:selection:content:)

<sub>Initializer</sub>

Creates a picker that generates its label from a localized string key and system image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleKey: LocalizedStringKey, systemImage: String, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleKey` — A localized string key that describes the purpose of selecting an option.

- `systemImage` — The name of the image resource to lookup.

- `selection` — A binding to a property that determines the currently-selected option.

- `content` — A view that contains the set of options.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf, and treats the localized key similar to [init(_:tableName:bundle:comment:)](<../text/init(__tablename_bundle_comment_).md>). See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a picker with an image label

- [init(_:image:selection:content:)](<init(__image_selection_content_).md>) — Creates a picker that generates its label from a localized string resource and image resource
- [init(_:image:sources:selection:content:)](<init(__image_sources_selection_content_).md>) — Creates a picker that generates its label from a localized string resource and image resource.
- [init(_:systemImage:sources:selection:content:)](<init(__systemimage_sources_selection_content_).md>) — Creates a picker bound to a collection of bindings that generates its label from a string.
