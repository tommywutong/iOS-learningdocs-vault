---
title: 'init(_:systemImage:sources:selection:content:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/picker/init(_:systemimage:sources:selection:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/picker/init%28_%3Asystemimage%3Asources%3Aselection%3Acontent%3A%29.json'
content_hash: 'sha256:6c76cbc704d35c07'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Picker](../picker.md)

# init(_:systemImage:sources:selection:content:)

<sub>Initializer</sub>

Creates a picker bound to a collection of bindings that generates its label from a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init<C, S>(_ title: S, systemImage: String, sources: C, selection: KeyPath<C.Element, Binding<SelectionValue>>, @ContentBuilder content: () -> Content) where C : RandomAccessCollection, S : StringProtocol, C.Element == Binding<SelectionValue>
```

## Parameters

- `title` — A string that describes the purpose of selecting an option.

- `systemImage` — The name of the image resource to lookup.

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

## See Also

### Creating a picker with an image label

- [init(_:image:selection:content:)](<init(__image_selection_content_).md>) — Creates a picker that generates its label from a localized string resource and image resource
- [init(_:image:sources:selection:content:)](<init(__image_sources_selection_content_).md>) — Creates a picker that generates its label from a localized string resource and image resource.
- [init(_:systemImage:selection:content:)](<init(__systemimage_selection_content_).md>) — Creates a picker that generates its label from a localized string key and system image.
