---
title: 'init(_:style:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/init(_:style:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/init(_:style:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/init%28_%3Astyle%3A%29.json'
content_hash: 'sha256:e02eb73d6fb9b13f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# init(_:style:)

<sub>Initializer</sub>

Creates an instance that displays localized dates and times using a specific style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ date: Date, style: Text.DateStyle)
```

## Parameters

- `date` — The target date to display.

- `style` — The style used when displaying a date.

## See Also

### Creating a text view

- [init(_:tableName:bundle:comment:)](<init(__tablename_bundle_comment_).md>) — Creates a text view that displays localized content identified by a key.
- [init(_:)](<init(__).md>) — Creates a text view that displays styled attributed content.
- [init(verbatim:)](<init(verbatim_).md>) — Creates a text view that displays a string literal without localization.
- [init(_:format:)](<init(__format_).md>) — Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](<init(__formatter_).md>) — Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval:pauseTime:countsDown:showsHours:)](<init(timerinterval_pausetime_countsdown_showshours_).md>) — Creates an instance that displays a timer counting within the provided interval.
