---
title: 'CFDataIncreaseLength(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdataincreaselength(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdataincreaselength(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdataincreaselength%28_%3A_%3A%29.json'
content_hash: 'sha256:b6eefbe627b389cb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDataIncreaseLength(_:_:)

<sub>Function</sub>

Increases the length of a CFMutableData object’s internal byte buffer, zero-filling the extension to the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDataIncreaseLength(_ theData: CFMutableData!, _ extraLength: CFIndex)
```

## Parameters

- `theData` — A CFMutableData object. If you pass an immutable CFData object, the behavior is not defined.

- `extraLength` — The number of bytes by which to increase the byte buffer.

## Discussion

This function increases the length of a CFMutableData object’s underlying byte buffer to a new size, initializing the new bytes to `0`.

## See Also

### Modifying a Mutable Data Object

- [CFDataAppendBytes](<cfdataappendbytes(______).md>) — Appends the bytes from a byte buffer to the contents of a CFData object.
- [CFDataDeleteBytes](<cfdatadeletebytes(____).md>) — Deletes the bytes in a CFMutableData object within a specified range.
- [CFDataReplaceBytes](<cfdatareplacebytes(________).md>) — Replaces those bytes in a CFMutableData object that fall within a specified range with other bytes.
- [CFDataSetLength](<cfdatasetlength(____).md>) — Resets the length of a CFMutableData object’s internal byte buffer.
