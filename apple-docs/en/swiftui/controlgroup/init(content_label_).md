---
title: 'init(content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlgroup/init(content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroup/init(content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroup/init%28content%3Alabel%3A%29.json'
content_hash: 'sha256:03063dde81447a34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroup](../controlgroup.md)

# init(content:label:)

<sub>Initializer</sub>

Creates a new control group with the specified content and a label.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated init<C, L>(@ContentBuilder content: () -> C, @ContentBuilder label: () -> L) where Content == LabeledControlGroupContent<C, L>, C : View, L : View
```

## Parameters

- `content` — The content to display.

- `label` — A view that describes the purpose of the group.

## See Also

### Creating a control group

- [init(content:)](<init(content_).md>) — Creates a new ControlGroup with the specified children
- [init(_:content:)](<init(__content_).md>) — Creates a new control group with the specified content that generates its label from a string.
