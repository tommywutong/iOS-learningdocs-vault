---
title: 'scrollTransition(topLeading:bottomTrailing:axis:transition:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrolltransition(topleading:bottomtrailing:axis:transition:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrolltransition(topleading:bottomtrailing:axis:transition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrolltransition%28topleading%3Abottomtrailing%3Aaxis%3Atransition%3A%29.json'
content_hash: 'sha256:76d277c1ce92a9dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollTransition(topLeading:bottomTrailing:axis:transition:)

<sub>Instance Method</sub>

Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollTransition(topLeading: ScrollTransitionConfiguration, bottomTrailing: ScrollTransitionConfiguration, axis: Axis? = nil, transition: @escaping @Sendable (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View

```

## Parameters

- `topLeading` — The configuration that drives the transition when the view is about to appear at the top edge of a vertical scroll view, or the leading edge of a horizont scroll view.

- `bottomTrailing` — The configuration that drives the transition when the view is about to appear at the bottom edge of a vertical scroll view, or the trailing edge of a horizont scroll view.

- `axis` — The axis of the containing scroll view over which the transition will be applied. The default value of `nil` uses the axis of the innermost containing scroll view, or `.vertical` if the innermost scroll view is scrollable along both axes.

- `transition` — The transition to apply.

## See Also

### Animating scroll transitions

- [scrollTransition(_:axis:transition:)](<scrolltransition(__axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [ScrollTransitionPhase](../scrolltransitionphase.md) — The phases that a view transitions between when it scrolls among other views.
- [ScrollTransitionConfiguration](../scrolltransitionconfiguration.md) — The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.
