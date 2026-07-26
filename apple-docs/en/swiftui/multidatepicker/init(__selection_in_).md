---
title: 'init(_:selection:in:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/multidatepicker/init(_:selection:in:)'
source_url: 'https://developer.apple.com/documentation/swiftui/multidatepicker/init(_:selection:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/multidatepicker/init%28_%3Aselection%3Ain%3A%29.json'
content_hash: 'sha256:05a969083102dbae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MultiDatePicker](../multidatepicker.md)

# init(_:selection:in:)

<sub>Initializer</sub>

Creates an instance that selects multiple dates on or after some start date.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Set<DateComponents>>, in bounds: PartialRangeFrom<Date>)
```

## Parameters

- `titleResource` — The localized title of `self`, describing its purpose.

- `selection` — The date values being displayed and selected.

- `bounds` — The open range from some selectable start date.

## See Also

### Picking dates in a range

- [init(selection:in:label:)](<init(selection_in_label_).md>) — Creates an instance that selects multiple dates on or after some start date.
