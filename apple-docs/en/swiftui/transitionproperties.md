---
title: TransitionProperties
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transitionproperties
source_url: 'https://developer.apple.com/documentation/swiftui/transitionproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transitionproperties.json'
content_hash: 'sha256:0bd85db372f72478'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TransitionProperties

<sub>Structure</sub>

The properties a `Transition` can have.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TransitionProperties
```

## Overview

A transition can have properties that specify high level information about it. This can determine how a transition interacts with other features like Accessibility settings.

- See Also: `Transition`

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating the transition properties

- [init(hasMotion:)](<transitionproperties/init(hasmotion_).md>)
- [hasMotion](transitionproperties/hasmotion.md) — Whether the transition includes motion.

## See Also

### Defining transitions

- [transition(_:)](<view/transition(__).md>) — Associates a transition with the view.
- [Transition](transition.md) — A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionPhase](transitionphase.md) — An indication of which the current stage of a transition.
- [AsymmetricTransition](asymmetrictransition.md) — A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](anytransition.md) — A type-erased transition.
- [contentTransition(_:)](<view/contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](environmentvalues/contenttransition.md) — The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](environmentvalues/contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](contenttransition.md) — A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](placeholdercontentview.md) — A placeholder used to construct an inline modifier, transition, or other helper type.
