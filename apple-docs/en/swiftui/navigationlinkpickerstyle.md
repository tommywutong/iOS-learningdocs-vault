---
title: NavigationLinkPickerStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationlinkpickerstyle
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlinkpickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlinkpickerstyle.json'
content_hash: 'sha256:d79bb12696ff506b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NavigationLinkPickerStyle

<sub>Structure</sub>

A picker style represented by a navigation link that presents the options by pushing a List-style picker view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
struct NavigationLinkPickerStyle
```

## Overview

In navigation stacks, prefer the default [menu](pickerstyle/menu.md) style. Consider the navigation link style when you have a large number of options or your design is better expressed by pushing onto a stack.

You can also use [navigationLink](pickerstyle/navigationlink.md) to construct this style.

## Relationships

- **Conforms To**: [PickerStyle](pickerstyle.md)

## Topics

### Creating the picker style

- [init()](<navigationlinkpickerstyle/init().md>) — Creates a navigation link picker style.

## See Also

### Supporting types

- [DefaultPickerStyle](defaultpickerstyle.md) — The default picker style, based on the picker’s context.
- [InlinePickerStyle](inlinepickerstyle.md) — A `PickerStyle` where each option is displayed inline with other views in the current container.
- [MenuPickerStyle](menupickerstyle.md) — A picker style that presents the options as a menu when the user presses a button, or as a submenu when nested within a larger menu.
- [PalettePickerStyle](palettepickerstyle.md) — A picker style that presents the options as a row of compact elements.
- [RadioGroupPickerStyle](radiogrouppickerstyle.md) — A picker style that presents the options as a group of radio buttons.
- [SegmentedPickerStyle](segmentedpickerstyle.md) — A picker style that presents the options in a segmented control.
- [TabsPickerStyle](tabspickerstyle.md) — A picker style that presents options as segmented tabs. _(beta)_
- [WheelPickerStyle](wheelpickerstyle.md) — A picker style that presents the options in a scrollable wheel that shows the selected option and a few neighboring options.
