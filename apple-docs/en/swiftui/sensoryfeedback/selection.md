---
title: selection
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/selection
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/selection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/selection.json'
content_hash: 'sha256:a2c463d05ee84335'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# selection

<sub>Type Property</sub>

Indicates that a UI element’s values are changing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let selection: SensoryFeedback
```

## Discussion

Equivalent to [selection(_:)](<selection(__).md>) with `SelectionFeedback/default`.

Only plays feedback on iOS and watchOS.

## See Also

### Indicating changes and selections

- [alignment](alignment.md) — Indicates the alignment of a dragged item.
- [decrease](decrease.md) — Indicates that an important value decreased below a significant threshold.
- [increase](increase.md) — Indicates that an important value increased above a significant threshold.
- [levelChange](levelchange.md) — Indicates movement between discrete levels of pressure.
- [pathComplete](pathcomplete.md) — Indicates a drawn path has completed and/or recognized.
