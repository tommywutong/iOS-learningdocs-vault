---
title: toggle
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/sensoryfeedback/pressfeedback/toggle
source_url: 'https://developer.apple.com/documentation/swiftui/sensoryfeedback/pressfeedback/toggle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/sensoryfeedback/pressfeedback/toggle.json'
content_hash: 'sha256:7a35c8f3645fd81a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SensoryFeedback](../../sensoryfeedback.md) · [PressFeedback](../pressfeedback.md)

# toggle

<sub>Type Property</sub>

Indicates that a toggle has been pressed (touch down).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let toggle: SensoryFeedback.PressFeedback
```

## Discussion

Toggle controls should also play [selection(_:)](<../selection(__).md>) with [on](../selectionfeedback/on.md) and [off](../selectionfeedback/off.md).

Only plays feedback on visionOS.
