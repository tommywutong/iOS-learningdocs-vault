---
title: graphical
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.15+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/datepickerstyle/graphical
source_url: 'https://developer.apple.com/documentation/swiftui/datepickerstyle/graphical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepickerstyle/graphical.json'
content_hash: 'sha256:f71657887a5f0c72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DatePickerStyle](../datepickerstyle.md)

# graphical

<sub>Type Property</sub>

A date picker style that displays an interactive calendar or clock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var graphical: GraphicalDatePickerStyle { get }
```

## Discussion

This style is useful when you want to allow browsing through days in a calendar, or when the look of a clock face is appropriate.

## See Also

### Getting built-in date picker styles

- [automatic](automatic.md) — The default style for date pickers.
- [compact](compact.md) — A date picker style that displays the components in a compact, textual format.
- [field](field.md) — A date picker style that displays the components in an editable field.
- [stepperField](stepperfield.md) — A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [wheel](wheel.md) — A date picker style that displays each component as columns in a scrollable wheel.
