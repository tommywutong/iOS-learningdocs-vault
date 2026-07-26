---
title: changeInLength
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/changeinlength
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/changeinlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/changeinlength.json'
content_hash: 'sha256:62d5771398790bc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# changeInLength

<sub>Instance Property</sub>

The difference between the current length of the edited range and its length before editing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var changeInLength: Int { get }
```

## Discussion

This property reflects difference between the current length of the edited range and its length before editing began—that is, before the first call to the [beginEditing()](<../../foundation/nsmutableattributedstring/beginediting().md>) method or a single call to the[- edited:range:changeInLength:](<edited(__range_changeinlength_).md>) method. This difference is accumulated with each call to the [- edited:range:changeInLength:](<edited(__range_changeinlength_).md>) method, until the changes are finally processed.

The text storage object’s delegate and layout managers can use this information to determine the nature of edits in their respective notification methods.

## See Also

### Determining the nature of changes

- [editedMask](editedmask.md) — A mask that describes the kinds of edits pending for the text storage object.
- [editedRange](editedrange.md) — The range of text that contains changes.
