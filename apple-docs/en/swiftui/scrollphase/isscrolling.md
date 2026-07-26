---
title: isScrolling
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollphase/isscrolling
source_url: 'https://developer.apple.com/documentation/swiftui/scrollphase/isscrolling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollphase/isscrolling.json'
content_hash: 'sha256:b1bfb68386566109'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ScrollPhase](../scrollphase.md)

# isScrolling

<sub>Instance Property</sub>

Whether the scroll view is actively scrolling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isScrolling: Bool { get }
```

## Discussion

This convenience is equivalent to `phase != .idle`.
