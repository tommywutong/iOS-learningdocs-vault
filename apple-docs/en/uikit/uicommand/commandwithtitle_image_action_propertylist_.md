---
title: 'commandWithTitle:image:action:propertyList:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicommand/commandwithtitle:image:action:propertylist:'
source_url: 'https://developer.apple.com/documentation/uikit/uicommand/commandwithtitle:image:action:propertylist:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicommand/commandwithtitle%3Aimage%3Aaction%3Apropertylist%3A.json'
content_hash: 'sha256:1d3e60fa1869522c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICommand](../uicommand.md)

# commandWithTitle:image:action:propertyList:

<sub>Type Method</sub>

Creates a command with the specified title, image, action, and property list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) commandWithTitle:(NSString *) title image:(UIImage *) image action:(SEL) action propertyList:(id) propertyList;
```

## Parameters

- `title` — The title to display for the command.

- `image` — The image to display next to the command’s title. Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

- `action` — The action to take after a person selects the command.

- `propertyList` — An object that contains data to associate with the command.

## Return Value

A newly initialized command object.

## See Also

### Creating a command

- [commandWithTitle:image:action:propertyList:alternates:](commandwithtitle_image_action_propertylist_alternates_.md) — Creates a command with the specified title, image, action, property list, and alternative commands.
- [- initWithCoder:](<init(coder_).md>) — Creates a command from data in an unarchiver.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
