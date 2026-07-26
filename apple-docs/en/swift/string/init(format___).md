---
title: 'init(format:_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(format:_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(format:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28format%3A_%3A%29.json'
content_hash: 'sha256:556818573a0072f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(format:_:)

<sub>Initializer</sub>

Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(format: String, _ arguments: any CVarArg...)
```

## See Also

### Creating a String Using Formats

- [init(format:arguments:)](<init(format_arguments_).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format:locale:_:)](<init(format_locale___).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [init(format:locale:arguments:)](<init(format_locale_arguments_).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [localizedStringWithFormat(_:_:)](<localizedstringwithformat(____).md>) — Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
