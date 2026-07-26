---
title: 'performEditingTransaction(for:using:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextstorageobserving/performeditingtransaction(for:using:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorageobserving/performeditingtransaction(for:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorageobserving/performeditingtransaction%28for%3Ausing%3A%29.json'
content_hash: 'sha256:883ef5aa413e4391'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextStorageObserving](../nstextstorageobserving.md)

# performEditingTransaction(for:using:)

<sub>Instance Method</sub>

Performs an editing transaction on the text storage.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func performEditingTransaction(for textStorage: NSTextStorage, using transaction: () -> Void)
```

## Parameters

- `textStorage` — The text storage.

- `transaction` — The block to execute within the transaction.

## See Also

### Managing the editing process

- [- processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:](<processediting(for_edited_range_changeinlength_invalidatedrange_).md>) — Notifies the observer that the text storage has been edited.
