---
title: 'datePickerStyle(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/datepickerstyle(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/datepickerstyle(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/datepickerstyle%28_%3A%29.json'
content_hash: 'sha256:244dce9fc1f2f888'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# datePickerStyle(_:)

<sub>Instance Method</sub>

Sets the style for date pickers within this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
nonisolated func datePickerStyle<S>(_ style: S) -> some View where S : DatePickerStyle

```

## See Also

### Choosing dates

- [DatePicker](../datepicker.md) — A control for selecting an absolute date.
- [MultiDatePicker](../multidatepicker.md) — A control for picking multiple dates.
- [calendar](../environmentvalues/calendar.md) — The current calendar that views should use when handling dates.
- [timeZone](../environmentvalues/timezone.md) — The current time zone that views should use when handling dates.
