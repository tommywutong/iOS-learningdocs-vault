---
title: WheelPickerStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/wheelpickerstyle
source_url: 'https://developer.apple.com/documentation/swiftui/wheelpickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/wheelpickerstyle.json'
content_hash: 'sha256:a4abe4c961305372'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WheelPickerStyle

<sub>Structure</sub>

A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
struct WheelPickerStyle
```

## Overview

You can also use [wheel](pickerstyle/wheel.md) to construct this style.

## Relationships

- **Conforms To**: [PickerStyle](pickerstyle.md)

## Topics

### Creating the picker style

- [init()](<wheelpickerstyle/init().md>) — Sets the picker style to display an item wheel from which the user makes a selection.

## See Also

### Supporting types

- [DefaultPickerStyle](defaultpickerstyle.md) — The default picker style, based on the picker’s context.
- [InlinePickerStyle](inlinepickerstyle.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [MenuPickerStyle](menupickerstyle.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [NavigationLinkPickerStyle](navigationlinkpickerstyle.md) — A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [PalettePickerStyle](palettepickerstyle.md) — A picker style that presents the options as a row of compact elements.
- [RadioGroupPickerStyle](radiogrouppickerstyle.md) — A picker style that presents the options as a group of radio buttons.
- [SegmentedPickerStyle](segmentedpickerstyle.md) — A picker style that presents the options in a segmented control.
- [TabsPickerStyle](tabspickerstyle.md) — A picker style that presents options as segmented tabs. _(beta)_
