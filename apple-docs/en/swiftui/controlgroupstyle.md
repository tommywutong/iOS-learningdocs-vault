---
title: ControlGroupStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlgroupstyle
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroupstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroupstyle.json'
content_hash: 'sha256:fd5bcdf6ed179253'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ControlGroupStyle

<sub>Protocol</sub>

Defines the implementation of all control groups within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency protocol ControlGroupStyle
```

## Overview

To configure the current `ControlGroupStyle` for a view hierarchy, use the [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) modifier.

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

- **Conforming Types**: [AutomaticControlGroupStyle](automaticcontrolgroupstyle.md), [CompactMenuControlGroupStyle](compactmenucontrolgroupstyle.md), [MenuControlGroupStyle](menucontrolgroupstyle.md), [NavigationControlGroupStyle](navigationcontrolgroupstyle.md), [PaletteControlGroupStyle](palettecontrolgroupstyle.md)

## Topics

### Getting built-in control group styles

- [automatic](controlgroupstyle/automatic.md) — The default control group style.
- [compactMenu](controlgroupstyle/compactmenu.md) — A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [menu](controlgroupstyle/menu.md) — A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [navigation](controlgroupstyle/navigation.md) — The navigation control group style.
- [palette](controlgroupstyle/palette.md) — A control group style that presents its content as a palette.

### Creating custom control group styles

- [makeBody(configuration:)](<controlgroupstyle/makebody(configuration_).md>) — Creates a view representing the body of a control group.
- [Configuration](controlgroupstyle/configuration.md) — The properties of a `ControlGroup` instance being created.
- [Body](controlgroupstyle/body.md) — A view representing the body of a control group.

### Supporting types

- [AutomaticControlGroupStyle](automaticcontrolgroupstyle.md) — The default control group style.
- [CompactMenuControlGroupStyle](compactmenucontrolgroupstyle.md) — A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [MenuControlGroupStyle](menucontrolgroupstyle.md) — A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [NavigationControlGroupStyle](navigationcontrolgroupstyle.md) — The navigation control group style.
- [PaletteControlGroupStyle](palettecontrolgroupstyle.md) — A control group style that presents its content as a palette.

## See Also

### Styling groups

- [controlGroupStyle(_:)](<view/controlgroupstyle(__).md>) — Sets the style for control groups within this view.
- [ControlGroupStyleConfiguration](controlgroupstyleconfiguration.md) — The properties of a control group.
- [formStyle(_:)](<view/formstyle(__).md>) — Sets the style for forms in a view hierarchy.
- [FormStyle](formstyle.md) — The appearance and behavior of a form.
- [FormStyleConfiguration](formstyleconfiguration.md) — The properties of a form instance.
- [groupBoxStyle(_:)](<view/groupboxstyle(__).md>) — Sets the style for group boxes within this view.
- [GroupBoxStyle](groupboxstyle.md) — A type that specifies the appearance and interaction of all group boxes within a view hierarchy.
- [GroupBoxStyleConfiguration](groupboxstyleconfiguration.md) — The properties of a group box instance.
- [indexViewStyle(_:)](<view/indexviewstyle(__).md>) — Sets the style for the index view within the current environment.
- [IndexViewStyle](indexviewstyle.md) — Defines the implementation of all `IndexView` instances within a view hierarchy.
- [labeledContentStyle(_:)](<view/labeledcontentstyle(__).md>) — Sets a style for labeled content.
- [LabeledContentStyle](labeledcontentstyle.md) — The appearance and behavior of a labeled content instance..
- [LabeledContentStyleConfiguration](labeledcontentstyleconfiguration.md) — The properties of a labeled content instance.
