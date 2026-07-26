---
title: UIMessageConversationContext.MessageEntry
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimessageconversationcontext/messageentry
source_url: 'https://developer.apple.com/documentation/uikit/uimessageconversationcontext/messageentry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimessageconversationcontext/messageentry.json'
content_hash: 'sha256:fb1461b88b2069b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMessageConversationContext](../uimessageconversationcontext.md)

# UIMessageConversationContext.MessageEntry

<sub>Class</sub>

A class that represents a message in a message conversation.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class MessageEntry
```

## Relationships

- **Inherits From**: [Entry](../uiconversationcontext/entry.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Categorizing the entry

- [dataKind](messageentry/datakind-swift.property.md) — An item that represents the kind of data the message contains.
- [DataKind](messageentry/datakind-swift.enum.md) — A list of options that represent the kinds of data a message can contain.
- [wasSentBySelf](messageentry/wassentbyself.md) — A Boolean value that indicates whether the current user sent the message.

## See Also

### Smart Reply for messaging

- [Adopting Smart Reply in your messaging or email app](../adopting-smart-reply-in-your-messaging-or-email-app.md) — Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [UIConversationContext](../uiconversationcontext.md) — A base class that represents a conversation between participants, such as in an email or messaging app.
- [Entry](../uiconversationcontext/entry.md) — A base class that represents a message in a conversation.
- [UIMailConversationContext](../uimailconversationcontext.md) — A class that represents an email conversation.
- [MailEntry](../uimailconversationcontext/mailentry.md) — A class that represents a specific email in an email thread.
- [UIMessageConversationContext](../uimessageconversationcontext.md) — A class that represents a message conversation.
- [UIInputSuggestion](../uiinputsuggestion.md) — A base class you use to handle suggestions from the keyboard or system.
- [UIPhotoSearchSuggestion](../uiphotosearchsuggestion.md) — An input suggestion that carries photo search metadata for people, subjects, locations, and time periods. _(beta)_
- [UISmartReplySuggestion](../uismartreplysuggestion.md) — A class you use to handle a Smart Reply suggestion.
