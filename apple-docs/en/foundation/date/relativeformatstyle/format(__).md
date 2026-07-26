---
title: 'format(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/date/relativeformatstyle/format(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/format(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/format%28_%3A%29.json'
content_hash: 'sha256:72b035dea4a5b76d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# format(_:)

<sub>Instance Method</sub>

Creates a locale-aware string representation from a relative date value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func format(_ destDate: Date) -> String
```

## Parameters

- `destDate` — The date to format.

## Return Value

A string representation of the relative date.

## Discussion

The [format(_:)](<format(__).md>) instance method generates a string from the provided relative date. Once you create a style, you can use it to format dates multiple times.

The following example applies a format style repeatedly to produce string representations of relative dates:

```swift
if let pastWeek = Calendar.current.date(byAdding: .day, value: -7, to: Date()) {
    if let pastDay = Calendar.current.date(byAdding: .day, value: -1, to: Date()) {

        let formatStyle = Date.RelativeFormatStyle(
            presentation: .named,
            unitsStyle: .spellOut,
            locale: Locale(identifier: "en_GB"),
            calendar: Calendar.current,
            capitalizationContext: .beginningOfSentence)
        
        formatStyle.format(pastDay) // "Yesterday"
        formatStyle.format(pastWeek) // "Last week"
    }
}
```
