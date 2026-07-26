---
title: 'init(_:id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 13.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/window/init(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/window/init(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/window/init%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:9b4d4256496821ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Window](../window.md)

# init(_:id:content:)

<sub>Initializer</sub>

Creates a window with a localized title and an identifier.

<sub>macOS, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, id: String, @ContentBuilder content: () -> Content)
```

## Parameters

- `titleResource` — A localized string resource to use for the window’s title in system menus and in the window’s title bar. Provide a title that describes the purpose of the window.

- `id` — A unique string identifier that you can use to open the window.

- `content` — The view content to display in the window.

## Discussion

The window displays the view that you specify.
