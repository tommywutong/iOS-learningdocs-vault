---
title: 'processEditing(for:edited:range:changeInLength:invalidatedRange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextstorageobserving/processediting(for:edited:range:changeinlength:invalidatedrange:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorageobserving/processediting(for:edited:range:changeinlength:invalidatedrange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorageobserving/processediting%28for%3Aedited%3Arange%3Achangeinlength%3Ainvalidatedrange%3A%29.json'
content_hash: 'sha256:f2001bcaae6b2a31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorageObserving](../nstextstorageobserving.md)

# processEditing(for:edited:range:changeInLength:invalidatedRange:)

<sub>Instance Method</sub>

Notifies the observer that the text storage has been edited.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func processEditing(for textStorage: NSTextStorage, edited editMask: NSTextStorage.EditActions, range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)
```

## Parameters

- `textStorage` — The text storage that was edited.

- `editMask` — The type of edit.

- `newCharRange` — The range of characters that changed.

- `delta` — The change in length.

- `invalidatedCharRange` — The full invalidated range including attribute fixing.

## Discussion

The `newCharRange` is the range in the final string which was explicitly edited. The `invalidatedRange` includes portions that changed as a result of attribute fixing — it is either equal to `newCharRange` or larger. Controllers should not change the contents of the text storage during the execution of this message.

## See Also

### Managing the editing process

- [- performEditingTransactionForTextStorage:usingBlock:](<performeditingtransaction(for_using_).md>) — Performs an editing transaction on the text storage.
