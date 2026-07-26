---
title: 'replaceMatches(in:options:range:withTemplate:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/replacematches(in:options:range:withtemplate:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/replacematches(in:options:range:withtemplate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/replacematches%28in%3Aoptions%3Arange%3Awithtemplate%3A%29.json'
content_hash: 'sha256:36bab1a0bb63b3b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# replaceMatches(in:options:range:withTemplate:)

<sub>Instance Method</sub>

Replaces regular expression matches within the mutable string using the template string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceMatches(in string: NSMutableString, options: NSRegularExpression.MatchingOptions = [], range: NSRange, withTemplate templ: String) -> Int
```

## Parameters

- `string` — The mutable string to search and replace values within.

- `options` — The matching options to use. See [MatchingOptions](matchingoptions.md) for possible values.

- `range` — The range of the string to search.

- `templ` — The substitution template used when replacing matching instances.

## Return Value

The number of matches.

## Discussion

See [Flag Options](../nsregularexpression.md#Flag-Options) for the format of `templ`.

## See Also

### Replacing Strings Using Regular Expressions

- [- stringByReplacingMatchesInString:options:range:withTemplate:](<stringbyreplacingmatches(in_options_range_withtemplate_).md>) — Returns a new string containing matching regular expressions replaced with the template string.
