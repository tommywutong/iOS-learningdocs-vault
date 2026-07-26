---
title: 'init(idType:edge:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollposition/init(idtype:edge:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/init(idtype:edge:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/init%28idtype%3Aedge%3A%29.json'
content_hash: 'sha256:a832067d493a202c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# init(idType:edge:)

<sub>Initializer</sub>

Creates a new scroll position to be scrolled to the provided edge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(idType: (some Hashable & Sendable).Type = Never.self, edge: Edge)
```

## Discussion

You can provide a type to indicate the type of ID the scroll view should look for views with an ID of that type within its scroll target layout.
