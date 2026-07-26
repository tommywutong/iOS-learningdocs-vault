---
title: MenuPickerStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/menupickerstyle
source_url: 'https://developer.apple.com/documentation/swiftui/menupickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/menupickerstyle.json'
content_hash: 'sha256:bf84c16ac32a2f9f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# MenuPickerStyle

<sub>Structure</sub>

A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct MenuPickerStyle
```

## Overview

You can also use [menu](pickerstyle/menu.md) to construct this style.

## Relationships

- **Conforms To**: [PickerStyle](pickerstyle.md)

## Topics

### Creating the picker style

- [init()](<menupickerstyle/init().md>) — Creates a menu picker style.

## See Also

### Supporting types

- [DefaultPickerStyle](defaultpickerstyle.md) — The default picker style, based on the picker’s context.
- [InlinePickerStyle](inlinepickerstyle.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [NavigationLinkPickerStyle](navigationlinkpickerstyle.md) — A picker style represented by a navigation link that presents the options by pushing a List-style picker view.
- [PalettePickerStyle](palettepickerstyle.md) — A picker style that presents the options as a row of compact elements.
- [RadioGroupPickerStyle](radiogrouppickerstyle.md) — A picker style that presents the options as a group of radio buttons.
- [SegmentedPickerStyle](segmentedpickerstyle.md) — A picker style that presents the options in a segmented control.
- [TabsPickerStyle](tabspickerstyle.md) — A picker style that presents options as segmented tabs. _(beta)_
- [WheelPickerStyle](wheelpickerstyle.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
