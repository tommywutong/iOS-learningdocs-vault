---
title: 'CFDataGetBytePtr(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatagetbyteptr(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatagetbyteptr(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatagetbyteptr%28_%3A%29.json'
content_hash: 'sha256:2ded00dc2c1dca5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataGetBytePtr(_:)

<sub>Function</sub>

Returns a read-only pointer to the bytes of a CFData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataGetBytePtr(_ theData: CFData!) -> UnsafePointer<UInt8>!
```

## Parameters

- `theData` — The CFData object to examine.

## Return Value

A read-only pointer to the bytes associated with `theData`.

## Discussion

This function is guaranteed to return a pointer to a CFData object’s internal bytes. CFData, unlike CFString, does not hide its internal storage.

## See Also

### Examining a CFData Object

- [CFDataGetBytes](<cfdatagetbytes(______).md>) — Copies the byte contents of a CFData object to an external buffer.
- [CFDataGetLength](<cfdatagetlength(__).md>) — Returns the number of bytes contained by a CFData object.
- [CFDataFind](<cfdatafind(________).md>) — Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.
