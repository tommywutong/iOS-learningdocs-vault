---
title: destructiveAction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/destructiveaction
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/destructiveaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/destructiveaction.json'
content_hash: 'sha256:47323957008fa6d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# destructiveAction

<sub>Type Property</sub>

A placement for destructive actions in a modal interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let destructiveAction: ToolbarItemPlacement
```

## Discussion

Destructive actions represent the opposite of a confirmation action. For example, a button labeled “Don’t Save” that allows the user to discard unsaved changes to a document before quitting.

In macOS and in Mac Catalyst apps, the system places `destructiveAction` items in the leading edge of the sheet and gives them a special appearance to caution against accidental use.

In iOS, tvOS, and watchOS, the system places `destructiveAction` items in the trailing edge of the navigation bar.

## See Also

### Getting placement for specific actions

- [primaryAction](primaryaction.md) — A placement for the primary action.
- [secondaryAction](secondaryaction.md) — A placement for secondary actions.
- [confirmationAction](confirmationaction.md) — A placement for confirmation actions in a modal interface.
- [cancellationAction](cancellationaction.md) — A placement for cancellation actions in a modal interface.
- [navigation](navigation.md) — A placement for navigation actions.
