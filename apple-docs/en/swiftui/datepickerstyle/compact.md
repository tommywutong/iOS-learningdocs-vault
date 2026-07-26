---
title: compact
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 13.4+, macOS 10.15.4+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/datepickerstyle/compact
source_url: 'https://developer.apple.com/documentation/swiftui/datepickerstyle/compact'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepickerstyle/compact.json'
content_hash: 'sha256:2495b808d8db83bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DatePickerStyle](../datepickerstyle.md)

# compact

<sub>Type Property</sub>

A date picker style that displays the components in a compact, textual format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor @export(implementation) @preconcurrency static var compact: CompactDatePickerStyle { get }
```

## Discussion

Use this style when space is constrained and users expect to make specific date and time selections. Some variants may include rich editing controls in a pop up.

## See Also

### Getting built-in date picker styles

- [automatic](automatic.md) — The default style for date pickers.
- [field](field.md) — A date picker style that displays the components in an editable field.
- [graphical](graphical.md) — A date picker style that displays an interactive calendar or clock.
- [stepperField](stepperfield.md) — A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [wheel](wheel.md) — A date picker style that displays each component as columns in a scrollable wheel.
