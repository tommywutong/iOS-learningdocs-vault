---
title: 'remove(menu:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/remove(menu:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/remove(menu:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/remove%28menu%3A%29.json'
content_hash: 'sha256:a64561072c4ed92b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# remove(menu:)

<sub>Instance Method</sub>

Removes a menu from the menu system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func remove(menu removedIdentifier: UIMenu.Identifier)
```

## Parameters

- `removedIdentifier` — The identifier of the menu element to remove.

## Discussion

Use this method to remove menus ([UIMenu](../uimenu.md) objects) from a menu system.
