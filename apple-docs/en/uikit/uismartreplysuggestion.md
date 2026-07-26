---
title: UISmartReplySuggestion
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uismartreplysuggestion
source_url: 'https://developer.apple.com/documentation/uikit/uismartreplysuggestion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uismartreplysuggestion.json'
content_hash: 'sha256:5266b1e42bbc1df2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISmartReplySuggestion

<sub>Class</sub>

A class you use to handle a Smart Reply suggestion.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class UISmartReplySuggestion
```

## Overview

Use the [smartReply](uismartreplysuggestion/smartreply.md) string as a signal of the user’s intention when you generate long form text based on the option the user selected.

## Relationships

- **Inherits From**: [UIInputSuggestion](uiinputsuggestion.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Smart Reply

- [smartReply](uismartreplysuggestion/smartreply.md) — A string from the Smart Reply option the user selected.

## See Also

### Smart Reply for messaging

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md) — Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [UIConversationContext](uiconversationcontext.md) — A base class that represents a conversation between participants, such as in an email or messaging app.
- [Entry](uiconversationcontext/entry.md) — A base class that represents a message in a conversation.
- [UIMailConversationContext](uimailconversationcontext.md) — A class that represents an email conversation.
- [MailEntry](uimailconversationcontext/mailentry.md) — A class that represents a specific email in an email thread.
- [UIMessageConversationContext](uimessageconversationcontext.md) — A class that represents a message conversation.
- [MessageEntry](uimessageconversationcontext/messageentry.md) — A class that represents a message in a message conversation.
- [UIInputSuggestion](uiinputsuggestion.md) — A base class you use to handle suggestions from the keyboard or system.
- [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md) — An input suggestion that carries photo search metadata for people, subjects, locations, and time periods. _(beta)_
