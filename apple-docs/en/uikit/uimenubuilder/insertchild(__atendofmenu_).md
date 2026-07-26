---
title: 'insertChild(_:atEndOfMenu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/insertchild(_:atendofmenu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/insertchild(_:atendofmenu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/insertchild%28_%3Aatendofmenu%3A%29.json'
content_hash: 'sha256:da9932f77c59990a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# insertChild(_:atEndOfMenu:)

<sub>Instance Method</sub>

Adds a child menu as the last element of the specified parent menu.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func insertChild(_ childMenu: UIMenu, atEndOfMenu parentIdentifier: UIMenu.Identifier)
```

## Parameters

- `childMenu` — The child menu to insert.

- `parentIdentifier` — The identifier of the parent menu in which to insert the child menu.

## See Also

### Inserting child menus

- [- insertChildMenu:atStartOfMenuForIdentifier:](<insertchild(__atstartofmenu_).md>) — Adds a child menu as the first element of the specified parent menu.
