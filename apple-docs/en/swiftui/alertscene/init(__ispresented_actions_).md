---
title: 'init(_:isPresented:actions:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/alertscene/init(_:ispresented:actions:)'
source_url: 'https://developer.apple.com/documentation/swiftui/alertscene/init(_:ispresented:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/alertscene/init%28_%3Aispresented%3Aactions%3A%29.json'
content_hash: 'sha256:e3ab59b7b1b5652a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [AlertScene](../alertscene.md)

# init(_:isPresented:actions:)

<sub>Initializer</sub>

Creates an alert scene with a title and a set of actions. Note that this creates a text view on your behalf.

<sub>macOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, isPresented: Binding<Bool>, @ContentBuilder actions: () -> Actions) where Message == EmptyView
```

## Parameters

- `titleResource` — Text resource for the localized string that is the title of the alert.

- `isPresented` — A binding to a Boolean value that determines whether to present the alert. When someone presses or taps one of the alert’s actions, the system sets this value to `false` and dismisses.

- `actions` — A [ContentBuilder](../contentbuilder.md) returning the actions for the dialog.
