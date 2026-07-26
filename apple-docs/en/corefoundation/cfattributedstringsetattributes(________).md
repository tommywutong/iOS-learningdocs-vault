---
title: 'CFAttributedStringSetAttributes(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringsetattributes(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringsetattributes(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringsetattributes%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0ede92b5eeba7859'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringSetAttributes(_:_:_:_:)

<sub>Function</sub>

Sets the value of attributes of a mutable attributed string over a specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringSetAttributes(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ replacement: CFDictionary!, _ clearOtherAttributes: Bool)
```

## Parameters

- `aStr` — The mutable attributed string to modify.

- `range` — The range of aStr over to which the new attributes apply. `range` must not exceed the bounds of `aStr`.

- `replacement` — A dictionary that contains key-value pairs that specify the new attributes to apply to `range`. The keys must be CFString objects, and the corresponding values must be CFType objects.

- `clearOtherAttributes` — If `false`, existing attributes (that aren’t being replaced) are left alone; otherwise they are cleared.

## Discussion

Note that after this call, if it is mutable, changes to `replacement` will not affect the contents of the attributed string.

## See Also

### Modifying a CFMutableAttributedString

- [CFAttributedStringBeginEditing](<cfattributedstringbeginediting(__).md>) — Defers internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>) — Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringGetMutableString](<cfattributedstringgetmutablestring(__).md>) — Gets as a mutable string the string for an attributed string.
- [CFAttributedStringRemoveAttribute](<cfattributedstringremoveattribute(______).md>) — Removes the value of a single attribute over a specified range.
- [CFAttributedStringReplaceString](<cfattributedstringreplacestring(______).md>) — Modifies the string of an attributed string.
- [CFAttributedStringReplaceAttributedString](<cfattributedstringreplaceattributedstring(______).md>) — Replaces the attributed substring over a range with another attributed string.
- [CFAttributedStringSetAttribute](<cfattributedstringsetattribute(________).md>) — Sets the value of a single attribute over the specified range.
