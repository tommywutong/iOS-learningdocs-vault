---
title: 'onPasteCommand(of:validator:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/onpastecommand(of:validator:perform:)-964k1'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onpastecommand(of:validator:perform:)-964k1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onpastecommand%28of%3Avalidator%3Aperform%3A%29-964k1.json'
content_hash: 'sha256:0ba53e6570cc93fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onPasteCommand(of:validator:perform:)

<sub>Instance Method</sub>

Adds an action to perform in response to the system’s Paste command with items that you validate.

> [!warning] Deprecated
> Use [onPasteCommand(of:validator:perform:)](<onpastecommand(of_validator_perform_)-4r73j.md>) instead.

<sub>macOS</sub>

```swift
nonisolated func onPasteCommand<Payload>(of supportedTypes: [String], validator: @escaping ([NSItemProvider]) -> Payload?, perform payloadAction: @escaping (Payload) -> Void) -> some View

```

## Parameters

- `supportedTypes` — The uniform type identifiers that describe the types of content this view can accept through a paste action. If the Clipboard doesn’t contain any of the supported types, the Paste command doesn’t trigger.

- `validator` — A handler that validates the command. This handler receives items from the Clipboard with the types you specify in the `supportedTypes` parameter. Use this handler to decide whether the items are valid and preprocess them for the `action` closure. If you return `nil` instead, the Paste command doesn’t trigger.

- `payloadAction` — The action to perform when the Paste command triggers.

## Return Value

A view that triggers `action` when the system Paste command is invoked, validating the Paste command with `validator`.

## Discussion

Pass an array of uniform type identifiers to the `supportedTypes` parameter. Place the higher priority types closer to the beginning of the array. The Clipboard items that the `validator` closure receives have the most preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer rich text, place the rich text type first in the array. If rich text is available when the paste action occurs, the `validator` closure passes that rich text along.
