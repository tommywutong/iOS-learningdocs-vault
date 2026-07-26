---
title: PlaceholderContentView
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/placeholdercontentview
source_url: 'https://developer.apple.com/documentation/swiftui/placeholdercontentview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/placeholdercontentview.json'
content_hash: 'sha256:c70d136114d7e72e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PlaceholderContentView

<sub>Structure</sub>

A placeholder used to construct an inline modifier, transition, or other helper type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct PlaceholderContentView<Value>
```

## Overview

You don’t use this type directly. Instead SwiftUI creates this type on your behalf.

## Relationships

- **Conforms To**: [View](view.md)

## See Also

### Defining transitions

- [transition(_:)](<view/transition(__).md>) — Associates a transition with the view.
- [Transition](transition.md) — A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionProperties](transitionproperties.md) — The properties a `Transition` can have.
- [TransitionPhase](transitionphase.md) — An indication of which the current stage of a transition.
- [AsymmetricTransition](asymmetrictransition.md) — A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](anytransition.md) — A type-erased transition.
- [contentTransition(_:)](<view/contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](environmentvalues/contenttransition.md) — The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](environmentvalues/contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](contenttransition.md) — A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
