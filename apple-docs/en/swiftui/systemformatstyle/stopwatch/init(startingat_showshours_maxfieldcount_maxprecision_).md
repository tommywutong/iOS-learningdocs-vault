---
title: 'init(startingAt:showsHours:maxFieldCount:maxPrecision:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/systemformatstyle/stopwatch/init(startingat:showshours:maxfieldcount:maxprecision:)'
source_url: 'https://developer.apple.com/documentation/swiftui/systemformatstyle/stopwatch/init(startingat:showshours:maxfieldcount:maxprecision:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/systemformatstyle/stopwatch/init%28startingat%3Ashowshours%3Amaxfieldcount%3Amaxprecision%3A%29.json'
content_hash: 'sha256:cc9e1c2bb8a31221'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SystemFormatStyle](../../systemformatstyle.md) · [Stopwatch](../stopwatch.md)

# init(startingAt:showsHours:maxFieldCount:maxPrecision:)

<sub>Initializer</sub>

Creates a stopwatch format style that starts counting up from zero from the date you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(startingAt startDate: Date, showsHours: Bool = true, maxFieldCount: Int = 4, maxPrecision: Duration = .milliseconds(10))
```

## Parameters

- `startDate` — The date at which the stopwatch starts counting. Any input date before this shows `00:00.00`.

- `showsHours` — If `true`, the stopwatch shows hours as a separate element once the elapsed time reaches one hour. If `false`, minutes accumulate beyond 60 (for example, `75:30.00`).

- `maxFieldCount` — The maximum number of fields shown at once. With the default of 4, output includes hours, minutes, seconds, and hundredths. Reducing this value removes fields starting from the least significant.

- `maxPrecision` — The smallest time interval between display updates. Defaults to 10 milliseconds (two fractional digits).
