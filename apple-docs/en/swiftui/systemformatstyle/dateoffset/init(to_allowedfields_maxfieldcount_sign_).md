---
title: 'init(to:allowedFields:maxFieldCount:sign:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/systemformatstyle/dateoffset/init(to:allowedfields:maxfieldcount:sign:)'
source_url: 'https://developer.apple.com/documentation/swiftui/systemformatstyle/dateoffset/init(to:allowedfields:maxfieldcount:sign:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/systemformatstyle/dateoffset/init%28to%3Aallowedfields%3Amaxfieldcount%3Asign%3A%29.json'
content_hash: 'sha256:e11732d153db782e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SystemFormatStyle](../../systemformatstyle.md) · [DateOffset](../dateoffset.md)

# init(to:allowedFields:maxFieldCount:sign:)

<sub>Initializer</sub>

Creates a format style that displays the offset between a comparison date and an anchor date that you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(to anchor: Date, allowedFields: Set<Date.ComponentsFormatStyle.Field> = [.year, .month, .week, .day, .hour, .minute, .second], maxFieldCount: Int = 2, sign: NumberFormatStyleConfiguration.SignDisplayStrategy = .automatic)
```

## Parameters

- `anchor` — The date the style uses to calculate the offset from the format input date.

- `allowedFields` — The units of time that may appear in the formatted output.

- `maxFieldCount` — The maximum number of units shown at once. For example, 1 hour, 34 minutes, and 23 seconds is shown as `1 hour, 34 minutes` by default, but as `1 hour` if `maxFieldCount` is set to 1.

- `sign` — The strategy for displaying a sign to signal whether the offset points toward the future or past.

## Discussion

The style uses a time-pattern representation (`3:46`) when `allowedFields` contains only `.minute` and `.second`, or contains `.hour`, `.minute`, and `.second`. For any other combination of fields, it uses calendar units like `3 months, 11 days`.
