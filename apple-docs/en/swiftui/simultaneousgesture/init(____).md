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
doc_path: '/documentation/swiftui/simultaneousgesture/init(_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/simultaneousgesture/init(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/simultaneousgesture/init%28_%3A_%3A%29.json'
content_hash: 'sha256:76338bc1159f0329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SimultaneousGesture](../simultaneousgesture.md)

# init(_:_:)

<sub>Initializer</sub>

Creates a gesture with two gestures that can receive updates or succeed independently of each other.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(_ first: First, _ second: Second)
```

## Parameters

- `first` — The first of two gestures that can happen simultaneously.

- `second` — The second of two gestures that can happen simultaneously.

## See Also

### Creating the gesture

- [first](first.md) — The first of two gestures that can happen simultaneously.
- [second](second.md) — The second of two gestures that can happen simultaneously.
