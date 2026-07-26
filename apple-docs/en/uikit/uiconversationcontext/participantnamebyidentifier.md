---
title: participantNameByIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconversationcontext/participantnamebyidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiconversationcontext/participantnamebyidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconversationcontext/participantnamebyidentifier.json'
content_hash: 'sha256:6d7099b2571eb901'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConversationContext](../uiconversationcontext.md)

# participantNameByIdentifier

<sub>Instance Property</sub>

A dictionary that relates participant identifiers to participant names.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var participantNameByIdentifier: [String : PersonNameComponents] { get set }
```

## See Also

### Getting conversation participants

- [selfIdentifiers](selfidentifiers.md) — A set of strings that identifies the active person in the conversation on the current device.
- [responsePrimaryRecipientIdentifiers](responseprimaryrecipientidentifiers.md) — A dictionary that relates participant identifiers to participant names.
