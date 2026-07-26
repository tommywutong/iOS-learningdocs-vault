---
title: UIWindowScene.ActivationInteraction.ConfigurationProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationinteraction/configurationprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationinteraction/configurationprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationinteraction/configurationprovider.json'
content_hash: 'sha256:6be333b77071e306'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationInteraction](../activationinteraction.md)

# UIWindowScene.ActivationInteraction.ConfigurationProvider

<sub>Type Alias</sub>

A type alias defining a closure that provides an activation configuration for the activation interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias ConfigurationProvider = (UIWindowScene.ActivationInteraction, CGPoint) -> UIWindowScene.ActivationConfiguration?
```

## Parameters

- `interaction` — The [ActivationInteraction](../activationinteraction.md) requesting a configuration.

- `location` — The location in the view of the interaction requesting a configuration.

## Return Value

An activation configuration you can use to request a window scene.

## See Also

### Creating an activation interaction

- [- initWithConfigurationProvider:errorHandler:](<init(__errorhandler_).md>) — Creates an activation interaction.
