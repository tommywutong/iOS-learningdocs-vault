---
title: 'init(selection:in:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/multidatepicker/init(selection:in:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/multidatepicker/init(selection:in:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/multidatepicker/init%28selection%3Ain%3Alabel%3A%29.json'
content_hash: 'sha256:3fe5bcd3e6d7d7f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MultiDatePicker](../multidatepicker.md)

# init(selection:in:label:)

<sub>Initializer</sub>

Creates an instance that selects multiple dates on or after some start date.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated init(selection: Binding<Set<DateComponents>>, in bounds: PartialRangeFrom<Date>, @ContentBuilder label: () -> Label)
```

## Parameters

- `selection` — The date values being displayed and selected.

- `bounds` — The open range from some selectable start date.

- `label` — A view that describes the use of the dates.

## See Also

### Picking dates in a range

- [init(_:selection:in:)](<init(__selection_in_).md>) — Creates an instance that selects multiple dates on or after some start date.
