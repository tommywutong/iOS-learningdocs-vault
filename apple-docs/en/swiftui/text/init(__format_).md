---
title: 'init(_:format:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/text/init(_:format:)'
source_url: 'https://developer.apple.com/documentation/swiftui/text/init(_:format:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/text/init%28_%3Aformat%3A%29.json'
content_hash: 'sha256:2ebfcc4f29d10256'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Text](../text.md)

# init(_:format:)

<sub>Initializer</sub>

Creates a text view that displays the formatted representation of a nonstring type supported by a corresponding format style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<F>(_ input: F.FormatInput, format: F) where F : FormatStyle, F.FormatInput : Equatable, F.FormatOutput == AttributedString
```

## Parameters

- `input` — The underlying value to display.

- `format` — A format style of type `F` to convert the underlying value of type `F.FormatInput` to an attributed string representation.

## Discussion

Use this initializer to create a text view backed by a nonstring value, using a [FormatStyle](../../foundation/formatstyle.md) to convert the type to an attributed string representation. Any changes to the value update the string displayed by the text view.

In the following example, three [Text](../text.md) views present a date with different combinations of date and time fields, by using different [Date.FormatStyle](../../foundation/date/formatstyle.md) options.

```swift
@State private var myDate = Date()
var body: some View {
    VStack {
        Text(myDate, format: Date.FormatStyle(date: .numeric, time: .omitted).attributedStyle)
        Text(myDate, format: Date.FormatStyle(date: .complete, time: .complete).attributedStyle)
        Text(myDate, format: Date.FormatStyle().hour(.defaultDigitsNoAMPM).minute().attributedStyle)
    }
}
```

![Three vertically stacked text views showing the date with different](../../../../attachments/3cbfd7e712f6d26122350b67f0db9862/Text-init-format-1@2x.png)

## See Also

### Creating a text view

- [init(_:tableName:bundle:comment:)](<init(__tablename_bundle_comment_).md>) — Creates a text view that displays localized content identified by a key.
- [init(_:)](<init(__).md>) — Creates a text view that displays styled attributed content.
- [init(verbatim:)](<init(verbatim_).md>) — Creates a text view that displays a string literal without localization.
- [init(_:style:)](<init(__style_).md>) — Creates an instance that displays localized dates and times using a specific style.
- [init(_:formatter:)](<init(__formatter_).md>) — Creates a text view that displays the formatted representation of a Foundation object.
- [init(timerInterval:pauseTime:countsDown:showsHours:)](<init(timerinterval_pausetime_countsdown_showshours_).md>) — Creates an instance that displays a timer counting within the provided interval.
