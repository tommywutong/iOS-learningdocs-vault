---
title: system
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimenubuilder/system
source_url: 'https://developer.apple.com/documentation/uikit/uimenubuilder/system'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenubuilder/system.json'
content_hash: 'sha256:78310809d791d03f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuBuilder](../uimenubuilder.md)

# system

<sub>Instance Property</sub>

The menu system that the menu builder modifies.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var system: UIMenuSystem { get }
```

## Discussion

Always check the [system](system.md) property to determine which menu system the builder is modifying before you add and remove menus. For example, when you want to modify the main menu bar, check [system](system.md) for [mainSystem](../uimenusystem/main.md).

```swift
override func buildMenu(with builder: UIMenuBuilder) {
    super.buildMenu(with: builder)
    
    // Ensure that the builder is modifying the menu bar system.
    guard builder.system == UIMenuSystem.main else { return }
    
    let refreshCommand = UICommand(title: "Refresh", action: #selector(refreshData(_:)))
    let refreshMenu = UIMenu(title: "", options: .displayInline, children: [refreshCommand])

    // Insert the menu into the File menu before the Close menu.
    builder.insertSibling(refreshMenu, beforeMenu: .close)
}
```

## See Also

### Getting menu systems and elements

- [- menuForIdentifier:](<menu(for_).md>) — Gets the menu for the specified menu identifier.
- [- actionForIdentifier:](<action(for_).md>) — Gets the action for the specified action identifier.
- [command(for:propertyList:)](<command(for_propertylist_).md>) — Gets the command for the specified selector and property list.
