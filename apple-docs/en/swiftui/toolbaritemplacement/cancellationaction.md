---
title: cancellationAction
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/toolbaritemplacement/cancellationaction
source_url: 'https://developer.apple.com/documentation/swiftui/toolbaritemplacement/cancellationaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/toolbaritemplacement/cancellationaction.json'
content_hash: 'sha256:aa268daf6b7ea206'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToolbarItemPlacement](../toolbaritemplacement.md)

# cancellationAction

<sub>Type Property</sub>

A placement for cancellation actions in a modal interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let cancellationAction: ToolbarItemPlacement
```

## Discussion

Cancellation actions dismiss the modal interface without taking any action, usually by tapping or clicking a Cancel button.

In macOS and in Mac Catalyst apps, the system places `cancellationAction` items on the trailing edge of the sheet but places them before any [confirmationAction](confirmationaction.md) items.

In iOS, iPadOS, tvOS, and watchOS, the system places `cancellationAction` items on the leading edge of the navigation bar.

## See Also

### Getting placement for specific actions

- [primaryAction](primaryaction.md) — A placement for the primary action.
- [secondaryAction](secondaryaction.md) — A placement for secondary actions.
- [confirmationAction](confirmationaction.md) — A placement for confirmation actions in a modal interface.
- [destructiveAction](destructiveaction.md) — A placement for destructive actions in a modal interface.
- [navigation](navigation.md) — A placement for navigation actions.
