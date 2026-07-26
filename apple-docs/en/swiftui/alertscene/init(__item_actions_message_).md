---
title: 'init(_:item:actions:message:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/alertscene/init(_:item:actions:message:)'
source_url: 'https://developer.apple.com/documentation/swiftui/alertscene/init(_:item:actions:message:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alertscene/init%28_%3Aitem%3Aactions%3Amessage%3A%29.json'
content_hash: 'sha256:73810b408d2cd27e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AlertScene](../alertscene.md)

# init(_:item:actions:message:)

<sub>Initializer</sub>

Creates an alert scene, using the given data to produce the alert’s content with a title, a set of actions, and a message. Note that this creates a text view on your behalf.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init<S, T>(_ title: S, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions, @ContentBuilder message: (T) -> Message) where S : StringProtocol
```

## Parameters

- `title` — A text string used as the title of the alert.

- `data` — A binding to optional source of truth for the alert. The system presents the alert when the binding’s value is non-nil. When someone presses or taps one of the alert’s actions, the system sets this value to `nil` and dismisses. The system passes the contents to the alert to populate the message and actions.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the actions for the dialog.

- `message` — A [ContentBuilder](../contentbuilder.md) returning the message for the dialog.
