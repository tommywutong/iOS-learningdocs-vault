---
title: 'init(id:anchor:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollposition/init(id:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/init(id:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/init%28id%3Aanchor%3A%29.json'
content_hash: 'sha256:01b9bd169535c0c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# init(id:anchor:)

<sub>Initializer</sub>

Creates a new scroll position to a view with a provided identity value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(id: some Hashable & Sendable, anchor: UnitPoint? = nil)
```

## Discussion

The type of the ID indicates the type of ID of views within a scroll target layout the scroll view should look for.
