---
title: allowsTypeSelect
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uicontextmenuconfiguration/allowstypeselect
source_url: 'https://developer.apple.com/documentation/uikit/uicontextmenuconfiguration/allowstypeselect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontextmenuconfiguration/allowstypeselect.json'
content_hash: 'sha256:c7a8590a534c3930'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContextMenuConfiguration](../uicontextmenuconfiguration.md)

# allowsTypeSelect

<sub>Instance Property</sub>

A Boolean value that indicates whether the context menu supports keystroke-based navigation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var allowsTypeSelect: Bool { get set }
```

## Discussion

TypeSelect lets users move focus to a matching menu option by typing on a hardware keyboard while the menu is open. When a context menu appears alongside a text field that actively receives keyboard input, TypeSelect can intercept keystrokes before they reach the text field.

Set this property to [false](../../swift/false.md) when the menu serves as a companion to an active text input, such as a suggestion menu or autocomplete picker. This allows keyboard input to flow to the text field without being captured by the menu’s navigation.

The default value is [true](../../swift/true.md).
