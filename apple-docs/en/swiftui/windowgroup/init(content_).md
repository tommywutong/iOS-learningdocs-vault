---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/windowgroup/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28content%3A%29.json'
content_hash: 'sha256:709e800ab944d567'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(content:)

<sub>Initializer</sub>

Creates a window group.

> [!warning] Deprecated
> Use the initializer which takes an escaping content builder instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each window in the group.

## See Also

### Creating a window group

- [init(_:content:)](<init(__content_).md>) — Creates a window group with a text view title. _(deprecated)_
