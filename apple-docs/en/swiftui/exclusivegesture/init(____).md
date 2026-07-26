---
title: 'init(_:_:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/exclusivegesture/init(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/exclusivegesture/init(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/exclusivegesture/init%28_%3A_%3A%29.json'
content_hash: 'sha256:c2493f8c011aa596'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ExclusiveGesture](../exclusivegesture.md)

# init(_:_:)

<sub>Initializer</sub>

Creates a gesture from two gestures where only one of them succeeds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ first: First, _ second: Second)
```

## Parameters

- `first` — The first of two gestures. This gesture has precedence over the other gesture.

- `second` — The second of two gestures.

## See Also

### Creating the gesture

- [first](first.md) — The first of two gestures.
- [second](second.md) — The second of two gestures.
