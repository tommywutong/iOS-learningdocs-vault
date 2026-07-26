---
title: 'replaceOccurrences(of:with:options:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablestring/replaceoccurrences(of:with:options:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring/replaceoccurrences(of:with:options:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring/replaceoccurrences%28of%3Awith%3Aoptions%3Arange%3A%29.json'
content_hash: 'sha256:d2f1d436b3ff7b8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableString](../nsmutablestring.md)

# replaceOccurrences(of:with:options:range:)

<sub>Instance Method</sub>

Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceOccurrences(of target: String, with replacement: String, options: NSString.CompareOptions = [], range searchRange: NSRange) -> Int
```

## Parameters

- `target` — The string to replace. > [!important] Important > Raises an `NSInvalidArgumentException` if `target` is `nil`.

- `replacement` — The string with which to replace `target`. > [!important] Important > Raises an `NSInvalidArgumentException` if `replacement` is `nil`.

- `options` — A mask specifying search options. See [String Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/introStrings.html#//apple_ref/doc/uid/10000035i) for details. If `opts` is `NSBackwardsSearch`, the search is done from the end of the range. If `opts` is `NSAnchoredSearch`, only anchored (but potentially multiple) instances are replaced. `NSLiteralSearch` and `NSCaseInsensitiveSearch` also apply.

- `searchRange` — The range of characters to replace. `searchRange` must not exceed the bounds of the receiver. Specify `searchRange` as `NSMakeRange(0, [receiver length])` to process the entire string. > [!important] Important > Raises an `NSRangeException` if any part of `searchRange` lies beyond the end of the receiver.

## Return Value

The number of replacements made.

## Discussion

This method treats the length of the string as a valid range value that returns an empty string.

## See Also

### Modifying a String

- [- appendString:](<append(__).md>) — Adds to the end of the receiver the characters of a given string.
- [- applyTransform:reverse:range:updatedRange:](<applytransform(__reverse_range_updatedrange_).md>) — Transliterates the receiver by applying a specified ICU string transform.
- [- deleteCharactersInRange:](<deletecharacters(in_).md>) — Removes from the receiver the characters in a given range.
- [- insertString:atIndex:](<insert(__at_).md>) — Inserts into the receiver the characters of a given string at a given location.
- [- replaceCharactersInRange:withString:](<replacecharacters(in_with_).md>) — Replaces the characters from `range` with those in `aString`.
- [- setString:](<setstring(__).md>) — Replaces the characters of the receiver with those in a given string.
