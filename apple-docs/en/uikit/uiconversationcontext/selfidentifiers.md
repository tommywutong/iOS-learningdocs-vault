---
title: selfIdentifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconversationcontext/selfidentifiers
source_url: 'https://developer.apple.com/documentation/uikit/uiconversationcontext/selfidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconversationcontext/selfidentifiers.json'
content_hash: 'sha256:88e78081e089795c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIConversationContext](../uiconversationcontext.md)

# selfIdentifiers

<sub>Instance Property</sub>

A set of strings that identifies the active person in the conversation on the current device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var selfIdentifiers: Set<String> { get set }
```

## See Also

### Getting conversation participants

- [responsePrimaryRecipientIdentifiers](responseprimaryrecipientidentifiers.md) — A dictionary that relates participant identifiers to participant names.
- [participantNameByIdentifier](participantnamebyidentifier.md) — A dictionary that relates participant identifiers to participant names.
