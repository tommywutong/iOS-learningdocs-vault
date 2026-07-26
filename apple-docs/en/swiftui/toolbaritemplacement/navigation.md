---
title: navigation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/navigation
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/navigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/navigation.json'
content_hash: 'sha256:7e0788a6fbba4d7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# navigation

<sub>Type Property</sub>

A placement for navigation actions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let navigation: ToolbarItemPlacement
```

## Discussion

Navigation actions allow the user to move between contexts. For example, the forward and back buttons of a web browser are navigation actions.

In macOS and in Mac Catalyst apps, the system places navigation items in the leading edge of the toolbar ahead of the inline title if that is present in the toolbar.

In iOS, iPadOS, and tvOS, navigation items appear in the leading edge of the navigation bar. If a system navigation item such as a back button is present in a compact width, it instead appears in the [primaryAction](primaryaction.md) placement.

## See Also

### Getting placement for specific actions

- [primaryAction](primaryaction.md) — A placement for the primary action.
- [secondaryAction](secondaryaction.md) — A placement for secondary actions.
- [confirmationAction](confirmationaction.md) — A placement for confirmation actions in a modal interface.
- [cancellationAction](cancellationaction.md) — A placement for cancellation actions in a modal interface.
- [destructiveAction](destructiveaction.md) — A placement for destructive actions in a modal interface.
