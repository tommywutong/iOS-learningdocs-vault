---
title: 'insertSibling(_:afterMenu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertsibling(_:aftermenu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertsibling(_:aftermenu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertsibling%28_%3Aaftermenu%3A%29.json'
content_hash: 'sha256:844a78bfeb5e210f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertSibling(_:afterMenu:)

<sub>Instance Method</sub>

Inserts a sibling menu after the specified menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertSibling(_ siblingMenu: UIMenu, afterMenu siblingIdentifier: UIMenu.Identifier)
```

## Parameters

- `siblingMenu` — The sibling menu to insert.

- `siblingIdentifier` — The identifier of the menu that comes before the inserted sibling menu.

## See Also

### Inserting sibling menus

- [- insertSiblingMenu:beforeMenuForIdentifier:](<insertsibling(__beforemenu_).md>) — Inserts a sibling menu before the specified menu.
