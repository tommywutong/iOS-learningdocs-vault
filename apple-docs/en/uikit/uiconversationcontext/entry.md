---
title: UIConversationContext.Entry
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconversationcontext/entry
source_url: 'https://developer.apple.com/documentation/uikit/uiconversationcontext/entry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconversationcontext/entry.json'
content_hash: 'sha256:a65f741936848643'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConversationContext](../uiconversationcontext.md)

# UIConversationContext.Entry

<sub>Class</sub>

A base class that represents a message in a conversation.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class Entry
```

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Inherited By**: [MailEntry](../uimailconversationcontext/mailentry.md), [MessageEntry](../uimessageconversationcontext/messageentry.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Identifying the entry

- [entryIdentifier](entry/entryidentifier.md) — A string that uniquely identifies this specific entry in the conversation.
- [replyThreadIdentifier](entry/replythreadidentifier.md) — An optional string that identifies another message in a conversation, when this entry is a reply to that message.

### Getting entry details

- [text](entry/text.md) — A string that contains the message’s text.
- [sentDate](entry/sentdate.md) — A date that notes when the sender added the message to the conversation.

### Identifying entry participants

- [senderIdentifier](entry/senderidentifier.md) — A string that identifies the message’s sender.
- [primaryRecipientIdentifiers](entry/primaryrecipientidentifiers.md) — A set of strings that identifies the primary recipients of the message.

## See Also

### Smart Reply for messaging

- [Adopting Smart Reply in your messaging or email app](../adopting-smart-reply-in-your-messaging-or-email-app.md) — Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [UIConversationContext](../uiconversationcontext.md) — A base class that represents a conversation between participants, such as in an email or messaging app.
- [UIMailConversationContext](../uimailconversationcontext.md) — A class that represents an email conversation.
- [MailEntry](../uimailconversationcontext/mailentry.md) — A class that represents a specific email in an email thread.
- [UIMessageConversationContext](../uimessageconversationcontext.md) — A class that represents a message conversation.
- [MessageEntry](../uimessageconversationcontext/messageentry.md) — A class that represents a message in a message conversation.
- [UIInputSuggestion](../uiinputsuggestion.md) — A base class you use to handle suggestions from the keyboard or system.
- [UIPhotoSearchSuggestion](../uiphotosearchsuggestion.md) — An input suggestion that carries photo search metadata for people, subjects, locations, and time periods. _(beta)_
- [UISmartReplySuggestion](../uismartreplysuggestion.md) — A class you use to handle a Smart Reply suggestion.
