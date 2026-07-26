---
title: 'textStorage(_:willProcessEditing:range:changeInLength:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextstoragedelegate/textstorage(_:willprocessediting:range:changeinlength:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextstoragedelegate/textstorage(_:willprocessediting:range:changeinlength:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstoragedelegate/textstorage%28_%3Awillprocessediting%3Arange%3Achangeinlength%3A%29.json'
content_hash: 'sha256:8055e418c7df7366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorageDelegate](../nstextstoragedelegate.md)

# textStorage(_:willProcessEditing:range:changeInLength:)

<sub>Instance Method</sub>

The method the framework calls when a text storage object is about to process edits.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func textStorage(_ textStorage: NSTextStorage, willProcessEditing editedMask: NSTextStorage.EditActions, range editedRange: NSRange, changeInLength delta: Int)
```

## Parameters

- `textStorage` — The text storage object processing edits.

- `editedMask` — The types of edits to do: [NSTextStorageEditedAttributes](../nstextstorage/editactions/editedattributes.md), [NSTextStorageEditedCharacters](../nstextstorage/editactions/editedcharacters.md), or both.

- `editedRange` — The range in the original string (before the edit).

- `delta` — The length delta for the editing changes.

## Discussion

Sent inside [- processEditing](<../nstextstorage/processediting().md>) right before fixing attributes. Delegates can change the characters or attributes.

The delegate can verify the changed state of the text storage object and make changes to the text storage object’s characters or attributes to enforce whatever constraints it establishes. Programmatic changes don’t cause the object to send this message.

## See Also

### Processing edit actions

- [- textStorage:didProcessEditing:range:changeInLength:](<textstorage(__didprocessediting_range_changeinlength_).md>) — The method the framework calls when a text storage object has finished processing edits.
