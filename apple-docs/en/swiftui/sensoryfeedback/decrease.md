---
title: decrease
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 26.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/decrease
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/decrease'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/decrease.json'
content_hash: 'sha256:36345ef316ce32db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# decrease

<sub>Type Property</sub>

Indicates that an important value decreased below a significant threshold.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let decrease: SensoryFeedback
```

## Discussion

Only plays feedback on watchOS and visionOS.

## See Also

### Indicating changes and selections

- [alignment](alignment.md) — Indicates the alignment of a dragged item.
- [increase](increase.md) — Indicates that an important value increased above a significant threshold.
- [levelChange](levelchange.md) — Indicates movement between discrete levels of pressure.
- [selection](selection.md) — Indicates that a UI element’s values are changing.
- [pathComplete](pathcomplete.md) — Indicates a drawn path has completed and/or recognized.
