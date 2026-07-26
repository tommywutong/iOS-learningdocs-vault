---
title: 'init(supportedTypes:validator:payloadAction:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/pastebutton/init(supportedtypes:validator:payloadaction:)'
source_url: 'https://developer.apple.com/documentation/swiftui/pastebutton/init(supportedtypes:validator:payloadaction:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pastebutton/init%28supportedtypes%3Avalidator%3Apayloadaction%3A%29.json'
content_hash: 'sha256:476707c51db7c8cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PasteButton](../pastebutton.md)

# init(supportedTypes:validator:payloadAction:)

<sub>Initializer</sub>

Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app.

> [!warning] Deprecated
> Use the [init(supportedContentTypes:validator:payloadAction:)](<init(supportedcontenttypes_validator_payloadaction_).md>) initializer instead.

<sub>macOS</sub>

```swift
nonisolated init<Payload>(supportedTypes: [String], validator: @escaping ([NSItemProvider]) -> Payload?, payloadAction: @escaping (Payload) -> Void)
```

## Parameters

- `supportedTypes` — The exact uniform type identifiers supported by the button. If the pasteboard doesn’t contain any of the supported types, the button becomes disabled.

- `validator` — A handler that receives those contents of the pasteboard that conform to `payloadAction`. Load and inspect these items to determine whether to validate the button. If you load a valid item, return it from this closure. If the pasteboard doesn’t contain any valid items, return `nil` to invalidate the button.

- `payloadAction` — The handler called when the user clicks the button. This closure receives the preprocessed result of `validator`.

## Discussion

Set the contents of `supportedTypes` in order of your app’s preference for its supported types. The Paste button takes the most-preferred type that the pasteboard source supports and delivers this to the `validator` closure.

## See Also

### Deprecated initializers

- [init(supportedTypes:payloadAction:)](<init(supportedtypes_payloadaction_).md>) — Creates a Paste button that accepts specific types of data from the pasteboard. _(deprecated)_
- [init(supportedContentTypes:validator:payloadAction:)](<init(supportedcontenttypes_validator_payloadaction_).md>) — Creates a Paste button that accepts specific types of data from the pasteboard, performing a custom validation of the data before sending it to your app. _(deprecated)_
