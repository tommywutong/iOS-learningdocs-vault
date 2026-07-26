---
title: 'rangeOfFirstMatch(in:options:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsregularexpression/rangeoffirstmatch(in:options:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsregularexpression/rangeoffirstmatch(in:options:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsregularexpression/rangeoffirstmatch%28in%3Aoptions%3Arange%3A%29.json'
content_hash: 'sha256:f3644c213ff06b41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRegularExpression](../nsregularexpression.md)

# rangeOfFirstMatch(in:options:range:)

<sub>Instance Method</sub>

Returns the range of the first match of the regular expression within the specified range of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func rangeOfFirstMatch(in string: String, options: NSRegularExpression.MatchingOptions = [], range: NSRange) -> NSRange
```

## Parameters

- `string` — The string to search.

- `options` — The matching options to use. See [MatchingOptions](matchingoptions.md) for possible values.

- `range` — The range of the string to search.

## Return Value

The range of the first match. Returns `{NSNotFound, 0}` if no match is found.

## Discussion

This is a convenience method that calls [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>).

## See Also

### Searching Strings Using Regular Expressions

- [- numberOfMatchesInString:options:range:](<numberofmatches(in_options_range_).md>) — Returns the number of matches of the regular expression within the specified range of the string.
- [- enumerateMatchesInString:options:range:usingBlock:](<enumeratematches(in_options_range_using_).md>) — Enumerates the string allowing the Block to handle each regular expression match.
- [- matchesInString:options:range:](<matches(in_options_range_).md>) — Returns an array containing all the matches of the regular expression in the string.
- [- firstMatchInString:options:range:](<firstmatch(in_options_range_).md>) — Returns the first match of the regular expression within the specified range of the string.
