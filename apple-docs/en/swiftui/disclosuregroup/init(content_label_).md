---
title: 'init(content:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/disclosuregroup/init(content:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/disclosuregroup/init(content:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/disclosuregroup/init%28content%3Alabel%3A%29.json'
content_hash: 'sha256:c067fe7869abe348'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DisclosureGroup](../disclosuregroup.md)

# init(content:label:)

<sub>Initializer</sub>

Creates a disclosure group with the given label and content views.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(@ContentBuilder content: @escaping () -> Content, @ContentBuilder label: () -> Label)
```

## Parameters

- `content` — The content shown when the disclosure group expands.

- `label` — A view that describes the content of the disclosure group.

## See Also

### Creating a disclosure group

- [init(_:content:)](<init(__content_).md>) — Creates a disclosure group, using a provided localized string resource to create a text view for the label.
- [init(_:isExpanded:content:)](<init(__isexpanded_content_).md>) — Creates a disclosure group, using a provided localized string resource to create a text view for the label, and a binding to the expansion state (expanded or collapsed).
- [init(isExpanded:content:label:)](<init(isexpanded_content_label_).md>) — Creates a disclosure group with the given label and content views, and a binding to the expansion state (expanded or collapsed).
