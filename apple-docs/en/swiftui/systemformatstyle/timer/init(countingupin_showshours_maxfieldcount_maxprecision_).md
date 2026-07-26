---
title: 'init(countingUpIn:showsHours:maxFieldCount:maxPrecision:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/systemformatstyle/timer/init(countingupin:showshours:maxfieldcount:maxprecision:)'
source_url: 'https://developer.apple.com/documentation/swiftui/systemformatstyle/timer/init(countingupin:showshours:maxfieldcount:maxprecision:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/systemformatstyle/timer/init%28countingupin%3Ashowshours%3Amaxfieldcount%3Amaxprecision%3A%29.json'
content_hash: 'sha256:de33d38311aebb96'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SystemFormatStyle](../../systemformatstyle.md) · [Timer](../timer.md)

# init(countingUpIn:showsHours:maxFieldCount:maxPrecision:)

<sub>Initializer</sub>

Creates a timer format style that counts up within the interval you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(countingUpIn interval: Range<Date>, showsHours: Bool = true, maxFieldCount: Int = 3, maxPrecision: Duration = .seconds(1))
```

## Parameters

- `interval` — The time interval during which the timer counts up.

- `showsHours` — If `true`, hours appear as a separate element when the elapsed time reaches one hour. If `false`, minutes accumulate beyond 60.

- `maxFieldCount` — The maximum number of fields shown at once. With the default of 3, output includes hours, minutes, and seconds. With 2, it shows hours and minutes once the time reaches hours.

- `maxPrecision` — The smallest time interval between display updates. Defaults to 1 second.

## Discussion

The timer displays the elapsed time, starting from zero and increasing toward the total interval duration.
