---
title: 'init(length:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutabledata/init(length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutabledata/init(length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutabledata/init%28length%3A%29.json'
content_hash: 'sha256:a10f00660d632280'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableData](../nsmutabledata.md)

# init(length:)

<sub>Initializer</sub>

Initializes and returns a mutable data object containing a given number of zeroed bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(length: Int)
```

## Parameters

- `length` — The number of bytes the object initially contains.

## Return Value

An initialized `NSMutableData` object containing `length` zeroed bytes. The returned object has the same memory alignment guarantees as `malloc(_:)`.

## See Also

### Creating Mutable Data

- [- initWithCapacity:](<init(capacity_).md>) — Returns an initialized mutable data object capable of holding the specified number of bytes.
