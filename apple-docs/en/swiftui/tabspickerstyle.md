---
title: TabsPickerStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/tabspickerstyle
source_url: 'https://developer.apple.com/documentation/swiftui/tabspickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tabspickerstyle.json'
content_hash: 'sha256:690c9629d3f50a55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# TabsPickerStyle

<sub>Structure</sub>

A picker style that presents options as segmented tabs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct TabsPickerStyle
```

## Overview

On macOS, this style produces a segmented picker with a visual treatment that distinguishes tab navigation from value selection. On iOS, tvOS, and visionOS, the visual appearance matches that of the standard standard `.segmented` style. On all supported platforms, VoiceOver announces options as tabs.

```swift
Picker("View", selection: $view) {
    Text("Events").tag(Views.events)
    Text("Reminders").tag(Views.reminders)
}
.pickerStyle(.tabs)
```

To apply this style to a picker, or to a view that contains pickers, use the [pickerStyle(_:)](<view/pickerstyle(__).md>) modifier.

You can also use [tabs](pickerstyle/tabs.md) to construct this style.

## Relationships

- **Conforms To**: [PickerStyle](pickerstyle.md)

## Topics

### Creating the picker style

- [init()](<tabspickerstyle/init().md>) — Creates a tabs picker style. _(beta)_

## See Also

### Supporting types

- [DefaultPickerStyle](defaultpickerstyle.md) — The default picker style, based on the picker’s context.
- [InlinePickerStyle](inlinepickerstyle.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [MenuPickerStyle](menupickerstyle.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [NavigationLinkPickerStyle](navigationlinkpickerstyle.md) — A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [PalettePickerStyle](palettepickerstyle.md) — A picker style that presents the options as a row of compact elements.
- [RadioGroupPickerStyle](radiogrouppickerstyle.md) — A picker style that presents the options as a group of radio buttons.
- [SegmentedPickerStyle](segmentedpickerstyle.md) — A picker style that presents the options in a segmented control.
- [WheelPickerStyle](wheelpickerstyle.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
