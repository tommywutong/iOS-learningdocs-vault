---
title: compactMenu
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlgroupstyle/compactmenu
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroupstyle/compactmenu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroupstyle/compactmenu.json'
content_hash: 'sha256:de31b73378efceb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroupStyle](../controlgroupstyle.md)

# compactMenu

<sub>Type Property</sub>

A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated static var compactMenu: CompactMenuControlGroupStyle { get }
```

## Discussion

To apply this style to a control group, or to a view that contains control groups, use the [controlGroupStyle(_:)](<../view/controlgroupstyle(__).md>) modifier.

## See Also

### Getting built-in control group styles

- [automatic](automatic.md) — The default control group style.
- [menu](menu.md) — A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [navigation](navigation.md) — The navigation control group style.
- [palette](palette.md) — A control group style that presents its content as a palette.
