---
title: ScrollTransitionConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltransitionconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionconfiguration.json'
content_hash: 'sha256:3a429752840019bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollTransitionConfiguration

<sub>Structure</sub>

The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollTransitionConfiguration
```

## Topics

### Getting the configuration

- [identity](scrolltransitionconfiguration/identity.md) — Creates a new configuration that does not change the appearance of the view.
- [animated](scrolltransitionconfiguration/animated.md) — Creates a new configuration that discretely animates the transition when the view becomes visible.
- [animated(_:)](<scrolltransitionconfiguration/animated(__).md>) — Creates a new configuration that discretely animates the transition when the view becomes visible.
- [interactive](scrolltransitionconfiguration/interactive.md) — Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.
- [interactive(timingCurve:)](<scrolltransitionconfiguration/interactive(timingcurve_).md>) — Creates a new configuration that interactively interpolates the transition’s effect as the view is scrolled into the visible region of the container.

### Accessing the configuration

- [animation(_:)](<scrolltransitionconfiguration/animation(__).md>) — Sets the animation with which the transition will be applied.
- [threshold(_:)](<scrolltransitionconfiguration/threshold(__).md>) — Sets the threshold at which the view will be considered fully visible.
- [Threshold](scrolltransitionconfiguration/threshold.md) — Describes a specific point in the progression of a target view within a container from hidden (fully outside the container) to visible.

## See Also

### Animating scroll transitions

- [scrollTransition(_:axis:transition:)](<view/scrolltransition(__axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](<view/scrolltransition(topleading_bottomtrailing_axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [ScrollTransitionPhase](scrolltransitionphase.md) — The phases that a view transitions between when it scrolls among other views.
