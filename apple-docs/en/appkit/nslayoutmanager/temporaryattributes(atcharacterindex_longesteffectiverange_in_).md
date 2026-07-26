---
title: 'temporaryAttributes(atCharacterIndex:longestEffectiveRange:in:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/temporaryattributes(atcharacterindex:longesteffectiverange:in:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/temporaryattributes(atcharacterindex:longesteffectiverange:in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/temporaryattributes%28atcharacterindex%3Alongesteffectiverange%3Ain%3A%29.json'
content_hash: 'sha256:4aa607636192fa81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# temporaryAttributes(atCharacterIndex:longestEffectiveRange:in:)

<sub>Instance Method</sub>

Returns the temporary attributes for a character, and the maximum range they apply to.

<sub>macOS</sub>

```swift
func temporaryAttributes(atCharacterIndex location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> [NSAttributedString.Key : Any]
```

## Parameters

- `location` — The index for which to return attributes. This value must not exceed the bounds of the receiver.

- `range` — If not `NULL`, on output, contains the maximum range over which the attributes and values are the same as those at `location`, clipped to `rangeLimit`.

- `rangeLimit` — The range over which to search for continuous presence of the attributes at `location`. This value must not exceed the bounds of the receiver.

## Return Value

The attributes for the character at `location`.

## Discussion

If you don’t need the longest effective range, it’s far more efficient to use the [- temporaryAttributesAtCharacterIndex:effectiveRange:](<temporaryattributes(atcharacterindex_effectiverange_).md>) method to retrieve the attribute value.

## See Also

### Managing temporary attribute support

- [- addTemporaryAttributes:forCharacterRange:](<addtemporaryattributes(__forcharacterrange_).md>) — Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [- addTemporaryAttribute:value:forCharacterRange:](<addtemporaryattribute(__value_forcharacterrange_).md>) — Adds a temporary attribute to the characters in the specified range.
- [- setTemporaryAttributes:forCharacterRange:](<settemporaryattributes(__forcharacterrange_).md>) — Sets one or more temporary attributes for the specified character range.
- [- removeTemporaryAttribute:forCharacterRange:](<removetemporaryattribute(__forcharacterrange_).md>) — Removes a temporary attribute from the list of attributes for the specified character range.
- [- temporaryAttribute:atCharacterIndex:effectiveRange:](<temporaryattribute(__atcharacterindex_effectiverange_).md>) — Returns the value for the temporary attribute of a character, and the range it applies to.
- [- temporaryAttribute:atCharacterIndex:longestEffectiveRange:inRange:](<temporaryattribute(__atcharacterindex_longesteffectiverange_in_).md>) — Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [- temporaryAttributesAtCharacterIndex:effectiveRange:](<temporaryattributes(atcharacterindex_effectiverange_).md>) — Returns the dictionary of temporary attributes for the specified character range.
