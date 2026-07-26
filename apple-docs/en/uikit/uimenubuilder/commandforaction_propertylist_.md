---
title: 'commandForAction:propertyList:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenubuilder/commandforaction:propertylist:'
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/commandforaction:propertylist:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/commandforaction%3Apropertylist%3A.json'
content_hash: 'sha256:3ab93a56fffbd528'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# commandForAction:propertyList:

<sub>Instance Method</sub>

Gets the command for the specified selector and property list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (UICommand *) commandForAction:(SEL) action propertyList:(id) propertyList;
```

## Parameters

- `action` — The selector of the command to retrieve.

- `propertyList` — The property list object that distinguish the command.

## Return Value

A command object; otherwise, `nil` if there is no such command.

## See Also

### Getting menu systems and elements

- [system](system.md) — The menu system that the menu builder modifies.
- [- menuForIdentifier:](<menu(for_).md>) — Gets the menu for the specified menu identifier.
- [- actionForIdentifier:](<action(for_).md>) — Gets the action for the specified action identifier.
