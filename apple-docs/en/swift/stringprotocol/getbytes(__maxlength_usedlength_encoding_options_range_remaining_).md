---
title: 'getBytes(_:maxLength:usedLength:encoding:options:range:remaining:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/getbytes(_:maxlength:usedlength:encoding:options:range:remaining:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/getbytes%28_%3Amaxlength%3Ausedlength%3Aencoding%3Aoptions%3Arange%3Aremaining%3A%29.json'
content_hash: 'sha256:6e4552e567f3bab5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# getBytes(_:maxLength:usedLength:encoding:options:range:remaining:)

<sub>Instance Method</sub>

Writes the given `range` of characters into `buffer` in a given `encoding`, without any allocations.  Does not NULL-terminate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getBytes<R>(_ buffer: inout [UInt8], maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>, encoding: String.Encoding, options: String.EncodingConversionOptions = [], range: R, remaining leftover: UnsafeMutablePointer<Range<Self.Index>>) -> Bool where R : RangeExpression, R.Bound == String.Index
```

## Parameters

- `buffer` — A buffer into which to store the bytes from the receiver. The returned bytes are not NUL-terminated.

- `maxBufferCount` — The maximum number of bytes to write to buffer.

- `usedBufferCount` — The number of bytes used from buffer. Pass `nil` if you do not need this value.

- `encoding` — The encoding to use for the returned bytes.

- `options` — A mask to specify options to use for converting the receiver’s contents to `encoding` (if conversion is necessary).

- `range` — The range of characters in the receiver to get.

- `leftover` — The remaining range. Pass `nil` If you do not need this value.

## Return Value

`true` if some characters were converted, `false` otherwise.

## Discussion

> [!note] Note
> Conversion stops when the buffer fills or when the conversion isn’t possible due to the chosen encoding.

> [!note] Note
> Will get a maximum of `min(buffer.count, maxLength)` bytes.
