---
title: action
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibarbuttonitem/action
source_url: 'https://developer.apple.com/documentation/uikit/uibarbuttonitem/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibarbuttonitem/action.json'
content_hash: 'sha256:e86349a871ee3a25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarButtonItem](../uibarbuttonitem.md)

# action

<sub>Instance Property</sub>

The selector defining the action message to send to the target object when the user taps this bar button item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var action: Selector? { get set }
```

## Discussion

If the value of this property is `nil`, no action message is sent. The default value is `nil`.

## See Also

### Managing the action

- [primaryAction](primaryaction.md) — The action associated with the item.
- [changesSelectionAsPrimaryAction](changesselectionasprimaryaction.md) — A Boolean value that indicates whether the button represents an action or selection.
- [target](target.md) — The object that receives an action when the user selects the item.
