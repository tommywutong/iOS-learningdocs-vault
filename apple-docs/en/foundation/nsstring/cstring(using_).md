---
title: 'cString(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/cstring(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/cstring(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/cstring%28using%3A%29.json'
content_hash: 'sha256:f42baabc7984d295'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# cString(using:)

<sub>Instance Method</sub>

Returns a representation of the string as a C string using a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cString(using encoding: UInt) -> UnsafePointer<CChar>?
```

## Parameters

- `encoding` — The encoding for the returned C string. For possible values, see [NSStringEncoding](../nsstringencoding.md).

## Return Value

A C string representation of the receiver using the encoding specified by `encoding`. Returns `NULL` if the receiver cannot be losslessly converted to `encoding`.

## Discussion

The returned C string is guaranteed to be valid only until either the receiver is freed, or until the current memory is emptied, whichever occurs first. You should copy the C string or use [- getCString:maxLength:encoding:](<getcstring(__maxlength_encoding_).md>) if it needs to store the C string beyond this time.

You can use [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) to check whether a string can be losslessly converted to `encoding`. If it can’t, you can use [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) to get a C-string representation using `encoding`, allowing some loss of information (note that the data returned by [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) is not a strict C-string since it does not have a `NULL` terminator).

### Special Considerations

UTF-16 and UTF-32 are not considered to be C string encodings, and should not be used with this method—the results of passing [NSUTF16StringEncoding](../nsutf16stringencoding.md), [NSUTF32StringEncoding](../nsutf32stringencoding.md), or any of their variants are undefined.

## See Also

### Related Documentation

- [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [- getCString:](<getcstring(__).md>) — Invokes [- getCString:maxLength:range:remainingRange:](<getcstring(__maxlength_range_remaining_).md>) with `NSMaximumStringLength` as the maximum length, the receiver’s entire extent as the range, and `NULL` for the remaining range. _(deprecated)_
- [- cStringLength](<cstringlength().md>) — Returns the length in char-sized units of the receiver’s C-string representation in the default C-string encoding. _(deprecated)_
- [defaultCStringEncoding](defaultcstringencoding.md) — Returns the C-string encoding assumed for any method accepting a C string as an argument.

### Getting C Strings

- [- getCString:maxLength:encoding:](<getcstring(__maxlength_encoding_).md>) — Converts the string to a given encoding and stores it in a buffer.
- [UTF8String](utf8string.md) — A null-terminated UTF8 representation of the string.
