---
title: 'hoverEffect(_:isEnabled:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/hovereffect(_:isenabled:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/hovereffect(_:isenabled:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/hovereffect%28_%3Aisenabled%3A%29.json'
content_hash: 'sha256:bb6dc79a54575cd8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# hoverEffect(_:isEnabled:)

<sub>Instance Method</sub>

Applies a hover effect to this view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func hoverEffect(_ effect: HoverEffect = .automatic, isEnabled: Bool = true) -> some View

```

## Parameters

- `effect` — The effect to apply to this view.

- `isEnabled` — Whether the effect is enabled or not.

## Return Value

A new view that applies a hover effect to `self`.

## Discussion

By default, [automatic](../hovereffect/automatic.md) is used. You can control the behavior of the automatic effect with the [defaultHoverEffect(_:)](<defaulthovereffect(__).md>) modifier.

## See Also

### Responding to hover events

- [onHover(perform:)](<onhover(perform_).md>) — Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](<oncontinuoushover(coordinatespace_perform_).md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffectDisabled(_:)](<hovereffectdisabled(__).md>) — Adds a condition that controls whether this view can display hover effects.
- [defaultHoverEffect(_:)](<defaulthovereffect(__).md>) — Sets the default hover effect to use for views within this view.
- [isHoverEffectEnabled](../environmentvalues/ishovereffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverPhase](../hoverphase.md) — The current hovering state and value of the pointer.
- [HoverEffectPhaseOverride](../hovereffectphaseoverride.md) — Options for overriding a hover effect’s current phase.
- [OrnamentHoverContentEffect](../ornamenthovercontenteffect.md) — Presents an ornament on hover using a custom effect.
- [OrnamentHoverEffect](../ornamenthovereffect.md) — Presents an ornament on hover.
