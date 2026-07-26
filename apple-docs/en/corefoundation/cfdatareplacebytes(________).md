---
title: 'CFDataReplaceBytes(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatareplacebytes(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatareplacebytes(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatareplacebytes%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f014734b8439edf6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataReplaceBytes(_:_:_:_:)

<sub>Function</sub>

Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataReplaceBytes(_ theData: CFMutableData!, _ range: CFRange, _ newBytes: UnsafePointer<UInt8>!, _ newLength: CFIndex)
```

## Parameters

- `theData` — A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.

- `range` — The range of bytes (that is, the starting byte and the number of bytes from that point) to delete from `theData`’s byte buffer.

- `newBytes` — A pointer to the buffer containing the replacement bytes.

- `newLength` — The number of bytes in the byte buffer `newBytes`.

## See Also

### Modifying a Mutable Data Object

- [CFDataAppendBytes](<cfdataappendbytes(______).md>) — Appends the bytes from a byte buffer to the contents of a CFData object.
- [CFDataDeleteBytes](<cfdatadeletebytes(____).md>) — Deletes the bytes in a CFMutableData object within a specified range.
- [CFDataIncreaseLength](<cfdataincreaselength(____).md>) — Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
- [CFDataSetLength](<cfdatasetlength(____).md>) — Resets the length of a CFMutableData object’s internal byte buffer.
