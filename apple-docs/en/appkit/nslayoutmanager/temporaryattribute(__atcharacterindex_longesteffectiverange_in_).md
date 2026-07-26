---
title: 'temporaryAttribute(_:atCharacterIndex:longestEffectiveRange:in:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/temporaryattribute(_:atcharacterindex:longesteffectiverange:in:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/temporaryattribute(_:atcharacterindex:longesteffectiverange:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/temporaryattribute%28_%3Aatcharacterindex%3Alongesteffectiverange%3Ain%3A%29.json'
content_hash: 'sha256:3abde7041fe05f03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# temporaryAttribute(_:atCharacterIndex:longestEffectiveRange:in:)

<sub>Instance Method</sub>

Returns the value for the temporary attribute of a character, and the maximum range it applies to.

<sub>macOS</sub>

```swift
func temporaryAttribute(_ attrName: NSAttributedString.Key, atCharacterIndex location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> Any?
```

## Parameters

- `attrName` — The name of a temporary attribute.

- `location` — The index for which to return attributes. This value must not exceed the bounds of the receiver.

- `range` — If non-`NULL`: - If the named attribute exists at `location`, on output, contains the maximum range over which the named attribute’s value applies, clipped to `rangeLimit`. - If the named attribute does not exist at `location`, on output, contains the maximum range over which the attribute does not exist. If you don’t need this value, pass `NULL`.

- `rangeLimit` — The range over which to search for continuous presence of `attrName`. This value must not exceed the bounds of the receiver.

## Return Value

The value for the attribute named `attrName` of the character at `location`, or `nil` if there is no such attribute.

## Discussion

If you don’t need the longest effective range, it’s far more efficient to use the [- temporaryAttribute:atCharacterIndex:effectiveRange:](<temporaryattribute(__atcharacterindex_effectiverange_).md>) method to retrieve the attribute value.

## See Also

### Managing temporary attribute support

- [- addTemporaryAttributes:forCharacterRange:](<addtemporaryattributes(__forcharacterrange_).md>) — Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [- addTemporaryAttribute:value:forCharacterRange:](<addtemporaryattribute(__value_forcharacterrange_).md>) — Adds a temporary attribute to the characters in the specified range.
- [- setTemporaryAttributes:forCharacterRange:](<settemporaryattributes(__forcharacterrange_).md>) — Sets one or more temporary attributes for the specified character range.
- [- removeTemporaryAttribute:forCharacterRange:](<removetemporaryattribute(__forcharacterrange_).md>) — Removes a temporary attribute from the list of attributes for the specified character range.
- [- temporaryAttribute:atCharacterIndex:effectiveRange:](<temporaryattribute(__atcharacterindex_effectiverange_).md>) — Returns the value for the temporary attribute of a character, and the range it applies to.
- [- temporaryAttributesAtCharacterIndex:effectiveRange:](<temporaryattributes(atcharacterindex_effectiverange_).md>) — Returns the dictionary of temporary attributes for the specified character range.
- [- temporaryAttributesAtCharacterIndex:longestEffectiveRange:inRange:](<temporaryattributes(atcharacterindex_longesteffectiverange_in_).md>) — Returns the temporary attributes for a character, and the maximum range they apply to.
