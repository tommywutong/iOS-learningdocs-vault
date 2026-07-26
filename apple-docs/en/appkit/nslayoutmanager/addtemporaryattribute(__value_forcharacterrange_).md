---
title: 'addTemporaryAttribute(_:value:forCharacterRange:)'
framework: AppKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/appkit/nslayoutmanager/addtemporaryattribute(_:value:forcharacterrange:)'
source_url: 'https://developer.apple.com/documentation/appkit/nslayoutmanager/addtemporaryattribute(_:value:forcharacterrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nslayoutmanager/addtemporaryattribute%28_%3Avalue%3Aforcharacterrange%3A%29.json'
content_hash: 'sha256:89141be036ccd3ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSLayoutManager](../nslayoutmanager.md)

# addTemporaryAttribute(_:value:forCharacterRange:)

<sub>Instance Method</sub>

Adds a temporary attribute to the characters in the specified range.

<sub>macOS</sub>

```swift
func addTemporaryAttribute(_ attrName: NSAttributedString.Key, value: Any, forCharacterRange charRange: NSRange)
```

## Parameters

- `attrName` — The name of a temporary attribute.

- `value` — The temporary attribute value associated with `attrName`.

- `charRange` — The range of characters to which the specified attribute-value pair applies.

## Discussion

Raises an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if `attrName` or `value` is `nil`.

## See Also

### Managing temporary attribute support

- [- addTemporaryAttributes:forCharacterRange:](<addtemporaryattributes(__forcharacterrange_).md>) — Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [- setTemporaryAttributes:forCharacterRange:](<settemporaryattributes(__forcharacterrange_).md>) — Sets one or more temporary attributes for the specified character range.
- [- removeTemporaryAttribute:forCharacterRange:](<removetemporaryattribute(__forcharacterrange_).md>) — Removes a temporary attribute from the list of attributes for the specified character range.
- [- temporaryAttribute:atCharacterIndex:effectiveRange:](<temporaryattribute(__atcharacterindex_effectiverange_).md>) — Returns the value for the temporary attribute of a character, and the range it applies to.
- [- temporaryAttribute:atCharacterIndex:longestEffectiveRange:inRange:](<temporaryattribute(__atcharacterindex_longesteffectiverange_in_).md>) — Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [- temporaryAttributesAtCharacterIndex:effectiveRange:](<temporaryattributes(atcharacterindex_effectiverange_).md>) — Returns the dictionary of temporary attributes for the specified character range.
- [- temporaryAttributesAtCharacterIndex:longestEffectiveRange:inRange:](<temporaryattributes(atcharacterindex_longesteffectiverange_in_).md>) — Returns the temporary attributes for a character, and the maximum range they apply to.
