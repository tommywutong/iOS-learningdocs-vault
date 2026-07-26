---
title: 'maximumLengthOfBytes(using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/maximumlengthofbytes(using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/maximumlengthofbytes(using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/maximumlengthofbytes%28using%3A%29.json'
content_hash: 'sha256:64b443ceec3a9431'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# maximumLengthOfBytes(using:)

<sub>Instance Method</sub>

Returns the maximum number of bytes needed to store the receiver in a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func maximumLengthOfBytes(using enc: UInt) -> Int
```

## Parameters

- `enc` — The encoding for which to determine the receiver’s length.

## Return Value

The maximum number of bytes needed to store the receiver in `encoding` in a non-external representation. The length does not include space for a terminating `NULL` character. Returns `0` if the amount of memory required for storing the results of the encoding conversion would exceed [NSIntegerMax](../../objectivec/nsintegermax.md).

## Discussion

The result is an estimate and is returned in `O(1)` time; the estimate may be considerably greater than the actual length needed.

## See Also

### Getting a String’s Length

- [length](length.md) — The number of UTF-16 code units in the receiver.
- [- lengthOfBytesUsingEncoding:](<lengthofbytes(using_).md>) — Returns the number of bytes required to store the receiver in a given encoding.
