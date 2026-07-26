---
title: 'init(_:isPresented:actions:message:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/alertscene/init(_:ispresented:actions:message:)'
source_url: 'https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:actions:message:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alertscene/init%28_%3Aispresented%3Aactions%3Amessage%3A%29.json'
content_hash: 'sha256:ee64c33b7afdca24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AlertScene](../alertscene.md)

# init(_:isPresented:actions:message:)

<sub>Initializer</sub>

Creates an alert scene with a title, a set of actions, and a message. Note that this creates a text view on your behalf.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, @ContentBuilder actions: () -> Actions, @ContentBuilder message: () -> Message)
```

## Parameters

- `titleResource` — Text resource for the localized string that is the title of the alert.

- `isPresented` — A binding to a Boolean value that determines whether to present the alert. When someone presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the actions for the dialog.

- `message` — A [ContentBuilder](../contentbuilder.md) returning the message for the dialog.
