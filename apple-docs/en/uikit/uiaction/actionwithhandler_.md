---
title: 'actionWithHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaction/actionwithhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uiaction/actionwithhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaction/actionwithhandler%3A.json'
content_hash: 'sha256:424de9e774c52d47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAction](../uiaction.md)

# actionWithHandler:

<sub>Type Method</sub>

Creates an action with the specified handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) actionWithHandler:(UIActionHandler) handler;
```

## Parameters

- `handler` — The handler to invoke after a person selects the action. This handler has the following parameter: - **action** — The action that a person selects.

## See Also

### Creating an action

- [actionWithTitle:image:identifier:handler:](actionwithtitle_image_identifier_handler_.md) — Creates an action with the specified title, image, identifier, and handler.
- [+ captureTextFromCameraActionForResponder:identifier:](<capturetextfromcamera(responder_identifier_).md>) — Creates an action for capturing text using the device’s camera.
- [Identifier](identifier-swift.struct.md) — A type that represents an action identifier.
- [UIActionHandler](../uiactionhandler.md) — A type that defines the closure for an action handler.
