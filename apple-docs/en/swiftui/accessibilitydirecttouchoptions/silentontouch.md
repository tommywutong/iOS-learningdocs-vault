---
title: silentOnTouch
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/accessibilitydirecttouchoptions/silentontouch
source_url: 'https://developer.apple.com/documentation/swiftui/accessibilitydirecttouchoptions/silentontouch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/accessibilitydirecttouchoptions/silentontouch.json'
content_hash: 'sha256:b9c54f3b3362a921'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AccessibilityDirectTouchOptions](../accessibilitydirecttouchoptions.md)

# silentOnTouch

<sub>Type Property</sub>

Allows a direct touch area to immediately receive touch events without an assitive technology, such as VoiceOver, speaking. Appropriate for apps that provide direct audio feedback on touch that would conflict with speech feedback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let silentOnTouch: AccessibilityDirectTouchOptions
```

## See Also

### Getting the options

- [requiresActivation](requiresactivation.md) — Prevents touch passthrough with the direct touch area until an assistive technology, such as VoiceOver, has activated the direct touch area through a user action, for example a double tap.
