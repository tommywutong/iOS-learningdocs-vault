---
title: borderedButton
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 11.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/menustyle/borderedbutton
source_url: 'https://developer.apple.com/documentation/swiftui/menustyle/borderedbutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menustyle/borderedbutton.json'
content_hash: 'sha256:2bef907738cf45bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuStyle](../menustyle.md)

# borderedButton

<sub>Type Property</sub>

A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed.

> [!warning] Deprecated
> Use [menuStyle(_:)](<../view/menustyle(__).md>) with [button](button.md) and [buttonStyle(_:)](<../view/buttonstyle(__)-66fbx.md>) with [bordered](../primitivebuttonstyle/bordered.md).

<sub>macOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var borderedButton: BorderedButtonMenuStyle { get }
```

## Discussion

On macOS, the button displays an arrow indicating that it presents a menu.

Pressing and then dragging into the contents triggers the chosen action on release.

## See Also

### Getting built-in menu styles

- [automatic](automatic.md) — The default menu style, based on the menu’s context.
- [button](button.md) — A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [borderlessButton](borderlessbutton.md) — A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed. _(deprecated)_
