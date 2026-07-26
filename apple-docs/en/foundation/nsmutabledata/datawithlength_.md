---
title: 'dataWithLength:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/datawithlength:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/datawithlength:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/datawithlength%3A.json'
content_hash: 'sha256:fa16d87fbd2cd85a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# dataWithLength:

<sub>Type Method</sub>

Creates and returns an mutable data object containing a given number of zeroed bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dataWithLength:(NSUInteger) length;
```

## Parameters

- `length` — The number of bytes the new data object initially contains.

## Return Value

A new `NSMutableData` object of `length` bytes, filled with zeros. The returned object has the same memory alignment guarantees as `malloc(_:)`.

## See Also

### Creating Mutable Data

- [dataWithCapacity:](datawithcapacity_.md) — Creates and returns a mutable data object capable of holding the specified number of bytes.
- [- initWithCapacity:](<init(capacity_).md>) — Returns an initialized mutable data object capable of holding the specified number of bytes.
- [- initWithLength:](<init(length_).md>) — Initializes and returns a mutable data object containing a given number of zeroed bytes.
