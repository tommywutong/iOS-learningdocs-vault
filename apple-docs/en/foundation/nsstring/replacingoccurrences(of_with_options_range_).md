---
title: 'replacingOccurrences(of:with:options:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/replacingoccurrences(of:with:options:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/replacingoccurrences(of:with:options:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/replacingoccurrences%28of%3Awith%3Aoptions%3Arange%3A%29.json'
content_hash: 'sha256:0b62e9d058e7fb73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# replacingOccurrences(of:with:options:range:)

<sub>Instance Method</sub>

Returns a new string in which all occurrences of a target string in a specified range of the receiver are replaced by another given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingOccurrences(of target: String, with replacement: String, options: NSString.CompareOptions = [], range searchRange: NSRange) -> String
```

## Parameters

- `target` — The string to replace.

- `replacement` — The string with which to replace `target`.

- `options` — A mask of options to use when comparing `target` with the receiver. Pass `0` to specify no options.

- `searchRange` — The range in the receiver in which to search for `target`.

## Return Value

A new string in which all occurrences of `target`, matched using `options`, in `searchRange` of the receiver are replaced by `replacement`.

## See Also

### Related Documentation

- [- stringByReplacingPercentEscapesUsingEncoding:](<replacingpercentescapes(using_).md>) — Returns a new string made by replacing in the receiver all percent escapes with the matching characters as determined by a given encoding. _(deprecated)_

### Replacing Substrings

- [- stringByReplacingOccurrencesOfString:withString:](<replacingoccurrences(of_with_).md>) — Returns a new string in which all occurrences of a target string in the receiver are replaced by another given string.
- [- stringByReplacingCharactersInRange:withString:](<replacingcharacters(in_with_).md>) — Returns a new string in which the characters in a specified range of the receiver are replaced by a given string.
