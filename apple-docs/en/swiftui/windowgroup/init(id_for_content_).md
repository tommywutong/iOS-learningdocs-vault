---
title: 'init(id:for:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowgroup/init(id:for:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(id:for:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28id%3Afor%3Acontent%3A%29.json'
content_hash: 'sha256:d7be8e98c538cd78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(id:for:content:)

<sub>Initializer</sub>

Creates a data-presenting window group with an identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<D, C>(id: String, for type: D.Type, @ContentBuilder content: @escaping (Binding<D?>) -> C) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View
```

## Parameters

- `id` — A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.

- `type` — The type of presented data this window group accepts.

- `content` — A closure that creates the content for each instance of the group. The closure receives a binding to the value that you pass into the [openWindow](../environmentvalues/openwindow.md) action when you open the window. SwiftUI automatically persists and restores the value of this binding as part of the state restoration process.

## Discussion

The window group uses the specified content as a template to create each window in the group.

SwiftUI creates a window from the group when you present a value of the specified type using the [openWindow](../environmentvalues/openwindow.md) action.

## See Also

### Identifying a data-driven window group

- [init(_:id:for:content:)](<init(__id_for_content_).md>) — Creates a data-presenting window group with a localized title string and an identifier.
