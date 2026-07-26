---
title: 'init(idType:x:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollposition/init(idtype:x:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/init(idtype:x:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/init%28idtype%3Ax%3A%29.json'
content_hash: 'sha256:c12ee5c70de6a987'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# init(idType:x:)

<sub>Initializer</sub>

Creates a new scroll position to be scrolled to the provided y value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(idType: (some Hashable & Sendable).Type = Never.self, x: CGFloat)
```

## Discussion

You can provide a type to the scroll position. This type should match the type of IDs associated to views in a scroll target layout. The scroll view will look for those views to update the value of the scroll position with.
