---
title: NSTextContentStorageDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextcontentstoragedelegate
source_url: 'https://developer.apple.com/documentation/uikit/nstextcontentstoragedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextcontentstoragedelegate.json'
content_hash: 'sha256:c5fd5108050da4a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextContentStorageDelegate

<sub>Protocol</sub>

The optional methods that delegates of content storage objects implement to handle content processing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol NSTextContentStorageDelegate : NSTextContentManagerDelegate
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTextContentManagerDelegate](nstextcontentmanagerdelegate.md)

## Topics

### Working with paragraphs

- [- textContentStorage:textParagraphWithRange:](<nstextcontentstoragedelegate/textcontentstorage(__textparagraphwith_).md>) — Returns a custom paragraph for a range that you provide from the object’s attributed string.

## See Also

### Accessing paragraphs

- [delegate](nstextcontentstorage/delegate.md) — The delegate for the content storage object.
