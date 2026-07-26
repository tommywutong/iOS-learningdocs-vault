---
title: primaryAction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/primaryaction
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/primaryaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/primaryaction.json'
content_hash: 'sha256:eb7977b016306fb7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# primaryAction

<sub>Type Property</sub>

A placement for the primary action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let primaryAction: ToolbarItemPlacement
```

## Discussion

A primary action is a more frequently used action for the current context. For example, a button the user clicks or taps to compose a new message in a chat app.

In macOS and in Mac Catalyst apps, the location for the primary action is the leading edge of the toolbar.

In iOS, iPadOS, and tvOS, the location for the primary action is the trailing edge of the navigation bar.

In watchOS the system places the primary action beneath the navigation bar; the user reveals the action by scrolling.

## See Also

### Getting placement for specific actions

- [secondaryAction](secondaryaction.md) — A placement for secondary actions.
- [confirmationAction](confirmationaction.md) — A placement for confirmation actions in a modal interface.
- [cancellationAction](cancellationaction.md) — A placement for cancellation actions in a modal interface.
- [destructiveAction](destructiveaction.md) — A placement for destructive actions in a modal interface.
- [navigation](navigation.md) — A placement for navigation actions.
