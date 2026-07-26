---
title: 'CFAttributedStringRemoveAttribute(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringremoveattribute(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringremoveattribute(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringremoveattribute%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c0117e330d74da06'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringRemoveAttribute(_:_:_:)

<sub>Function</sub>

Removes the value of a single attribute over a specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringRemoveAttribute(_ aStr: CFMutableAttributedString!, _ range: CFRange, _ attrName: CFString!)
```

## Parameters

- `aStr` — The mutable attributed string to modify.

- `range` — The range of `aStr` from which to remove the specified attribute. `range` must not exceed the bounds of `aStr`.

- `attrName` — The name of the attribute to remove.

## Discussion

It is _not_ an error of the specified attribute does not exist over the given range.

## See Also

### Modifying a CFMutableAttributedString

- [CFAttributedStringBeginEditing](<cfattributedstringbeginediting(__).md>) — Defers internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>) — Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringGetMutableString](<cfattributedstringgetmutablestring(__).md>) — Gets as a mutable string the string for an attributed string.
- [CFAttributedStringReplaceString](<cfattributedstringreplacestring(______).md>) — Modifies the string of an attributed string.
- [CFAttributedStringReplaceAttributedString](<cfattributedstringreplaceattributedstring(______).md>) — Replaces the attributed substring over a range with another attributed string.
- [CFAttributedStringSetAttribute](<cfattributedstringsetattribute(________).md>) — Sets the value of a single attribute over the specified range.
- [CFAttributedStringSetAttributes](<cfattributedstringsetattributes(________).md>) — Sets the value of attributes of a mutable attributed string over a specified range.
