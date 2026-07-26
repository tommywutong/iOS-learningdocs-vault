---
title: UISpringLoadedInteractionContext
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uispringloadedinteractioncontext
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteractioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteractioncontext.json'
content_hash: 'sha256:a50851dd372d134b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISpringLoadedInteractionContext

<sub>Protocol</sub>

The interface an object implements to provide information about a spring-loaded interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UISpringLoadedInteractionContext : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing state

- [state](uispringloadedinteractioncontext/state.md) — The current view style for the spring-loaded interaction.
- [targetItem](uispringloadedinteractioncontext/targetitem.md) — The specific subview, or associated model object, of the target view to use for the spring-loaded interaction.
- [targetView](uispringloadedinteractioncontext/targetview.md) — The view to which the current spring-loaded interaction view style is applied.
- [UISpringLoadedInteractionEffectState](uispringloadedinteractioneffectstate.md) — The spring-loaded interaction states that determine the style of the interaction view.

### Getting the drag activity’s location

- [- locationInView:](<uispringloadedinteractioncontext/location(in_).md>) — Returns the location of the drag activity within the specified view.

## See Also

### Spring-loaded interactions

- [UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md) — The interface for specifying the behavior of a spring-loaded interaction.
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md) — The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [UISpringLoadedInteraction](uispringloadedinteraction.md) — An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.
- [UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md) — The interface for providing visual styling to a spring-loaded interaction based on the interaction state.
