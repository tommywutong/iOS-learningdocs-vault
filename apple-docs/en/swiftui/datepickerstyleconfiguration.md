---
title: DatePickerStyleConfiguration
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/datepickerstyleconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/datepickerstyleconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepickerstyleconfiguration.json'
content_hash: 'sha256:f6f9e0ba03aeeb31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DatePickerStyleConfiguration

<sub>Structure</sub>

The properties of a `DatePicker`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
struct DatePickerStyleConfiguration
```

## Topics

### Establishing the date range

- [minimumDate](datepickerstyleconfiguration/minimumdate.md) — The oldest selectable date.
- [maximumDate](datepickerstyleconfiguration/maximumdate.md) — The most recent selectable date.

### Labeling the date picker

- [label](datepickerstyleconfiguration/label-swift.property.md) — A description of the `DatePicker`.
- [Label](datepickerstyleconfiguration/label-swift.struct.md) — A type-erased label of a `DatePicker`.
- [displayedComponents](datepickerstyleconfiguration/displayedcomponents.md) — The date components that the user is able to view and edit.

### Selecting the date

- [selection](datepickerstyleconfiguration/selection.md) — The date value being displayed and selected.
- [$selection](datepickerstyleconfiguration/$selection.md)

## See Also

### Creating custom date picker styles

- [makeBody(configuration:)](<datepickerstyle/makebody(configuration_).md>) — Returns the appearance and interaction content for a `DatePicker`.
- [Configuration](datepickerstyle/configuration.md) — A type alias for the properties of a `DatePicker`.
- [Body](datepickerstyle/body.md) — A view representing the appearance and interaction of a `DatePicker`.
