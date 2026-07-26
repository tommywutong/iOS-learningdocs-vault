---
title: editedMask
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/editedmask
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/editedmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/editedmask.json'
content_hash: 'sha256:968e18010dd5d4f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# editedMask

<sub>Instance Property</sub>

A mask that describes the kinds of edits pending for the text storage object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var editedMask: NSTextStorage.EditActions { get }
```

## Discussion

This property indicates pending changes for attributes, characters, or both. Use the C bitwise AND operator to test the value against the [NSTextStorageEditedAttributes](editactions/editedattributes.md) or [NSTextStorageEditedCharacters](editactions/editedcharacters.md) constants; testing for equality fails if you add additional mask flags later. The text storage object’s associated delegate and layout managers can use this information to determine the nature of edits in their respective notification methods.

## See Also

### Determining the nature of changes

- [editedRange](editedrange.md) — The range of text that contains changes.
- [changeInLength](changeinlength.md) — The difference between the current length of the edited range and its length before editing.
