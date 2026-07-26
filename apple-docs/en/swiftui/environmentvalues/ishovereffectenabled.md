---
title: isHoverEffectEnabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/ishovereffectenabled
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/ishovereffectenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/ishovereffectenabled.json'
content_hash: 'sha256:aaffc86b31c9ee98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# isHoverEffectEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isHoverEffectEnabled: Bool { get set }
```

## Discussion

The default value is `true`.

## See Also

### Responding to hover events

- [onHover(perform:)](<../view/onhover(perform_).md>) — Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](<../view/oncontinuoushover(coordinatespace_perform_).md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:isEnabled:)](<../view/hovereffect(__isenabled_).md>) — Applies a hover effect to this view.
- [hoverEffectDisabled(_:)](<../view/hovereffectdisabled(__).md>) — Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](<../view/defaulthovereffect(__).md>) — Sets the default hover effect to use for views within this view.
- [HoverPhase](../hoverphase.md) — The current hovering state and value of the pointer.
- [HoverEffectPhaseOverride](../hovereffectphaseoverride.md) — Options for overriding a hover effect’s current phase.
- [OrnamentHoverContentEffect](../ornamenthovercontenteffect.md) — Presents an ornament on hover using a custom effect.
- [OrnamentHoverEffect](../ornamenthovereffect.md) — Presents an ornament on hover.
