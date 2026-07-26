---
title: 'hoverEffectDisabled(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/hovereffectdisabled(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/hovereffectdisabled(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/hovereffectdisabled%28_%3A%29.json'
content_hash: 'sha256:82b8c31b1deb9e81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# hoverEffectDisabled(_:)

<sub>Instance Method</sub>

Adds a condition that controls whether this view can display hover effects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func hoverEffectDisabled(_ disabled: Bool = true) -> some View

```

## Parameters

- `disabled` — A Boolean value that determines whether this view can display hover effects.

## Return Value

A view that controls whether hover effects can be displayed in this view.

## Discussion

The higher views in a view hierarchy can override the value you set on this view. In the following example, the button does not display a hover effect because the outer `hoverEffectDisabled(_:)` modifier overrides the inner one:

```swift
HStack {
    Button("Press") {}
        .hoverEffectDisabled(false)
}
.hoverEffectDisabled(true)
```

## See Also

### Responding to hover events

- [onHover(perform:)](<onhover(perform_).md>) — Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](<oncontinuoushover(coordinatespace_perform_).md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:isEnabled:)](<hovereffect(__isenabled_).md>) — Applies a hover effect to this view.
- [defaultHoverEffect(_:)](<defaulthovereffect(__).md>) — Sets the default hover effect to use for views within this view.
- [isHoverEffectEnabled](../environmentvalues/ishovereffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverPhase](../hoverphase.md) — The current hovering state and value of the pointer.
- [HoverEffectPhaseOverride](../hovereffectphaseoverride.md) — Options for overriding a hover effect’s current phase.
- [OrnamentHoverContentEffect](../ornamenthovercontenteffect.md) — Presents an ornament on hover using a custom effect.
- [OrnamentHoverEffect](../ornamenthovereffect.md) — Presents an ornament on hover.
