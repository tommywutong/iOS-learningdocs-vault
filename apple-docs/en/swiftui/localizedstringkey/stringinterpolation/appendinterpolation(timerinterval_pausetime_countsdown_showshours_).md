---
title: 'appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(timerinterval:pausetime:countsdown:showshours:)'
source_url: 'https://developer.apple.com/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation(timerinterval:pausetime:countsdown:showshours:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/localizedstringkey/stringinterpolation/appendinterpolation%28timerinterval%3Apausetime%3Acountsdown%3Ashowshours%3A%29.json'
content_hash: 'sha256:842f76fa5b0d6de5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [LocalizedStringKey](../../localizedstringkey.md) · [StringInterpolation](../stringinterpolation.md)

# appendInterpolation(timerInterval:pauseTime:countsDown:showsHours:)

<sub>Instance Method</sub>

Appends a timer interval to a string interpolation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(timerInterval: ClosedRange<Date>, pauseTime: Date? = nil, countsDown: Bool = true, showsHours: Bool = true)
```

## Parameters

- `timerInterval` — The interval between where to run the timer.

- `pauseTime` — If present, the date at which to pause the timer. The default is `nil` which indicates to never pause.

- `countsDown` — Whether to count up or down. The default is `true`.

- `showsHours` — Whether to include an hours component if there are more than 60 minutes left on the timer. The default is `true`.

## Discussion

Don’t call this method directly; it’s used by the compiler when interpreting string interpolations.

## See Also

### Appending to an interpolation

- [appendInterpolation(_:)](<appendinterpolation(__).md>) — Appends an attributed substring to a string interpolation.
- [appendInterpolation(_:specifier:)](<appendinterpolation(__specifier_).md>) — Appends a type, convertible to a string with a format specifier, to a string interpolation.
- [appendInterpolation(_:format:)](<appendinterpolation(__format_).md>) — Appends the formatted representation  of a nonstring type supported by a corresponding format style.
- [appendInterpolation(_:formatter:)](<appendinterpolation(__formatter_).md>) — Appends an optionally-formatted instance of an Objective-C subclass to a string interpolation.
- [appendInterpolation(_:style:)](<appendinterpolation(__style_).md>) — Appends a formatted date to a string interpolation.
- [appendLiteral(_:)](<appendliteral(__).md>) — Appends a literal string.
