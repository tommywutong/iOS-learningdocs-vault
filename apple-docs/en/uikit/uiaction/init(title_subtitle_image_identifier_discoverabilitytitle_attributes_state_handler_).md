---
title: 'init(title:subtitle:image:identifier:discoverabilityTitle:attributes:state:handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:state:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaction/init(title:subtitle:image:identifier:discoverabilitytitle:attributes:state:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaction/init%28title%3Asubtitle%3Aimage%3Aidentifier%3Adiscoverabilitytitle%3Aattributes%3Astate%3Ahandler%3A%29.json'
content_hash: 'sha256:bb72bff67eb65aff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAction](../uiaction.md)

# init(title:subtitle:image:identifier:discoverabilityTitle:attributes:state:handler:)

<sub>Initializer</sub>

Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(title: String = "", subtitle: String? = nil, image: UIImage? = nil, identifier: UIAction.Identifier? = nil, discoverabilityTitle: String? = nil, attributes: UIMenuElement.Attributes = [], state: UIMenuElement.State = .off, handler: @escaping UIActionHandler)
```

## Parameters

- `title` — The title to display for the action.

- `subtitle` — The subtitle to display alongside the action’s title.

- `image` — The image to display next to the action’s `title`. Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

- `identifier` — The unique identifier for the action. Specify `nil` to let this method create a unique identifier for you.

- `discoverabilityTitle` — An elaborated title that explains the purpose of the action.

- `attributes` — The attributes indicating the style of the action.

- `state` — The initial state of the action.

- `handler` — The handler to invoke after a person selects the action. This handler has the following parameter: - **action** — The action that a person selects.

## See Also

### Creating an action

- [init(title:image:identifier:discoverabilityTitle:attributes:state:handler:)](<init(title_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [+ captureTextFromCameraActionForResponder:identifier:](<capturetextfromcamera(responder_identifier_).md>) — Creates an action for capturing text using the device’s camera.
- [Identifier](identifier-swift.struct.md) — A type that represents an action identifier.
- [UIActionHandler](../uiactionhandler.md) — A type that defines the closure for an action handler.
