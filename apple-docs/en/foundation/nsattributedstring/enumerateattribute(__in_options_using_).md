---
title: 'enumerateAttribute(_:in:options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/enumerateattribute(_:in:options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/enumerateattribute(_:in:options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/enumerateattribute%28_%3Ain%3Aoptions%3Ausing%3A%29.json'
content_hash: 'sha256:3b05e8a4495d9a3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# enumerateAttribute(_:in:options:using:)

<sub>Instance Method</sub>

Executes the specified closure or block for each range of a particular attribute in the attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateAttribute(_ attrName: NSAttributedString.Key, in enumerationRange: NSRange, options opts: NSAttributedString.EnumerationOptions = [], using block: (Any?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `attrName` — The name of the attribute to enumerate.

- `enumerationRange` — The range over which the attribute values are enumerated.

- `opts` — The options used by the enumeration. For possible values, see [EnumerationOptions](enumerationoptions.md).

- `block` — A closure or block to apply to ranges of the specified attribute in the attributed string, taking three arguments: - The value for the specified attribute. - The range of the attribute value in the attributed string. - A reference to a Boolean value, which you can set to [true](../../swift/true.md) within the closure to stop further processing of the attributed string.

## Discussion

If this method is called by an instance of [NSMutableAttributedString](../nsmutableattributedstring.md), mutation (deletion, addition, or change) is allowed only if the mutation is within the range provided to the block. After a mutation, the enumeration continues with the range immediately following the processed range, adjusting for any change in length caused by the mutation. For example, if `block` is called with a range starting at location `N`, and the block deletes all the characters in the provided range, the next call will also pass `N` as the location of the range.

## See Also

### Getting attributes for a range of text

- [- attributesAtIndex:effectiveRange:](<attributes(at_effectiverange_).md>) — Returns the attributes for the character at the specified index.
- [- attributesAtIndex:longestEffectiveRange:inRange:](<attributes(at_longesteffectiverange_in_).md>) — Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [- attribute:atIndex:effectiveRange:](<attribute(__at_effectiverange_).md>) — Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- attribute:atIndex:longestEffectiveRange:inRange:](<attribute(__at_longesteffectiverange_in_).md>) — Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- enumerateAttributesInRange:options:usingBlock:](<enumerateattributes(in_options_using_).md>) — Executes the specified closure or block for each range of attributes in the attributed string.
- [EnumerationOptions](enumerationoptions.md) — Options for enumerating attributes.
