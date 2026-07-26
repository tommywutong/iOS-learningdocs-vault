---
title: 'init(title:subtitle:image:identifier:discoverabilityTitle:attributes:alternate:_:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiwindowscene/activationaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:alternate:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscene/activationaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:alternate:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscene/activationaction/init%28title%3Asubtitle%3Aimage%3Aidentifier%3Adiscoverabilitytitle%3Aattributes%3Aalternate%3A_%3A%29.json'
content_hash: 'sha256:b167430f77db3f40'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIWindowScene](../../uiwindowscene.md) · [ActivationAction](../activationaction.md)

# init(title:subtitle:image:identifier:discoverabilityTitle:attributes:alternate:_:)

<sub>Initializer</sub>

Creates an activation action using the specified parameters.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(title: String? = nil, subtitle: String? = nil, image: UIImage? = nil, identifier: UIAction.Identifier? = nil, discoverabilityTitle: String? = nil, attributes: UIMenuElement.Attributes = [], alternate: UIAction? = nil, _ configuration: @escaping UIWindowScene.ActivationAction.ConfigurationProvider)
```

## Parameters

- `title` — The title to display for the action.

- `subtitle` — The subtitle to display for the action.

- `image` — The image to display next to the action’s title. Only the [contextSystem](../../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

- `identifier` — The unique identifier for the action. Specify `nil` to let this method create a unique identifier for you.

- `discoverabilityTitle` — An elaborated title that explains the purpose of the action.

- `attributes` — The attributes indicating the style of the action.

- `alternate` — An alternate action to perform if the platform doesn’t support multiple scenes or if requesting a scene fails.

- `configuration` — The closure the system calls when the user selects the action. The closure should return a [ActivationConfiguration](../activationconfiguration.md) object.

## See Also

### Creating an activation action

- [ConfigurationProvider](configurationprovider.md) — A type alias defining a closure that provides an activation configuration for the activation action.
