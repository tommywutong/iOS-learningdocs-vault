---
title: 'attributes(at:longestEffectiveRange:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/attributes(at:longesteffectiverange:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/attributes(at:longesteffectiverange:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/attributes%28at%3Alongesteffectiverange%3Ain%3A%29.json'
content_hash: 'sha256:d9662ac827d0aee5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# attributes(at:longestEffectiveRange:in:)

<sub>Instance Method</sub>

Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attributes(at location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> [NSAttributedString.Key : Any]
```

## Parameters

- `location` — The index for which to return attributes. This value must not exceed the bounds of the receiver.

- `range` — If non-`NULL`, upon return contains the maximum range over which the attributes and values are the same as those at `index`, clipped to `rangeLimit`.

- `rangeLimit` — The range over which to search for continuous presence of the attributes at `index`. This value must not exceed the bounds of the receiver.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `index` or any part of `rangeLimit` lies beyond the end of the receiver’s characters.

If you don’t need the range information, it’s far more efficient to use the [- attributesAtIndex:effectiveRange:](<attributes(at_effectiverange_).md>) method to retrieve the attribute value.

For a list of possible attributes, see [Key](key.md).

## See Also

### Getting attributes for a range of text

- [- attributesAtIndex:effectiveRange:](<attributes(at_effectiverange_).md>) — Returns the attributes for the character at the specified index.
- [- attribute:atIndex:effectiveRange:](<attribute(__at_effectiverange_).md>) — Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- attribute:atIndex:longestEffectiveRange:inRange:](<attribute(__at_longesteffectiverange_in_).md>) — Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- enumerateAttribute:inRange:options:usingBlock:](<enumerateattribute(__in_options_using_).md>) — Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [- enumerateAttributesInRange:options:usingBlock:](<enumerateattributes(in_options_using_).md>) — Executes the specified closure or block for each range of attributes in the attributed string.
- [EnumerationOptions](enumerationoptions.md) — Options for enumerating attributes.
