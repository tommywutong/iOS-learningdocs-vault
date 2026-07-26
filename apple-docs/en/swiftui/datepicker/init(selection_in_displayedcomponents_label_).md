---
title: 'init(selection:in:displayedComponents:label:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/datepicker/init(selection:in:displayedcomponents:label:)'
source_url: 'https://developer.apple.com/documentation/swiftui/datepicker/init(selection:in:displayedcomponents:label:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepicker/init%28selection%3Ain%3Adisplayedcomponents%3Alabel%3A%29.json'
content_hash: 'sha256:833a2df58c799414'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DatePicker](../datepicker.md)

# init(selection:in:displayedComponents:label:)

<sub>Initializer</sub>

Creates an instance that selects a `Date` in a closed range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated init(selection: Binding<Date>, in range: ClosedRange<Date>, displayedComponents: DatePicker<Label>.Components = [.hourAndMinute, .date], @ContentBuilder label: () -> Label)
```

## Parameters

- `selection` — The date value being displayed and selected.

- `range` — The inclusive range of selectable dates.

- `displayedComponents` — The date components that user is able to view and edit. Defaults to `[.hourAndMinute, .date]`. On watchOS, if `.hourAndMinute` or `.hourMinuteAndSecond` are included with `.date`, only `.date` is displayed.

- `label` — A view that describes the use of the date.

## See Also

### Creating a date picker for specific dates

- [init(_:selection:in:displayedComponents:)](<init(__selection_in_displayedcomponents_).md>) — Creates an instance that selects a `Date` in a closed range.
