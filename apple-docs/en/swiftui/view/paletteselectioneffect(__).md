---
title: 'paletteSelectionEffect(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/paletteselectioneffect(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/paletteselectioneffect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/paletteselectioneffect%28_%3A%29.json'
content_hash: 'sha256:de9c17dcf150a20b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# paletteSelectionEffect(_:)

<sub>Instance Method</sub>

Specifies the selection effect to apply to a palette item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func paletteSelectionEffect(_ effect: PaletteSelectionEffect) -> some View

```

## Parameters

- `effect` — The type of effect to apply when a palette item is selected.

## Discussion

[automatic](../paletteselectioneffect/automatic.md) applies the system’s default appearance when selected. When using un-tinted SF Symbols or template images, the current tint color is applied to the selected items’ image. If the provided SF Symbols have custom tints, a stroke is drawn around selected items.

If you wish to provide a specific image (or SF Symbol) to indicate selection, use [custom](../paletteselectioneffect/custom.md) to forgo the system’s default selection appearance allowing the provided image to solely indicate selection instead.

The following example creates a palette picker that disables the system selection behavior:

```swift
Menu {
    Picker("Palettes", selection: $selection) {
        ForEach(palettes) { palette in
            Label(palette.title, image: selection == palette ?
                  "selected-palette" : "palette")
            .tint(palette.tint)
            .tag(palette)
        }
    }
    .pickerStyle(.palette)
    .paletteSelectionEffect(.custom)
} label: {
    ...
}
```

If a specific SF Symbol variant is preferable instead, use [symbolVariant(_:)](<../paletteselectioneffect/symbolvariant(__).md>).

```swift
Menu {
    ControlGroup {
        ForEach(ColorTags.allCases) { colorTag in
            Toggle(isOn: $selectedColorTags[colorTag]) {
                Label(colorTag.name, systemImage: "circle")
            }
            .tint(colorTag.color)
        }
    }
    .controlGroupStyle(.palette)
    .paletteSelectionEffect(.symbolVariant(.fill))
}
```

## See Also

### Choosing from a set of options

- [Picker](../picker.md) — A control for selecting from a set of mutually exclusive values.
- [pickerStyle(_:)](<pickerstyle(__).md>) — Sets the style for pickers within this view.
- [horizontalRadioGroupLayout()](<horizontalradiogrouplayout().md>) — Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.
- [defaultWheelPickerItemHeight(_:)](<defaultwheelpickeritemheight(__).md>) — Sets the default wheel-style picker item height.
- [defaultWheelPickerItemHeight](../environmentvalues/defaultwheelpickeritemheight.md) — The default height of an item in a wheel-style picker, such as a date picker.
- [PaletteSelectionEffect](../paletteselectioneffect.md) — The selection effect to apply to a palette item.
