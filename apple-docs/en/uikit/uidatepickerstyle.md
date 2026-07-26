---
title: UIDatePickerStyle
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatepickerstyle
source_url: 'https://developer.apple.com/documentation/uikit/uidatepickerstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatepickerstyle.json'
content_hash: 'sha256:7b761673e7d2deee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDatePickerStyle

<sub>Enumeration</sub>

Styles that determine the appearance of a date picker.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIDatePickerStyle
```

## Overview

A date picker style determines how your app displays the date picker value and its editor. For instance, a date picker with a [datePickerMode](uidatepicker/datepickermode.md) of [UIDatePickerModeDateAndTime](uidatepicker/mode/dateandtime.md) and [datePickerStyle](uidatepicker/datepickerstyle.md) of [UIDatePickerStyleCompact](uidatepickerstyle/compact.md) displays the date picker’s value as a label that the user can tap to view a calendar-style editor. On the other hand, the same date picker using the [UIDatePickerStyleInline](uidatepickerstyle/inline.md) style displays a view that lets the user edit the value without having to tap the label shown in the [UIDatePickerStyleCompact](uidatepickerstyle/compact.md) style.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Styles

- [UIDatePickerStyleAutomatic](uidatepickerstyle/automatic.md) — A style indicating that the system picks the concrete style based on the current platform and date picker mode.
- [UIDatePickerStyleCompact](uidatepickerstyle/compact.md) — A style indicating that the date picker displays as a label that when tapped displays a calendar-style editor.
- [UIDatePickerStyleInline](uidatepickerstyle/inline.md) — A style indicating that the date pickers displays as an inline, editable field.
- [UIDatePickerStyleWheels](uidatepickerstyle/wheels.md) — A style indicating that the date picker displays as a wheel picker.

### Initializers

- [init(rawValue:)](<uidatepickerstyle/init(rawvalue_).md>)

## See Also

### Configuring the date picker style

- [datePickerStyle](uidatepicker/datepickerstyle.md) — The current style of the date picker.
- [preferredDatePickerStyle](uidatepicker/preferreddatepickerstyle.md) — The preferred style of the date picker.
