---
title: enabled
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/textselectability/enabled
source_url: 'https://developer.apple.com/documentation/swiftui/textselectability/enabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/textselectability/enabled.json'
content_hash: 'sha256:042d0c53aa108f89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TextSelectability](../textselectability.md)

# enabled

<sub>Type Property</sub>

A selectability value that enables text selection by a person using your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static var enabled: EnabledTextSelectability { get }
```

## Discussion

Enabling text selection allows people to perform actions on the text content, such as copying and sharing. Enable text selection in views where those operations are useful, such as copying unique IDs or error messages. This allows people to paste the data into emails or documents.

The following example enables text selection on the second of two [Text](../text.md) views in a [VStack](../vstack.md).

```swift
VStack {
    Text("Event Invite")
        .font(.title)
    Text(invite.date.formatted(date: .long, time: .shortened))
        .textSelection(.enabled)
}
```

## See Also

### Getting selectability options

- [disabled](disabled.md) — A selectability value that disables text selection by the person using your app.
