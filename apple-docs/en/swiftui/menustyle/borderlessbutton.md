---
title: borderlessButton
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/menustyle/borderlessbutton
source_url: 'https://developer.apple.com/documentation/swiftui/menustyle/borderlessbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menustyle/borderlessbutton.json'
content_hash: 'sha256:d540b65041f9914c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuStyle](../menustyle.md)

# borderlessButton

<sub>Type Property</sub>

A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed.

> [!warning] Deprecated
> Use [menuStyle(_:)](<../view/menustyle(__).md>) with [button](button.md) and [buttonStyle(_:)](<../view/buttonstyle(__)-66fbx.md>) with [borderless](../primitivebuttonstyle/borderless.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@export(implementation) nonisolated static var borderlessButton: BorderlessButtonMenuStyle { get }
```

## Discussion

On macOS, the button optionally displays an arrow indicating that it presents a menu.

Pressing and then dragging into the contents triggers the chosen action on release.

## See Also

### Getting built-in menu styles

- [automatic](automatic.md) — The default menu style, based on the menu’s context.
- [button](button.md) — A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [borderedButton](borderedbutton.md) — A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed. _(deprecated)_
