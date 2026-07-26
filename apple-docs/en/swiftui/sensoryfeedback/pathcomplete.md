---
title: pathComplete
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, macOS 14.5+, tvOS 17.5+, visionOS 26.0+, watchOS 10.5+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/pathcomplete
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/pathcomplete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/pathcomplete.json'
content_hash: 'sha256:db83de0c0da48831'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [SensoryFeedback](../sensoryfeedback.md)

# pathComplete

<sub>Type Property</sub>

Indicates a drawn path has completed and/or recognized.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let pathComplete: SensoryFeedback
```

## Discussion

Use this to provide feedback for closed shape drawing or similar actions. It should supplement the user experience, since only some platforms will play feedback in response to it.

Only plays feedback on iOS.

## See Also

### Indicating changes and selections

- [alignment](alignment.md) — Indicates the alignment of a dragged item.
- [decrease](decrease.md) — Indicates that an important value decreased below a significant threshold.
- [increase](increase.md) — Indicates that an important value increased above a significant threshold.
- [levelChange](levelchange.md) — Indicates movement between discrete levels of pressure.
- [selection](selection.md) — Indicates that a UI element’s values are changing.
