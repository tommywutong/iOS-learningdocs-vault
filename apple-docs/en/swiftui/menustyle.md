---
title: MenuStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menustyle
source_url: 'https://developer.apple.com/documentation/swiftui/menustyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menustyle.json'
content_hash: 'sha256:e23c16c947b9117a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MenuStyle

<sub>Protocol</sub>

A type that applies standard interaction behavior and a custom appearance to all menus within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol MenuStyle
```

## Overview

To configure the current menu style for a view hierarchy, use the [menuStyle(_:)](<view/menustyle(__).md>) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [BorderedButtonMenuStyle](borderedbuttonmenustyle.md), [BorderlessButtonMenuStyle](borderlessbuttonmenustyle.md), [ButtonMenuStyle](buttonmenustyle.md), [DefaultMenuStyle](defaultmenustyle.md)

## Topics

### Getting built-in menu styles

- [automatic](menustyle/automatic.md) — The default menu style, based on the menu’s context.
- [button](menustyle/button.md) — A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [borderedButton](menustyle/borderedbutton.md) — A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed. _(deprecated)_
- [borderlessButton](menustyle/borderlessbutton.md) — A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed. _(deprecated)_

### Creating custom menu styles

- [makeBody(configuration:)](<menustyle/makebody(configuration_).md>) — Creates a view that represents the body of a menu.
- [Configuration](menustyle/configuration.md) — The properties of a menu.
- [Body](menustyle/body.md) — A view that represents the body of a menu.

### Supporting types

- [DefaultMenuStyle](defaultmenustyle.md) — The default menu style, based on the menu’s context.
- [ButtonMenuStyle](buttonmenustyle.md) — A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [BorderlessButtonMenuStyle](borderlessbuttonmenustyle.md) — A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed. _(deprecated)_
- [BorderedButtonMenuStyle](borderedbuttonmenustyle.md) — A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed. _(deprecated)_

## See Also

### Styling menus

- [menuStyle(_:)](<view/menustyle(__).md>) — Sets the style for menus within this view.
- [MenuStyleConfiguration](menustyleconfiguration.md) — A configuration of a menu.
