---
title: TransitionPhase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transitionphase
source_url: 'https://developer.apple.com/documentation/swiftui/transitionphase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transitionphase.json'
content_hash: 'sha256:8fbf7fd6fc5702db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TransitionPhase

<sub>Enumeration</sub>

An indication of which the current stage of a transition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum TransitionPhase
```

## Overview

When a view is appearing with a transition, the transition will first be shown with the `willAppear` phase, then will be immediately moved to the `identity` phase. When a view is being removed, its transition is changed from the `identity` phase to the `didDisappear` phase. If a view is removed while it is still transitioning in, then its phase will change to `didDisappear`. If a view is re-added while it is transitioning out, its phase will change back to `identity`.

In the `identity` phase, transitions should generally not make any visual change to the view they are applied to, since the transition’s view modifications in the `identity` phase will be applied to the view as long as it is visible. In the `willAppear` and `didDisappear` phases, transitions should apply a change that will be animated to create the transition. If no animatable change is applied, then the transition will be a no-op.

- See Also: `Transition`
- See Also: `AnyTransition`

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the phase

- [TransitionPhase.identity](transitionphase/identity.md) — The transition is being applied to a view that is in the view hierarchy.
- [TransitionPhase.willAppear](transitionphase/willappear.md) — The transition is being applied to a view that is about to be inserted into the view hierarchy.
- [TransitionPhase.didDisappear](transitionphase/diddisappear.md) — The transition is being applied to a view that has been requested to be removed from the view hierarchy.

### Getting phase characteristics

- [isIdentity](transitionphase/isidentity.md) — A Boolean that indicates whether the transition should have an identity effect, i.e. not change the appearance of its view.
- [value](transitionphase/value.md) — A value that can be used to multiply effects that are applied differently depending on the phase.

## See Also

### Defining transitions

- [transition(_:)](<view/transition(__).md>) — Associates a transition with the view.
- [Transition](transition.md) — A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionProperties](transitionproperties.md) — The properties a `Transition` can have.
- [AsymmetricTransition](asymmetrictransition.md) — A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](anytransition.md) — A type-erased transition.
- [contentTransition(_:)](<view/contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](environmentvalues/contenttransition.md) — The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](environmentvalues/contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](contenttransition.md) — A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](placeholdercontentview.md) — A placeholder used to construct an inline modifier, transition, or other helper type.
