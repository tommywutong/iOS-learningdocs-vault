---
title: UISpringLoadedInteractionBehavior
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uispringloadedinteractionbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteractionbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteractionbehavior.json'
content_hash: 'sha256:d3b14026b2e6f0bd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISpringLoadedInteractionBehavior

<sub>Protocol</sub>

The interface for specifying the behavior of a spring-loaded interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UISpringLoadedInteractionBehavior : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Managing spring-loaded interactions

- [- shouldAllowInteraction:withContext:](<uispringloadedinteractionbehavior/shouldallow(__with_).md>) — Returns a Boolean value that determines whether spring-loaded interaction should begin or should continue for the specified context.

### Handling spring-loaded interaction notifications

- [- interactionDidFinish:](<uispringloadedinteractionbehavior/interactiondidfinish(__).md>) — Tells the behavior object when the spring-loading interaction is finished, either because it was canceled or because spring loading was activated.

## See Also

### Spring-loaded interactions

- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md) — The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [UISpringLoadedInteraction](uispringloadedinteraction.md) — An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.
- [UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md) — The interface an object implements to provide information about a spring-loaded interaction.
- [UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md) — The interface for providing visual styling to a spring-loaded interaction based on the interaction state.
