---
title: 'CFAttributedStringSetAttribute(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringsetattribute(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringsetattribute(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringsetattribute%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:27be256ec46f05b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringSetAttribute(_:_:_:_:)

<sub>Function</sub>

Sets the value of a single attribute over the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringSetAttribute(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ attrName: CFString!, _ value: CFTypeRef!)
```

## Parameters

- `aStr` — The mutable attributed string to modify.

- `range` — The range of `aStr` over to which the new attributes apply. `range` must not exceed the bounds of `aStr`.

- `attrName` — The name of the attribute whose value to set.

- `value` — The value of the attribute `attrName` to apply over `range`. This value may not be `NULL`. If you want to remove an attribute, use [CFAttributedStringRemoveAttribute](<cfattributedstringremoveattribute(______).md>).

## See Also

### Modifying a CFMutableAttributedString

- [CFAttributedStringBeginEditing](<cfattributedstringbeginediting(__).md>) — Defers internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>) — Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringGetMutableString](<cfattributedstringgetmutablestring(__).md>) — Gets as a mutable string the string for an attributed string.
- [CFAttributedStringRemoveAttribute](<cfattributedstringremoveattribute(______).md>) — Removes the value of a single attribute over a specified range.
- [CFAttributedStringReplaceString](<cfattributedstringreplacestring(______).md>) — Modifies the string of an attributed string.
- [CFAttributedStringReplaceAttributedString](<cfattributedstringreplaceattributedstring(______).md>) — Replaces the attributed substring over a range with another attributed string.
- [CFAttributedStringSetAttributes](<cfattributedstringsetattributes(________).md>) — Sets the value of attributes of a mutable attributed string over a specified range.
