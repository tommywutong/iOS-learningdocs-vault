---
title: 'handleInputModeList(from:with:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiinputviewcontroller/handleinputmodelist(from:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewcontroller/handleinputmodelist(from:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewcontroller/handleinputmodelist%28from%3Awith%3A%29.json'
content_hash: 'sha256:5a0f540c5fbc6ec6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputViewController](../uiinputviewcontroller.md)

# handleInputModeList(from:with:)

<sub>Instance Method</sub>

Supports interaction with the list of user-enabled keyboards.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func handleInputModeList(from view: UIView, with event: UIEvent)
```

## Discussion

Use this method to launch the input mode list from your input view when the user long-presses or swipes up from the view; advance to the next input mode in the list when the user taps the view.

## See Also

### Controlling a custom keyboard

- [- advanceToNextInputMode](<advancetonextinputmode().md>) — Switches to the next keyboard in the list of user-enabled keyboards.
- [- dismissKeyboard](<dismisskeyboard().md>) — Dismisses the custom keyboard from the screen.
