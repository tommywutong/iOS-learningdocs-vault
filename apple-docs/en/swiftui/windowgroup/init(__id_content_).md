---
title: 'init(_:id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/windowgroup/init(_:id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(_:id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28_%3Aid%3Acontent%3A%29.json'
content_hash: 'sha256:6343116c966031d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(_:id:content:)

<sub>Initializer</sub>

Creates a window group with a text view title and an identifier.

> [!warning] Deprecated
> Use the initializer which takes an escaping content builder instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ title: Text, id: String, @ContentBuilder content: () -> Content)
```

## Parameters

- `title` — The [Text](../text.md) view to use for the group’s title.

- `id` — A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.

- `content` — A closure that creates the content for each instance of the group.

## Discussion

The window group uses the specified content as a template to create each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

> [!important] Important
> The system ignores any text styling that you apply to the [Text](../text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

## See Also

### Identifying a window group

- [init(id:content:)](<init(id_content_).md>) — Creates a window group with an identifier. _(deprecated)_
