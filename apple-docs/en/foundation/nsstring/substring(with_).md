---
title: 'substring(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/substring(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/substring(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/substring%28with%3A%29.json'
content_hash: 'sha256:e8381340a61f36ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# substring(with:)

<sub>Instance Method</sub>

Returns a string object containing the characters of the receiver that lie within a given range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func substring(with range: NSRange) -> String
```

## Parameters

- `range` — A range. The range must not exceed the bounds of the receiver. Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if (`aRange.location` - 1) or (`aRange.location` + `aRange.length` - 1) lies beyond the end of the receiver.

## Return Value

A string object containing the characters of the receiver that lie within `aRange`.

## Discussion

This method detects all invalid ranges (including those with negative lengths). For applications linked against macOS 10.6 and later, this error causes an exception; for applications linked against earlier releases, this error causes a warning, which is displayed just once per application execution.

## See Also

### Dividing Strings

- [- componentsSeparatedByString:](<components(separatedby_)-238fy.md>) — Returns an array containing substrings from the receiver that have been divided by a given separator.
- [- componentsSeparatedByCharactersInSet:](<components(separatedby_)-27x9g.md>) — Returns an array containing substrings from the receiver that have been divided by characters in a given set.
- [- stringByTrimmingCharactersInSet:](<trimmingcharacters(in_).md>) — Returns a new string made by removing from both ends of the receiver characters contained in a given character set.
- [- substringFromIndex:](<substring(from_).md>) — Returns a new string containing the characters of the receiver from the one at a given index to the end.
- [- substringToIndex:](<substring(to_).md>) — Returns a new string containing the characters of the receiver up to, but not including, the one at a given index.
