---
title: UIWindowScene.ActivationAction.ConfigurationProvider
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwindowscene/activationaction/configurationprovider
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction/configurationprovider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationaction/configurationprovider.json'
content_hash: 'sha256:f3ef5a15dec81ad7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationAction](../activationaction.md)

# UIWindowScene.ActivationAction.ConfigurationProvider

<sub>Type Alias</sub>

A type alias defining a closure that provides an activation configuration for the activation action.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
typealias ConfigurationProvider = (UIWindowScene.ActivationAction) -> UIWindowScene.ActivationConfiguration?
```

## Parameters

- `action` — The [ActivationAction](../activationaction.md) requesting a configuration.

## Return Value

An activation configuration you can use to request a window scene.

## See Also

### Creating an activation action

- [init(title:subtitle:image:identifier:discoverabilityTitle:attributes:alternate:_:)](<init(title_subtitle_image_identifier_discoverabilitytitle_attributes_alternate___).md>) — Creates an activation action using the specified parameters.
