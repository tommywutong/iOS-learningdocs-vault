---
title: 'replacingCharacters(in:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/replacingcharacters(in:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/replacingcharacters(in:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/replacingcharacters%28in%3Awith%3A%29.json'
content_hash: 'sha256:50b6e0b53a006432'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# replacingCharacters(in:with:)

<sub>Instance Method</sub>

Returns a new string in which the characters in a specified range of the receiver are replaced by a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingCharacters(in range: NSRange, with replacement: String) -> String
```

## Parameters

- `range` — A range of characters in the receiver.

- `replacement` — The string with which to replace the characters in `range`.

## Return Value

A new string in which the characters in `range` of the receiver are replaced by `replacement`.

## See Also

### Related Documentation

- [- stringByReplacingPercentEscapesUsingEncoding:](<replacingpercentescapes(using_).md>) — Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding. _(deprecated)_

### Replacing Substrings

- [- stringByReplacingOccurrencesOfString:withString:](<replacingoccurrences(of_with_).md>) — Returns a new string in which all occurrences of a target string in the receiver are replaced by another given string.
- [- stringByReplacingOccurrencesOfString:withString:options:range:](<replacingoccurrences(of_with_options_range_).md>) — Returns a new string in which all occurrences of a target string in a specified range of the receiver are replaced by another given string.
