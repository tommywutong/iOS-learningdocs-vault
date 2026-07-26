---
title: keyboardDidHideNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/keyboarddidhidenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/keyboarddidhidenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/keyboarddidhidenotification.json'
content_hash: 'sha256:f504c026e103025f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# keyboardDidHideNotification

<sub>Type Property</sub>

A notification that posts immediately after dismissing the keyboard.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let keyboardDidHideNotification: NSNotification.Name
```

## Discussion

In iOS 16.1 and later, the notification object is the [UIScreen](../uiscreen.md) that the keyboard appears on. In earlier versions of iOS, the notification object is `nil`.

The `userInfo` dictionary contains information about the keyboard. To get the location and size of the keyboard from the `userInfo` dictionary, use [UIKeyboardFrameBeginUserInfoKey](keyboardframebeginuserinfokey.md) and [UIKeyboardFrameEndUserInfoKey](keyboardframeenduserinfokey.md).

The keyboard’s frame uses the screen’s coordinate space, which is different than the coordinate space of your views. Although they might sometimes match, such as when your app is full screen, they might be different when your app isn’t full screen, such as in Split View, Slide Over, and Stage Manager. This means you need to account for this difference by converting the keyboard’s frame from the screen’s coordinate space to that of your views. For an example of how to handle this conversion, see [UIKeyboardFrameEndUserInfoKey](keyboardframeenduserinfokey.md).

The system posts this notification on the main actor. An app running in visionOS never receives this notification. The system displays the keyboard in a separate window, leaving the app’s window unaffected by the keyboard’s appearance and disappearance.

## See Also

### Constants

- [UIKeyboardAnimationCurveUserInfoKey](keyboardanimationcurveuserinfokey.md) — A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [UIKeyboardAnimationDurationUserInfoKey](keyboardanimationdurationuserinfokey.md) — A user info key to retrieve the duration of the keyboard animation in seconds.
- [UIKeyboardDidChangeFrameNotification](keyboarddidchangeframenotification.md) — A notification that posts immediately after a change in the keyboard’s frame.
- [UIKeyboardDidShowNotification](keyboarddidshownotification.md) — A notification that posts immediately after displaying the keyboard.
- [UIKeyboardFrameBeginUserInfoKey](keyboardframebeginuserinfokey.md) — A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [UIKeyboardFrameEndUserInfoKey](keyboardframeenduserinfokey.md) — A user info key to retrieve the keyboard’s frame at the end of its animation.
- [UIKeyboardIsLocalUserInfoKey](keyboardislocaluserinfokey.md) — A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [UIKeyboardWillChangeFrameNotification](keyboardwillchangeframenotification.md) — A notification that posts immediately prior to a change in the keyboard’s frame.
- [UIKeyboardWillHideNotification](keyboardwillhidenotification.md) — A notification that posts immediately prior to dismissing the keyboard.
- [UIKeyboardWillShowNotification](keyboardwillshownotification.md) — A notification that posts immediately prior to displaying the keyboard.
