---
title: 'menuWithTitle:children:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenu/menuwithtitle:children:'
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/menuwithtitle:children:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/menuwithtitle%3Achildren%3A.json'
content_hash: 'sha256:36f15ff2658728fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenu](../uimenu.md)

# menuWithTitle:children:

<sub>Type Method</sub>

Creates a menu with the specified title and child menu elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIMenu *) menuWithTitle:(NSString *) title children:(NSArray<UIMenuElement *> *) children;
```

## Parameters

- `title` — The title of the menu.

- `children` — The menu elements in the menu. Specify leaf menu elements using [UIMenuElement](../uimenuelement.md) subclasses like [UIAction](../uiaction.md), [UICommand](../uicommand.md), or [UIKeyCommand](../uikeycommand.md), and specify submenus using [UIMenu](../uimenu.md) objects. You may specify an empty array if the menu has no child menu elements.

## Return Value

A new menu object.

## Discussion

This method creates a unique identifier for the menu and exposes that value from the [identifier](identifier-swift.property.md) property.

## See Also

### Creating a menu object

- [menuWithChildren:](menuwithchildren_.md) — Creates a new menu with the specified child elements.
- [menuWithTitle:image:identifier:options:children:](menuwithtitle_image_identifier_options_children_.md) — Creates a new menu with the specified values.
- [Identifier](identifier-swift.struct.md) — Constants you use to identify an app’s standard menus.
- [Options](options-swift.struct.md) — Options you use to configure a menu’s appearance.
- [- initWithCoder:](<init(coder_).md>) — Creates a menu from data in an unarchiver.
