---
title: 'init(interactionBehavior:interactionEffect:activationHandler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uispringloadedinteraction/init(interactionbehavior:interactioneffect:activationhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteraction/init(interactionbehavior:interactioneffect:activationhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteraction/init%28interactionbehavior%3Ainteractioneffect%3Aactivationhandler%3A%29.json'
content_hash: 'sha256:03f1a69e12796924'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISpringLoadedInteraction](../uispringloadedinteraction.md)

# init(interactionBehavior:interactionEffect:activationHandler:)

<sub>Initializer</sub>

Initializes a new spring-loaded interaction with a specific behavior, visual effect, and activation handler block.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(interactionBehavior: (any UISpringLoadedInteractionBehavior)?, interactionEffect: (any UISpringLoadedInteractionEffect)?, activationHandler handler: @escaping (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)
```

## Parameters

- `interactionBehavior` — The interaction behavior object controlling the spring-loaded interaction activation. If the value is `nil`, the default behavior is used.

- `interactionEffect` — The interaction effect object styling the interaction’s view. If the value is `nil`, the default effect is used.

- `handler` — The handler that is invoked when the spring-loaded interaction is activated.

## Return Value

A spring-loaded interaction that has a specific behavior, visual effect, and activation handler block.

## See Also

### Initializing a spring-loaded interaction

- [- initWithActivationHandler:](<init(activationhandler_).md>) — Initializes a new spring-loaded interaction with a specified activation handler block, employing the default behavior and visual effect.
