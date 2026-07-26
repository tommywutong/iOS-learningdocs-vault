---
title: 'range(of:options:locale:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/range(of:options:locale:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/range(of:options:locale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/range%28of%3Aoptions%3Alocale%3A%29.json'
content_hash: 'sha256:c7570e0e7592a1e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# range(of:options:locale:)

<sub>Instance Method</sub>

Returns the range of a substring in the attributed string, if it exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func range<T>(of stringToFind: T, options: String.CompareOptions = [], locale: Locale? = nil) -> Range<AttributedString.Index>? where T : StringProtocol
```

## Parameters

- `stringToFind` — The string to find.

- `options` — Options that affect the search behavior, such as case-insensivity, search direction, and regular expression matching.

- `locale` — The locale to use when searching, or `nil` to use the current locale. The default is `nil`.

## Return Value

The range where `stringToFind` exists in the attributed string, or `nil` if it isn’t present.
