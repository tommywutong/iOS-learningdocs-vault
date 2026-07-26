---
title: navigation
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlgroupstyle/navigation
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroupstyle/navigation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroupstyle/navigation.json'
content_hash: 'sha256:6f84e3596a5960cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroupStyle](../controlgroupstyle.md)

# navigation

<sub>Type Property</sub>

The navigation control group style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var navigation: NavigationControlGroupStyle { get }
```

## Discussion

Use this style to group controls related to navigation, such as back/forward buttons or timeline navigation controls.

The navigation control group style can vary by platform. On iOS, it renders as individual borderless buttons, while on macOS, it displays as a separated momentary segmented control.

To apply this style to a control group or to a view that contains a control group, use the [controlGroupStyle(_:)](<../view/controlgroupstyle(__).md>) modifier.

## See Also

### Getting built-in control group styles

- [automatic](automatic.md) — The default control group style.
- [compactMenu](compactmenu.md) — A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [menu](menu.md) — A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [palette](palette.md) — A control group style that presents its content as a palette.
