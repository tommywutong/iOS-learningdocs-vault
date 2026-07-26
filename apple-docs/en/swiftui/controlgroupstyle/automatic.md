---
title: automatic
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/controlgroupstyle/automatic
source_url: 'https://developer.apple.com/documentation/swiftui/controlgroupstyle/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/controlgroupstyle/automatic.json'
content_hash: 'sha256:800c18ddb868d0d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ControlGroupStyle](../controlgroupstyle.md)

# automatic

<sub>Type Property</sub>

The default control group style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var automatic: AutomaticControlGroupStyle { get }
```

## Discussion

The default control group style can vary by platform. By default, both platforms use a momentary segmented control style that’s appropriate for the environment in which it is rendered.

You can override a control group’s style. To apply the default style to a control group or to a view that contains a control group, use the [controlGroupStyle(_:)](<../view/controlgroupstyle(__).md>) modifier.

## See Also

### Getting built-in control group styles

- [compactMenu](compactmenu.md) — A control group style that presents its content as a compact menu when the user presses the control, or as a submenu when nested within a larger menu.
- [menu](menu.md) — A control group style that presents its content as a menu when the user presses the control, or as a submenu when nested within a larger menu.
- [navigation](navigation.md) — The navigation control group style.
- [palette](palette.md) — A control group style that presents its content as a palette.
