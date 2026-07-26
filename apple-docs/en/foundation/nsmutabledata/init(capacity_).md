---
title: 'init(capacity:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/init(capacity:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/init(capacity:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/init%28capacity%3A%29.json'
content_hash: 'sha256:269d9343cf42275a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# init(capacity:)

<sub>Initializer</sub>

Returns an initialized mutable data object capable of holding the specified number of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(capacity: Int)
```

## Parameters

- `capacity` — The number of bytes the data object can initially contain.

## Return Value

An initialized `NSMutableData` object capable of holding `capacity` bytes. The returned object has the same memory alignment guarantees as `malloc(_:)`.

## Discussion

This method doesn’t necessarily allocate the requested memory right away. Mutable data objects allocate additional memory as needed, so `capacity` simply establishes the object’s initial capacity. When it does allocate the initial memory, though, it allocates the specified amount. This method sets the length of the data object to `0`.

If the capacity specified in `capacity` is greater than four memory pages in size, this method may round the amount of requested memory up to the nearest full page.

## See Also

### Creating Mutable Data

- [- initWithLength:](<init(length_).md>) — Initializes and returns a mutable data object containing a given number of zeroed bytes.
