---
title: field
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/datepickerstyle/field
source_url: 'https://developer.apple.com/documentation/swiftui/datepickerstyle/field'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepickerstyle/field.json'
content_hash: 'sha256:70a28340527efd36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DatePickerStyle](../datepickerstyle.md)

# field

<sub>Type Property</sub>

A date picker style that displays the components in an editable field.

<sub>macOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var field: FieldDatePickerStyle { get }
```

## Discussion

You can use this style when space is constrained and users expect to make specific date and time selections. However, you should generally use [stepperField](stepperfield.md) instead of this style, unless your your app requires hiding the stepper.

## See Also

### Getting built-in date picker styles

- [automatic](automatic.md) — The default style for date pickers.
- [compact](compact.md) — A date picker style that displays the components in a compact, textual format.
- [graphical](graphical.md) — A date picker style that displays an interactive calendar or clock.
- [stepperField](stepperfield.md) — A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [wheel](wheel.md) — A date picker style that displays each component as columns in a scrollable wheel.
