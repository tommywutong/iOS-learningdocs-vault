---
title: ContentTransition
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/contenttransition
source_url: 'https://developer.apple.com/documentation/swiftui/contenttransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/contenttransition.json'
content_hash: 'sha256:5d517a57d82cd50f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ContentTransition

<sub>Structure</sub>

A kind of transition that applies to the content within a single view, rather than to the insertion or removal of a view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ContentTransition
```

## Overview

Set the behavior of content transitions within a view with the [contentTransition(_:)](<view/contenttransition(__).md>) modifier, passing in one of the defined transitions, such as [opacity](contenttransition/opacity.md) or [interpolate](contenttransition/interpolate.md) as the parameter.

> [!tip] Tip
> Content transitions only take effect within transactions that apply an [Animation](animation.md) to the views inside the [contentTransition(_:)](<view/contenttransition(__).md>) modifier.

Content transitions only take effect within the context of an [Animation](animation.md) block.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting content transitions

- [identity](contenttransition/identity.md) — The identity content transition, which indicates that content changes shouldn’t animate.
- [interpolate](contenttransition/interpolate.md) — A content transition that indicates the views attempt to interpolate their contents during transitions, where appropriate.
- [numericText(countsDown:)](<contenttransition/numerictext(countsdown_).md>) — Creates a content transition intended to be used with `Text` views displaying numeric text. In certain environments changes to the text will enable a nonstandard transition tailored to numeric characters that count up or down.
- [numericText(value:)](<contenttransition/numerictext(value_).md>) — Creates a content transition intended to be used with `Text` views displaying numbers.
- [opacity](contenttransition/opacity.md) — A content transition that indicates content fades from transparent to opaque on insertion, and from opaque to transparent on removal.
- [symbolEffect](contenttransition/symboleffect.md) — A content transition that applies the default symbol effect transition to symbol images within the inserted or removed view hierarchy. Other views are unaffected by this transition.
- [symbolEffect(_:options:)](<contenttransition/symboleffect(__options_).md>) — Creates a content transition that applies the symbol Replace animation to symbol images that it is applied to.

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
- [PlaceholderContentView](placeholdercontentview.md) — A placeholder used to construct an inline modifier, transition, or other helper type.
