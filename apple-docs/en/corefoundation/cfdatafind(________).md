---
title: 'CFDataFind(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatafind(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatafind(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatafind%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:feb5fa9196b804ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataFind(_:_:_:_:)

<sub>Function</sub>

Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataFind(_ theData: CFData!, _ dataToFind: CFData!, _ searchRange: CFRange, _ compareOptions: CFDataSearchFlags) -> CFRange
```

## Parameters

- `theData` — The data object within which to search.

- `dataToFind` — The data to find. Must not be `NULL`.

- `searchRange` — The range within `theData` to be searched.

- `compareOptions` — A bit mask specifying search options. The [CFDataSearchFlags](cfdatasearchflags.md) options can be specified singly or combined with the C bitwise `OR` operator

## Return Value

The range representing the location and length of `dataToFind` within `searchRange`, modulo the options in `compareOptions`. The range returned is relative to the start of the searched data, not the passed-in search range. Returns [kCFNotFound](kcfnotfound.md) if `dataToFind` is not found.

## See Also

### Examining a CFData Object

- [CFDataGetBytePtr](<cfdatagetbyteptr(__).md>) — Returns a read-only pointer to the bytes of a CFData object.
- [CFDataGetBytes](<cfdatagetbytes(______).md>) — Copies the byte contents of a CFData object to an external buffer.
- [CFDataGetLength](<cfdatagetlength(__).md>) — Returns the number of bytes contained by a CFData object.
