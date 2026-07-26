---
title: 'init(_:isPresented:presenting:actions:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/alertscene/init(_:ispresented:presenting:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:presenting:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alertscene/init%28_%3Aispresented%3Apresenting%3Aactions%3A%29.json'
content_hash: 'sha256:8e3d80c67bdd35fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AlertScene](../alertscene.md)

# init(_:isPresented:presenting:actions:)

<sub>Initializer</sub>

Creates an alert scene, using the given data to produce the alert’s content with a title, and a set of actions. Note that this creates a text view on your behalf.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init<T>(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, presenting data: T?, @ContentBuilder actions: (T) -> Actions) where Message == EmptyView
```

## Parameters

- `titleResource` — The title of the alert.

- `isPresented` — A binding to a Boolean value that determines whether to present the alert. When someone presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.

- `data` — A source of truth that is passed to the alert to populate the message and actions.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the actions for the dialog.
