---
title: 'CFDataGetBytes(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatagetbytes(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatagetbytes(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatagetbytes%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3dc48ec6601b2c7d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataGetBytes(_:_:_:)

<sub>Function</sub>

Copies the byte contents of a CFData object to an external buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataGetBytes(_ theData: CFData!, _ range: CFRange, _ buffer: UnsafeMutablePointer<UInt8>!)
```

## Parameters

- `theData` — The CFData object to examine.

- `range` — The range of bytes in `theData` to get. To get all of the contents, pass `CFRangeMake(0,CFDataGetLength(theData))`.

- `buffer` — A pointer to the byte buffer of length `range.length` that is allocated on the stack or heap. On return, the buffer contains the requested range of bytes.

## See Also

### Examining a CFData Object

- [CFDataGetBytePtr](<cfdatagetbyteptr(__).md>) — Returns a read-only pointer to the bytes of a CFData object.
- [CFDataGetLength](<cfdatagetlength(__).md>) — Returns the number of bytes contained by a CFData object.
- [CFDataFind](<cfdatafind(________).md>) — Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.
