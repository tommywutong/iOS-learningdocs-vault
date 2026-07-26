---
title: accessibilityPrefersHeadAnchorAlternative
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/accessibilityprefersheadanchoralternative
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityprefersheadanchoralternative'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/accessibilityprefersheadanchoralternative.json'
content_hash: 'sha256:0f8b4dfb829ca7d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# accessibilityPrefersHeadAnchorAlternative

<sub>Instance Property</sub>

Whether the system setting to prefer alternatives to head-anchored content is on.

<sub>visionOS</sub>

```swift
var accessibilityPrefersHeadAnchorAlternative: Bool { get }
```

## Discussion

If this property’s value is true, alternate anchors should be used for most head-anchored UI, such as world anchors.

## See Also

### Accessibility

- [accessibilityAssistiveAccessEnabled](accessibilityassistiveaccessenabled.md) — A Boolean value that indicates whether Assistive Access is in use.
- [accessibilityDimFlashingLights](accessibilitydimflashinglights.md) — Whether the setting to reduce flashing or strobing lights in video content is on. This setting can also be used to determine if UI in playback controls should be shown to indicate upcoming content that includes flashing or strobing lights.
- [accessibilityDifferentiateWithoutColor](accessibilitydifferentiatewithoutcolor.md) — Whether the system preference for Differentiate without Color is enabled.
- [accessibilityEnabled](accessibilityenabled.md) — A Boolean value that indicates whether the user has enabled an assistive technology.
- [accessibilityInvertColors](accessibilityinvertcolors.md) — Whether the system preference for Invert Colors is enabled.
- [accessibilityLargeContentViewerEnabled](accessibilitylargecontentviewerenabled.md) — Whether the Large Content Viewer is enabled.
- [accessibilityPlayAnimatedImages](accessibilityplayanimatedimages.md) — Whether the setting for playing animations in an animated image is on. When this value is false, any presented image that contains animation should not play automatically.
- [accessibilityPrefersCrossFadeTransitions](accessibilitypreferscrossfadetransitions.md) — A Boolean value that indicates whether the Reduce Motion and the Prefer Cross-Fade Transitions settings are in an enabled state.
- [accessibilityQuickActionsEnabled](accessibilityquickactionsenabled.md) — A Boolean that indicates whether the quick actions feature is enabled.
- [accessibilityReduceMotion](accessibilityreducemotion.md) — Whether the system preference for Reduce Motion is enabled.
- [accessibilityReduceTransparency](accessibilityreducetransparency.md) — Whether the system preference for Reduce Transparency is enabled.
- [accessibilityShowButtonShapes](accessibilityshowbuttonshapes.md) — Whether the system preference for Show Button Shapes is enabled. _(deprecated)_
- [accessibilitySwitchControlEnabled](accessibilityswitchcontrolenabled.md) — A Boolean value that indicates whether the Switch Control motor accessibility feature is in use.
- [accessibilityVoiceOverEnabled](accessibilityvoiceoverenabled.md) — A Boolean value that indicates whether the VoiceOver screen reader is in use.
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
