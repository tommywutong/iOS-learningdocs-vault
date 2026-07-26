---
title: 'menu(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/menu(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/menu(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/menu%28for%3A%29.json'
content_hash: 'sha256:c24a326f60a73b47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# menu(for:)

<sub>Instance Method</sub>

Gets the menu for the specified menu identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func menu(for identifier: UIMenu.Identifier) -> UIMenu?
```

## Parameters

- `identifier` — The identifier of the menu to retrieve.

## Return Value

A menu object; otherwise, `nil` if there are no menus with the specified identifier.

## See Also

### Getting menu systems and elements

- [system](system.md) — The menu system that the menu builder modifies.
- [- actionForIdentifier:](<action(for_).md>) — Gets the action for the specified action identifier.
- [command(for:propertyList:)](<command(for_propertylist_).md>) — Gets the command for the specified selector and property list.
