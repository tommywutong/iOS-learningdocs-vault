---
title: 'makeBody(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/datepickerstyle/makebody(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/datepickerstyle/makebody(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepickerstyle/makebody%28configuration%3A%29.json'
content_hash: 'sha256:7100cfecbb2c8c01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DatePickerStyle](../datepickerstyle.md)

# makeBody(configuration:)

<sub>Instance Method</sub>

Returns the appearance and interaction content for a `DatePicker`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@ContentBuilder @MainActor @preconcurrency func makeBody(configuration: Self.Configuration) -> Self.Body
```

## Parameters

- `configuration` — The properties of the date picker.

## Discussion

The system calls this method for each [DatePicker](../datepicker.md) instance in a view hierarchy where this style is the current date picker style.

## See Also

### Creating custom date picker styles

- [DatePickerStyleConfiguration](../datepickerstyleconfiguration.md) — The properties of a `DatePicker`.
- [Configuration](configuration.md) — A type alias for the properties of a `DatePicker`.
- [Body](body.md) — A view representing the appearance and interaction of a `DatePicker`.
