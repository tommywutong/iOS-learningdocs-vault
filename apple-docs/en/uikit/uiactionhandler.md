---
title: UIActionHandler
framework: UIKit
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiactionhandler
source_url: 'https://developer.apple.com/documentation/uikit/uiactionhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionhandler.json'
content_hash: 'sha256:37e3e9e473b71b44'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIActionHandler

<sub>Type Alias</sub>

A type that defines the closure for an action handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
typealias UIActionHandler = (UIAction) -> Void
```

## Parameters

- `action` — The action selected by the user.

## See Also

### Creating an action

- [init(title:subtitle:image:identifier:discoverabilityTitle:attributes:state:handler:)](<uiaction/init(title_subtitle_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [init(title:image:identifier:discoverabilityTitle:attributes:state:handler:)](<uiaction/init(title_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [+ captureTextFromCameraActionForResponder:identifier:](<uiaction/capturetextfromcamera(responder_identifier_).md>) — Creates an action for capturing text using the device’s camera.
- [Identifier](uiaction/identifier-swift.struct.md) — A type that represents an action identifier.
