---
title: 'init(_:makeContent:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/windowgroup/init(_:makecontent:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(_:makecontent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28_%3Amakecontent%3A%29.json'
content_hash: 'sha256:75fa83ac4a9e13f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(_:makeContent:)

<sub>Initializer</sub>

Creates a window group with a text view title.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ title: Text, @ContentBuilder makeContent: @escaping () -> Content)
```

## Parameters

- `title` — The [Text](../text.md) view to use for the group’s title.

- `makeContent` — A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

> [!important] Important
> The system ignores any text styling that you apply to the [Text](../text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.
