---
title: editedRange
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/editedrange
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/editedrange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/editedrange.json'
content_hash: 'sha256:85c9e9efe0ee17d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# editedRange

<sub>Instance Property</sub>

The range of text that contains changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var editedRange: NSRange { get }
```

## Discussion

The specified range can reflect changes to characters or attributes. The text storage object’s delegate and layout managers can use this information to determine the nature of edits in their respective notification methods.

## See Also

### Determining the nature of changes

- [editedMask](editedmask.md) — A mask that describes the kinds of edits pending for the text storage object.
- [changeInLength](changeinlength.md) — The difference between the current length of the edited range and its length before editing.
