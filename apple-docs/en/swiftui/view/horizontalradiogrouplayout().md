---
title: horizontalRadioGroupLayout()
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/view/horizontalradiogrouplayout()
source_url: 'https://developer.apple.com/documentation/swiftui/view/horizontalradiogrouplayout()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/horizontalradiogrouplayout%28%29.json'
content_hash: 'sha256:0322185160334e0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# horizontalRadioGroupLayout()

<sub>Instance Method</sub>

Sets the style for radio group style pickers within this view to be horizontally positioned with the radio buttons inside the layout.

<sub>macOS</sub>

```swift
nonisolated func horizontalRadioGroupLayout() -> some View

```

## Discussion

Use `horizontalRadioGroupLayout()` to configure the visual layout of radio buttons in a [Picker](../picker.md) so that the radio buttons are arranged horizontally in the view.

The example below shows two [Picker](../picker.md) controls configured as radio button groups; the first group shows the default vertical layout; the second group shows the effect of `horizontalRadioGroupLayout()` which renders the radio buttons horizontally.

```swift
struct HorizontalRadioGroupLayout: View {
    @State private var selected = 1
    var body: some View {
        VStack(spacing: 20) {
            Picker(selection: $selected, label: Text("Favorite Color")) {
                Text("Red").tag(1)
                Text("Green").tag(2)
                Text("Blue").tag(3)
                Text("Other").tag(4)
            }
            .pickerStyle(.radioGroup)

            Picker(selection: $selected, label: Text("Favorite Color")) {
                Text("Red").tag(1)
                Text("Green").tag(2)
                Text("Blue").tag(3)
                Text("Other").tag(4)
            }
            .pickerStyle(.radioGroup)
            .horizontalRadioGroupLayout()
        }
        .padding(20)
        .border(Color.gray)
    }
}
```

![A screenshot showing radio button groups laid out horizontally and](../../../../attachments/8f2854f2770dea6cb22a722e3aac8095/SwiftUI-view-horizontalRadioGroupLayout@2x.png)

## See Also

### Choosing from a set of options

- [Picker](../picker.md) — A control for selecting from a set of mutually exclusive values.
- [pickerStyle(_:)](<pickerstyle(__).md>) — Sets the style for pickers within this view.
- [defaultWheelPickerItemHeight(_:)](<defaultwheelpickeritemheight(__).md>) — Sets the default wheel-style picker item height.
- [defaultWheelPickerItemHeight](../environmentvalues/defaultwheelpickeritemheight.md) — The default height of an item in a wheel-style picker, such as a date picker.
- [paletteSelectionEffect(_:)](<paletteselectioneffect(__).md>) — Specifies the selection effect to apply to a palette item.
- [PaletteSelectionEffect](../paletteselectioneffect.md) — The selection effect to apply to a palette item.
