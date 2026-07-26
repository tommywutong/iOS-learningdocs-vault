---
title: 'stringByReplacingMatches(in:options:range:withTemplate:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/stringbyreplacingmatches(in:options:range:withtemplate:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/stringbyreplacingmatches(in:options:range:withtemplate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/stringbyreplacingmatches%28in%3Aoptions%3Arange%3Awithtemplate%3A%29.json'
content_hash: 'sha256:28cb17eea65d9b60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# stringByReplacingMatches(in:options:range:withTemplate:)

<sub>Instance Method</sub>

Returns a new string containing matching regular expressions replaced with the template string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func stringByReplacingMatches(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange, withTemplate templ: String) -> String
```

## Parameters

- `string` — The string to search for values within.

- `options` — The matching options to use. See [MatchingOptions](matchingoptions.md) for possible values.

- `range` — The range of the string to search.

- `templ` — The substitution template used when replacing matching instances.

## Return Value

A string with matching regular expressions replaced by the template string.

## Discussion

See [Flag Options](../nsregularexpression.md#Flag-Options) for the format of `templ`.

## See Also

### Replacing Strings Using Regular Expressions

- [- replaceMatchesInString:options:range:withTemplate:](<replacematches(in_options_range_withtemplate_).md>) — Replaces regular expression matches within the mutable string using the template string.
