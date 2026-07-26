---
title: 'deleteCharacters(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablestring/deletecharacters(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring/deletecharacters(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring/deletecharacters%28in%3A%29.json'
content_hash: 'sha256:308f98c7e762260d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableString](../nsmutablestring.md)

# deleteCharacters(in:)

<sub>Instance Method</sub>

Removes from the receiver the characters in a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deleteCharacters(in range: NSRange)
```

## Parameters

- `range` — The range of characters to delete. `range` must not exceed the bounds of the receiver. > [!important] Important > Raises an `NSRangeException` if any part of `range` lies beyond the end of the string.

## Discussion

This method treats the length of the string as a valid range value that returns an empty string.

## See Also

### Modifying a String

- [- appendString:](<append(__).md>) — Adds to the end of the receiver the characters of a given string.
- [- applyTransform:reverse:range:updatedRange:](<applytransform(__reverse_range_updatedrange_).md>) — Transliterates the receiver by applying a specified ICU string transform.
- [- insertString:atIndex:](<insert(__at_).md>) — Inserts into the receiver the characters of a given string at a given location.
- [- replaceCharactersInRange:withString:](<replacecharacters(in_with_).md>) — Replaces the characters from `range` with those in `aString`.
- [- replaceOccurrencesOfString:withString:options:range:](<replaceoccurrences(of_with_options_range_).md>) — Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [- setString:](<setstring(__).md>) — Replaces the characters of the receiver with those in a given string.
