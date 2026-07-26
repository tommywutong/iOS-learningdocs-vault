---
title: 'init(_:errorHandler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowscene/activationinteraction/init(_:errorhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction/init(_:errorhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationinteraction/init%28_%3Aerrorhandler%3A%29.json'
content_hash: 'sha256:2f3576a4ebe7d14c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationInteraction](../activationinteraction.md)

# init(_:errorHandler:)

<sub>Initializer</sub>

Creates an activation interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(_ configurationProvider: @escaping UIWindowScene.ActivationInteraction.ConfigurationProvider, errorHandler: @escaping (any Error) -> Void)
```

## Parameters

- `configurationProvider` — The closure the system calls when the user triggers the interaction. The closure should return a [ActivationConfiguration](../activationconfiguration.md) object.

- `errorHandler` — The closure the system calls when the activation request fails.

## Return Value

A newly initialized activation interaction object.

## See Also

### Creating an activation interaction

- [ConfigurationProvider](configurationprovider.md) — A type alias defining a closure that provides an activation configuration for the activation interaction.
