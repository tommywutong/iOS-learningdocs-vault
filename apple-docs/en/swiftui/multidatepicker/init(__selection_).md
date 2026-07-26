---
title: 'init(_:selection:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/multidatepicker/init(_:selection:)'
source_url: 'https://developer.apple.com/documentation/swiftui/multidatepicker/init(_:selection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/multidatepicker/init%28_%3Aselection%3A%29.json'
content_hash: 'sha256:7a5de509f5fefc8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [MultiDatePicker](../multidatepicker.md)

# init(_:selection:)

<sub>Initializer</sub>

Creates an instance that selects multiple dates with an unbounded range.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Set<DateComponents>>)
```

## Parameters

- `titleResource` — The localized title of `self`, describing its purpose.

- `selection` — The date values being displayed and selected.

## See Also

### Picking dates

- [init(selection:label:)](<init(selection_label_).md>) — Creates an instance that selects multiple dates with an unbounded range.
