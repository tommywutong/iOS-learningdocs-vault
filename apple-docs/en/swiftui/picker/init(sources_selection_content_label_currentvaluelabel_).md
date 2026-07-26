---
title: 'init(sources:selection:content:label:currentValueLabel:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(sources:selection:content:label:currentvaluelabel:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(sources:selection:content:label:currentvaluelabel:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28sources%3Aselection%3Acontent%3Alabel%3Acurrentvaluelabel%3A%29.json'
content_hash: 'sha256:5a2eab5feee817e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(sources:selection:content:label:currentValueLabel:)

<sub>Initializer</sub>

Creates a picker that displays a custom label and current value label where applicable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<C>(sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content, @ContentBuilder label: () -> Label, @ContentBuilder currentValueLabel: () -> some View) where C : RandomAccessCollection
```

## Parameters

- `sources` — A collection of values used as the source for displaying the Picker’s selection.

- `selection` — The key path of the values that determines the currently-selected options. When a user selects an option from the picker, the values at the key path of all items in the `sources` collection are updated with the selected option.

- `content` — A view that contains the set of options.

- `label` — A view that describes the purpose of selecting an option.

- `currentValueLabel` — A view that represents the current value of the picker.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the same, some styles render the selection in a mixed state. The specific presentation depends on the style.  For example, a Picker with a menu style uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the thickness of borders for the currently selected shapes.

```swift
enum Thickness: String, CaseIterable, Identifiable {
    case thin
    case regular
    case thick

    var id: String { rawValue }
}

struct Border {
    var color: Color
    var thickness: Thickness
}

@State private var selectedObjectBorders = [
    Border(color: .black, thickness: .thin),
    Border(color: .red, thickness: .thick)
]

Picker(
    sources: $selectedObjectBorders,
    selection: \.thickness
) {
    ForEach(Thickness.allCases) { thickness in
        Text(thickness.rawValue)
    }
} currentValueLabel: {
     switch selectedObjectBorders.count {
        case 0: Text("None")
        case 1: Text(selectedObjectBorders[0].thickness.rawValue)
        default: Text("Multiple")
     }
} label: {
    Text("Border Thickness")
}
```
