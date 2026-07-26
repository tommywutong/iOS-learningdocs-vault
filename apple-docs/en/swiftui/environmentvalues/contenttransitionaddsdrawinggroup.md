---
title: contentTransitionAddsDrawingGroup
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/contenttransitionaddsdrawinggroup.json'
content_hash: 'sha256:ef81661771d6bb53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# contentTransitionAddsDrawingGroup

<sub>Instance Property</sub>

A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contentTransitionAddsDrawingGroup: Bool { get set }
```

## Discussion

Setting this value to `true` causes SwiftUI to wrap content transitions with a [drawingGroup(opaque:colorMode:)](<../view/drawinggroup(opaque_colormode_).md>) modifier.

## See Also

### Defining transitions

- [transition(_:)](<../view/transition(__).md>) — Associates a transition with the view.
- [Transition](../transition.md) — A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionProperties](../transitionproperties.md) — The properties a `Transition` can have.
- [TransitionPhase](../transitionphase.md) — An indication of which the current stage of a transition.
- [AsymmetricTransition](../asymmetrictransition.md) — A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](../anytransition.md) — A type-erased transition.
- [contentTransition(_:)](<../view/contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](contenttransition.md) — The current method of animating the contents of views.
- [ContentTransition](../contenttransition.md) — A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](../placeholdercontentview.md) — A placeholder used to construct an inline modifier, transition, or other helper type.
