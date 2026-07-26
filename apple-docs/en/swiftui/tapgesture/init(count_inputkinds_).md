---
title: 'init(count:inputKinds:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/tapgesture/init(count:inputkinds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tapgesture/init(count:inputkinds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tapgesture/init%28count%3Ainputkinds%3A%29.json'
content_hash: 'sha256:51ec775a66ceada4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TapGesture](../tapgesture.md)

# init(count:inputKinds:)

<sub>Initializer</sub>

Creates a tap gesture with the number of required taps and the input kinds the gesture recognizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(count: Int = 1, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `count` — The required number of taps to complete the tap gesture.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

### Creating a tap gesture

- [init(count:)](<init(count_).md>) — Creates a tap gesture with the number of required taps.
- [count](count.md) — The required number of tap events.
