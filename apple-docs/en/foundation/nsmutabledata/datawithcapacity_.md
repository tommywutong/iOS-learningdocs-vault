---
title: 'dataWithCapacity:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/datawithcapacity:'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/datawithcapacity:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/datawithcapacity%3A.json'
content_hash: 'sha256:ff9fabf8dc144239'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# dataWithCapacity:

<sub>Type Method</sub>

Creates and returns a mutable data object capable of holding the specified number of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dataWithCapacity:(NSUInteger) aNumItems;
```

## Parameters

- `aNumItems` — The number of bytes the new data object can initially contain.

## Return Value

A new `NSMutableData` object capable of holding `aNumItems` bytes.

The returned object has the same memory alignment guarantees as `malloc(_:)`.

## Discussion

This method doesn’t necessarily allocate the requested memory right away. Mutable data objects allocate additional memory as needed, so `aNumItems` simply establishes the object’s initial capacity. When it does allocate the initial memory, though, it allocates the specified amount. This method sets the length of the data object to `0`.

If the capacity specified in `aNumItems` is greater than four memory pages in size, this method may round the amount of requested memory up to the nearest full page.

## See Also

### Related Documentation

- [Binary Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/BinaryData.html#//apple_ref/doc/uid/10000037i)

### Creating Mutable Data

- [dataWithLength:](datawithlength_.md) — Creates and returns an mutable data object containing a given number of zeroed bytes.
- [- initWithCapacity:](<init(capacity_).md>) — Returns an initialized mutable data object capable of holding the specified number of bytes.
- [- initWithLength:](<init(length_).md>) — Initializes and returns a mutable data object containing a given number of zeroed bytes.
