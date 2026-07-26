---
title: 'temporaryAttributes(atCharacterIndex:effectiveRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/temporaryattributes(atcharacterindex:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/temporaryattributes(atcharacterindex:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/temporaryattributes%28atcharacterindex%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:ae8bbf3cec07fb78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# temporaryAttributes(atCharacterIndex:effectiveRange:)

<sub>Instance Method</sub>

Returns the dictionary of temporary attributes for the specified character range.

<sub>macOS</sub>

```swift
func temporaryAttributes(atCharacterIndex charIndex: Int, effectiveRange effectiveCharRange: NSRangePointer?) -> [NSAttributedString.Key : Any]
```

## Return Value

The dictionary of temporary attributes for the character range specified in `effectiveCharRange` at character index `charIndex`.

## Discussion

Temporary attributes are used only for onscreen drawing and are not persistent in any way. `NSTextView` uses them to color misspelled words when continuous spell checking is enabled. Currently the only temporary attributes recognized are those that do not affect layout (colors, underlines, and so on).

## See Also

### Managing temporary attribute support

- [- addTemporaryAttributes:forCharacterRange:](<addtemporaryattributes(__forcharacterrange_).md>) — Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [- addTemporaryAttribute:value:forCharacterRange:](<addtemporaryattribute(__value_forcharacterrange_).md>) — Adds a temporary attribute to the characters in the specified range.
- [- setTemporaryAttributes:forCharacterRange:](<settemporaryattributes(__forcharacterrange_).md>) — Sets one or more temporary attributes for the specified character range.
- [- removeTemporaryAttribute:forCharacterRange:](<removetemporaryattribute(__forcharacterrange_).md>) — Removes a temporary attribute from the list of attributes for the specified character range.
- [- temporaryAttribute:atCharacterIndex:effectiveRange:](<temporaryattribute(__atcharacterindex_effectiverange_).md>) — Returns the value for the temporary attribute of a character, and the range it applies to.
- [- temporaryAttribute:atCharacterIndex:longestEffectiveRange:inRange:](<temporaryattribute(__atcharacterindex_longesteffectiverange_in_).md>) — Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [- temporaryAttributesAtCharacterIndex:longestEffectiveRange:inRange:](<temporaryattributes(atcharacterindex_longesteffectiverange_in_).md>) — Returns the temporary attributes for a character, and the maximum range they apply to.
