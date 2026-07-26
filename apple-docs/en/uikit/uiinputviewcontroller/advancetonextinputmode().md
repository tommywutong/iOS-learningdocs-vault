---
title: advanceToNextInputMode()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputviewcontroller/advancetonextinputmode()
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewcontroller/advancetonextinputmode()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewcontroller/advancetonextinputmode%28%29.json'
content_hash: 'sha256:aef3e2344d9dddf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputViewController](../uiinputviewcontroller.md)

# advanceToNextInputMode()

<sub>Instance Method</sub>

Switches to the next keyboard in the list of user-enabled keyboards.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func advanceToNextInputMode()
```

## Discussion

When the user taps the Globe or a custom “next keyboard” key, the system picks the appropriate “next” keyboard from the list of user-enabled keyboards. To determine whether your custom keyboard needs to display a “next keyboard” key, check the [needsInputModeSwitchKey](needsinputmodeswitchkey.md) property. If the value of the property is [true](../../swift/true.md), your keyboard should include this key.

## See Also

### Controlling a custom keyboard

- [- dismissKeyboard](<dismisskeyboard().md>) — Dismisses the custom keyboard from the screen.
- [- handleInputModeListFromView:withEvent:](<handleinputmodelist(from_with_).md>) — Supports interaction with the list of user-enabled keyboards.
