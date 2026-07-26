---
title: 'init(timerInterval:pauseTime:countsDown:showsHours:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/init(timerinterval:pausetime:countsdown:showshours:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/init%28timerinterval%3Apausetime%3Acountsdown%3Ashowshours%3A%29.json'
content_hash: 'sha256:eea65bf45d7b7ed4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# init(timerInterval:pauseTime:countsDown:showsHours:)

<sub>Initializer</sub>

Creates an instance that displays a timer counting within the provided interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(timerInterval: ClosedRange<Date>, pauseTime: Date? = nil, countsDown: Bool = true, showsHours: Bool = true)
```

## Parameters

- `timerInterval` — The interval between where to run the timer.

- `pauseTime` — If present, the date at which to pause the timer. The default is `nil` which indicates to never pause.

- `countsDown` — Whether to count up or down. The default is `true`.

- `showsHours` — Whether to include an hours component if there are more than 60 minutes left on the timer. The default is `true`.

## Discussion

```swift
Text(
    timerInterval: Date.now...Date(timeInterval: 12 * 60, since: .now),
    pauseTime: Date.now + (10 * 60))
```

The example above shows a text that displays a timer counting down from “12:00” and will pause when reaching “10:00”.

## See Also

### Creating a text view

- [init(_:tableName:bundle:comment:)](<init(__tablename_bundle_comment_).md>) — Creates a text view that displays localized content identified by a key.
- [init(_:)](<init(__).md>) — Creates a text view that displays styled attributed content.
- [init(verbatim:)](<init(verbatim_).md>) — Creates a text view that displays a string literal without localization.
- [init(_:style:)](<init(__style_).md>) — Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](<init(__format_).md>) — Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](<init(__formatter_).md>) — Creates a text view that displays the formatted representation of a Foundation object.
