---
title: 'getCString(_:maxLength:encoding:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/getcstring(_:maxlength:encoding:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/getcstring(_:maxlength:encoding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/getcstring%28_%3Amaxlength%3Aencoding%3A%29.json'
content_hash: 'sha256:7a25e44c42a673b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# getCString(_:maxLength:encoding:)

<sub>Instance Method</sub>

Converts the string to a given encoding and stores it in a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getCString(_ buffer: UnsafeMutablePointer<CChar>, maxLength maxBufferCount: Int, encoding: UInt) -> Bool
```

## Parameters

- `buffer` — Upon return, contains the converted C-string plus the `NULL` termination byte. The buffer must include room for `maxBufferCount` bytes.

- `maxBufferCount` — The maximum number of bytes in the string to return in buffer (_including_ the `NULL` termination byte).

- `encoding` — The encoding for the returned C string. For possible values, see [NSStringEncoding](../nsstringencoding.md).

## Return Value

[true](../../swift/true.md) if the operation was successful, otherwise [false](../../swift/false.md). Returns [false](../../swift/false.md) if conversion is not possible due to encoding errors or if `buffer` is too small.

## Discussion

Note that in the treatment of the `maxBufferCount` argument, this method differs from the deprecated [- getCString:maxLength:](<getcstring(__maxlength_).md>) method which it replaces. (The buffer should include room for `maxBufferCount` bytes; this number should accommodate the expected size of the return value plus the `NULL` termination byte, which this method adds.)

You can use [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) to check whether a string can be losslessly converted to `encoding`. If it can’t, you can use [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) to get a C-string representation using `encoding`, allowing some loss of information (note that the data returned by [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) is not a strict C-string since it does not have a `NULL` terminator).

## See Also

### Related Documentation

- [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.

### Getting C Strings

- [- cStringUsingEncoding:](<cstring(using_).md>) — Returns a representation of the string as a C string using a given encoding.
- [UTF8String](utf8string.md) — A null-terminated UTF8 representation of the string.
