---
title: 'textField(_:insertInputSuggestion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.4+, iPadOS 18.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextfielddelegate/textfield(_:insertinputsuggestion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextfielddelegate/textfield(_:insertinputsuggestion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfielddelegate/textfield%28_%3Ainsertinputsuggestion%3A%29.json'
content_hash: 'sha256:40dd49eb6281b891'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextFieldDelegate](../uitextfielddelegate.md)

# textField(_:insertInputSuggestion:)

<sub>Instance Method</sub>

Tells the delegate when the keyboard delivers an input suggestion.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
optional func textField(_ textField: UITextField, insertInputSuggestion inputSuggestion: UIInputSuggestion)
```

## Parameters

- `textField` — The text field that is currently the first responder.

- `inputSuggestion` — The input suggestion that the user or system selected.
