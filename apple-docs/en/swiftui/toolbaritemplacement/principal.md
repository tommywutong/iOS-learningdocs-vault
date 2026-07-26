---
title: principal
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/principal
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/principal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/principal.json'
content_hash: 'sha256:8ad83588337d9ea9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# principal

<sub>Type Property</sub>

A placement for the principal item section.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let principal: ToolbarItemPlacement
```

## Discussion

Principal actions are key units of functionality that receive prominent placement. For example, the location field for a web browser is a principal item.

In macOS and in Mac Catalyst apps, the system places the principal item in the center of the toolbar.

In iOS, iPadOS, and tvOS, the system places the principal item in the center of the navigation bar. This item takes precedent over a title specified through `View/navigationTitle`.

## See Also

### Getting semantic placement

- [automatic](automatic.md) — A placement the system positions automatically.
- [status](status.md) — A placement for items that represents a change in status.
