---
title: processEditing()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorage/processediting()
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorage/processediting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorage/processediting%28%29.json'
content_hash: 'sha256:46c24dd128c9e760'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorage](../nstextstorage.md)

# processEditing()

<sub>Instance Method</sub>

Cleans up changes to the text storage object and notifies its delegate and layout managers of changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func processEditing()
```

## Discussion

This method is automatically invoked in response to an [- edited:range:changeInLength:](<edited(__range_changeinlength_).md>) message or an [endEditing()](<../../foundation/nsmutableattributedstring/endediting().md>) message if edits were made within the scope of a [beginEditing()](<../../foundation/nsmutableattributedstring/beginediting().md>) block. You should never need to invoke it directly.

This method begins by posting an [NSTextStorageWillProcessEditingNotification](willprocesseditingnotification.md) to the default notification center (which results in the delegate receiving a [- textStorage:willProcessEditing:range:changeInLength:](<../nstextstoragedelegate/textstorage(__willprocessediting_range_changeinlength_).md>) message). Then it fixes attributes. After this, it posts an [NSTextStorageDidProcessEditingNotification](didprocesseditingnotification.md) to the default notification center (which results in the delegate receiving a [- textStorage:didProcessEditing:range:changeInLength:](<../nstextstoragedelegate/textstorage(__didprocessediting_range_changeinlength_).md>) message). Finally, it sends a [textStorage(_:edited:range:changeInLength:invalidatedRange:)](<../../appkit/nslayoutmanager/textstorage(__edited_range_changeinlength_invalidatedrange_).md>) message to each of the receiver’s layout managers using the argument values provided.

## See Also

### Managing edits

- [- edited:range:changeInLength:](<edited(__range_changeinlength_).md>) — Tracks changes made to the text storage object, allowing the text storage to record the full extent of changes.
