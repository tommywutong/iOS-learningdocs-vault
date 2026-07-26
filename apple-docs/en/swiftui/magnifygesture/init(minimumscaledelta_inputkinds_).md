---
title: 'init(minimumScaleDelta:inputKinds:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/magnifygesture/init(minimumscaledelta:inputkinds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/magnifygesture/init(minimumscaledelta:inputkinds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/magnifygesture/init%28minimumscaledelta%3Ainputkinds%3A%29.json'
content_hash: 'sha256:700361ef391dcc89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MagnifyGesture](../magnifygesture.md)

# init(minimumScaleDelta:inputKinds:)

<sub>Initializer</sub>

Creates a magnify gesture with a given minimum delta for the gesture to start, and the input kinds the gesture recognizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(minimumScaleDelta: CGFloat = 0.01, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `minimumScaleDelta` — The minimum scale delta required before the gesture starts.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

### Creating the gesture

- [init(minimumScaleDelta:)](<init(minimumscaledelta_).md>) — Creates a magnify gesture with a given minimum delta for the gesture to start.
- [minimumScaleDelta](minimumscaledelta.md) — The minimum required delta before the gesture starts.
