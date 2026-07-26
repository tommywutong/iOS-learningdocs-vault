---
title: NSTextStorageDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextstoragedelegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextstoragedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextstoragedelegate.json'
content_hash: 'sha256:3d84e296b570b4b2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextStorageDelegate

<sub>Protocol</sub>

The optional methods that delegates of text storage objects implement to handle text-edit processing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextStorageDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Processing edit actions

- [- textStorage:willProcessEditing:range:changeInLength:](<nstextstoragedelegate/textstorage(__willprocessediting_range_changeinlength_).md>) — The method the framework calls when a text storage object is about to process edits.
- [- textStorage:didProcessEditing:range:changeInLength:](<nstextstoragedelegate/textstorage(__didprocessediting_range_changeinlength_).md>) — The method the framework calls when a text storage object has finished processing edits.

## See Also

### Processing the editing actions

- [delegate](nstextstorage/delegate.md) — The delegate for the text storage object.
