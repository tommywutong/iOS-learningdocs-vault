---
title: responseSecondaryRecipientIdentifiers
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimailconversationcontext/responsesecondaryrecipientidentifiers
source_url: 'https://developer.apple.com/documentation/uikit/uimailconversationcontext/responsesecondaryrecipientidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimailconversationcontext/responsesecondaryrecipientidentifiers.json'
content_hash: 'sha256:beb94c357cd8708d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMailConversationContext](../uimailconversationcontext.md)

# responseSecondaryRecipientIdentifiers

<sub>Instance Property</sub>

A set of strings that identifies the secondary recipients of the message, such as those in CC or BCC messages.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var responseSecondaryRecipientIdentifiers: Set<String> { get set }
```

## See Also

### Getting message details

- [responseSubject](responsesubject.md) — A string that contains the subject line of an intended response.
- [responseHasCustomSignature](responsehascustomsignature.md) — A Boolean value that indicates whether the intended response contains a custom signature.
