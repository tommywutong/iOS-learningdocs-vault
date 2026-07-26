---
title: 'defaultHoverEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/defaulthovereffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/defaulthovereffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/defaulthovereffect%28_%3A%29.json'
content_hash: 'sha256:113d069c6d259329'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# defaultHoverEffect(_:)

<sub>Instance Method</sub>

Sets the default hover effect to use for views within this view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated func defaultHoverEffect(_ effect: HoverEffect?) -> some View

```

## Parameters

- `effect` — The default hover effect to use for views within this view.

## Return Value

A view that uses this effect as the default hover effect.

## Discussion

Use this modifier to set a specific hover effect for all views with the [hoverEffect(_:)](<hovereffect(__).md>) modifier applied within a view. The default effect is typically used when no [HoverEffect](../hovereffect.md) was provided or if [automatic](../hovereffect/automatic.md) is specified.

For example, this view uses [highlight](../hovereffect/highlight.md) for both the red and green Color views:

```swift
HStack {
    Color.red.hoverEffect()
    Color.green.hoverEffect()
}
.defaultHoverEffect(.highlight)
```

This also works for customizing the default hover effect in views like [Button](../button.md)s when using a SwiftUI-defined style like `ButtonStyle/bordered`, which can provide a hover effect by default. For example, this view replaces the hover effect for a [Button](../button.md) with [highlight](../hovereffect/highlight.md):

```swift
Button("Next") {}
    // perform action
}
.buttonStyle(.bordered)
.defaultHoverEffect(.highlight)
```

Use a `nil` effect to indicate that the default hover effect should not be modified.

## See Also

### Responding to hover events

- [onHover(perform:)](<onhover(perform_).md>) — Adds an action to perform when the user moves the pointer over or away from the view’s frame.
- [onContinuousHover(coordinateSpace:perform:)](<oncontinuoushover(coordinatespace_perform_).md>) — Adds an action to perform when the pointer enters, moves within, and exits the view’s bounds.
- [hoverEffect(_:isEnabled:)](<hovereffect(__isenabled_).md>) — Applies a hover effect to this view.
- [hoverEffectDisabled(_:)](<hovereffectdisabled(__).md>) — Adds a condition that controls whether this view can display hover effects.
- [isHoverEffectEnabled](../environmentvalues/ishovereffectenabled.md) — A Boolean value that indicates whether the view associated with this environment allows hover effects to be displayed.
- [HoverPhase](../hoverphase.md) — The current hovering state and value of the pointer.
- [HoverEffectPhaseOverride](../hovereffectphaseoverride.md) — Options for overriding a hover effect’s current phase.
- [OrnamentHoverContentEffect](../ornamenthovercontenteffect.md) — Presents an ornament on hover using a custom effect.
- [OrnamentHoverEffect](../ornamenthovereffect.md) — Presents an ornament on hover.
