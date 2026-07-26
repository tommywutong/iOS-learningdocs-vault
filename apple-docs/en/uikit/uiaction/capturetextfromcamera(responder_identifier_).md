---
title: 'captureTextFromCamera(responder:identifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaction/capturetextfromcamera(responder:identifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiaction/capturetextfromcamera(responder:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaction/capturetextfromcamera%28responder%3Aidentifier%3A%29.json'
content_hash: 'sha256:4213e40502543992'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAction](../uiaction.md)

# captureTextFromCamera(responder:identifier:)

<sub>Type Method</sub>

Creates an action for capturing text using the device’s camera.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func captureTextFromCamera(responder: any UIResponder & UIKeyInput, identifier: UIAction.Identifier?) -> Self
```

## Parameters

- `responder` — The [UIKeyInput](../uikeyinput.md) responder to send the [- captureTextFromCamera:](<../uiresponder/capturetextfromcamera(__).md>) message to.

- `identifier` — The unique identifier for the action. Specify `nil` to let this method create a unique identifier for you.

## See Also

### Creating an action

- [init(title:subtitle:image:identifier:discoverabilityTitle:attributes:state:handler:)](<init(title_subtitle_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [init(title:image:identifier:discoverabilityTitle:attributes:state:handler:)](<init(title_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [Identifier](identifier-swift.struct.md) — A type that represents an action identifier.
- [UIActionHandler](../uiactionhandler.md) — A type that defines the closure for an action handler.
