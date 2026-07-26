---
title: accessibilityReduceMotion
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/accessibilityreducemotion
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducemotion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilityreducemotion.json'
content_hash: 'sha256:82b4085537abcc27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityReduceMotion

<sub>Instance Property</sub>

Whether the system preference for Reduce Motion is enabled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var accessibilityReduceMotion: Bool { get }
```

## Discussion

If this property’s value is true, UI should avoid large animations, especially those that simulate the third dimension.

## See Also

### Minimizing motion

- [accessibilityDimFlashingLights](accessibilitydimflashinglights.md) — Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [accessibilityPlayAnimatedImages](accessibilityplayanimatedimages.md) — Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
