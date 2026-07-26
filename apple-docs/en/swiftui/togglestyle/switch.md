---
title: switch
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 18.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/togglestyle/switch
source_url: 'https://developer.apple.com/documentation/swiftui/togglestyle/switch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/togglestyle/switch.json'
content_hash: 'sha256:1a5417134ed715f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ToggleStyle](../togglestyle.md)

# switch

<sub>Type Property</sub>

A toggle style that displays a leading label and a trailing switch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated static var `switch`: SwitchToggleStyle { get }
```

## Discussion

Apply this style to a [Toggle](../toggle.md) or to a view hierarchy that contains toggles using the [toggleStyle(_:)](<../view/togglestyle(__).md>) modifier:

```swift
Toggle("Enhance Sound", isOn: $isEnhanced)
    .toggleStyle(.switch)
```

The style produces a label that describes the purpose of the toggle and a switch that shows the toggle’s state. The user taps or clicks the switch to change the toggle’s state. The default appearance is similar across platforms, although the way you use switches in your user interface varies a little, as described in [Toggles](../../design/human-interface-guidelines/toggles.md) in the Human Interface Guidelines.

**iOS**

![](../../../../attachments/cd8fb717861a884a81f391126c10b6f2/ToggleStyle-switch-1-iOS@2x.png)

<sub>A screenshot of the text On appearing to the left of a toggle switch that's on. The toggle's tint color is green. The toggle and its text appear in a rounded rectangle, and are aligned with opposite edges of the rectangle.</sub>

**macOS**

![](../../../../attachments/25cb3cd1a4a49c5a468e61527d4a6287/ToggleStyle-switch-1-macOS@2x.png)

<sub>A screenshot of the text On appearing to the left of a toggle switch that's on. The toggle's tint color is blue. The toggle and its text are adjacent to each other.</sub>

**watchOS**

![](../../../../attachments/b46e6bdcecb7dd1580bd1d5314d3b070/ToggleStyle-switch-1-watchOS@2x.png)

<sub>A screenshot of the text On appearing to the left of a toggle switch that's on. The toggle's tint color is green. The toggle and its text appear in a rounded rectangle, and are aligned with opposite edges of the rectangle.</sub>

**tvOS**

![](../../../../attachments/e314e49a988f16dd7b011c53c4039fda/ToggleStyle-automatic-2-tvOS@2x.png)

<sub>A screenshot of three buttons labeled Show Lyrics, Shuffle, and Repeat, stacked vertically. The first is highlighted. The second is on, while the others are off.</sub>

In iOS, iPadOS, watchOS, and tvOS, the label and switch fill as much horizontal space as the toggle’s parent offers by aligning the label’s leading edge and the switch’s trailing edge with the containing view’s respective leading and trailing edges. In macOS, the style uses a minimum of horizontal space by aligning the trailing edge of the label with the leading edge of the switch. SwiftUI helps you to manage the spacing and alignment when this style appears in a [Form](../form.md).

SwiftUI uses this style as the default for iOS, iPadOS, watchOS, and tvOS in most contexts when you don’t set a style, or when you apply the [automatic](automatic.md) style.

## See Also

### Getting built-in toggle styles

- [automatic](automatic.md) — The default toggle style.
- [button](button.md) — A toggle style that displays as a button with its label as the title.
- [checkbox](checkbox.md) — A toggle style that displays a checkbox followed by its label.
