---
title: 'init(minimumDuration:maximumDistance:inputKinds:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/longpressgesture/init(minimumduration:maximumdistance:inputkinds:)'
source_url: 'https://developer.apple.com/documentation/swiftui/longpressgesture/init(minimumduration:maximumdistance:inputkinds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/longpressgesture/init%28minimumduration%3Amaximumdistance%3Ainputkinds%3A%29.json'
content_hash: 'sha256:dd4c6e31f984bc9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LongPressGesture](../longpressgesture.md)

# init(minimumDuration:maximumDistance:inputKinds:)

<sub>Initializer</sub>

Creates a long-press gesture with a minimum duration, a maximum distance, and the input kinds the gesture recognizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, inputKinds: GestureInputKinds = .all)
```

## Parameters

- `minimumDuration` — The minimum duration of the long press that must elapse before the gesture succeeds.

- `maximumDistance` — The maximum distance that the fingers or cursor performing the long press can move before the gesture fails.

- `inputKinds` — A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.

## See Also

### Creating a long press gesture

- [init(minimumDuration:)](<init(minimumduration_).md>) — Creates a long-press gesture with a minimum duration
- [init(minimumDuration:maximumDistance:)](<init(minimumduration_maximumdistance_).md>) — Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.
- [minimumDuration](minimumduration.md) — The minimum duration of the long press that must elapse before the gesture succeeds.
- [maximumDistance](maximumdistance.md) — The maximum distance that the long press can move before the gesture fails.
