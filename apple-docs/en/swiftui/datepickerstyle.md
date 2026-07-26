---
title: DatePickerStyle
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/datepickerstyle
source_url: 'https://developer.apple.com/documentation/swiftui/datepickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/datepickerstyle.json'
content_hash: 'sha256:d1a3cd6de66501fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# DatePickerStyle

<sub>Protocol</sub>

A type that specifies the appearance and interaction of all date pickers within a view hierarchy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency protocol DatePickerStyle
```

## Overview

To configure the current date picker style for a view hierarchy, use the [datePickerStyle(_:)](<view/datepickerstyle(__).md>) modifier.

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Relationships

- **Conforming Types**: [CompactDatePickerStyle](compactdatepickerstyle.md), [DefaultDatePickerStyle](defaultdatepickerstyle.md), [FieldDatePickerStyle](fielddatepickerstyle.md), [GraphicalDatePickerStyle](graphicaldatepickerstyle.md), [StepperFieldDatePickerStyle](stepperfielddatepickerstyle.md), [WheelDatePickerStyle](wheeldatepickerstyle.md)

## Topics

### Getting built-in date picker styles

- [automatic](datepickerstyle/automatic.md) — The default style for date pickers.
- [compact](datepickerstyle/compact.md) — A date picker style that displays the components in a compact, textual format.
- [field](datepickerstyle/field.md) — A date picker style that displays the components in an editable field.
- [graphical](datepickerstyle/graphical.md) — A date picker style that displays an interactive calendar or clock.
- [stepperField](datepickerstyle/stepperfield.md) — A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [wheel](datepickerstyle/wheel.md) — A date picker style that displays each component as columns in a scrollable wheel.

### Creating custom date picker styles

- [makeBody(configuration:)](<datepickerstyle/makebody(configuration_).md>) — Returns the appearance and interaction content for a `DatePicker`.
- [DatePickerStyleConfiguration](datepickerstyleconfiguration.md) — The properties of a `DatePicker`.
- [Configuration](datepickerstyle/configuration.md) — A type alias for the properties of a `DatePicker`.
- [Body](datepickerstyle/body.md) — A view representing the appearance and interaction of a `DatePicker`.

### Supporting types

- [DefaultDatePickerStyle](defaultdatepickerstyle.md) — The default style for date pickers.
- [CompactDatePickerStyle](compactdatepickerstyle.md) — A date picker style that displays the components in a compact, textual format.
- [FieldDatePickerStyle](fielddatepickerstyle.md) — A date picker style that displays the components in an editable field.
- [GraphicalDatePickerStyle](graphicaldatepickerstyle.md) — A date picker style that displays an interactive calendar or clock.
- [StepperFieldDatePickerStyle](stepperfielddatepickerstyle.md) — A system style that displays the components in an editable field, with adjoining stepper that can increment/decrement the selected component.
- [WheelDatePickerStyle](wheeldatepickerstyle.md) — A date picker style that displays each component as columns in a scrollable wheel.

## See Also

### Styling pickers

- [pickerStyle(_:)](<view/pickerstyle(__).md>) — Sets the style for pickers within this view.
- [PickerStyle](pickerstyle.md) — A type that specifies the appearance and interaction of all pickers within a view hierarchy.
- [datePickerStyle(_:)](<view/datepickerstyle(__).md>) — Sets the style for date pickers within this view.
