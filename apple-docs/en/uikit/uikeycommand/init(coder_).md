---
title: 'init(coder:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uikeycommand/init(coder:)'
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/init(coder:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/init%28coder%3A%29.json'
content_hash: 'sha256:e5220adc4fb85820'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# init(coder:)

<sub>Initializer</sub>

Creates a key command from data in an unarchiver.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init?(coder: NSCoder)
```

## See Also

### Creating a key command object

- [init(title:image:action:input:modifierFlags:propertyList:alternates:discoverabilityTitle:attributes:state:)](<init(title_image_action_input_modifierflags_propertylist_alternates_discoverabilitytitle_attributes_state_).md>) — Creates a key command that you can use as a menu element with a shortcut key, or a shortcut key only for a view controller.
- [+ keyCommandWithInput:modifierFlags:action:](<init(input_modifierflags_action_).md>) — Creates a key command that matches the specified input.
- [- init](<init().md>) — Creates a key command.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
- [Navigating an app’s user interface using a keyboard](../navigating-an-app-s-user-interface-using-a-keyboard.md) — Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
