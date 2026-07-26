---
title: inputAssistantItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/inputassistantitem
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/inputassistantitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/inputassistantitem.json'
content_hash: 'sha256:9930d5e2856c1a46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# inputAssistantItem

<sub>Instance Property</sub>

The input assistant to use when configuring the keyboard’s shortcuts bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var inputAssistantItem: UITextInputAssistantItem { get }
```

## Discussion

On iPad, the shortcuts bar above the keyboard contains typing suggestions and other controls for managing text, such as cut, copy, and paste commands. This property contains the text input assistant item you use to configure the custom bar button items that you want included in the shortcuts bar. The shortcuts bar isn’t available on iPhone or iPod Touch.

This property has special considerations in visionOS:

- In apps built for visionOS, this property isn’t available. Use [bottomOrnament](../../swiftui/toolbaritemplacement/bottomornament.md) instead.
- In compatible iPad apps running in visionOS, the shortcuts bar behaves similar to iPadOS. It contains the custom bar button items you configure using this property and system items (such as cut, copy, and paste). The shortcuts bar renders at the bottom of the app window, but it doesn’t anchor to the keyboard in visionOS.

## See Also

### Managing the text input mode

- [textInputMode](textinputmode.md) — The text input mode for this responder object.
- [textInputContextIdentifier](textinputcontextidentifier.md) — An identifier signifying that the responder should preserve its text input mode information.
- [+ clearTextInputContextIdentifier:](<cleartextinputcontextidentifier(__).md>) — Clears text input mode information from the app’s user defaults.
