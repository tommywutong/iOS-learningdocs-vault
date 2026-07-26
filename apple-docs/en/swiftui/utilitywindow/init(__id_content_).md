---
title: 'init(_:id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/utilitywindow/init(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/utilitywindow/init(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/utilitywindow/init%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:ba7cf8e130d1b984'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [UtilityWindow](../utilitywindow.md)

# init(_:id:content:)

<sub>Initializer</sub>

Creates a utility window with a localized title and identifier.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, id: String, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — A localized string resource to use in the utility window’s title bar. Provide a title that describes the purpose of the utility window.

- `id` — An unique string identifier that you can use to open the utility window.

- `content` — The view content to display in the utility window.
