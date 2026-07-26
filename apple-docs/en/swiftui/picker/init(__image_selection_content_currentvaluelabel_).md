---
title: 'init(_:image:selection:content:currentValueLabel:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(_:image:selection:content:currentvaluelabel:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(_:image:selection:content:currentvaluelabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28_%3Aimage%3Aselection%3Acontent%3Acurrentvaluelabel%3A%29.json'
content_hash: 'sha256:b9329a532e822901'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(_:image:selection:content:currentValueLabel:)

<sub>Initializer</sub>

Creates a picker that accepts a custom current value label and generates its label from a localized string key and image resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, image: ImageResource, selection: Binding<SelectionValue>, @ContentBuilder content: () -> Content, @ContentBuilder currentValueLabel: () -> some View)
```

## Parameters

- `titleResource` — A localized string resource that describes the purpose of selecting an option.

- `image` — The name of the image resource to lookup.

- `selection` — A binding to a property that determines the currently-selected option.

- `content` — A view that contains the set of options.

- `currentValueLabel` — A view that represents the current value of the picker.

## Discussion

This initializer creates a [Text](../text.md) view on your behalf. See [Text](../text.md) for more information about localizing strings.
