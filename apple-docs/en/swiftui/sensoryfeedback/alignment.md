---
title: alignment
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/alignment
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/alignment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/alignment.json'
content_hash: 'sha256:9d5176d1e5e7228f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# alignment

<sub>Type Property</sub>

Indicates the alignment of a dragged item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let alignment: SensoryFeedback
```

## Discussion

For example, use this pattern in a drawing app when the user drags a shape into alignment with another shape.

Only plays feedback on iOS and macOS.

## See Also

### Indicating changes and selections

- [decrease](decrease.md) — Indicates that an important value decreased below a significant threshold.
- [increase](increase.md) — Indicates that an important value increased above a significant threshold.
- [levelChange](levelchange.md) — Indicates movement between discrete levels of pressure.
- [selection](selection.md) — Indicates that a UI element’s values are changing.
- [pathComplete](pathcomplete.md) — Indicates a drawn path has completed and/or recognized.
