---
title: 'getBytes(_:maxLength:usedLength:encoding:options:range:remaining:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/getbytes%28_%3Amaxlength%3Ausedlength%3Aencoding%3Aoptions%3Arange%3Aremaining%3A%29.json'
content_hash: 'sha256:ffe26134bd7833be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# getBytes(_:maxLength:usedLength:encoding:options:range:remaining:)

<sub>Instance Method</sub>

Gets a given range of characters as bytes in a specified encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getBytes(_ buffer: UnsafeMutableRawPointer?, maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>?, encoding: UInt, options: NSString.EncodingConversionOptions = [], range: NSRange, remaining leftover: NSRangePointer?) -> Bool
```

## Parameters

- `buffer` — A buffer into which to store the bytes from the receiver. The returned bytes are _not_ `NULL`-terminated.

- `maxBufferCount` — The maximum number of bytes to write to `buffer`.

- `usedBufferCount` — The number of bytes used from `buffer`. Pass `NULL` if you do not need this value.

- `encoding` — The encoding to use for the returned bytes. For possible values, see [NSStringEncoding](../nsstringencoding.md).

- `options` — A mask to specify options to use for converting the receiver’s contents to `encoding` (if conversion is necessary).

- `range` — The range of characters in the receiver to get.

- `leftover` — The remaining range. Pass `NULL` If you do not need this value.

## Return Value

[true](../../swift/true.md) if some characters were converted, otherwise [false](../../swift/false.md).

## Discussion

Conversion might stop when the buffer fills, but it might also stop when the conversion isn’t possible due to the chosen encoding.

## See Also

### Getting Characters and Bytes

- [- characterAtIndex:](<character(at_).md>) — Returns the character at a given UTF-16 code unit index.
- [- getCharacters:range:](<getcharacters(__range_).md>) — Copies characters from a given range in the receiver into a given buffer.
