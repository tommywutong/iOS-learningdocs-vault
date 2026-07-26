---
title: 'init(content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/controlgroup/init(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroup/init(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroup/init%28content%3A%29.json'
content_hash: 'sha256:a397abedb665aa57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroup](../controlgroup.md)

# init(content:)

<sub>Initializer</sub>

Creates a new ControlGroup with the specified children

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated init(@ContentBuilder content: () -> Content)
```

## Parameters

- `content` — The children to display

## See Also

### Creating a control group

- [init(content:label:)](<init(content_label_).md>) — Creates a new control group with the specified content and a label.
- [init(_:content:)](<init(__content_).md>) — Creates a new control group with the specified content that generates its label from a string.
