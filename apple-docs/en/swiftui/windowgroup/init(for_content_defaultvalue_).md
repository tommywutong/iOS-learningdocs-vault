---
title: 'init(for:content:defaultValue:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowgroup/init(for:content:defaultvalue:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(for:content:defaultvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28for%3Acontent%3Adefaultvalue%3A%29.json'
content_hash: 'sha256:23b7f25ed2e31555'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(for:content:defaultValue:)

<sub>Initializer</sub>

Creates a data-presenting window group with a default value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<D, C>(for type: D.Type = D.self, @ContentBuilder content: @escaping (Binding<D>) -> C, defaultValue: @escaping () -> D) where Content == PresentedWindowContent<D, C>, D : Decodable, D : Encodable, D : Hashable, C : View
```

## Parameters

- `type` — The type of presented data this window group accepts.

- `content` — A closure that creates the content for each instance of the group. The closure receives a binding to the value that you pass into the [openWindow](../environmentvalues/openwindow.md) action when you open the window. SwiftUI automatically persists and restores the value of this binding as part of the state restoration process.

- `defaultValue` — A closure that returns a default value to present. SwiftUI calls this closure when it has no data to provide, like when someone opens a new window from the File \> New Window menu item.

## Discussion

The window group using the given view as a template to form the content of each window in the group.

SwiftUI creates a window from the group when you present a value of the specified type using the [openWindow](../environmentvalues/openwindow.md) action.

## See Also

### Providing default data to a window group

- [init(_:for:content:defaultValue:)](<init(__for_content_defaultvalue_).md>) — Creates a data-presenting window group with a localized title string and a default value.
