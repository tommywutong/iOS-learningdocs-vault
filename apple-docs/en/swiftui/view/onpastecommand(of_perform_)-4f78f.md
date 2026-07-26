---
title: 'onPasteCommand(of:perform:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/onpastecommand(of:perform:)-4f78f'
source_url: 'https://developer.apple.com/documentation/swiftui/view/onpastecommand(of:perform:)-4f78f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/onpastecommand%28of%3Aperform%3A%29-4f78f.json'
content_hash: 'sha256:eac552cb5d2a12da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# onPasteCommand(of:perform:)

<sub>Instance Method</sub>

Adds an action to perform in response to the system’s Paste command.

> [!warning] Deprecated
> Use [onPasteCommand(of:perform:)](<onpastecommand(of_perform_)-9s227.md>) instead.

<sub>macOS</sub>

```swift
nonisolated func onPasteCommand(of supportedTypes: [String], perform payloadAction: @escaping ([NSItemProvider]) -> Void) -> some View

```

## Parameters

- `supportedTypes` — The uniform type identifiers that describe the types of content this view can accept through a paste action. If the Clipboard doesn’t contain any of the supported types, the Paste command doesn’t trigger.

- `payloadAction` — The action to perform when the Paste command triggers. The action closure’s parameter contains items from the Clipboard with the types you specify in the `supportedTypes` parameter.

## Return Value

A view that triggers `action` when a system Paste command occurs.

## Discussion

Pass an array of uniform type identifiers to the `supportedTypes` parameter. Place the higher priority types closer to the beginning of the array. The Clipboard items that the `action` closure receives have the most preferred type out of all the types the source supports.

For example, if your app can handle plain text and rich text, but you prefer rich text, place the rich text type first in the array. If rich text is available when the paste action occurs, the `action` closure passes that rich text along.
