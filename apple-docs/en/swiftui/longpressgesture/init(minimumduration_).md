---
title: 'init(minimumDuration:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [tvOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/longpressgesture/init(minimumduration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/longpressgesture/init(minimumduration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/longpressgesture/init%28minimumduration%3A%29.json'
content_hash: 'sha256:c234ee16b2731953'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LongPressGesture](../longpressgesture.md)

# init(minimumDuration:)

<sub>Initializer</sub>

Creates a long-press gesture with a minimum duration

<sub>tvOS</sub>

```swift
nonisolated init(minimumDuration: Double = 0.5)
```

## Parameters

- `minimumDuration` — The minimum duration of the long press that must elapse before the gesture succeeds.

## See Also

### Creating a long press gesture

- [init(minimumDuration:maximumDistance:)](<init(minimumduration_maximumdistance_).md>) — Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.
- [init(minimumDuration:maximumDistance:inputKinds:)](<init(minimumduration_maximumdistance_inputkinds_).md>) — Creates a long-press gesture with a minimum duration, a maximum distance, and the input kinds the gesture recognizes. _(beta)_
- [minimumDuration](minimumduration.md) — The minimum duration of the long press that must elapse before the gesture succeeds.
- [maximumDistance](maximumdistance.md) — The maximum distance that the long press can move before the gesture fails.
