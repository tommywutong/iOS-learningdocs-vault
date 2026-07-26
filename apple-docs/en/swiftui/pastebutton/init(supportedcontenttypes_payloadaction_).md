---
title: 'init(supportedContentTypes:payloadAction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/pastebutton/init(supportedcontenttypes:payloadaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pastebutton/init(supportedcontenttypes:payloadaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pastebutton/init%28supportedcontenttypes%3Apayloadaction%3A%29.json'
content_hash: 'sha256:9cbd33534f652ae2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PasteButton](../pastebutton.md)

# init(supportedContentTypes:payloadAction:)

<sub>Initializer</sub>

Creates a Paste button that accepts specific types of data from the pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(supportedContentTypes: [UTType], payloadAction: @escaping ([NSItemProvider]) -> Void)
```

## Parameters

- `supportedContentTypes` — The exact uniform type identifiers supported by the button. If the pasteboard doesn’t contain any of the supported types, the button becomes disabled.

- `payloadAction` — The handler to call when the user clicks the Paste button and the pasteboard has items that conform to `supportedContentTypes`. This closure receives an array of item providers that you use to inspect and load the pasteboard data.

## Discussion

Set the contents of `supportedContentTypes` in order of your app’s preference for its supported types. The Paste button takes the most-preferred type that the pasteboard source supports and delivers this to the `payloadAction` closure.

## See Also

### Creating a paste button

- [init(payloadType:onPaste:)](<init(payloadtype_onpaste_).md>) — Creates an instance that accepts values of the specified type.
