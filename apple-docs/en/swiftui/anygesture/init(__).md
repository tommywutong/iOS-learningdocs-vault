---
title: 'init(_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/anygesture/init(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/anygesture/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/anygesture/init%28_%3A%29.json'
content_hash: 'sha256:c4af72e3306a092a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AnyGesture](../anygesture.md)

# init(_:)

<sub>Initializer</sub>

Creates an instance from another gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<T>(_ gesture: T) where Value == T.Value, T : Gesture
```

## Parameters

- `gesture` — A gesture that you use to create a new gesture.
