---
title: 'init(title:subtitle:image:action:propertyList:alternates:discoverabilityTitle:attributes:state:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicommand/init(title:subtitle:image:action:propertylist:alternates:discoverabilitytitle:attributes:state:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicommand/init(title:subtitle:image:action:propertylist:alternates:discoverabilitytitle:attributes:state:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicommand/init%28title%3Asubtitle%3Aimage%3Aaction%3Apropertylist%3Aalternates%3Adiscoverabilitytitle%3Aattributes%3Astate%3A%29.json'
content_hash: 'sha256:40cc1a60ae87c020'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICommand](../uicommand.md)

# init(title:subtitle:image:action:propertyList:alternates:discoverabilityTitle:attributes:state:)

<sub>Initializer</sub>

Creates a command with the specified title, subtitle, image, action, property list, alternative commands, discoverability title, attributes, and state.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(title: String = "", subtitle: String? = nil, image: UIImage? = nil, action: Selector, propertyList: Any? = nil, alternates: [UICommandAlternate] = [], discoverabilityTitle: String? = nil, attributes: UIMenuElement.Attributes = [], state: UIMenuElement.State = .off)
```

## Parameters

- `title` — The title to display for the command.

- `subtitle` — The subtitle to display alongside the command’s title.

- `image` — The image to display next to the command’s title. Only the [contextSystem](../uimenusystem/context.md) menu system supports the display of an image, and only when the app is running in iOS.

- `action` — The action to take after a person selects the command.

- `propertyList` — An object that contains data to associate with the command.

- `alternates` — An array of alternatives for the command.

- `discoverabilityTitle` — An elaborated title that explains the purpose of the command.

- `attributes` — The attributes indicating the style of the command.

- `state` — The initial state of the command.

## See Also

### Creating a command

- [init(title:image:action:propertyList:alternates:discoverabilityTitle:attributes:state:)](<init(title_image_action_propertylist_alternates_discoverabilitytitle_attributes_state_).md>) — Creates a command with the specified title, image, action, property list, alternative commands, discoverability title, attributes, and state.
- [- initWithCoder:](<init(coder_).md>) — Creates a command from data in an unarchiver.
- [Adding menus and shortcuts to the menu bar and user interface](../adding-menus-and-shortcuts-to-the-menu-bar-and-user-interface.md) — Provide quick access to useful actions by adding menus and keyboard shortcuts to your Mac app built with Mac Catalyst.
