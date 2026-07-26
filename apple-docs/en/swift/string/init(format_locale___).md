---
title: 'init(format:locale:_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(format:locale:_:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(format:locale:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28format%3Alocale%3A_%3A%29.json'
content_hash: 'sha256:efe286065e5400c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(format:locale:_:)

<sub>Initializer</sub>

Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(format: String, locale: Locale?, _ args: any CVarArg...)
```

## See Also

### Creating a String Using Formats

- [init(format:_:)](<init(format___).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted.
- [init(format:arguments:)](<init(format_arguments_).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
- [init(format:locale:arguments:)](<init(format_locale_arguments_).md>) — Returns a `String` object initialized by using a given format string as a template into which the remaining argument values are substituted according to given locale information.
- [localizedStringWithFormat(_:_:)](<localizedstringwithformat(____).md>) — Returns a string created by using a given format string as a template into which the remaining argument values are substituted according to the user’s default locale.
