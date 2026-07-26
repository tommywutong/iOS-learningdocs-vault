---
title: 'insert(_:at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablestring/insert(_:at:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring/insert(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring/insert%28_%3Aat%3A%29.json'
content_hash: 'sha256:3e24a3c0fd4b570d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableString](../nsmutablestring.md)

# insert(_:at:)

<sub>Instance Method</sub>

Inserts into the receiver the characters of a given string at a given location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func insert(_ aString: String, at loc: Int)
```

## Parameters

- `aString` — The string to insert into the receiver. `aString` must not be `nil`.

- `loc` — The location at which `aString` is inserted. The location must not exceed the bounds of the receiver. > [!important] Important > Raises an `NSRangeException` if `loc` lies beyond the end of the string.

## Discussion

The new characters begin at `loc` and the existing characters from `loc` to the end are shifted by the length of `aString`.

This method treats the length of the string as a valid index value that returns an empty string.

## See Also

### Modifying a String

- [- appendString:](<append(__).md>) — Adds to the end of the receiver the characters of a given string.
- [- applyTransform:reverse:range:updatedRange:](<applytransform(__reverse_range_updatedrange_).md>) — Transliterates the receiver by applying a specified ICU string transform.
- [- deleteCharactersInRange:](<deletecharacters(in_).md>) — Removes from the receiver the characters in a given range.
- [- replaceCharactersInRange:withString:](<replacecharacters(in_with_).md>) — Replaces the characters from `range` with those in `aString`.
- [- replaceOccurrencesOfString:withString:options:range:](<replaceoccurrences(of_with_options_range_).md>) — Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [- setString:](<setstring(__).md>) — Replaces the characters of the receiver with those in a given string.
