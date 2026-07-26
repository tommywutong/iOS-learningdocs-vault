---
title: accessibilityDimFlashingLights
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/accessibilitydimflashinglights
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilitydimflashinglights'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilitydimflashinglights.json'
content_hash: 'sha256:003b5a01e0706d84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityDimFlashingLights

<sub>Instance Property</sub>

Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accessibilityDimFlashingLights: Bool { get }
```

## See Also

### Minimizing motion

- [accessibilityPlayAnimatedImages](accessibilityplayanimatedimages.md) — Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
- [accessibilityReduceMotion](accessibilityreducemotion.md) — Whether the system preference for Reduce Motion is enabled.
