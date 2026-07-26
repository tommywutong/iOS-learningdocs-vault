---
title: dismissKeyboard()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputviewcontroller/dismisskeyboard()
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewcontroller/dismisskeyboard()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewcontroller/dismisskeyboard%28%29.json'
content_hash: 'sha256:63aeedc4a2978ebf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputViewController](../uiinputviewcontroller.md)

# dismissKeyboard()

<sub>Instance Method</sub>

Dismisses the custom keyboard from the screen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func dismissKeyboard()
```

## Discussion

Because a custom keyboard does not have access to the current text input object, you cannot send it a [- resignFirstResponder](<../uiresponder/resignfirstresponder().md>) message (as you would to dismiss the system keyboard when you are developing an app with text entry). To dismiss the custom keyboard, call [- dismissKeyboard](<dismisskeyboard().md>) instead.

## See Also

### Controlling a custom keyboard

- [- advanceToNextInputMode](<advancetonextinputmode().md>) — Switches to the next keyboard in the list of user-enabled keyboards.
- [- handleInputModeListFromView:withEvent:](<handleinputmodelist(from_with_).md>) — Supports interaction with the list of user-enabled keyboards.
