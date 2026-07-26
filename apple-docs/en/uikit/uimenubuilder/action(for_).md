---
title: 'action(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/action(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/action(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/action%28for%3A%29.json'
content_hash: 'sha256:9a381c327a880a0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# action(for:)

<sub>Instance Method</sub>

Gets the action for the specified action identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func action(for identifier: UIAction.Identifier) -> UIAction?
```

## Parameters

- `identifier` — The identifier of the action to retrieve.

## Return Value

An action object; otherwise, `nil` if there are no actions with the specified identifier.

## See Also

### Getting menu systems and elements

- [system](system.md) — The menu system that the menu builder modifies.
- [- menuForIdentifier:](<menu(for_).md>) — Gets the menu for the specified menu identifier.
- [command(for:propertyList:)](<command(for_propertylist_).md>) — Gets the command for the specified selector and property list.
