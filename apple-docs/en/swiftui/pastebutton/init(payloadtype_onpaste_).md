---
title: 'init(payloadType:onPaste:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/pastebutton/init(payloadtype:onpaste:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pastebutton/init(payloadtype:onpaste:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pastebutton/init%28payloadtype%3Aonpaste%3A%29.json'
content_hash: 'sha256:d46d0660586b9f8a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PasteButton](../pastebutton.md)

# init(payloadType:onPaste:)

<sub>Initializer</sub>

Creates an instance that accepts values of the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init<T>(payloadType: T.Type, onPaste: @escaping ([T]) -> Void) where T : Transferable
```

## Parameters

- `onPaste` — The handler to call on trigger of the button with at least one item of the specified `Transferable` type from the pasteboard.

## See Also

### Creating a paste button

- [init(supportedContentTypes:payloadAction:)](<init(supportedcontenttypes_payloadaction_).md>) — Creates a Paste button that accepts specific types of data from the pasteboard.
