---
title: UISpringLoadedInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uispringloadedinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteraction.json'
content_hash: 'sha256:c557d7c59441cdbd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISpringLoadedInteraction

<sub>Class</sub>

An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UISpringLoadedInteraction
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Initializing a spring-loaded interaction

- [- initWithInteractionBehavior:interactionEffect:activationHandler:](<uispringloadedinteraction/init(interactionbehavior_interactioneffect_activationhandler_).md>) — Initializes a new spring-loaded interaction with a specific behavior, visual effect, and activation handler block.
- [- initWithActivationHandler:](<uispringloadedinteraction/init(activationhandler_).md>) — Initializes a new spring-loaded interaction with a specified activation handler block, employing the default behavior and visual effect.

### Getting information about the spring-loaded interaction

- [interactionBehavior](uispringloadedinteraction/interactionbehavior.md) — The behavior for the spring-loaded interaction.
- [interactionEffect](uispringloadedinteraction/interactioneffect.md) — The visual effect for the spring-loaded interaction.

## See Also

### Spring-loaded interactions

- [UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md) — The interface for specifying the behavior of a spring-loaded interaction.
- [UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md) — The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md) — The interface an object implements to provide information about a spring-loaded interaction.
- [UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md) — The interface for providing visual styling to a spring-loaded interaction based on the interaction state.
