---
title: UIInputSuggestion
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputsuggestion
source_url: 'https://developer.apple.com/documentation/uikit/uiinputsuggestion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputsuggestion.json'
content_hash: 'sha256:fa7523002a62bcd3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIInputSuggestion

<sub>Class</sub>

A base class you use to handle suggestions from the keyboard or system.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class UIInputSuggestion
```

## Discussion

To handle photo search suggestions from Smart Actions, use [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md), which provides the filter metadata you need to present a pre-populated photo picker or build a custom photo search. To handle Smart Reply suggestions, use [UISmartReplySuggestion](uismartreplysuggestion.md), which provides the reply text the person selected to guide a long-form response.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md), [UISmartReplySuggestion](uismartreplysuggestion.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

### Smart Reply for messaging

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md) — Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [UIConversationContext](uiconversationcontext.md) — A base class that represents a conversation between participants, such as in an email or messaging app.
- [Entry](uiconversationcontext/entry.md) — A base class that represents a message in a conversation.
- [UIMailConversationContext](uimailconversationcontext.md) — A class that represents an email conversation.
- [MailEntry](uimailconversationcontext/mailentry.md) — A class that represents a specific email in an email thread.
- [UIMessageConversationContext](uimessageconversationcontext.md) — A class that represents a message conversation.
- [MessageEntry](uimessageconversationcontext/messageentry.md) — A class that represents a message in a message conversation.
- [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md) — An input suggestion that carries photo search metadata for people, subjects, locations, and time periods. _(beta)_
- [UISmartReplySuggestion](uismartreplysuggestion.md) — A class you use to handle a Smart Reply suggestion.
