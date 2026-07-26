---
title: 'init(title:subtitle:image:identifier:options:preferredElementSize:children:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uimenu/init(title:subtitle:image:identifier:options:preferredelementsize:children:)'
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/init(title:subtitle:image:identifier:options:preferredelementsize:children:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/init%28title%3Asubtitle%3Aimage%3Aidentifier%3Aoptions%3Apreferredelementsize%3Achildren%3A%29.json'
content_hash: 'sha256:ca0efde1ec26db16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenu](../uimenu.md)

# init(title:subtitle:image:identifier:options:preferredElementSize:children:)

<sub>Initializer</sub>

Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init(title: String = "", subtitle: String? = nil, image: UIImage? = nil, identifier: UIMenu.Identifier? = nil, options: UIMenu.Options = [], preferredElementSize: UIMenu.ElementSize = { if #available(iOS 17.0, tvOS 17.0, watchOS 10.0, *) { .automatic } else { .large } }(), children: [UIMenuElement] = [])
```

## Parameters

- `title` — The title of the menu.

- `subtitle` — The subtitle of the menu.

- `image` — The image to display next to the menu’s title.

- `identifier` — The unique identifier for the menu. When creating standard menus for your app, specify an appropriate constant defined in [Identifier](identifier-swift.struct.md). For custom menus, specify a custom reverse domain name value, or specify `nil` to let this method create a unique identifier for you.

- `options` — Additional configuration options for the menu. For a list of possible values, see [Options](options-swift.struct.md).

- `preferredElementSize` — The size of the menu’s child elements. For a list of possible values, see [ElementSize](elementsize.md).

- `children` — The menu elements in the menu. Specify leaf menu elements using [UIMenuElement](../uimenuelement.md) subclasses like [UIAction](../uiaction.md), [UICommand](../uicommand.md), or [UIKeyCommand](../uikeycommand.md), and specify submenus using [UIMenu](../uimenu.md) objects. You may specify an empty array if the menu has no child menu elements.

## See Also

### Creating a menu object

- [init(title:image:identifier:options:children:)](<init(title_image_identifier_options_children_).md>) — Creates a new menu with the specified values.
- [init(title:subtitle:image:identifier:options:children:)](<init(title_subtitle_image_identifier_options_children_).md>) — Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [Identifier](identifier-swift.struct.md) — Constants you use to identify an app’s standard menus.
- [Options](options-swift.struct.md) — Options you use to configure a menu’s appearance.
- [- initWithCoder:](<init(coder_).md>) — Creates a menu from data in an unarchiver.
