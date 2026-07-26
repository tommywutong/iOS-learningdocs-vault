---
title: 'init(_:showsIndicators:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+（27.0 起废弃）, iPadOS 13.0+（27.0 起废弃）, Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.15+（27.0 起废弃）, tvOS 13.0+（27.0 起废弃）, visionOS 1.0+, watchOS 6.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/scrollview/init(_:showsindicators:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollview/init(_:showsindicators:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollview/init%28_%3Ashowsindicators%3Acontent%3A%29.json'
content_hash: 'sha256:26a578b9bdd310e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollView](../scrollview.md)

# init(_:showsIndicators:content:)

<sub>Initializer</sub>

Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.

> [!warning] Deprecated
> Use the ScrollView(_:content:) initializer and the scrollIndicators(:_) modifier

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ axes: Axis.Set = .vertical, showsIndicators: Bool = true, @ContentBuilder content: () -> Content)
```

## Parameters

- `axes` — The scroll view’s scrollable axis. The default axis is the vertical axis.

- `showsIndicators` — A Boolean value that indicates whether the scroll view displays the scrollable component of the content offset, in a way suitable for the platform. The default value for this parameter is `true`.

- `content` — The content builder that creates the scrollable view.

## See Also

### Creating a scroll view

- [init(_:content:)](<init(__content_).md>) — Creates a new instance that’s scrollable in the direction of the given axis and can show indicators while scrolling.
