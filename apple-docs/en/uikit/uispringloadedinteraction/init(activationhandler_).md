---
title: 'init(activationHandler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uispringloadedinteraction/init(activationhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uispringloadedinteraction/init(activationhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uispringloadedinteraction/init%28activationhandler%3A%29.json'
content_hash: 'sha256:64e927d2612ba183'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISpringLoadedInteraction](../uispringloadedinteraction.md)

# init(activationHandler:)

<sub>Initializer</sub>

Initializes a new spring-loaded interaction with a specified activation handler block, employing the default behavior and visual effect.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(activationHandler handler: @escaping (UISpringLoadedInteraction, any UISpringLoadedInteractionContext) -> Void)
```

## Parameters

- `handler` — The handler that is invoked when the spring-loaded interaction is activated.

## Return Value

A spring-loaded interaction that has a specific activation handler block and a default behavior and visual effect.

## See Also

### Initializing a spring-loaded interaction

- [- initWithInteractionBehavior:interactionEffect:activationHandler:](<init(interactionbehavior_interactioneffect_activationhandler_).md>) — Initializes a new spring-loaded interaction with a specific behavior, visual effect, and activation handler block.
