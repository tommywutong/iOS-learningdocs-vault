---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menustyle/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/menustyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menustyle/automatic.json'
content_hash: 'sha256:50c9bfc51f7e4df4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MenuStyle](../menustyle.md)

# automatic

<sub>Type Property</sub>

The default menu style, based on the menu’s context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var automatic: DefaultMenuStyle { get }
```

## Discussion

The default menu style can vary by platform. By default, macOS uses the bordered button style.

If you create a menu inside a container, the style resolves to the recommended style for menus inside that container for that specific platform. For example, a menu nested within another menu will resolve to a submenu:

```swift
Menu("Edit") {
    Menu("Arrange") {
        Button("Bring to Front", action: moveSelectionToFront)
        Button("Send to Back", action: moveSelectionToBack)
    }
    Button("Delete", action: deleteSelection)
}
```

You can override a menu’s style. To apply the default style to a menu, or to a view that contains a menu, use the [menuStyle(_:)](<../view/menustyle(__).md>) modifier.

## See Also

### Getting built-in menu styles

- [button](button.md) — A menu style that displays a button that toggles the display of the menu’s contents when pressed.
- [borderedButton](borderedbutton.md) — A menu style that displays a bordered button that toggles the display of the menu’s contents when pressed. _(deprecated)_
- [borderlessButton](borderlessbutton.md) — A menu style that displays a borderless button that toggles the display of the menu’s contents when pressed. _(deprecated)_
