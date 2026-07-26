---
title: UIConversationContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconversationcontext
source_url: 'https://developer.apple.com/documentation/uikit/uiconversationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconversationcontext.json'
content_hash: 'sha256:a8ea70ab1880362c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIConversationContext

<sub>Class</sub>

A base class that represents a conversation between participants, such as in an email or messaging app.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class UIConversationContext
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIMailConversationContext](uimailconversationcontext.md), [UIMessageConversationContext](uimessageconversationcontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Identifying the conversation

- [threadIdentifier](uiconversationcontext/threadidentifier.md) — A string that uniquely identifies a conversation. This identifier is persistent for the life of the conversation.

### Getting messages from the conversation

- [entries](uiconversationcontext/entries.md) — An array of messages in the conversation.

### Getting conversation participants

- [selfIdentifiers](uiconversationcontext/selfidentifiers.md) — A set of strings that identifies the active person in the conversation on the current device.
- [responsePrimaryRecipientIdentifiers](uiconversationcontext/responseprimaryrecipientidentifiers.md) — A dictionary that relates participant identifiers to participant names.
- [participantNameByIdentifier](uiconversationcontext/participantnamebyidentifier.md) — A dictionary that relates participant identifiers to participant names.

## See Also

### Smart Reply for messaging

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md) — Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [Entry](uiconversationcontext/entry.md) — A base class that represents a message in a conversation.
- [UIMailConversationContext](uimailconversationcontext.md) — A class that represents an email conversation.
- [MailEntry](uimailconversationcontext/mailentry.md) — A class that represents a specific email in an email thread.
- [UIMessageConversationContext](uimessageconversationcontext.md) — A class that represents a message conversation.
- [MessageEntry](uimessageconversationcontext/messageentry.md) — A class that represents a message in a message conversation.
- [UIInputSuggestion](uiinputsuggestion.md) — A base class you use to handle suggestions from the keyboard or system.
- [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md) — An input suggestion that carries photo search metadata for people, subjects, locations, and time periods. _(beta)_
- [UISmartReplySuggestion](uismartreplysuggestion.md) — A class you use to handle a Smart Reply suggestion.
