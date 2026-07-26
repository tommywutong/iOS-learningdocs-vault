---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/automatic.json'
content_hash: 'sha256:9f52abc9e14d616c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# automatic

<sub>Type Property</sub>

A placement the system positions automatically.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let automatic: ToolbarItemPlacement
```

## Discussion

In macOS and in Mac Catalyst apps, the system places items in the current toolbar section in order of leading to trailing. On watchOS, only the first item appears, pinned beneath the navigation bar.

In iPadOS, the system places items in the center of the navigation bar if the navigation bar supports customization. Otherwise, it places items in the trailing position of the navigation bar.

In iOS, and tvOS, the system places items in the trailing position of the navigation bar.

In iOS, iPadOS, and macOS, the system uses the space available to the toolbar when determining how many items to render in the toolbar. If not all items fit in the available space, an overflow menu may be created and remaining items placed in that menu.

## See Also

### Getting semantic placement

- [principal](principal.md) — A placement for the principal item section.
- [status](status.md) — A placement for items that represents a change in status.
