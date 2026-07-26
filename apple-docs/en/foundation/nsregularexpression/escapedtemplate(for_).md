---
title: 'escapedTemplate(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/escapedtemplate(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/escapedtemplate(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/escapedtemplate%28for%3A%29.json'
content_hash: 'sha256:2ed15f4823a6afc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# escapedTemplate(for:)

<sub>Type Method</sub>

Returns a template string by adding backslash escapes as necessary to protect any characters that would match as pattern metacharacters

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func escapedTemplate(for string: String) -> String
```

## Parameters

- `string` — The template string

## Return Value

The escaped template string.

## Discussion

Returns a string by adding backslash escapes as necessary to the given string, to escape any characters that would otherwise be treated as pattern metacharacters. You typically use this method to match on a particular string within a larger pattern.

For example, the string `"(N/A)"` contains the pattern metacharacters `(`, `/`, and `)`. The result of adding backslash escapes to this string is `"\\(N\\/A\\)"`.

See [Flag Options](../nsregularexpression.md#Flag-Options) for the format of the resulting template string.

## See Also

### Escaping Characters in a String

- [+ escapedPatternForString:](<escapedpattern(for_).md>) — Returns a string by adding backslash escapes as necessary to protect any characters that would match as pattern metacharacters.
