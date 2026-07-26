---
title: 'insertSibling(_:beforeMenu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertsibling(_:beforemenu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertsibling(_:beforemenu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertsibling%28_%3Abeforemenu%3A%29.json'
content_hash: 'sha256:f96d105665015716'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertSibling(_:beforeMenu:)

<sub>Instance Method</sub>

Inserts a sibling menu before the specified menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertSibling(_ siblingMenu: UIMenu, beforeMenu siblingIdentifier: UIMenu.Identifier)
```

## Parameters

- `siblingMenu` — The sibling menu to insert.

- `siblingIdentifier` — The identifier of the menu that comes after the inserted sibling menu.

## See Also

### Inserting sibling menus

- [- insertSiblingMenu:afterMenuForIdentifier:](<insertsibling(__aftermenu_).md>) — Inserts a sibling menu after the specified menu.
