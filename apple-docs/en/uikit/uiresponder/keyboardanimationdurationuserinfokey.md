---
title: keyboardAnimationDurationUserInfoKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/keyboardanimationdurationuserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/keyboardanimationdurationuserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/keyboardanimationdurationuserinfokey.json'
content_hash: 'sha256:e614caf7ad32eaae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# keyboardAnimationDurationUserInfoKey

<sub>Type Property</sub>

A user info key to retrieve the duration of the keyboard animation in seconds.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let keyboardAnimationDurationUserInfoKey: String
```

## Discussion

The value for this key is an [NSNumber](../../foundation/nsnumber.md) object containing a `double` that represents the duration of the keyboard animation in seconds. You can use this value to match the animation of the keyboard in your own animations.

For an example of how to match the keyboard’s animation, see [UIKeyboardAnimationCurveUserInfoKey](keyboardanimationcurveuserinfokey.md).

## See Also

### Constants

- [UIKeyboardAnimationCurveUserInfoKey](keyboardanimationcurveuserinfokey.md) — A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [UIKeyboardDidChangeFrameNotification](keyboarddidchangeframenotification.md) — A notification that posts immediately after a change in the keyboard’s frame.
- [UIKeyboardDidHideNotification](keyboarddidhidenotification.md) — A notification that posts immediately after dismissing the keyboard.
- [UIKeyboardDidShowNotification](keyboarddidshownotification.md) — A notification that posts immediately after displaying the keyboard.
- [UIKeyboardFrameBeginUserInfoKey](keyboardframebeginuserinfokey.md) — A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [UIKeyboardFrameEndUserInfoKey](keyboardframeenduserinfokey.md) — A user info key to retrieve the keyboard’s frame at the end of its animation.
- [UIKeyboardIsLocalUserInfoKey](keyboardislocaluserinfokey.md) — A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [UIKeyboardWillChangeFrameNotification](keyboardwillchangeframenotification.md) — A notification that posts immediately prior to a change in the keyboard’s frame.
- [UIKeyboardWillHideNotification](keyboardwillhidenotification.md) — A notification that posts immediately prior to dismissing the keyboard.
- [UIKeyboardWillShowNotification](keyboardwillshownotification.md) — A notification that posts immediately prior to displaying the keyboard.
