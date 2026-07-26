---
title: 'commandWithTitle:image:action:input:modifierFlags:propertyList:alternates:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uikeycommand/commandwithtitle:image:action:input:modifierflags:propertylist:alternates:'
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/commandwithtitle:image:action:input:modifierflags:propertylist:alternates:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/commandwithtitle%3Aimage%3Aaction%3Ainput%3Amodifierflags%3Apropertylist%3Aalternates%3A.json'
content_hash: 'sha256:a4412acb2fd1eaf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# commandWithTitle:image:action:input:modifierFlags:propertyList:alternates:

<sub>Type Method</sub>

Creates a key command with alternatives that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) commandWithTitle:(NSString *) title image:(UIImage *) image action:(SEL) action input:(NSString *) input modifierFlags:(UIKeyModifierFlags) modifierFlags propertyList:(id) propertyList alternates:(NSArray<UICommandAlternate *> *) alternates;
```

## Parameters

- `title` — The title to display for the key command.

- `image` — The image to display next to the key command’s title. Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of an image, and only when the app runs in iOS.

- `action` — The action to take after a person selects the key command.

- `input` — The keys that a person must press. The string must contain one or more characters corresponding to the keys a person pressed. For a list of special characters that don’t have a textual representation, see [Input strings for special keys](../input-strings-for-special-keys.md).

- `modifierFlags` — The bit mask of modifier keys that a person must press. You can use this parameter to specify which modifier keys (Command, Option, and so on) a person must also press. You may specify more than one modifier key. For a list of possible values, see [UIKeyModifierFlags](../uikeymodifierflags.md).

- `propertyList` — An object that contains data to associate with the key command.

- `alternates` — An array of alternatives for the key command.

## Return Value

A newly initialized key command object.

## Discussion

After creating a key command object, you can:

- Add it as a child of a [UIMenu](../uimenu.md) using the menu’s [init(title:image:identifier:options:children:)](<../uimenu/init(title_image_identifier_options_children_).md>) method.
- Add it to a view controller using the [- addKeyCommand:](<../uiviewcontroller/addkeycommand(__).md>) method of the view controller.
- Override any responder class and return the key command directly from the responder’s [keyCommands](../uiresponder/keycommands.md) property.

## See Also

### Creating a key command object

- [commandWithTitle:image:action:input:modifierFlags:propertyList:](commandwithtitle_image_action_input_modifierflags_propertylist_.md) — Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [+ keyCommandWithInput:modifierFlags:action:](<init(input_modifierflags_action_).md>) — Creates a key command that matches the specified input.
- [- initWithCoder:](<init(coder_).md>) — Creates a key command from data in an unarchiver.
- [- init](<init().md>) — Creates a key command.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
