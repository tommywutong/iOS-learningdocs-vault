---
title: 'CFAttributedStringGetMutableString(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfattributedstringgetmutablestring(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfattributedstringgetmutablestring(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfattributedstringgetmutablestring%28_%3A%29.json'
content_hash: 'sha256:dd405449a1cfd726'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFAttributedStringGetMutableString(_:)

<sub>Function</sub>

Gets as a mutable string the string for an attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFAttributedStringGetMutableString(_ aStr: CFMutableAttributedString!) -> CFMutableString!
```

## Parameters

- `aStr` — The mutable attributed string from which to retrieve the string.

## Return Value

The string for the specified attributed string as a mutable string.

## Discussion

This function allows you to edit the character contents of the attributed string as if it were a CFMutableString. Attributes corresponding to the edited range are appropriately modified. If, as a result of the edit, new characters are introduced into the string, they inherit the attributes of the first replaced character from range. If no existing characters are replaced by the edit, the new characters inherit the attributes of the character preceding range if it has any, otherwise of the character following range. If the initial string is empty, the attributes for the new characters are also empty.

## See Also

### Modifying a CFMutableAttributedString

- [CFAttributedStringBeginEditing](<cfattributedstringbeginediting(__).md>) — Defers internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringEndEditing](<cfattributedstringendediting(__).md>) — Re-enables internal consistency-checking and coalescing for a mutable attributed string.
- [CFAttributedStringRemoveAttribute](<cfattributedstringremoveattribute(______).md>) — Removes the value of a single attribute over a specified range.
- [CFAttributedStringReplaceString](<cfattributedstringreplacestring(______).md>) — Modifies the string of an attributed string.
- [CFAttributedStringReplaceAttributedString](<cfattributedstringreplaceattributedstring(______).md>) — Replaces the attributed substring over a range with another attributed string.
- [CFAttributedStringSetAttribute](<cfattributedstringsetattribute(________).md>) — Sets the value of a single attribute over the specified range.
- [CFAttributedStringSetAttributes](<cfattributedstringsetattributes(________).md>) — Sets the value of attributes of a mutable attributed string over a specified range.
