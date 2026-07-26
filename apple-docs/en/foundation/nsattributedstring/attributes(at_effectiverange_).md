---
title: 'attributes(at:effectiveRange:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/attributes(at:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/attributes(at:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/attributes%28at%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:36f3c821ca0cd2b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# attributes(at:effectiveRange:)

<sub>Instance Method</sub>

Returns the attributes for the character at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attributes(at location: Int, effectiveRange range: NSRangePointer?) -> [NSAttributedString.Key : Any]
```

## Parameters

- `location` — The index for which to return attributes. This value must lie within the bounds of the receiver.

- `range` — Upon return, the range over which the attributes and values are the same as those at `index`. This range isn’t necessarily the maximum range covered, and its extent is implementation-dependent. If you need the maximum range, use [- attributesAtIndex:longestEffectiveRange:inRange:](<attributes(at_longesteffectiverange_in_).md>). If you don’t need this value, pass `NULL`.

## Return Value

The attributes for the character at `index`.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `index` lies beyond the end of the receiver’s characters.

For a list of possible attributes, see [Key](key.md).

## See Also

### Getting attributes for a range of text

- [- attributesAtIndex:longestEffectiveRange:inRange:](<attributes(at_longesteffectiverange_in_).md>) — Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [- attribute:atIndex:effectiveRange:](<attribute(__at_effectiverange_).md>) — Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- attribute:atIndex:longestEffectiveRange:inRange:](<attribute(__at_longesteffectiverange_in_).md>) — Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- enumerateAttribute:inRange:options:usingBlock:](<enumerateattribute(__in_options_using_).md>) — Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [- enumerateAttributesInRange:options:usingBlock:](<enumerateattributes(in_options_using_).md>) — Executes the specified closure or block for each range of attributes in the attributed string.
- [EnumerationOptions](enumerationoptions.md) — Options for enumerating attributes.
