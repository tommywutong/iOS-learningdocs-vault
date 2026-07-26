---
title: button
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menustyle/button
source_url: 'https://developer.apple.com/documentation/swiftui/menustyle/button'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menustyle/button.json'
content_hash: 'sha256:f705814cc44cf7ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuStyle](../menustyle.md)

# button

<sub>Type Property</sub>

A menu style that displays a button that toggles the display of the menu’s contents when pressed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated static var button: ButtonMenuStyle { get }
```

## Discussion

On macOS, the button displays an arrow to indicate that it presents a menu.

Pressing and then dragging into the contents activates the selected action on release.

## See Also

### Getting built-in menu styles

- [automatic](automatic.md) — The default menu style, based on the menu’s context.
- [borderedButton](borderedbutton.md) — A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed. _(deprecated)_
- [borderlessButton](borderlessbutton.md) — A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed. _(deprecated)_
