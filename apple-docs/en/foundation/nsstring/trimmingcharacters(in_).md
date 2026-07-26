---
title: 'trimmingCharacters(in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/trimmingcharacters(in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/trimmingcharacters(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/trimmingcharacters%28in%3A%29.json'
content_hash: 'sha256:5a15d8ab66b0b350'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# trimmingCharacters(in:)

<sub>Instance Method</sub>

Returns a new string made by removing from both ends of the receiver characters contained in a given character set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func trimmingCharacters(in set: CharacterSet) -> String
```

## Parameters

- `set` — A character set containing the characters to remove from the receiver. `set` must not be `nil`.

## Return Value

A new string made by removing from both ends of the receiver characters contained in `set`. If the receiver is composed entirely of characters from `set`, the empty string is returned.

## Discussion

Use [whitespaceCharacterSet](../nscharacterset/whitespaces.md) or [whitespaceAndNewlineCharacterSet](../nscharacterset/whitespacesandnewlines.md) to remove whitespace around strings.

## See Also

### Dividing Strings

- [- componentsSeparatedByString:](<components(separatedby_)-238fy.md>) — Returns an array containing substrings from the receiver that have been divided by a given separator.
- [- componentsSeparatedByCharactersInSet:](<components(separatedby_)-27x9g.md>) — Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [- substringFromIndex:](<substring(from_).md>) — Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [- substringWithRange:](<substring(with_).md>) — Returns a string object containing the characters of the receiver that lie within a given range.
- [- substringToIndex:](<substring(to_).md>) — Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.
