---
title: 'CFDataSetLength(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatasetlength(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatasetlength(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatasetlength%28_%3A_%3A%29.json'
content_hash: 'sha256:7da4b034862e5096'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataSetLength(_:_:)

<sub>Function</sub>

Resets the length of a CFMutableData object’s internal byte buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataSetLength(_ theData: CFMutableData!, _ length: CFIndex)
```

## Parameters

- `theData` — A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.

- `length` — The new size of `theData`’s byte buffer.

## Discussion

This function resets the length of a CFMutableData object’s underlying byte buffer to a new size. If that size is less than the current size, it truncates the excess bytes. If that size is greater than the current size, it zero-fills the extension to the byte buffer.

## See Also

### Modifying a Mutable Data Object

- [CFDataAppendBytes](<cfdataappendbytes(______).md>) — Appends the bytes from a byte buffer to the contents of a CFData object.
- [CFDataDeleteBytes](<cfdatadeletebytes(____).md>) — Deletes the bytes in a CFMutableData object within a specified range.
- [CFDataReplaceBytes](<cfdatareplacebytes(________).md>) — Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [CFDataIncreaseLength](<cfdataincreaselength(____).md>) — Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.
