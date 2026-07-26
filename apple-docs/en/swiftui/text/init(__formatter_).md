---
title: 'init(_:formatter:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/init(_:formatter:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/init(_:formatter:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/init%28_%3Aformatter%3A%29.json'
content_hash: 'sha256:37608e53d98f1855'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# init(_:formatter:)

<sub>Initializer</sub>

Creates a text view that displays the formatted representation of a Foundation object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Subject>(_ subject: Subject, formatter: Formatter) where Subject : NSObject
```

## Parameters

- `subject` — An [NSObject](../../objectivec/nsobject-swift.class.md) instance compatible with `formatter`.

- `formatter` — A [Formatter](../../foundation/formatter.md) capable of converting `subject` into a string representation.

## Discussion

Use this initializer to create a text view that formats `subject` using `formatter`.

## See Also

### Creating a text view

- [init(_:tableName:bundle:comment:)](<init(__tablename_bundle_comment_).md>) — Creates a text view that displays localized content identified by a key.
- [init(_:)](<init(__).md>) — Creates a text view that displays styled attributed content.
- [init(verbatim:)](<init(verbatim_).md>) — Creates a text view that displays a string literal without localization.
- [init(_:style:)](<init(__style_).md>) — Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](<init(__format_).md>) — Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(timerInterval:pauseTime:countsDown:showsHours:)](<init(timerinterval_pausetime_countsdown_showshours_).md>) — Creates an instance that displays a timer counting within the provided interval.
