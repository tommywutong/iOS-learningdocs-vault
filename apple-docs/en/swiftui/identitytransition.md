---
title: IdentityTransition
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/identitytransition
source_url: 'https://developer.apple.com/documentation/swiftui/identitytransition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/identitytransition.json'
content_hash: 'sha256:1e6e4dcd2efc8f48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# IdentityTransition

<sub>Structure</sub>

A transition that returns the input view, unmodified, as the output view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated struct IdentityTransition
```

## Relationships

- **Conforms To**: [Transition](transition.md)

## Topics

### Creating the transition

- [init()](<identitytransition/init().md>)

## See Also

### Supporting types

- [BlurReplaceTransition](blurreplacetransition.md) — A transition that animates the insertion or removal of a view by combining blurring and scaling effects.
- [MoveTransition](movetransition.md) — Returns a transition that moves the view away, towards the specified edge of the view.
- [OffsetTransition](offsettransition.md) — Returns a transition that offset the view by the specified amount.
- [OpacityTransition](opacitytransition.md) — A transition from transparent to opaque on insertion, and from opaque to transparent on removal.
- [PushTransition](pushtransition.md) — A transition that when added to a view will animate the view’s insertion by moving it in from the specified edge while fading it in, and animate its removal by moving it out towards the opposite edge and fading it out.
- [ScaleTransition](scaletransition.md) — Returns a transition that scales the view.
- [SlideTransition](slidetransition.md) — A transition that inserts by moving in from the leading edge, and removes by moving out towards the trailing edge.
