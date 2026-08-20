---
title: App Programming Guide for tvOS
apple_id: TP40015241
resource_type: Guide
platform: tvOS
topic: General
technology: null
published: '2017-01-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/AppleTV_PG/DetectingButtonPressesandGestures.html
archived_at: '2026-07-15T07:33:06.011263Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [App Programming Guide for tvOS](index.md)



## Detecting Gestures and Button Presses

Most UIKit views react appropriately when the user presses a button on the remote or makes a gesture on the touchpad. For example, a [UIButton](https://developer.apple.com/documentation/uikit/uibutton) object sends its action message when it has focus and the user presses the select button. However, you may also want to perform custom actions in your app when the user presses a button or makes a gesture, just as you would with touch events on iOS. Button press events are handled through the responder chain, just like other events. The [UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer) and [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) classes include new methods to respond when buttons on the remote are pressed or released. In addition, gesture recognizers that work with movement gestures, such as pan and swipe recognizers, automatically work when the gesture is performed on a Siri Remote’s touchpad.

### Using Gesture Recognizers

Tap gesture recognizers can be used to detect button presses. By default, a tap gesture recognizer is triggered when the Select button is pressed. The [allowedPressTypes](https://developer.apple.com/documentation/uikit/uigesturerecognizer/1624231-allowedpresstypes) property is used to specify which buttons trigger the recognizer.

Listing 4-1 creates a gesture recognizer that is triggered when the Play/Pause button is pressed.

__Listing 4-1__Detecting the Play/Pause button

1. `let tapRecognizer = UITapGestureRecognizer(target: self, action: "tapped:")`
2. `tapRecognizer.allowedPressTypes = [NSNumber(integer: UIPressType.PlayPause.rawValue)];`
3. `self.view.addGestureRecognizer(tapRecognizer)`

Similarly, a swipe or pan gesture recognizer can be used to detect motions across the remote’s touchpad. Listing 4-2 shows how to detect a left-to-right gesture across the touchpad.

__Listing 4-2__Detecting a swipe gesture

1. `let swipeRecognizer = UISwipeGestureRecognizer(target: self, action: "swiped:")`
2. `swipeRecognizer.direction = .Right`
3. `self.view.addGestureRecognizer(swipeRecognizer)`

### Working with Low-Level Event Handling

A [UIPress](https://developer.apple.com/documentation/uikit/uipress) object is analogous to a [UITouch](https://developer.apple.com/documentation/uikit/uitouch) object, but provides information about buttons on a remote or on other devices, such as a game controller. A `UIPress` object tells you which button is being described and the current state of the button, such as whether the button was just pressed, just released, or is still being held down. For analog buttons, a `UIPress` object provides information about how much force is being applied to the button. The [type](https://developer.apple.com/documentation/uikit/uipress/1620370-type) property specifies which physical button’s state has changed, and the other properties of the `UIPress` object describe the change.

[UIGestureRecognizer](https://developer.apple.com/documentation/uikit/uigesturerecognizer) and [UIResponder](https://developer.apple.com/documentation/uikit/uiresponder) objects can implement methods to be called when press events are triggered and delivered to the responder chain. These methods all receive a [UIPressesEvent](https://developer.apple.com/documentation/uikit/uipressesevent) object that describes the event as well as a set that describes the buttons that just changed state. Listing 4-3 shows how a view controller might implement low-level handling for a select event. As with touch event handling, when you implement handling for press events, if you implement any of the press method handlers, you should implement all four of them.

__Listing 4-3__Responding to low-level press events

1. `override func pressesBegan(presses: Set<UIPress>, withEvent event: UIPressesEvent?) {`
2. `for item in presses {`
3. `if item.type == .Select {`
4. `self.view.backgroundColor = UIColor.greenColor()`
5. `}`
6. `}`
7. `}`
9. `override func pressesEnded(presses: Set<UIPress>, withEvent event: UIPressesEvent?) {`
10. `for item in presses {`
11. `if item.type == .Select {`
12. `self.view.backgroundColor = UIColor.whiteColor()`
13. `}`
14. `}`
15. `}`
17. `override func pressesChanged(presses: Set<UIPress>, withEvent event: UIPressesEvent?) {`
18. `// ignored`
19. `}`
21. `override func pressesCancelled(presses: Set<UIPress>, withEvent event: UIPressesEvent?) {`
22. `for item in presses {`
23. `if item.type == .Select {`
24. `self.view.backgroundColor = UIColor.whiteColor()`
25. `}`
26. `}`
27. `}`

[Controlling the User Interface with the Apple TV Remote](WorkingwiththeAppleTVRemote.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqnjnknlti)

[Designing the Keyboard Input Experience](CreatingaGreatTextInputExperience.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbrfvbuqmjxfvjvomi)
