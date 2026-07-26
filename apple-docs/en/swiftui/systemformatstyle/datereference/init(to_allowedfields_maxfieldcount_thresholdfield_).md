---
title: 'init(to:allowedFields:maxFieldCount:thresholdField:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/systemformatstyle/datereference/init(to:allowedfields:maxfieldcount:thresholdfield:)'
source_url: 'https://developer.apple.com/documentation/swiftui/systemformatstyle/datereference/init(to:allowedfields:maxfieldcount:thresholdfield:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/systemformatstyle/datereference/init%28to%3Aallowedfields%3Amaxfieldcount%3Athresholdfield%3A%29.json'
content_hash: 'sha256:40a1909e3bd505c9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SystemFormatStyle](../../systemformatstyle.md) · [DateReference](../datereference.md)

# init(to:allowedFields:maxFieldCount:thresholdField:)

<sub>Initializer</sub>

Creates a format style that refers to a comparison date using natural language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(to date: Date, allowedFields: Set<Date.RelativeFormatStyle.Field> = [.year, .month, .day, .hour, .minute], maxFieldCount: Int = 2, thresholdField: Date.RelativeFormatStyle.Field = .day)
```

## Parameters

- `date` — The date this format references.

- `allowedFields` — The units of time that may appear in the relative representation. The style always includes the `thresholdField` regardless of this set.

- `maxFieldCount` — The maximum number of fields the style shows in the absolute representation. The style excludes more significant fields whose value matches the reference date, making room for less significant ones.

- `thresholdField` — The time unit that tells the style when to switch from relative to absolute representation. For example, if you provide `.minute` and the time difference extends to hours or days, the style switches from relative to absolute.
