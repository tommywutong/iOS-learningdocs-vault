---
title: responseSubject
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimailconversationcontext/responsesubject
source_url: 'https://developer.apple.com/documentation/uikit/uimailconversationcontext/responsesubject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimailconversationcontext/responsesubject.json'
content_hash: 'sha256:6fb71d6c099cae3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMailConversationContext](../uimailconversationcontext.md)

# responseSubject

<sub>Instance Property</sub>

A string that contains the subject line of an intended response.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var responseSubject: String { get set }
```

## See Also

### Getting message details

- [responseHasCustomSignature](responsehascustomsignature.md) — A Boolean value that indicates whether the intended response contains a custom signature.
- [responseSecondaryRecipientIdentifiers](responsesecondaryrecipientidentifiers.md) — A set of strings that identifies the secondary recipients of the message, such as those in CC or BCC messages.
