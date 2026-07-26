---
title: 'init(selection:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/multidatepicker/init(selection:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/multidatepicker/init(selection:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/multidatepicker/init%28selection%3Alabel%3A%29.json'
content_hash: 'sha256:f1b8e9ac5133c32a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MultiDatePicker](../multidatepicker.md)

# init(selection:label:)

<sub>Initializer</sub>

Creates an instance that selects multiple dates with an unbounded range.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated init(selection: Binding<Set<DateComponents>>, @ContentBuilder label: () -> Label)
```

## Parameters

- `selection` — The date values being displayed and selected.

- `label` — A view that describes the use of the dates.

## See Also

### Picking dates

- [init(_:selection:)](<init(__selection_).md>) — Creates an instance that selects multiple dates with an unbounded range.
