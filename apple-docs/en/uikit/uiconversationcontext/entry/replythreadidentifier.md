---
title: replyThreadIdentifier
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconversationcontext/entry/replythreadidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uiconversationcontext/entry/replythreadidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconversationcontext/entry/replythreadidentifier.json'
content_hash: 'sha256:ff8bfa439940c4bf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIConversationContext](../../uiconversationcontext.md) · [Entry](../entry.md)

# replyThreadIdentifier

<sub>Instance Property</sub>

An optional string that identifies another message in a conversation, when this entry is a reply to that message.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var replyThreadIdentifier: String? { get set }
```

## Discussion

When an entry is a reply to another conversation entry, this contains the identifier of the conversation entry that the person replied to.

## See Also

### Identifying the entry

- [entryIdentifier](entryidentifier.md) — A string that uniquely identifies this specific entry in the conversation.
