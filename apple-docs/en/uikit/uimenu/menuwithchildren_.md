---
title: 'menuWithChildren:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenu/menuwithchildren:'
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/menuwithchildren:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/menuwithchildren%3A.json'
content_hash: 'sha256:4e013e49a595586e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenu](../uimenu.md)

# menuWithChildren:

<sub>Type Method</sub>

Creates a new menu with the specified child elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (UIMenu *) menuWithChildren:(NSArray<UIMenuElement *> *) children;
```

## Parameters

- `children` — The menu elements in the menu. Specify leaf menu elements using [UIMenuElement](../uimenuelement.md) subclasses like [UIAction](../uiaction.md), [UICommand](../uicommand.md), or [UIKeyCommand](../uikeycommand.md), and specify submenus using [UIMenu](../uimenu.md) objects. You may specify an empty array if the menu has no child menu elements.

## See Also

### Creating a menu object

- [menuWithTitle:children:](menuwithtitle_children_.md) — Creates a menu with the specified title and child menu elements.
- [menuWithTitle:image:identifier:options:children:](menuwithtitle_image_identifier_options_children_.md) — Creates a new menu with the specified values.
- [Identifier](identifier-swift.struct.md) — Constants you use to identify an app’s standard menus.
- [Options](options-swift.struct.md) — Options you use to configure a menu’s appearance.
- [- initWithCoder:](<init(coder_).md>) — Creates a menu from data in an unarchiver.
