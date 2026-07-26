---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anylayout/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anylayout/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anylayout/init%28_%3A%29.json'
content_hash: 'sha256:7528ba3304a26b74'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyLayout](../anylayout.md)

# init(_:)

<sub>Initializer</sub>

Creates a type-erased value that wraps the specified layout.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<L>(_ layout: L) where L : Layout
```

## Discussion

You can switch between type-erased layouts without losing the state of the subviews.
