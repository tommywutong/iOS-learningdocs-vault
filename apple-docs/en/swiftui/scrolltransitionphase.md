---
title: ScrollTransitionPhase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrolltransitionphase
source_url: 'https://developer.apple.com/documentation/swiftui/scrolltransitionphase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrolltransitionphase.json'
content_hash: 'sha256:8c0a786dae1fe935'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollTransitionPhase

<sub>Enumeration</sub>

The phases that a view transitions between when it scrolls among other views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum ScrollTransitionPhase
```

## Overview

When a view with a scroll transition modifier applied is approaching the visible region of the containing scroll view or other container, the effect  will first be applied with the `topLeading` or `bottomTrailing` phase (depending on which edge the view is approaching), then will be moved to the `identity` phase as the view moves into the visible area. The timing and behavior that determines when a view is visible within the container is controlled by the configuration that is provided to the `scrollTransition` modifier.

In the `identity` phase, scroll transitions should generally not make any visual change to the view they are applied to, since the transition’s view modifications in the `identity` phase will be applied to the view as long as it is visible. In the `topLeading` and `bottomTrailing` phases, transitions should apply a change that will be animated to create the transition.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting the phase

- [ScrollTransitionPhase.identity](scrolltransitionphase/identity.md) — The scroll transition is being applied to a view that is in the visible area.
- [ScrollTransitionPhase.topLeading](scrolltransitionphase/topleading.md) — The scroll transition is being applied to a view that is about to move into the visible area at the top edge of a vertical scroll view, or the leading edge of a horizont scroll view.
- [ScrollTransitionPhase.bottomTrailing](scrolltransitionphase/bottomtrailing.md) — The scroll transition is being applied to a view that is about to move into the visible area at the bottom edge of a vertical scroll view, or the trailing edge of a horizontal scroll view.

### Accessing the phase state

- [isIdentity](scrolltransitionphase/isidentity.md)
- [value](scrolltransitionphase/value.md) — A phase-derived value that can be used to scale or otherwise modify effects.

## See Also

### Animating scroll transitions

- [scrollTransition(_:axis:transition:)](<view/scrolltransition(__axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [scrollTransition(topLeading:bottomTrailing:axis:transition:)](<view/scrolltransition(topleading_bottomtrailing_axis_transition_).md>) — Applies the given transition, animating between the phases of the transition as this view appears and disappears within the visible region of the containing scroll view.
- [ScrollTransitionConfiguration](scrolltransitionconfiguration.md) — The configuration of a scroll transition that controls how a transition is applied as a view is scrolled through the visible region of a containing scroll view or other container.
