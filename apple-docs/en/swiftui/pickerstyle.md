---
title: PickerStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/pickerstyle
source_url: 'https://developer.apple.com/documentation/swiftui/pickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/pickerstyle.json'
content_hash: 'sha256:8c14e5368bfe4d0e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PickerStyle

<sub>Protocol</sub>

A type that specifies the appearance and interaction of all pickers within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol PickerStyle
```

## Relationships

- **Conforming Types**: [DefaultPickerStyle](defaultpickerstyle.md), [InlinePickerStyle](inlinepickerstyle.md), [MenuPickerStyle](menupickerstyle.md), [NavigationLinkPickerStyle](navigationlinkpickerstyle.md), [PalettePickerStyle](palettepickerstyle.md), [PopUpButtonPickerStyle](popupbuttonpickerstyle.md), [RadioGroupPickerStyle](radiogrouppickerstyle.md), [SegmentedPickerStyle](segmentedpickerstyle.md), [TabsPickerStyle](tabspickerstyle.md), [WheelPickerStyle](wheelpickerstyle.md)

## Topics

### Getting built-in picker styles

- [automatic](pickerstyle/automatic.md) — The default picker style, based on the picker’s context.
- [inline](pickerstyle/inline.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [menu](pickerstyle/menu.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [navigationLink](pickerstyle/navigationlink.md) — A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [palette](pickerstyle/palette.md) — A picker style that presents the options as a row of compact elements.
- [radioGroup](pickerstyle/radiogroup.md) — A picker style that presents the options as a group of radio buttons.
- [segmented](pickerstyle/segmented.md) — A picker style that presents the options in a segmented control.
- [tabs](pickerstyle/tabs.md) — A picker style that presents options as segmented tabs. _(beta)_
- [wheel](pickerstyle/wheel.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.

### Supporting types

- [DefaultPickerStyle](defaultpickerstyle.md) — The default picker style, based on the picker’s context.
- [InlinePickerStyle](inlinepickerstyle.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [MenuPickerStyle](menupickerstyle.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [NavigationLinkPickerStyle](navigationlinkpickerstyle.md) — A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [PalettePickerStyle](palettepickerstyle.md) — A picker style that presents the options as a row of compact elements.
- [RadioGroupPickerStyle](radiogrouppickerstyle.md) — A picker style that presents the options as a group of radio buttons.
- [SegmentedPickerStyle](segmentedpickerstyle.md) — A picker style that presents the options in a segmented control.
- [TabsPickerStyle](tabspickerstyle.md) — A picker style that presents options as segmented tabs. _(beta)_
- [WheelPickerStyle](wheelpickerstyle.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.

### Deprecated styles

- [PopUpButtonPickerStyle](popupbuttonpickerstyle.md) — A picker style that presents the options as a menu when the user presses a button. _(deprecated)_

## See Also

### Styling pickers

- [pickerStyle(_:)](<view/pickerstyle(__).md>) — Sets the style for pickers within this view.
- [datePickerStyle(_:)](<view/datepickerstyle(__).md>) — Sets the style for date pickers within this view.
- [DatePickerStyle](datepickerstyle.md) — A type that specifies the appearance and interaction of all date pickers within a view hierarchy.
