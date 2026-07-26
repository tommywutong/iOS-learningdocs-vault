---
title: 'setTemporaryAttributes(_:forCharacterRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/settemporaryattributes(_:forcharacterrange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/settemporaryattributes(_:forcharacterrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/settemporaryattributes%28_%3Aforcharacterrange%3A%29.json'
content_hash: 'sha256:8759a906565da29e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# setTemporaryAttributes(_:forCharacterRange:)

<sub>Instance Method</sub>

Sets one or more temporary attributes for the specified character range.

<sub>macOS</sub>

```swift
func setTemporaryAttributes(_ attrs: [NSAttributedString.Key : Any], forCharacterRange charRange: NSRange)
```

## Parameters

- `attrs` — Attributes dictionary containing the temporary attributes to set.

- `charRange` — The range of characters to which the specified attributes apply.

## Discussion

Temporary attributes are used only for onscreen drawing and are not persistent in any way. `NSTextView` uses them to color misspelled words when continuous spell checking is enabled. Currently the only temporary attributes recognized are those that do not affect layout (colors, underlines, and so on).

## See Also

### Managing temporary attribute support

- [- addTemporaryAttributes:forCharacterRange:](<addtemporaryattributes(__forcharacterrange_).md>) — Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [- addTemporaryAttribute:value:forCharacterRange:](<addtemporaryattribute(__value_forcharacterrange_).md>) — Adds a temporary attribute to the characters in the specified range.
- [- removeTemporaryAttribute:forCharacterRange:](<removetemporaryattribute(__forcharacterrange_).md>) — Removes a temporary attribute from the list of attributes for the specified character range.
- [- temporaryAttribute:atCharacterIndex:effectiveRange:](<temporaryattribute(__atcharacterindex_effectiverange_).md>) — Returns the value for the temporary attribute of a character, and the range it applies to.
- [- temporaryAttribute:atCharacterIndex:longestEffectiveRange:inRange:](<temporaryattribute(__atcharacterindex_longesteffectiverange_in_).md>) — Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [- temporaryAttributesAtCharacterIndex:effectiveRange:](<temporaryattributes(atcharacterindex_effectiverange_).md>) — Returns the dictionary of temporary attributes for the specified character range.
- [- temporaryAttributesAtCharacterIndex:longestEffectiveRange:inRange:](<temporaryattributes(atcharacterindex_longesteffectiverange_in_).md>) — Returns the temporary attributes for a character, and the maximum range they apply to.
