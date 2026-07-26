---
title: 'init(for:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowgroup/init(for:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(for:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28for%3Acontent%3A%29.json'
content_hash: 'sha256:45a829723509cb22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(for:content:)

<sub>Initializer</sub>

Creates a data-presenting window group.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<D, C>(for type: D.Type, @ContentBuilder content: @escaping (Binding<D?>) -> C) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View
```

## Parameters

- `type` — The type of presented data this window group accepts.

- `content` — A closure that creates the content for each instance of the group. The closure receives a binding to the value that you pass into the [openWindow](../environmentvalues/openwindow.md) action when you open the window. SwiftUI automatically persists and restores the value of this binding as part of the state restoration process.

## Discussion

The window group uses the given view as a template to form the content of each window in the group.

SwiftUI creates a window from the group when you present a value of the specified type using the [openWindow](../environmentvalues/openwindow.md) action.

## See Also

### Creating a data-driven window group

- [init(_:for:content:)](<init(__for_content_).md>) — Creates a data-presenting window group with a localized title string.
