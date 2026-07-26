---
title: 'map(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/gesture/map(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/gesture/map(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesture/map%28_%3A%29.json'
content_hash: 'sha256:776694ac8f42b6e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Gesture](../gesture.md)

# map(_:)

<sub>Instance Method</sub>

Returns a gesture that uses the given closure to map over this gesture’s value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func map<T>(_ body: @escaping (Self.Value) -> T) -> _MapGesture<Self, T>
```
