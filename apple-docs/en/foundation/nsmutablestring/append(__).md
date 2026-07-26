---
title: 'append(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablestring/append(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablestring/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablestring/append%28_%3A%29.json'
content_hash: 'sha256:feddc3005dc1caf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableString](../nsmutablestring.md)

# append(_:)

<sub>Instance Method</sub>

Adds to the end of the receiver the characters of a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func append(_ aString: String)
```

## Parameters

- `aString` — The string to append to the receiver. `aString` must not be `nil`

## See Also

### Modifying a String

- [- applyTransform:reverse:range:updatedRange:](<applytransform(__reverse_range_updatedrange_).md>) — Transliterates the receiver by applying a specified ICU string transform.
- [- deleteCharactersInRange:](<deletecharacters(in_).md>) — Removes from the receiver the characters in a given range.
- [- insertString:atIndex:](<insert(__at_).md>) — Inserts into the receiver the characters of a given string at a given location.
- [- replaceCharactersInRange:withString:](<replacecharacters(in_with_).md>) — Replaces the characters from `range` with those in `aString`.
- [- replaceOccurrencesOfString:withString:options:range:](<replaceoccurrences(of_with_options_range_).md>) — Replaces all occurrences of a given string in a given range with another given string, returning the number of replacements.
- [- setString:](<setstring(__).md>) — Replaces the characters of the receiver with those in a given string.
