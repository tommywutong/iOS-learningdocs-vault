---
title: 'textStorage(_:didProcessEditing:range:changeInLength:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextstoragedelegate/textstorage(_:didprocessediting:range:changeinlength:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextstoragedelegate/textstorage(_:didprocessediting:range:changeinlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstoragedelegate/textstorage%28_%3Adidprocessediting%3Arange%3Achangeinlength%3A%29.json'
content_hash: 'sha256:bf9a853a961a8c1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorageDelegate](../nstextstoragedelegate.md)

# textStorage(_:didProcessEditing:range:changeInLength:)

<sub>Instance Method</sub>

The method the framework calls when a text storage object has finished processing edits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textStorage(_ textStorage: NSTextStorage, didProcessEditing editedMask: NSTextStorage.EditActions, range editedRange: NSRange, changeInLength delta: Int)
```

## Parameters

- `textStorage` — The text storage object processing edits.

- `editedMask` — The types of edits done: [NSTextStorageEditedAttributes](../nstextstorage/editactions/editedattributes.md), [NSTextStorageEditedCharacters](../nstextstorage/editactions/editedcharacters.md), or both.

- `editedRange` — The range in the original string (before the edit).

- `delta` — The length delta for the editing changes.

## Discussion

Sent inside [- processEditing](<../nstextstorage/processediting().md>) right before notifying layout managers. Delegates can change the attributes.

The delegate can verify the final state of the text storage object; it can’t change the text storage object’s characters without leaving it in an inconsistent state, but if necessary it can change attributes. Note that even in this case it’s possible to put a text storage object into an inconsistent state—for example, by changing the font of a range to one that doesn’t support the characters in that range, such as using a Latin font for Kanji text.

## See Also

### Processing edit actions

- [- textStorage:willProcessEditing:range:changeInLength:](<textstorage(__willprocessediting_range_changeinlength_).md>) — The method the framework calls when a text storage object is about to process edits.
