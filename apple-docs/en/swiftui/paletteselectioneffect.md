---
title: PaletteSelectionEffect
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/paletteselectioneffect
source_url: 'https://developer.apple.com/documentation/swiftui/paletteselectioneffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/paletteselectioneffect.json'
content_hash: 'sha256:dd96b3daef041f22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PaletteSelectionEffect

<sub>Structure</sub>

The selection effect to apply to a palette item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct PaletteSelectionEffect
```

## Overview

You can configure the selection effect of a palette item by using the [paletteSelectionEffect(_:)](<view/paletteselectioneffect(__).md>) view modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting palette selection effects

- [automatic](paletteselectioneffect/automatic.md) — Applies the system’s default effect when selected.
- [custom](paletteselectioneffect/custom.md) — Does not apply any system effect when selected.
- [symbolVariant(_:)](<paletteselectioneffect/symbolvariant(__).md>) — Applies the specified symbol variant when selected.

## See Also

### Choosing from a set of options

- [Picker](picker.md) — A control for selecting from a set of mutually exclusive values.
- [pickerStyle(_:)](<view/pickerstyle(__).md>) — Sets the style for pickers within this view.
- [horizontalRadioGroupLayout()](<view/horizontalradiogrouplayout().md>) — Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [defaultWheelPickerItemHeight(_:)](<view/defaultwheelpickeritemheight(__).md>) — Sets the default wheel-style picker item height.
- [defaultWheelPickerItemHeight](environmentvalues/defaultwheelpickeritemheight.md) — The default height of an item in a wheel-style picker, such as a date picker.
- [paletteSelectionEffect(_:)](<view/paletteselectioneffect(__).md>) — Specifies the selection effect to apply to a palette item.
