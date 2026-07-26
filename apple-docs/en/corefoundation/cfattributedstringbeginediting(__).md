---
title: 'CFAttributedStringBeginEditing(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringbeginediting(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringbeginediting(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringbeginediting%28_%3A%29.json'
content_hash: 'sha256:fe9fdc0df4386aba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringBeginEditing(_:)

<sub>Function</sub>

Defers internal consistency-checking and coalescing for a mutable attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringBeginEditing(_ aStr: CFMutableAttributedString!)
```

## Parameters

- `aStr` — A mutable attributed string that is to be edited.

## Discussion

Defers internal consistency-checking and coalescing for a mutable attributed string. You must balance a call to this function with a corresponding [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>).

## See Also

### Modifying a CFMutableAttributedString

- [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>) — Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringGetMutableString](<cfattributedstringgetmutablestring(__).md>) — Gets as a mutable string the string for an attributed string.
- [CFAttributedStringRemoveAttribute](<cfattributedstringremoveattribute(______).md>) — Removes the value of a single attribute over a specified range.
- [CFAttributedStringReplaceString](<cfattributedstringreplacestring(______).md>) — Modifies the string of an attributed string.
- [CFAttributedStringReplaceAttributedString](<cfattributedstringreplaceattributedstring(______).md>) — Replaces the attributed substring over a range with another attributed string.
- [CFAttributedStringSetAttribute](<cfattributedstringsetattribute(________).md>) — Sets the value of a single attribute over the specified range.
- [CFAttributedStringSetAttributes](<cfattributedstringsetattributes(________).md>) — Sets the value of attributes of a mutable attributed string over a specified range.
