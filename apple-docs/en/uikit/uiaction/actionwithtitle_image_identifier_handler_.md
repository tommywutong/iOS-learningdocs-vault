---
title: 'actionWithTitle:image:identifier:handler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiaction/actionwithtitle:image:identifier:handler:'
source_url: 'https://developer.apple.com/documentation/uikit/uiaction/actionwithtitle:image:identifier:handler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaction/actionwithtitle%3Aimage%3Aidentifier%3Ahandler%3A.json'
content_hash: 'sha256:64f88c1c86fe20fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAction](../uiaction.md)

# actionWithTitle:image:identifier:handler:

<sub>Type Method</sub>

Creates an action with the specified title, image, identifier, and handler.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) actionWithTitle:(NSString *) title image:(UIImage *) image identifier:(UIActionIdentifier) identifier handler:(UIActionHandler) handler;
```

## Parameters

- `title` — The title to display for the action.

- `image` — The image to display next to the action’s `title`. Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

- `identifier` — The unique identifier for the action. Specify `nil` to let this method create a unique identifier for you.

- `handler` — The handler to invoke after a person selects the action. This handler has the following parameter: - **action** — The action that a person selects.

## Return Value

A newly initialized action object.

## See Also

### Creating an action

- [actionWithHandler:](actionwithhandler_.md) — Creates an action with the specified handler.
- [+ captureTextFromCameraActionForResponder:identifier:](<capturetextfromcamera(responder_identifier_).md>) — Creates an action for capturing text using the device’s camera.
- [Identifier](identifier-swift.struct.md) — A type that represents an action identifier.
- [UIActionHandler](../uiactionhandler.md) — A type that defines the closure for an action handler.
