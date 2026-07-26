---
title: 'init(verbatim:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/init(verbatim:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/init(verbatim:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/init%28verbatim%3A%29.json'
content_hash: 'sha256:9736b226b44aa715'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# init(verbatim:)

<sub>Initializer</sub>

Creates a text view that displays a string literal without localization.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(verbatim content: String)
```

## Parameters

- `content` — A string to display without localization.

## Discussion

Use this initializer to create a text view with a string literal without performing localization:

```swift
Text(verbatim: "pencil") // Displays the string "pencil" in any locale.
```

If you want to localize a string literal before displaying it, use the [init(_:tableName:bundle:comment:)](<init(__tablename_bundle_comment_).md>) initializer instead. If you want to display a string variable, use the [init(_:)](<init(__)-9d1g4.md>) initializer, which also bypasses localization.

## See Also

### Creating a text view

- [init(_:tableName:bundle:comment:)](<init(__tablename_bundle_comment_).md>) — Creates a text view that displays localized content identified by a key.
- [init(_:)](<init(__).md>) — Creates a text view that displays styled attributed content.
- [init(_:style:)](<init(__style_).md>) — Creates an instance that displays localized dates and times using a specific style.
- [init(_:format:)](<init(__format_).md>) — Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.
- [init(_:formatter:)](<init(__formatter_).md>) — Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval:pauseTime:countsDown:showsHours:)](<init(timerinterval_pausetime_countsdown_showshours_).md>) — Creates an instance that displays a timer counting within the provided interval.
