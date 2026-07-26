---
title: target
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/target
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/target'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/target.json'
content_hash: 'sha256:c1452894c9d7f858'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# target

<sub>Instance Property</sub>

The object that receives an action when the user selects the item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var target: AnyObject? { get set }
```

## Discussion

If `nil`, the action message is passed up the responder chain where it may be handled by any object implementing a method corresponding to the selector held by the [action](action.md) property. The default value is `nil`.

## See Also

### Managing the action

- [primaryAction](primaryaction.md) — The action associated with the item.
- [changesSelectionAsPrimaryAction](changesselectionasprimaryaction.md) — A Boolean value that indicates whether the button represents an action or selection.
- [action](action.md) — The selector defining the action message to send to the target object when the user taps this bar button item.
