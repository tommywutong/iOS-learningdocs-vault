---
title: 'CFDataGetLength(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatagetlength(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatagetlength(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatagetlength%28_%3A%29.json'
content_hash: 'sha256:f3980952df6a1a2d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataGetLength(_:)

<sub>Function</sub>

Returns the number of bytes contained by a CFData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataGetLength(_ theData: CFData!) -> CFIndex
```

## Parameters

- `theData` — The CFData object to examine.

## Return Value

An index that specifies the number of bytes in `theData`.

## See Also

### Examining a CFData Object

- [CFDataGetBytePtr](<cfdatagetbyteptr(__).md>) — Returns a read-only pointer to the bytes of a CFData object.
- [CFDataGetBytes](<cfdatagetbytes(______).md>) — Copies the byte contents of a CFData object to an external buffer.
- [CFDataFind](<cfdatafind(________).md>) — Finds and returns the range within a data object of the first occurrence of the given data, within a given range, subject to any given options.
