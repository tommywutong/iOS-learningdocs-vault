---
title: stepperField
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/datepickerstyle/stepperfield
source_url: 'https://developer.apple.com/documentation/swiftui/datepickerstyle/stepperfield'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepickerstyle/stepperfield.json'
content_hash: 'sha256:e2b4678e390f6407'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DatePickerStyle](../datepickerstyle.md)

# stepperField

<sub>Type Property</sub>

A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.

<sub>macOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var stepperField: StepperFieldDatePickerStyle { get }
```

## Discussion

This style is useful when space is constrained and users expect to make specific date and time selections.

## See Also

### Getting built-in date picker styles

- [automatic](automatic.md) — The default style for date pickers.
- [compact](compact.md) — A date picker style that displays the components in a compact, textual format.
- [field](field.md) — A date picker style that displays the components in an editable field.
- [graphical](graphical.md) — A date picker style that displays an interactive calendar or clock.
- [wheel](wheel.md) — A date picker style that displays each component as columns in a scrollable wheel.
