---
title: 'CFDataAppendBytes(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdataappendbytes(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdataappendbytes(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdataappendbytes%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:aeccf36e9c506442'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataAppendBytes(_:_:_:)

<sub>Function</sub>

Appends the bytes from a byte buffer to the contents of a CFData object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataAppendBytes(_ theData: CFMutableData!, _ bytes: UnsafePointer<UInt8>!, _ length: CFIndex)
```

## Parameters

- `theData` — A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.

- `bytes` — A pointer to the buffer of bytes to be added to `theData`.

- `length` — The number of bytes in the byte buffer `bytes`.

## See Also

### Modifying a Mutable Data Object

- [CFDataDeleteBytes](<cfdatadeletebytes(____).md>) — Deletes the bytes in a CFMutableData object within a specified range.
- [CFDataReplaceBytes](<cfdatareplacebytes(________).md>) — Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [CFDataIncreaseLength](<cfdataincreaselength(____).md>) — Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
- [CFDataSetLength](<cfdatasetlength(____).md>) — Resets the length of a CFMutableData object’s internal byte buffer.
