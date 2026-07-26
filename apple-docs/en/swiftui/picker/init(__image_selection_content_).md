---
title: 'init(_:image:selection:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(_:image:selection:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(_:image:selection:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28_%3Aimage%3Aselection%3Acontent%3A%29.json'
content_hash: 'sha256:da73a7d972b4e0f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(_:image:selection:content:)

<sub>Initializer</sub>

Creates a picker that generates its label from a localized string resource and image resource

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — A localized string resource that describes the purpose of selecting an option.

- `image` — The name of the image resource to lookup.

- `selection` — A binding to a property that determines the currently-selected option.

- `content` — A view that contains the set of options.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a picker with an image label

- [init(_:image:sources:selection:content:)](<init(__image_sources_selection_content_).md>) — Creates a picker that generates its label from a localized string resource and image resource.
- [init(_:systemImage:selection:content:)](<init(__systemimage_selection_content_).md>) — Creates a picker that generates its label from a localized string key and system image.
- [init(_:systemImage:sources:selection:content:)](<init(__systemimage_sources_selection_content_).md>) — Creates a picker bound to a collection of bindings that generates its label from a string.
