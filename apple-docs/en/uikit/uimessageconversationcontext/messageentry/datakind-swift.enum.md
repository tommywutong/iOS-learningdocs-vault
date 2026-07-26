---
title: UIMessageConversationContext.MessageEntry.DataKind
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimessageconversationcontext/messageentry/datakind-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uimessageconversationcontext/messageentry/datakind-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimessageconversationcontext/messageentry/datakind-swift.enum.json'
content_hash: 'sha256:479e2ab5fbeea863'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIMessageConversationContext](../../uimessageconversationcontext.md) · [MessageEntry](../messageentry.md)

# UIMessageConversationContext.MessageEntry.DataKind

<sub>Enumeration</sub>

A list of options that represent the kinds of data a message can contain.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum DataKind
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Kinds of data in a message

- [UIMessageConversationEntryDataKindAttachment](datakind-swift.enum/attachment.md) — The message contains an attachment, such as an image or file.
- [UIMessageConversationEntryDataKindOther](datakind-swift.enum/other.md) — The message contains other data, such as data that represents a sticker or a payment.
- [UIMessageConversationEntryDataKindText](datakind-swift.enum/text.md) — The message contains text.

### Initializers

- [init(rawValue:)](<datakind-swift.enum/init(rawvalue_).md>)

## See Also

### Categorizing the entry

- [dataKind](datakind-swift.property.md) — An item that represents the kind of data the message contains.
- [wasSentBySelf](wassentbyself.md) — A Boolean value that indicates whether the current user sent the message.
