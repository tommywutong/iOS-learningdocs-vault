---
title: 'transition(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/transition(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/transition(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/transition%28_%3A%29.json'
content_hash: 'sha256:3b1c6f309457a563'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# transition(_:)

<sub>Instance Method</sub>

Associates a transition with the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated func transition<T>(_ transition: T) -> some View where T : Transition

```

## Discussion

When this view appears or disappears, the transition will be applied to it, allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or disappears, will use a custom RotatingFadeTransition transition to show it.

```swift
if isActive {
    MyView()
        .transition(RotatingFadeTransition())
}
Button("Toggle") {
    withAnimation {
        isActive.toggle()
    }
}
```

## See Also

### Defining transitions

- [Transition](../transition.md) — A description of view changes to apply when a view is added to and removed from the view hierarchy.
- [TransitionProperties](../transitionproperties.md) — The properties a `Transition` can have.
- [TransitionPhase](../transitionphase.md) — An indication of which the current stage of a transition.
- [AsymmetricTransition](../asymmetrictransition.md) — A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](../anytransition.md) — A type-erased transition.
- [contentTransition(_:)](<contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](../environmentvalues/contenttransition.md) — The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](../environmentvalues/contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](../contenttransition.md) — A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](../placeholdercontentview.md) — A placeholder used to construct an inline modifier, transition, or other helper type.
