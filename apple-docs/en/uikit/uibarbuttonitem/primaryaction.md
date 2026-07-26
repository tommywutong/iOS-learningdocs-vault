---
title: primaryAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/primaryaction
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/primaryaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/primaryaction.json'
content_hash: 'sha256:72bed8f914bfde2a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# primaryAction

<sub>Instance Property</sub>

The action associated with the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var primaryAction: UIAction? { get set }
```

## Discussion

When you assign a new value to this property, the title and image of the item update to match the primary action’s [title](../uiaction/title.md) and [image](../uiaction/image.md).

If this property has a non-`nil` value, the system ignores the item’s [target](target.md) and [action](action.md) properties.

## See Also

### Managing the action

- [changesSelectionAsPrimaryAction](changesselectionasprimaryaction.md) — A Boolean value that indicates whether the button represents an action or selection.
- [action](action.md) — The selector defining the action message to send to the target object when the user taps this bar button item.
- [target](target.md) — The object that receives an action when the user selects the item.
