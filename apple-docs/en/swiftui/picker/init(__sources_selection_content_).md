---
title: 'init(_:sources:selection:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(_:sources:selection:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(_:sources:selection:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28_%3Asources%3Aselection%3Acontent%3A%29.json'
content_hash: 'sha256:ce082a9513beee64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(_:sources:selection:content:)

<sub>Initializer</sub>

Creates a picker that generates its label from a localized string resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<C>(_ titleResource: LocalizedStringResource, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content) where C : RandomAccessCollection
```

## Parameters

- `titleResource` — A localized string resource that describes the purpose of selecting an option.

- `sources` — A collection of values used as the source for displaying the Picker’s selection.

- `selection` — The key path of the values that determines the currently-selected options. When a user selects an option from the picker, the values at the key path of all items in the `sources` collection are updated with the selected option.

- `content` — A view that contains the set of options.

## Discussion

If the wrapped values of the collection passed to `sources` are not all the same, some styles render the selection in a mixed state. The specific presentation depends on the style.  For example, a Picker with a menu style uses dashes instead of checkmarks to indicate the selected values.

In the following example, a picker in a document inspector controls the thickness of borders for the currently-selected shapes, which can be of any number.

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
    "Border Thickness",
    sources: $selectedObjectBorders,
    selection: \.thickness
) {
    ForEach(Thickness.allCases) { thickness in
        Text(thickness.rawValue)
    }
}
```

This initializer creates a [Text](../text.md) view on your behalf. See [Text](../text.md) for more information about localizing strings.

## See Also

### Creating a picker for a collection

- [init(sources:selection:content:label:)](<init(sources_selection_content_label_).md>) — Creates a picker that displays a custom label.
