---
title: Transition
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transition
source_url: 'https://developer.apple.com/documentation/swiftui/transition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transition.json'
content_hash: 'sha256:9bdcc4bdb5eaa514'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Transition

<sub>Protocol</sub>

A description of view changes to apply when a view is added to and removed from the view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol Transition
```

## Overview

A transition should generally be made by applying one or more modifiers to the `content`. For symmetric transitions, the `isIdentity` property on `phase` can be used to change the properties of modifiers. For asymmetric transitions, the phase itself can be used to change those properties. Transitions should not use any identity-affecting changes like `.id`, `if`, and `switch` on the `content`, since doing so would reset the state of the view they’re applied to, causing wasted work and potentially surprising behavior when it appears and disappears.

The following code defines a transition that can be used to change the opacity and rotation when a view appears and disappears.

```swift
struct RotatingFadeTransition: Transition {
    func body(content: Content, phase: TransitionPhase) -> some View {
        content
          .opacity(phase.isIdentity ? 1.0 : 0.0)
          .rotationEffect(phase.rotation)
    }
}
extension TransitionPhase {
    fileprivate var rotation: Angle {
        switch self {
        case .willAppear: return .degrees(30)
        case .identity: return .zero
        case .didDisappear: return .degrees(-30)
        }
    }
}
```

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

- See Also: `TransitionPhase`
- See Also: `AnyTransition`

## Relationships

- **Conforming Types**: [AsymmetricTransition](asymmetrictransition.md), [BlurReplaceTransition](blurreplacetransition.md), [IdentityTransition](identitytransition.md), [MoveTransition](movetransition.md), [OffsetTransition](offsettransition.md), [OpacityTransition](opacitytransition.md), [PushTransition](pushtransition.md), [ScaleTransition](scaletransition.md), [SlideTransition](slidetransition.md), [SymbolEffectTransition](symboleffecttransition.md)

## Topics

### Getting built-in transitions

- [blurReplace](transition/blurreplace.md) — A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [blurReplace(_:)](<transition/blurreplace(__).md>) — A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [identity](transition/identity.md) — A transition that returns the input view, unmodified, as the output view.
- [move(edge:)](<transition/move(edge_).md>) — Returns a transition that moves the view away, towards the specified edge of the view.
- [offset(_:)](<transition/offset(__).md>) — Returns a transition that offset the view by the specified amount.
- [offset(x:y:)](<transition/offset(x_y_).md>) — Returns a transition that offset the view by the specified x and y values.
- [opacity](transition/opacity.md) — A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [push(from:)](<transition/push(from_).md>) — Creates a transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [scale](transition/scale.md) — Returns a transition that scales the view.
- [scale(_:anchor:)](<transition/scale(__anchor_).md>) — Returns a transition that scales the view by the specified amount.
- [slide](transition/slide.md) — A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.
- [symbolEffect](transition/symboleffect.md) — A transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [symbolEffect(_:options:)](<transition/symboleffect(__options_).md>) — Creates a transition that applies the provided effect to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.

### Configuring a transition

- [animation(_:)](<transition/animation(__).md>) — Attaches an animation to this transition.
- [properties](transition/properties.md) — Returns the properties this transition type has.

### Using a transition

- [apply(content:phase:)](<transition/apply(content_phase_).md>)
- [combined(with:)](<transition/combined(with_).md>)

### Creating a custom transition

- [body(content:phase:)](<transition/body(content_phase_).md>) — Gets the current body of the caller.
- [Body](transition/body.md) — The type of view representing the body.
- [Content](transition/content.md) — The content view type passed to `body()`.

### Supporting types

- [BlurReplaceTransition](blurreplacetransition.md) — A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [IdentityTransition](identitytransition.md) — A transition that returns the input view, unmodified, as the output view.
- [MoveTransition](movetransition.md) — Returns a transition that moves the view away, towards the specified edge of the view.
- [OffsetTransition](offsettransition.md) — Returns a transition that offset the view by the specified amount.
- [OpacityTransition](opacitytransition.md) — A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [PushTransition](pushtransition.md) — A transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [ScaleTransition](scaletransition.md) — Returns a transition that scales the view.
- [SlideTransition](slidetransition.md) — A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.

## See Also

### Defining transitions

- [transition(_:)](<view/transition(__).md>) — Associates a transition with the view.
- [TransitionProperties](transitionproperties.md) — The properties a `Transition` can have.
- [TransitionPhase](transitionphase.md) — An indication of which the current stage of a transition.
- [AsymmetricTransition](asymmetrictransition.md) — A composite `Transition` that uses a different transition for insertion versus removal.
- [AnyTransition](anytransition.md) — A type-erased transition.
- [contentTransition(_:)](<view/contenttransition(__).md>) — Modifies the view to use a given transition as its method of animating changes to the contents of its views.
- [contentTransition](environmentvalues/contenttransition.md) — The current method of animating the contents of views.
- [contentTransitionAddsDrawingGroup](environmentvalues/contenttransitionaddsdrawinggroup.md) — A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [ContentTransition](contenttransition.md) — A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.
- [PlaceholderContentView](placeholdercontentview.md) — A placeholder used to construct an inline modifier, transition, or other helper type.
