---
title: 'localizedStringWithFormat(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/localizedstringwithformat(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/localizedstringwithformat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/localizedstringwithformat%28_%3A_%3A%29.json'
content_hash: 'sha256:bc07205fa6041c13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# localizedStringWithFormat(_:_:)

<sub>Type Method</sub>

Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func localizedStringWithFormat(_ format: String, _ arguments: any CVarArg...) -> String
```

## See Also

### Creating a String Using Formats

- [init(format:_:)](<init(format___).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [init(format:arguments:)](<init(format_arguments_).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format:locale:_:)](<init(format_locale___).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [init(format:locale:arguments:)](<init(format_locale_arguments_).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
