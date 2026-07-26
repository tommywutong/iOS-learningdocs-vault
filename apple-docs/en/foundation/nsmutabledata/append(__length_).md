---
title: 'append(_:length:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/append(_:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/append(_:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/append%28_%3Alength%3A%29.json'
content_hash: 'sha256:b9b31fdcf3166f3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# append(_:length:)

<sub>Instance Method</sub>

Appends to the receiver a given number of bytes from a given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func append(_ bytes: UnsafeRawPointer, length: Int)
```

## Parameters

- `bytes` — A buffer containing data to append to the receiver’s content.

- `length` — The number of bytes from `bytes` to append.

## Discussion

A sample using this method can be found in [Working With Mutable Binary Data](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/Tasks/WorkingMutableData.html#//apple_ref/doc/uid/20002150).

## See Also

### Adding Bytes

- [- appendData:](<append(__).md>) — Appends the content of another data object to the receiver.
- [- increaseLengthBy:](<increaselength(by_).md>) — Increases the length of the receiver by a given number of bytes.
