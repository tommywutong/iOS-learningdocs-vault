---
title: UISpringLoadedInteractionEffect
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uispringloadedinteractioneffect
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteractioneffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteractioneffect.json'
content_hash: 'sha256:b84007c6f5728631'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISpringLoadedInteractionEffect

<sub>Protocol</sub>

The interface for providing visual styling to a spring-loaded interaction based on the interaction state.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UISpringLoadedInteractionEffect : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Handling changes

- [- interaction:didChangeWithContext:](<uispringloadedinteractioneffect/interaction(__didchangewith_).md>) — Called when the spring-loaded interaction state has changed.

## See Also

### Spring-loaded interactions

- [UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md) — The interface for specifying the behavior of a spring-loaded interaction.
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md) — The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [UISpringLoadedInteraction](uispringloadedinteraction.md) — An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.
- [UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md) — The interface an object implements to provide information about a spring-loaded interaction.
