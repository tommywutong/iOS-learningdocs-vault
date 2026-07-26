---
title: 'escapedPattern(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/escapedpattern(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/escapedpattern(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/escapedpattern%28for%3A%29.json'
content_hash: 'sha256:5b995362fc572104'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# escapedPattern(for:)

<sub>Type Method</sub>

Returns a string by adding backslash escapes as necessary to protect any characters that would match as pattern metacharacters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func escapedPattern(for string: String) -> String
```

## Parameters

- `string` — The string.

## Return Value

The escaped string.

## Discussion

Returns a string by adding backslash escapes as necessary to the given string, to escape any characters that would otherwise be treated as pattern metacharacters. You typically use this method to match on a particular string within a larger pattern.

For example, the string `"(N/A)"` contains the pattern metacharacters `(`, `/`, and `)`. The result of adding backslash escapes to this string is `"\\(N\\/A\\)"`.

## See Also

### Escaping Characters in a String

- [+ escapedTemplateForString:](<escapedtemplate(for_).md>) — Returns a template string by adding backslash escapes as necessary to protect any characters that would match as pattern metacharacters
