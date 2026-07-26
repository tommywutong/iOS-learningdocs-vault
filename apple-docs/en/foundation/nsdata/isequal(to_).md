---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/isequal%28to%3A%29.json'
content_hash: 'sha256:a53c876a3d3d5240'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# isEqual(to:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this data object is the same as another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to other: Data) -> Bool
```

## Parameters

- `other` — The data object with which to compare the receiver.

## Return Value

[true](../../swift/true.md) if the contents of `otherData` are equal to the contents of the receiver, otherwise [false](../../swift/false.md).

## Discussion

Two data objects are equal if they hold the same number of bytes, and if the bytes at the same position in the objects are the same.

## See Also

### Testing Data

- [length](length.md) — The number of bytes contained by the data object.
