---
title: levelChange
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/levelchange
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/levelchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/levelchange.json'
content_hash: 'sha256:fdf80904041804b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# levelChange

<sub>Type Property</sub>

Indicates movement between discrete levels of pressure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let levelChange: SensoryFeedback
```

## Discussion

For example, as the user presses a fast-forward button on a video player, playback could increase or decrease and haptic feedback could be provided as different levels of pressure are reached.

Only plays feedback on macOS.

## See Also

### Indicating changes and selections

- [alignment](alignment.md) — Indicates the alignment of a dragged item.
- [decrease](decrease.md) — Indicates that an important value decreased below a significant threshold.
- [increase](increase.md) — Indicates that an important value increased above a significant threshold.
- [selection](selection.md) — Indicates that a UI element’s values are changing.
- [pathComplete](pathcomplete.md) — Indicates a drawn path has completed and/or recognized.
