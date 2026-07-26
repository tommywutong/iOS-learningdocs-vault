---
title: 'attribute(_:at:longestEffectiveRange:in:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/attribute(_:at:longesteffectiverange:in:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/attribute(_:at:longesteffectiverange:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/attribute%28_%3Aat%3Alongesteffectiverange%3Ain%3A%29.json'
content_hash: 'sha256:d931f32cb02d2aba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# attribute(_:at:longestEffectiveRange:in:)

<sub>Instance Method</sub>

Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attribute(_ attrName: NSAttributedString.Key, at location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> Any?
```

## Parameters

- `attrName` — The name of an attribute.

- `location` — The index at which to test for `attributeName`.

- `range` — If non-`NULL`: - If the named attribute exists at `index`, upon return `aRange` contains the full range over which the value of the named attribute is the same as that at `index`, clipped to `rangeLimit`. - If the named attribute does not exist at `index`, upon return `aRange` contains the full range over which the attribute does not exist, clipped to `rangeLimit`. If you don’t need this value, pass `NULL`.

- `rangeLimit` — The range over which to search for continuous presence of `attributeName`. This value must not exceed the bounds of the receiver.

## Return Value

The value for the attribute named `attributeName` of the character at `index`, or `nil` if there is no such attribute.

## Discussion

Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `index` or any part of `rangeLimit` lies beyond the end of the receiver’s characters.

If you don’t need the longest effective range, it’s far more efficient to use the [- attribute:atIndex:effectiveRange:](<attribute(__at_effectiverange_).md>) method to retrieve the attribute value.

For a list of possible attributes, see [Key](key.md).

## See Also

### Getting attributes for a range of text

- [- attributesAtIndex:effectiveRange:](<attributes(at_effectiverange_).md>) — Returns the attributes for the character at the specified index.
- [- attributesAtIndex:longestEffectiveRange:inRange:](<attributes(at_longesteffectiverange_in_).md>) — Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [- attribute:atIndex:effectiveRange:](<attribute(__at_effectiverange_).md>) — Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- enumerateAttribute:inRange:options:usingBlock:](<enumerateattribute(__in_options_using_).md>) — Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [- enumerateAttributesInRange:options:usingBlock:](<enumerateattributes(in_options_using_).md>) — Executes the specified closure or block for each range of attributes in the attributed string.
- [EnumerationOptions](enumerationoptions.md) — Options for enumerating attributes.
