---
title: 'init(_:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/windowgroup/init(_:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(_:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28_%3Acontent%3A%29.json'
content_hash: 'sha256:c77f5a77c6686a73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(_:content:)

<sub>Initializer</sub>

Creates a window group with a text view title.

> [!warning] Deprecated
> Use the initializer which takes an escaping content builder instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ title: Text, @ContentBuilder content: () -> Content)
```

## Parameters

- `title` — The [Text](../text.md) view to use for the group’s title.

- `content` — A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each window in the group. The system uses the title to distinguish the window group in the user interface, such as in the name of commands associated with the group.

> [!important] Important
> The system ignores any text styling that you apply to the [Text](../text.md) view title, like bold or italics. However, you can use the formatting controls that the view offers, like for localization, dates, and numerical representations.

## See Also

### Creating a window group

- [init(content:)](<init(content_).md>) — Creates a window group. _(deprecated)_
