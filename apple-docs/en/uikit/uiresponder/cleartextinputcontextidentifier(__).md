---
title: 'clearTextInputContextIdentifier(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponder/cleartextinputcontextidentifier(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/cleartextinputcontextidentifier(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/cleartextinputcontextidentifier%28_%3A%29.json'
content_hash: 'sha256:2a487bc655a4daac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# clearTextInputContextIdentifier(_:)

<sub>Type Method</sub>

Clears text input mode information from the app’s user defaults.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func clearTextInputContextIdentifier(_ identifier: String)
```

## Parameters

- `identifier` — An identifier assigned to the [textInputContextIdentifier](textinputcontextidentifier.md) property of one of your responders.

## Discussion

Calling this method removes any text input mode information associated with the specified identifier from the app’s user defaults. Removing this information causes the responder to use the default text input mode again.

## See Also

### Managing the text input mode

- [textInputMode](textinputmode.md) — The text input mode for this responder object.
- [textInputContextIdentifier](textinputcontextidentifier.md) — An identifier signifying that the responder should preserve its text input mode information.
- [inputAssistantItem](inputassistantitem.md) — The input assistant to use when configuring the keyboard’s shortcuts bar.
