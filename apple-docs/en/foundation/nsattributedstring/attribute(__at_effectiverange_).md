---
title: 'attribute(_:at:effectiveRange:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsattributedstring/attribute(_:at:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsattributedstring/attribute(_:at:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsattributedstring/attribute%28_%3Aat%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:615576c1f62551e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSAttributedString](../nsattributedstring.md)

# attribute(_:at:effectiveRange:)

<sub>Instance Method</sub>

Returns the value for an attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func attribute(_ attrName: NSAttributedString.Key, at location: Int, effectiveRange range: NSRangePointer?) -> Any?
```

## Parameters

- `attrName` — The name of an attribute.

- `location` — The index for which to return attributes. This value must not exceed the bounds of the receiver. > [!important] Important > Raises an [NSRangeException](../nsexceptionname/rangeexception.md) if `index` lies beyond the end of the receiver’s characters.

- `range` — If non-`NULL`: - If the named attribute exists at `index`, upon return `aRange` contains a range over which the named attribute’s value applies. - If the named attribute does not exist at `index`, upon return `aRange` contains the range over which the attribute does not exist. The range isn’t necessarily the maximum range covered by `attributeName`, and its extent is implementation-dependent. If you need the maximum range, use [- attribute:atIndex:longestEffectiveRange:inRange:](<attribute(__at_longesteffectiverange_in_).md>). If you don’t need this value, pass `NULL`.

## Return Value

The value for the attribute named `attrName` of the character at `location`, or `nil` if there is no such attribute.

## Discussion

For a list of possible attributes, see [Key](key.md).

## See Also

### Getting attributes for a range of text

- [- attributesAtIndex:effectiveRange:](<attributes(at_effectiverange_).md>) — Returns the attributes for the character at the specified index.
- [- attributesAtIndex:longestEffectiveRange:inRange:](<attributes(at_longesteffectiverange_in_).md>) — Returns the attributes for the character at the specified index and, by reference, the range where the attributes apply.
- [- attribute:atIndex:longestEffectiveRange:inRange:](<attribute(__at_longesteffectiverange_in_).md>) — Returns the value for the attribute with the specified name of the character at the specified index and, by reference, the range where the attribute applies.
- [- enumerateAttribute:inRange:options:usingBlock:](<enumerateattribute(__in_options_using_).md>) — Executes the specified closure or block for each range of a particular attribute in the attributed string.
- [- enumerateAttributesInRange:options:usingBlock:](<enumerateattributes(in_options_using_).md>) — Executes the specified closure or block for each range of attributes in the attributed string.
- [EnumerationOptions](enumerationoptions.md) — Options for enumerating attributes.
