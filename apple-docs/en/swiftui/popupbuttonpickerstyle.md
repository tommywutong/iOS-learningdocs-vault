---
title: PopUpButtonPickerStyle
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swiftui/popupbuttonpickerstyle
source_url: 'https://developer.apple.com/documentation/swiftui/popupbuttonpickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/popupbuttonpickerstyle.json'
content_hash: 'sha256:ba397d5b7df5d2ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PopUpButtonPickerStyle

<sub>Structure</sub>

A picker style that presents the options as a menu when the user presses a button.

> [!warning] Deprecated
> Use [MenuPickerStyle](menupickerstyle.md) instead.

<sub>macOS</sub>

```swift
struct PopUpButtonPickerStyle
```

## Overview

Use this style when there are more than five options. Consider using [RadioGroupPickerStyle](radiogrouppickerstyle.md) when there are fewer than five options.

The button itself indicates the selected option. You can include additional controls in the set of options, such as a button to customize the list of options.

To apply this style to a picker, or to a view that contains pickers, use the [pickerStyle(_:)](<view/pickerstyle(__).md>) modifier.

### Creating the picker style

- [init()](<popupbuttonpickerstyle/init().md>)

## Relationships

- **Conforms To**: [PickerStyle](pickerstyle.md)

## Topics

### Initializers

- [init()](<popupbuttonpickerstyle/init().md>) — Creates a pop-up button picker style. _(deprecated)_
