---
title: leadingBarButtonGroups
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputassistantitem/leadingbarbuttongroups
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputassistantitem/leadingbarbuttongroups'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputassistantitem/leadingbarbuttongroups.json'
content_hash: 'sha256:fc839ad5f179d660'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputAssistantItem](../uitextinputassistantitem.md)

# leadingBarButtonGroups

<sub>Instance Property</sub>

The array of button item groups to display before the typing suggestions.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var leadingBarButtonGroups: [UIBarButtonItemGroup] { get set }
```

## Discussion

Assigning a value to this property installs the corresponding bar button items so that they lead the typing suggestions. (In a left-to-right environment, leading items are placed to the left of the typing suggestions.) If there is not enough room to display all of the items, UIKit may display a group’s representative item instead, if one was provided.

## See Also

### Configuring the shortcuts bar

- [trailingBarButtonGroups](trailingbarbuttongroups.md) — The array of button item groups to display after the typing suggestions.
- [allowsHidingShortcuts](allowshidingshortcuts.md) — A Boolean value that indicates whether the user can hide the shortcuts bar.
