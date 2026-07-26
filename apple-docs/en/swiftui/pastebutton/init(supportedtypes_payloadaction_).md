---
title: 'init(supportedTypes:payloadAction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/pastebutton/init(supportedtypes:payloadaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pastebutton/init(supportedtypes:payloadaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pastebutton/init%28supportedtypes%3Apayloadaction%3A%29.json'
content_hash: 'sha256:2ec6439e530a69ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PasteButton](../pastebutton.md)

# init(supportedTypes:payloadAction:)

<sub>Initializer</sub>

Creates a Paste button that accepts specific types of data from the pasteboard.

> [!warning] Deprecated
> Use the [init(supportedContentTypes:payloadAction:)](<init(supportedcontenttypes_payloadaction_).md>) initializer instead.

<sub>macOS</sub>

```swift
nonisolated init(supportedTypes: [String], payloadAction: @escaping ([NSItemProvider]) -> Void)
```

## Parameters

- `supportedTypes` — The exact uniform type identifiers supported by the button. If the pasteboard doesn’t contain any of the supported types, the button becomes disabled.

- `payloadAction` — The handler to call when the user clicks the Paste button, and the pasteboard has items that conform to `supportedTypes`. This closure receives an array of item providers that you use to inspect and load the pasteboard data.

## Discussion

Set the contents of `supportedTypes` in order of your app’s preference for its supported types. The Paste button takes the most-preferred type that the pasteboard source supports and delivers this to the `payloadAction` closure.

## See Also

### Deprecated initializers

- [init(supportedTypes:validator:payloadAction:)](<init(supportedtypes_validator_payloadaction_).md>) — Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app. _(deprecated)_
- [init(supportedContentTypes:validator:payloadAction:)](<init(supportedcontenttypes_validator_payloadaction_).md>) — Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app. _(deprecated)_
