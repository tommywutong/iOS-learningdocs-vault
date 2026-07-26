---
title: 'init(id:makeContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowgroup/init(id:makecontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(id:makecontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28id%3Amakecontent%3A%29.json'
content_hash: 'sha256:a660bfa05331eddb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(id:makeContent:)

<sub>Initializer</sub>

Creates a window group with an identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(id: String, @ContentBuilder makeContent: @escaping () -> Content)
```

## Parameters

- `id` — A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.

- `makeContent` — A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each window in the group.
