---
title: UIMailConversationContext
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimailconversationcontext
source_url: 'https://developer.apple.com/documentation/uikit/uimailconversationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimailconversationcontext.json'
content_hash: 'sha256:6aff85f23217ad5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMailConversationContext

<sub>Class</sub>

A class that represents an email conversation.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class UIMailConversationContext
```

## Relationships

- **Inherits From**: [UIConversationContext](uiconversationcontext.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting message details

- [responseSubject](uimailconversationcontext/responsesubject.md) — A string that contains the subject line of an intended response.
- [responseHasCustomSignature](uimailconversationcontext/responsehascustomsignature.md) — A Boolean value that indicates whether the intended response contains a custom signature.
- [responseSecondaryRecipientIdentifiers](uimailconversationcontext/responsesecondaryrecipientidentifiers.md) — A set of strings that identifies the secondary recipients of the message, such as those in CC or BCC messages.

## See Also

### Smart Reply for messaging

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md) — Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [UIConversationContext](uiconversationcontext.md) — A base class that represents a conversation between participants, such as in an email or messaging app.
- [Entry](uiconversationcontext/entry.md) — A base class that represents a message in a conversation.
- [MailEntry](uimailconversationcontext/mailentry.md) — A class that represents a specific email in an email thread.
- [UIMessageConversationContext](uimessageconversationcontext.md) — A class that represents a message conversation.
- [MessageEntry](uimessageconversationcontext/messageentry.md) — A class that represents a message in a message conversation.
- [UIInputSuggestion](uiinputsuggestion.md) — A base class you use to handle suggestions from the keyboard or system.
- [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md) — An input suggestion that carries photo search metadata for people, subjects, locations, and time periods. _(beta)_
- [UISmartReplySuggestion](uismartreplysuggestion.md) — A class you use to handle a Smart Reply suggestion.
