---
title: UIMenu.Options
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenu/options-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uimenu/options-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenu/options-swift.struct.json'
content_hash: 'sha256:04d9b88c76f6dc3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenu](../uimenu.md)

# UIMenu.Options

<sub>Structure</sub>

Options you use to configure a menu’s appearance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Options

- [UIMenuOptionsDisplayInline](options-swift.struct/displayinline.md) — An option indicating the menu displays inline with its parent menu instead of displaying as a submenu.
- [UIMenuOptionsDestructive](options-swift.struct/destructive.md) — An option indicating the menu’s appearance represents a destructive action.
- [UIMenuOptionsSingleSelection](options-swift.struct/singleselection.md) — An option indicating whether the menu and its submenus allow a single menu item that’s in the “on” state.
- [UIMenuOptionsDisplayAsPalette](options-swift.struct/displayaspalette.md) — An option indicating the menu displays as a row of menu elements for choosing from a collection of items.

### Initializers

- [init(rawValue:)](<options-swift.struct/init(rawvalue_).md>) — Creates a menu options structure from data in an unarchiver.

## See Also

### Creating a menu object

- [init(title:image:identifier:options:children:)](<init(title_image_identifier_options_children_).md>) — Creates a new menu with the specified values.
- [init(title:subtitle:image:identifier:options:children:)](<init(title_subtitle_image_identifier_options_children_).md>) — Creates a new menu with the specified title, subtitle, image, identifier, menu options, and child elements.
- [init(title:subtitle:image:identifier:options:preferredElementSize:children:)](<init(title_subtitle_image_identifier_options_preferredelementsize_children_).md>) — Creates a new menu with the specified title, subtitle, image, identifier, menu options, element size, and child elements.
- [Identifier](identifier-swift.struct.md) — Constants you use to identify an app’s standard menus.
- [- initWithCoder:](<init(coder_).md>) — Creates a menu from data in an unarchiver.
