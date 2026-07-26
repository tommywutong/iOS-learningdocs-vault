---
title: keyboardIsLocalUserInfoKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/keyboardislocaluserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/keyboardislocaluserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/keyboardislocaluserinfokey.json'
content_hash: 'sha256:f1fd02dc8cfb4d0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# keyboardIsLocalUserInfoKey

<sub>Type Property</sub>

A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let keyboardIsLocalUserInfoKey: String
```

## Discussion

The value for this key is an [NSNumber](../../foundation/nsnumber.md) object containing a Boolean value that indicates whether the keyboard belongs to the current app. With Multitasking in iPadOS, the system notifies all visible apps when the keyboard appears and disappears. The value is [true](../../swift/true.md) for the app that caused the keyboard to appear and [false](../../swift/false.md) for the other apps.

## See Also

### Constants

- [UIKeyboardAnimationCurveUserInfoKey](keyboardanimationcurveuserinfokey.md) — A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [UIKeyboardAnimationDurationUserInfoKey](keyboardanimationdurationuserinfokey.md) — A user info key to retrieve the duration of the keyboard animation in seconds.
- [UIKeyboardDidChangeFrameNotification](keyboarddidchangeframenotification.md) — A notification that posts immediately after a change in the keyboard’s frame.
- [UIKeyboardDidHideNotification](keyboarddidhidenotification.md) — A notification that posts immediately after dismissing the keyboard.
- [UIKeyboardDidShowNotification](keyboarddidshownotification.md) — A notification that posts immediately after displaying the keyboard.
- [UIKeyboardFrameBeginUserInfoKey](keyboardframebeginuserinfokey.md) — A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [UIKeyboardFrameEndUserInfoKey](keyboardframeenduserinfokey.md) — A user info key to retrieve the keyboard’s frame at the end of its animation.
- [UIKeyboardWillChangeFrameNotification](keyboardwillchangeframenotification.md) — A notification that posts immediately prior to a change in the keyboard’s frame.
- [UIKeyboardWillHideNotification](keyboardwillhidenotification.md) — A notification that posts immediately prior to dismissing the keyboard.
- [UIKeyboardWillShowNotification](keyboardwillshownotification.md) — A notification that posts immediately prior to displaying the keyboard.
