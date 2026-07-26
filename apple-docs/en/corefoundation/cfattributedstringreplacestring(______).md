---
title: 'CFAttributedStringReplaceString(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringreplacestring(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringreplacestring(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringreplacestring%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3a259e1e56613ebb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringReplaceString(_:_:_:)

<sub>Function</sub>

Modifies the string of an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringReplaceString(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ replacement: CFString!)
```

## Parameters

- `aStr` — The mutable attributed string to modify.

- `range` — The range of `aStr` to be modified. `range` must not specify characters outside the bounds of `aStr`.

- `replacement` — The string to replace the existing string in `range`.

## See Also

### Modifying a CFMutableAttributedString

- [CFAttributedStringBeginEditing](<cfattributedstringbeginediting(__).md>) — Defers internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>) — Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringGetMutableString](<cfattributedstringgetmutablestring(__).md>) — Gets as a mutable string the string for an attributed string.
- [CFAttributedStringRemoveAttribute](<cfattributedstringremoveattribute(______).md>) — Removes the value of a single attribute over a specified range.
- [CFAttributedStringReplaceAttributedString](<cfattributedstringreplaceattributedstring(______).md>) — Replaces the attributed substring over a range with another attributed string.
- [CFAttributedStringSetAttribute](<cfattributedstringsetattribute(________).md>) — Sets the value of a single attribute over the specified range.
- [CFAttributedStringSetAttributes](<cfattributedstringsetattributes(________).md>) — Sets the value of attributes of a mutable attributed string over a specified range.
