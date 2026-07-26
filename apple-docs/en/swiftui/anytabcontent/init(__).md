---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anytabcontent/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anytabcontent/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anytabcontent/init%28_%3A%29.json'
content_hash: 'sha256:f26eac9792a7e243'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyTabContent](../anytabcontent.md)

# init(_:)

<sub>Initializer</sub>

Create an instance that type-erases `tabContent`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<T>(_ tabContent: T) where SelectionValue == T.TabValue, T : TabContent
```
