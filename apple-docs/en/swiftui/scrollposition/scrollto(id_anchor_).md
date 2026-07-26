---
title: 'scrollTo(id:anchor:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/scrollposition/scrollto(id:anchor:)'
source_url: 'https://developer.apple.com/documentation/swiftui/scrollposition/scrollto(id:anchor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollposition/scrollto%28id%3Aanchor%3A%29.json'
content_hash: 'sha256:22170c528434c2ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPosition](../scrollposition.md)

# scrollTo(id:anchor:)

<sub>Instance Method</sub>

Scrolls the position of the scroll view to a view with a identity value and anchor you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func scrollTo(id: some Hashable & Sendable, anchor: UnitPoint? = nil)
```

## Discussion

Inform the scroll view of which layout it should look for view’s with the identity value you provide using the `View/scrollTargetLayout()` modifier.
