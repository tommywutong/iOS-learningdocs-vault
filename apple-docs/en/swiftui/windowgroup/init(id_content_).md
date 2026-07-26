---
title: 'init(id:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+（18.0 起废弃）, iPadOS 14.0+（18.0 起废弃）, Mac Catalyst 14.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 14.0+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/windowgroup/init(id:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/windowgroup/init(id:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/windowgroup/init%28id%3Acontent%3A%29.json'
content_hash: 'sha256:ba245484b3316c1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WindowGroup](../windowgroup.md)

# init(id:content:)

<sub>Initializer</sub>

Creates a window group with an identifier.

> [!warning] Deprecated
> Use the initializer which takes an escaping content builder instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(id: String, @ContentBuilder content: () -> Content)
```

## Parameters

- `id` — A string that uniquely identifies the window group. Identifiers must be unique among the window groups in your app.

- `content` — A closure that creates the content for each instance of the group.

## Discussion

The window group uses the given view as a template to form the content of each window in the group.

## See Also

### Identifying a window group

- [init(_:id:content:)](<init(__id_content_).md>) — Creates a window group with a text view title and an identifier. _(deprecated)_
