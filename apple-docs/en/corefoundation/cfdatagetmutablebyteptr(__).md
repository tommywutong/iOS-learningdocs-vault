---
title: 'CFDataGetMutableBytePtr(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatagetmutablebyteptr(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatagetmutablebyteptr(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatagetmutablebyteptr%28_%3A%29.json'
content_hash: 'sha256:a8092abc734fcef5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataGetMutableBytePtr(_:)

<sub>Function</sub>

Returns a pointer to a mutable byte buffer of a CFMutableData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataGetMutableBytePtr(_ theData: CFMutableData!) -> UnsafeMutablePointer<UInt8>!
```

## Parameters

- `theData` — A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.

## Return Value

A pointer to the bytes associated with `theData`.

## Discussion

If the length of `theData`‘s data is not zero, this function is guaranteed to return a pointer to a CFMutableData object’s internal bytes. If the length of `theData`’s data _is_ zero, this function may or may not return `NULL` dependent upon many factors related to how the object was created (moreover, in this case the function result might change between different releases and on different platforms).
