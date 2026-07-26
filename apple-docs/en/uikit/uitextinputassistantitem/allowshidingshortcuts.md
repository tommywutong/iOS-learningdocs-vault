---
title: allowsHidingShortcuts
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputassistantitem/allowshidingshortcuts
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputassistantitem/allowshidingshortcuts'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputassistantitem/allowshidingshortcuts.json'
content_hash: 'sha256:d19f9aecf89883b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputAssistantItem](../uitextinputassistantitem.md)

# allowsHidingShortcuts

<sub>Instance Property</sub>

A Boolean value that indicates whether the user can hide the shortcuts bar.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var allowsHidingShortcuts: Bool { get set }
```

## Discussion

When the value of this property is [true](../../swift/true.md), the user may hide the shortcuts bar when the keyboard is visible. When the value is [false](../../swift/false.md), the shortcuts bar remains visible while the keyboard is visible. The default value of this property is [true](../../swift/true.md).

## See Also

### Configuring the shortcuts bar

- [leadingBarButtonGroups](leadingbarbuttongroups.md) — The array of button item groups to display before the typing suggestions.
- [trailingBarButtonGroups](trailingbarbuttongroups.md) — The array of button item groups to display after the typing suggestions.
