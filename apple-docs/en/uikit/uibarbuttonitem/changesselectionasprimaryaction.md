---
title: changesSelectionAsPrimaryAction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/changesselectionasprimaryaction
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/changesselectionasprimaryaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/changesselectionasprimaryaction.json'
content_hash: 'sha256:5d47ce171c1d098d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# changesSelectionAsPrimaryAction

<sub>Instance Property</sub>

A Boolean value that indicates whether the button represents an action or selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var changesSelectionAsPrimaryAction: Bool { get set }
```

## Discussion

When a button has this property set to [true](../../swift/true.md), the button changes to a toggle button where tapping it changes it between selected and unselected.

## See Also

### Managing the action

- [primaryAction](primaryaction.md) — The action associated with the item.
- [action](action.md) — The selector defining the action message to send to the target object when the user taps this bar button item.
- [target](target.md) — The object that receives an action when the user selects the item.
