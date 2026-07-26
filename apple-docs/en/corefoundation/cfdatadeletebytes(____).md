---
title: 'CFDataDeleteBytes(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatadeletebytes(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatadeletebytes(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatadeletebytes%28_%3A_%3A%29.json'
content_hash: 'sha256:d8cb4e1984881e12'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataDeleteBytes(_:_:)

<sub>Function</sub>

Deletes the bytes in a CFMutableData object within a specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataDeleteBytes(_ theData: CFMutableData!, _ range: CFRange)
```

## Parameters

- `theData` — A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.

- `range` — The range of bytes (that is, the starting byte and the number of bytes from that point) to delete from `theData`’s byte buffer.

## See Also

### Modifying a Mutable Data Object

- [CFDataAppendBytes](<cfdataappendbytes(______).md>) — Appends the bytes from a byte buffer to the contents of a CFData object.
- [CFDataReplaceBytes](<cfdatareplacebytes(________).md>) — Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [CFDataIncreaseLength](<cfdataincreaselength(____).md>) — Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
- [CFDataSetLength](<cfdatasetlength(____).md>) — Resets the length of a CFMutableData object’s internal byte buffer.
