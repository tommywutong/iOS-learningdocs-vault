---
title: 'init(_:item:actions:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/alertscene/init(_:item:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/alertscene/init(_:item:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alertscene/init%28_%3Aitem%3Aactions%3A%29.json'
content_hash: 'sha256:451ffa1295195294'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AlertScene](../alertscene.md)

# init(_:item:actions:)

<sub>Initializer</sub>

Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions. Note that this creates a text view on your behalf.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init<S, T>(_ title: S, item data: Binding<T?>, @ContentBuilder actions: (T) -> Actions) where Message == EmptyView, S : StringProtocol
```

## Parameters

- `title` — The title of the alert.

- `data` — A binding to optional source of truth for the alert. The system presents the alert when the binding’s value is non-nil. When someone presses or taps one of the alert’s actions, the system sets this value to `nil` and dismisses. The system passes the contents to the alert to populate the message and actions.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the actions for the dialog.
