---
title: 'init(minimumDuration:maximumDistance:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/longpressgesture/init(minimumduration:maximumdistance:)'
source_url: 'https://developer.apple.com/documentation/swiftui/longpressgesture/init(minimumduration:maximumdistance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/longpressgesture/init%28minimumduration%3Amaximumdistance%3A%29.json'
content_hash: 'sha256:5172c71fb67bc9ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LongPressGesture](../longpressgesture.md)

# init(minimumDuration:maximumDistance:)

<sub>Initializer</sub>

Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10)
```

## Parameters

- `minimumDuration` — The minimum duration of the long press that must elapse before the gesture succeeds.

- `maximumDistance` — The maximum distance that the fingers or cursor performing the long press can move before the gesture fails.

## See Also

### Creating a long press gesture

- [init(minimumDuration:)](<init(minimumduration_).md>) — Creates a long-press gesture with a minimum duration
- [init(minimumDuration:maximumDistance:inputKinds:)](<init(minimumduration_maximumdistance_inputkinds_).md>) — Creates a long-press gesture with a minimum duration, a maximum distance, and the input kinds the gesture recognizes. _(beta)_
- [minimumDuration](minimumduration.md) — The minimum duration of the long press that must elapse before the gesture succeeds.
- [maximumDistance](maximumdistance.md) — The maximum distance that the long press can move before the gesture fails.
