---
title: search
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbardefaultitemkind/search
source_url: 'https://developer.apple.com/documentation/swiftui/toolbardefaultitemkind/search'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbardefaultitemkind/search.json'
content_hash: 'sha256:010fee2c082d1f20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarDefaultItemKind](../toolbardefaultitemkind.md)

# search

<sub>Type Property</sub>

The search item added by a `View/searchable(text:isPresented:placement:prompt)` modifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let search: ToolbarDefaultItemKind
```

## Discussion

Use a `.search` default item kind with `DefaultToolbarItem/init(kind:placment:)` to customize the [ToolbarItemPlacement](../toolbaritemplacement.md) of a default item kind. The search default item kind can be placed in the `.bottomBar` on iPhone only. All available platforms support `.topBarTrailing` and `.automatic`.
