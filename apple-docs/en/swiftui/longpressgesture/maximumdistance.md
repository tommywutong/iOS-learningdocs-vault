---
title: maximumDistance
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/longpressgesture/maximumdistance
source_url: 'https://developer.apple.com/documentation/swiftui/longpressgesture/maximumdistance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/longpressgesture/maximumdistance.json'
content_hash: 'sha256:46cdb36dd0ff4818'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [LongPressGesture](../longpressgesture.md)

# maximumDistance

<sub>Instance Property</sub>

The maximum distance that the long press can move before the gesture fails.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated var maximumDistance: CGFloat { get set }
```

## See Also

### Creating a long press gesture

- [init(minimumDuration:)](<init(minimumduration_).md>) — Creates a long-press gesture with a minimum duration
- [init(minimumDuration:maximumDistance:)](<init(minimumduration_maximumdistance_).md>) — Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.
- [init(minimumDuration:maximumDistance:inputKinds:)](<init(minimumduration_maximumdistance_inputkinds_).md>) — Creates a long-press gesture with a minimum duration, a maximum distance, and the input kinds the gesture recognizes. _(beta)_
- [minimumDuration](minimumduration.md) — The minimum duration of the long press that must elapse before the gesture succeeds.
