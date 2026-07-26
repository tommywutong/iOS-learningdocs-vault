---
title: 'menuWithTitle:image:identifier:options:children:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenu/menuwithtitle:image:identifier:options:children:'
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/menuwithtitle:image:identifier:options:children:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/menuwithtitle%3Aimage%3Aidentifier%3Aoptions%3Achildren%3A.json'
content_hash: 'sha256:ac5a20ecf530be4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenu](../uimenu.md)

# menuWithTitle:image:identifier:options:children:

<sub>Type Method</sub>

Creates a new menu with the specified values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIMenu *) menuWithTitle:(NSString *) title image:(UIImage *) image identifier:(UIMenuIdentifier) identifier options:(UIMenuOptions) options children:(NSArray<UIMenuElement *> *) children;
```

## Parameters

- `title` — The title of the menu.

- `image` — The image to display next to the menu’s title.

- `identifier` — The unique identifier for the menu. When creating standard menus for your app, specify an appropriate constant defined in [Identifier](identifier-swift.struct.md). For custom menus, specify a custom reverse domain name value, or specify `nil` to let this method create a unique identifier for you.

- `options` — Additional configuration options for the menu. For a list of possible values, see [Options](options-swift.struct.md).

- `children` — The menu elements in the menu. Specify leaf menu elements using [UIMenuElement](../uimenuelement.md) subclasses like [UIAction](../uiaction.md), [UICommand](../uicommand.md), or [UIKeyCommand](../uikeycommand.md), and specify submenus using [UIMenu](../uimenu.md) objects. You may specify an empty array if the menu has no child menu elements.

## Return Value

A new menu object containing the specified menu elements.

## See Also

### Creating a menu object

- [menuWithChildren:](menuwithchildren_.md) — Creates a new menu with the specified child elements.
- [menuWithTitle:children:](menuwithtitle_children_.md) — Creates a menu with the specified title and child menu elements.
- [Identifier](identifier-swift.struct.md) — Constants you use to identify an app’s standard menus.
- [Options](options-swift.struct.md) — Options you use to configure a menu’s appearance.
- [- initWithCoder:](<init(coder_).md>) — Creates a menu from data in an unarchiver.
