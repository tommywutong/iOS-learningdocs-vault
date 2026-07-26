---
title: 'scrollTransition(_:axis:transition:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/scrolltransition(_:axis:transition:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/scrolltransition(_:axis:transition:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/scrolltransition%28_%3Aaxis%3Atransition%3A%29.json'
content_hash: 'sha256:71af96ba15ff9111'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# scrollTransition(_:axis:transition:)

<sub>Instance Method</sub>

Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func scrollTransition(_ configuration: ScrollTransitionConfiguration = .interactive, axis: Axis? = nil, transition: @escaping @Sendable (EmptyVisualEffect, ScrollTransitionPhase) -> some VisualEffect) -> some View

```

## Parameters

- `configuration` — The configuration controlling how the transition will be applied. The configuration will be applied both while the view is coming into view and while it is disappearing (the transition is symmetrical).

- `axis` — The axis of the containing scroll view over which the transition will be applied. The default value of `nil` uses the axis of the innermost containing scroll view, or `.vertical` if the innermost scroll view is scrollable along both axes.

- `transition` — A closure that applies visual effects as a function of the provided phase.

## See Also

### Animating scroll transitions

- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](<scrolltransition(topleading_bottomtrailing_axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [ScrollTransitionPhase](../scrolltransitionphase.md) — The phases that a view transitions between when it scrolls among other views.
- [ScrollTransitionConfiguration](../scrolltransitionconfiguration.md) — The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.
