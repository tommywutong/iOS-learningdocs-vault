---
title: 'components(separatedBy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/components(separatedby:)-27x9g'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/components(separatedby:)-27x9g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/components%28separatedby%3A%29-27x9g.json'
content_hash: 'sha256:942d3d93efb6d030'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# components(separatedBy:)

<sub>Instance Method</sub>

Returns an array containing substrings from the receiver that have been divided by characters in a given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func components(separatedBy separator: CharacterSet) -> [String]
```

## Parameters

- `separator` — A character set containing the characters to use to split the receiver. Must not be `nil`.

## Return Value

An `NSArray` object containing substrings from the receiver that have been divided by characters in `separator`.

## Discussion

The substrings in the array appear in the order they did in the receiver. Adjacent occurrences of the separator characters produce empty strings in the result. Similarly, if the string begins or ends with separator characters, the first or last substring, respectively, is empty.

## See Also

### Dividing Strings

- [- componentsSeparatedByString:](<components(separatedby_)-238fy.md>) — Returns an array containing substrings from the receiver that have been divided by a given separator.
- [- stringByTrimmingCharactersInSet:](<trimmingcharacters(in_).md>) — Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [- substringFromIndex:](<substring(from_).md>) — Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [- substringWithRange:](<substring(with_).md>) — Returns a string object containing the characters of the receiver that lie within a given range.
- [- substringToIndex:](<substring(to_).md>) — Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.
