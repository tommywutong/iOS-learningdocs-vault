---
title: 'init(_:selection:displayedComponents:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/datepicker/init(_:selection:displayedcomponents:)'
source_url: 'https://developer.apple.com/documentation/swiftui/datepicker/init(_:selection:displayedcomponents:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepicker/init%28_%3Aselection%3Adisplayedcomponents%3A%29.json'
content_hash: 'sha256:635cbd55b7c9b80b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DatePicker](../datepicker.md)

# init(_:selection:displayedComponents:)

<sub>Initializer</sub>

Creates an instance that selects a `Date` with an unbounded range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@export(implementation) nonisolated init(_ titleResource: LocalizedStringResource, selection: Binding<Date>, displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date])
```

## Parameters

- `titleResource` — The localized title of `self`, describing its purpose.

- `selection` — The date value being displayed and selected.

- `displayedComponents` — The date components that user is able to view and edit. Defaults to `[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or `.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

## See Also

### Creating a date picker for any date

- [init(selection:displayedComponents:label:)](<init(selection_displayedcomponents_label_).md>) — Creates an instance that selects a `Date` with an unbounded range.
