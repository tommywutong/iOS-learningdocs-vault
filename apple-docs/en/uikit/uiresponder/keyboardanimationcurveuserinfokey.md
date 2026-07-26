---
title: keyboardAnimationCurveUserInfoKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/keyboardanimationcurveuserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/keyboardanimationcurveuserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/keyboardanimationcurveuserinfokey.json'
content_hash: 'sha256:887743e6737d6305'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# keyboardAnimationCurveUserInfoKey

<sub>Type Property</sub>

A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let keyboardAnimationCurveUserInfoKey: String
```

## Discussion

The value for this key is an [NSNumber](../../foundation/nsnumber.md) object that contains a [AnimationCurve](../uiview/animationcurve.md) constant used to determine how the system animates the keyboard onto or off the screen. You can use this value to match the animation of the keyboard in your own animations.

Before using this value, convert the animation curve constant to [AnimationOptions](../uiview/animationoptions.md), which you can pass to one of UIKit’s animation methods, such as [+ animateWithDuration:animations:completion:](<../uiview/animate(withduration_animations_completion_).md>).

**Swift**

```swift
// Get the animation curve constant and the duration for your animation.
guard let animationCurve = userInfo[UIResponder.keyboardAnimationCurveUserInfoKey] as? UInt,
      let animationDuration = userInfo[UIResponder.keyboardAnimationDurationUserInfoKey] as? Double else { return }

// Convert the animation curve constant to animation options.
let animationOptions = UIView.AnimationOptions(rawValue: animationCurve << 16)

// Perform your animation.
UIView.animate(withDuration: animationDuration,
               delay: 0,
               options: animationOptions) {
    // Specify what to animate. For example, calling layoutIfNeeded animates a change to
    // the view's constraints.
    self.view.layoutIfNeeded()
} completion: { _ in
    // Use the completion handler to perform anything that needs to happen after the keyboard
    // frame finishes animating, such as scrolling your text view after the animation completes.
}
```

**Objective-C**

```objc
// Convert the animation curve constant to animation options.
UIViewAnimationOptions options = (UIViewAnimationOptions)[[userInfo objectForKey:UIKeyboardAnimationCurveUserInfoKey]
                          integerValue] << 16;

// Get the duration for your animation.
CGFloat duration = [[userInfo objectForKey:UIKeyboardAnimationDurationUserInfoKey] floatValue];

// Perform your animation.
[UIView animateWithDuration:duration
                      delay:0.0
                    options:options
                 animations:^{
    // Specify what to animate. For example, calling layoutIfNeeded animates a change 
    // to the view's constraints.
    [self.view layoutIfNeeded]; 
}
                 completion:^(BOOL finished) {
    // Use the completion handler to perform anything that needs to happen after the keyboard
    // frame finishes animating, such as scrolling your text view after the animation completes.
}];
```

## See Also

### Constants

- [UIKeyboardAnimationDurationUserInfoKey](keyboardanimationdurationuserinfokey.md) — A user info key to retrieve the duration of the keyboard animation in seconds.
- [UIKeyboardDidChangeFrameNotification](keyboarddidchangeframenotification.md) — A notification that posts immediately after a change in the keyboard’s frame.
- [UIKeyboardDidHideNotification](keyboarddidhidenotification.md) — A notification that posts immediately after dismissing the keyboard.
- [UIKeyboardDidShowNotification](keyboarddidshownotification.md) — A notification that posts immediately after displaying the keyboard.
- [UIKeyboardFrameBeginUserInfoKey](keyboardframebeginuserinfokey.md) — A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [UIKeyboardFrameEndUserInfoKey](keyboardframeenduserinfokey.md) — A user info key to retrieve the keyboard’s frame at the end of its animation.
- [UIKeyboardIsLocalUserInfoKey](keyboardislocaluserinfokey.md) — A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [UIKeyboardWillChangeFrameNotification](keyboardwillchangeframenotification.md) — A notification that posts immediately prior to a change in the keyboard’s frame.
- [UIKeyboardWillHideNotification](keyboardwillhidenotification.md) — A notification that posts immediately prior to dismissing the keyboard.
- [UIKeyboardWillShowNotification](keyboardwillshownotification.md) — A notification that posts immediately prior to displaying the keyboard.
