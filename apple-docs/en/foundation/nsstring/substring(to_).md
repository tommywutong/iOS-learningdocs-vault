---
title: 'substring(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/substring(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/substring(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/substring%28to%3A%29.json'
content_hash: 'sha256:a9ca56b8c765bc33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# substring(to:)

<sub>Instance Method</sub>

Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func substring(to: Int) -> String
```

## Parameters

- `to` — An index. The value must lie within the bounds of the receiver, or be equal to the length of the receiver. Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if (`anIndex` - 1) lies beyond the end of the receiver.

## Return Value

A new string containing the characters of the receiver up to, but not including, the one at `anIndex`. If `anIndex` is equal to the length of the string, returns a copy of the receiver.

## See Also

### Dividing Strings

- [- componentsSeparatedByString:](<components(separatedby_)-238fy.md>) — Returns an array containing substrings from the receiver that have been divided by a given separator.
- [- componentsSeparatedByCharactersInSet:](<components(separatedby_)-27x9g.md>) — Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [- stringByTrimmingCharactersInSet:](<trimmingcharacters(in_).md>) — Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [- substringFromIndex:](<substring(from_).md>) — Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [- substringWithRange:](<substring(with_).md>) — Returns a string object containing the characters of the receiver that lie within a given range.
