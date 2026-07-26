---
title: 'replaceCharacters(in:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablestring/replacecharacters(in:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring/replacecharacters(in:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring/replacecharacters%28in%3Awith%3A%29.json'
content_hash: 'sha256:2fe11495ed0454f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableString](../nsmutablestring.md)

# replaceCharacters(in:with:)

<sub>Instance Method</sub>

Replaces the characters from `range` with those in `aString`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replaceCharacters(in range: NSRange, with aString: String)
```

## Parameters

- `range` — The range of characters to replace. `range` must not exceed the bounds of the receiver. > [!important] Important > Raises an `NSRangeException` if any part of `range` lies beyond the end of the receiver.

- `aString` — The string with which to replace the characters in `range`. `aString` must not be `nil`.

## Discussion

This method treats the length of the string as a valid range value that returns an empty string.

## See Also

### Modifying a String

- [- appendString:](<append(__).md>) — Adds to the end of the receiver the characters of a given string.
- [- applyTransform:reverse:range:updatedRange:](<applytransform(__reverse_range_updatedrange_).md>) — Transliterates the receiver by applying a specified ICU string transform.
- [- deleteCharactersInRange:](<deletecharacters(in_).md>) — Removes from the receiver the characters in a given range.
- [- insertString:atIndex:](<insert(__at_).md>) — Inserts into the receiver the characters of a given string at a given location.
- [- replaceOccurrencesOfString:withString:options:range:](<replaceoccurrences(of_with_options_range_).md>) — Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [- setString:](<setstring(__).md>) — Replaces the characters of the receiver with those in a given string.
