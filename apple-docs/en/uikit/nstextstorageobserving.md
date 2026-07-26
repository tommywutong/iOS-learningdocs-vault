---
title: NSTextStorageObserving
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstorageobserving
source_url: 'https://developer.apple.com/documentation/uikit/nstextstorageobserving'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstorageobserving.json'
content_hash: 'sha256:a75ca5afd6effdd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextStorageObserving

<sub>Protocol</sub>

Optional methods that delegates implement to handle editing and transaction processing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextStorageObserving : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [NSTextContentStorage](nstextcontentstorage.md)

## Topics

### Accessing the text storage

- [textStorage](nstextstorageobserving/textstorage.md) — The document text storage object.

### Managing the editing process

- [- performEditingTransactionForTextStorage:usingBlock:](<nstextstorageobserving/performeditingtransaction(for_using_).md>) — Performs an editing transaction on the text storage.
- [- processEditingForTextStorage:edited:range:changeInLength:invalidatedRange:](<nstextstorageobserving/processediting(for_edited_range_changeinlength_invalidatedrange_).md>) — Notifies the observer that the text storage has been edited.

## See Also

### Accessing the storage controller

- [textStorageObserver](nstextstorage/textstorageobserver.md) — The observer for the text storage object.
