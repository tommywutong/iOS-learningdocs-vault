---
title: conversationContext
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/conversationcontext
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/conversationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/conversationcontext.json'
content_hash: 'sha256:e80a3e6566e3da1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# conversationContext

<sub>Instance Property</sub>

A reference to a conversation, such as a mail or messaging thread.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional var conversationContext: UIConversationContext? { get set }
```

## Discussion

Set this conversation context before the keyboard appears; the keyboard uses this context to initialize its conversation context value. When updates occur in the conversation, call [- conversationContext:didChange:](<../uitextinputdelegate/conversationcontext(__didchange_).md>) on the `inputDelegate` property for [UITextInput](../uitextinput.md) objects, such as UITextView/inputDelegate`or`UITextField/inputDelegate``.
