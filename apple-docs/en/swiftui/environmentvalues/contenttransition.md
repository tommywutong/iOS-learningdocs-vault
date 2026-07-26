---
title: contentTransition
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/contenttransition
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/contenttransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/contenttransition.json'
content_hash: 'sha256:d4c5deb402ff9ebf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# contentTransition

<sub>Instance Property</sub>

The current method of animating the contents of views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contentTransition: ContentTransition { get set }
```

## See Also

### Defining transitions

- [transition(_:)](<../view/transition(__).md>) — Associates a transition with the view.
- [Transition](../transition.md) — A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionProperties](../transitionproperties.md) — The properties a `Transition` can have.
- [TransitionPhase](../transitionphase.md) — An indication of which the current stage of a transition.
- [AsymmetricTransition](../asymmetrictransition.md) — A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](../anytransition.md) — A type-erased transition.
- [contentTransition(_:)](<../view/contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransitionAddsDrawingGroup](contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](../contenttransition.md) — A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](../placeholdercontentview.md) — A placeholder used to construct an inline modifier, transition, or other helper type.
