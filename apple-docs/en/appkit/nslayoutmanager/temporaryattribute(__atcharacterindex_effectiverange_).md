---
title: 'temporaryAttribute(_:atCharacterIndex:effectiveRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/temporaryattribute(_:atcharacterindex:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/temporaryattribute(_:atcharacterindex:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/temporaryattribute%28_%3Aatcharacterindex%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:478838e32aaa14cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# temporaryAttribute(_:atCharacterIndex:effectiveRange:)

<sub>Instance Method</sub>

Returns the value for the temporary attribute of a character, and the range it applies to.

<sub>macOS</sub>

```swift
func temporaryAttribute(_ attrName: NSAttributedString.Key, atCharacterIndex location: Int, effectiveRange range: NSRangePointer?) -> Any?
```

## Parameters

- `attrName` — The name of a temporary attribute.

- `location` — The index for which to return attributes. This value must not exceed the bounds of the receiver.

- `range` — If non-`NULL`: - If the named attribute exists at `location`, on output, contains the range over which the named attribute’s value applies. - If the named attribute does not exist at `location`, on output, contains the range over which the attribute does not exist. The range isn’t necessarily the maximum range covered by `attrName`, and its extent is implementation-dependent. If you need the maximum range, use [- temporaryAttribute:atCharacterIndex:longestEffectiveRange:inRange:](<temporaryattribute(__atcharacterindex_longesteffectiverange_in_).md>). If you don’t need this value, pass `NULL`.

## Return Value

The value for the temporary attribute named `attrName` of the character at index `location`, or `nil` if there is no such attribute.

## See Also

### Managing temporary attribute support

- [- addTemporaryAttributes:forCharacterRange:](<addtemporaryattributes(__forcharacterrange_).md>) — Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [- addTemporaryAttribute:value:forCharacterRange:](<addtemporaryattribute(__value_forcharacterrange_).md>) — Adds a temporary attribute to the characters in the specified range.
- [- setTemporaryAttributes:forCharacterRange:](<settemporaryattributes(__forcharacterrange_).md>) — Sets one or more temporary attributes for the specified character range.
- [- removeTemporaryAttribute:forCharacterRange:](<removetemporaryattribute(__forcharacterrange_).md>) — Removes a temporary attribute from the list of attributes for the specified character range.
- [- temporaryAttribute:atCharacterIndex:longestEffectiveRange:inRange:](<temporaryattribute(__atcharacterindex_longesteffectiverange_in_).md>) — Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [- temporaryAttributesAtCharacterIndex:effectiveRange:](<temporaryattributes(atcharacterindex_effectiverange_).md>) — Returns the dictionary of temporary attributes for the specified character range.
- [- temporaryAttributesAtCharacterIndex:longestEffectiveRange:inRange:](<temporaryattributes(atcharacterindex_longesteffectiverange_in_).md>) — Returns the temporary attributes for a character, and the maximum range they apply to.
