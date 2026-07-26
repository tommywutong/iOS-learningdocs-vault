---
title: keyboardFrameBeginUserInfoKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/keyboardframebeginuserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/keyboardframebeginuserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/keyboardframebeginuserinfokey.json'
content_hash: 'sha256:84fbf1c62ebd8855'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# keyboardFrameBeginUserInfoKey

<sub>Type Property</sub>

A user info key to retrieve the keyboard’s frame at the beginning of its animation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let keyboardFrameBeginUserInfoKey: String
```

## Discussion

The value for this key is an [NSValue](../../foundation/nsvalue.md) object that contains a [CGRect](../../corefoundation/cgrect.md) for identifying the frame rectangle of the keyboard (in the screen’s coordinate space) before animating the keyboard. The frame rectangle reflects the current orientation of the device.

The keyboard’s frame uses the screen’s coordinate space, which is different than the coordinate space of your views. Although they might sometimes match, such as when your app is full screen, they might be different when your app isn’t full screen, such as in Split View, Slide Over, and Stage Manager. This means you need to account for this difference by converting the keyboard’s frame from the screen’s coordinate space to that of your views. For an example of how to handle this conversion, see [UIKeyboardFrameEndUserInfoKey](keyboardframeenduserinfokey.md).

## See Also

### Constants

- [UIKeyboardAnimationCurveUserInfoKey](keyboardanimationcurveuserinfokey.md) — A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [UIKeyboardAnimationDurationUserInfoKey](keyboardanimationdurationuserinfokey.md) — A user info key to retrieve the duration of the keyboard animation in seconds.
- [UIKeyboardDidChangeFrameNotification](keyboarddidchangeframenotification.md) — A notification that posts immediately after a change in the keyboard’s frame.
- [UIKeyboardDidHideNotification](keyboarddidhidenotification.md) — A notification that posts immediately after dismissing the keyboard.
- [UIKeyboardDidShowNotification](keyboarddidshownotification.md) — A notification that posts immediately after displaying the keyboard.
- [UIKeyboardFrameEndUserInfoKey](keyboardframeenduserinfokey.md) — A user info key to retrieve the keyboard’s frame at the end of its animation.
- [UIKeyboardIsLocalUserInfoKey](keyboardislocaluserinfokey.md) — A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [UIKeyboardWillChangeFrameNotification](keyboardwillchangeframenotification.md) — A notification that posts immediately prior to a change in the keyboard’s frame.
- [UIKeyboardWillHideNotification](keyboardwillhidenotification.md) — A notification that posts immediately prior to dismissing the keyboard.
- [UIKeyboardWillShowNotification](keyboardwillshownotification.md) — A notification that posts immediately prior to displaying the keyboard.
