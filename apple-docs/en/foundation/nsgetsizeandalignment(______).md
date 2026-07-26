---
title: 'NSGetSizeAndAlignment(_:_:_:)'
framework: Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsgetsizeandalignment(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsgetsizeandalignment(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsgetsizeandalignment%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:443d20fd06c81fbe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSGetSizeAndAlignment(_:_:_:)

<sub>Function</sub>

Obtains the actual size and the aligned size of an encoded type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func NSGetSizeAndAlignment(_ typePtr: UnsafePointer<CChar>, _ sizep: UnsafeMutablePointer<Int>?, _ alignp: UnsafeMutablePointer<Int>?) -> UnsafePointer<CChar>
```

## Discussion

Obtains the actual size and the aligned size of the first data type represented by `typePtr` and returns a pointer to the position of the next data type in `typePtr`. You can specify `NULL` for either `sizep` or `alignp` to ignore the corresponding information.

The value returned in `alignp` is the aligned size of the data type; for example, on some platforms, the aligned size of a `char` might be 2 bytes while the actual physical size is 1 byte.
