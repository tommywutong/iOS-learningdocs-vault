---
title: UIGestureRecognizer
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uigesturerecognizer
source_url: 'https://developer.apple.com/documentation/uikit/uigesturerecognizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigesturerecognizer.json'
content_hash: 'sha256:551687f43bfa547f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGestureRecognizer

<sub>Class</sub>

The base class for concrete gesture recognizers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIGestureRecognizer
```

## Overview

A _gesture recognizer_ decouples the logic for recognizing a sequence of touches (or other input) and acting on that recognition. When one of these objects recognizes a common gesture or, in some cases, a change in the gesture, it sends an action message to each designated target object.

The concrete subclasses of [UIGestureRecognizer](uigesturerecognizer.md) are the following:

- [UITapGestureRecognizer](uitapgesturerecognizer.md)
- [UIPinchGestureRecognizer](uipinchgesturerecognizer.md)
- [UIRotationGestureRecognizer](uirotationgesturerecognizer.md)
- [UISwipeGestureRecognizer](uiswipegesturerecognizer.md)
- [UIPanGestureRecognizer](uipangesturerecognizer.md)
- [UIScreenEdgePanGestureRecognizer](uiscreenedgepangesturerecognizer.md)
- [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md)
- [UIHoverGestureRecognizer](uihovergesturerecognizer.md)

The [UIGestureRecognizer](uigesturerecognizer.md) class defines a set of common behaviors that can be configured for all concrete gesture recognizers. It can also communicate with its delegate (an object that adopts the [UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md) protocol), thereby enabling finer-grained customization of some behaviors.

A gesture recognizer operates on touches hit-tested to a specific view and all of that view’s subviews. It thus must be associated with that view. To make that association you must call the [UIView](uiview.md) method [- addGestureRecognizer:](<uiview/addgesturerecognizer(__).md>). A gesture recognizer doesn’t participate in the view’s responder chain.

A gesture recognizer has one or more target-action pairs associated with it. If there are multiple target-action pairs, they’re discrete, and not cumulative. Recognition of a gesture results in the dispatch of an action message to a target for each of the associated pairs. The action methods invoked must conform to one of the following signatures:

**Swift**

```swift
@IBAction func myActionMethod()
@IBAction func myActionMethod(_ sender: UIGestureRecognizer)
```

**Objective-C**

```objc
- (IBAction)handleGesture;
- (IBAction)handleGesture:(UIGestureRecognizer *)gestureRecognizer;
```

Methods conforming to the latter signature permit the target in some cases to query the gesture recognizer sending the message for additional information. For example, the target could ask a [UIRotationGestureRecognizer](uirotationgesturerecognizer.md) object for the angle of rotation (in radians) since the last invocation of the action method for this gesture. Clients of gesture recognizers can also ask for the location of a gesture by calling [- locationInView:](<uigesturerecognizer/location(in_).md>) or [- locationOfTouch:inView:](<uigesturerecognizer/location(oftouch_in_).md>).

The gesture interpreted by a gesture recognizer can be either discrete or continuous. A discrete gesture, such as a double tap, occurs but once in a multi-touch sequence and results in a single action sent. However, when a gesture recognizer interprets a continuous gesture such as a rotation gesture, it sends an action message for each incremental change until the multi-touch sequence concludes.

A window delivers touch events to a gesture recognizer before it delivers them to the hit-tested view attached to the gesture recognizer. Generally, if a gesture recognizer analyzes the stream of touches in a multi-touch sequence and doesn’t recognize its gesture, the view receives the full complement of touches. If a gesture recognizer recognizes its gesture, the remaining touches for the view are canceled. The usual sequence of actions in gesture recognition follows a path determined by default values of the [cancelsTouchesInView](uigesturerecognizer/cancelstouchesinview.md), [delaysTouchesBegan](uigesturerecognizer/delaystouchesbegan.md), [delaysTouchesEnded](uigesturerecognizer/delaystouchesended.md) properties:

- [cancelsTouchesInView](uigesturerecognizer/cancelstouchesinview.md) — If a gesture recognizer recognizes its gesture, it unbinds the remaining touches of that gesture from their view (so the window won’t deliver them). The window cancels the previously delivered touches with a ([- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>)) message. If a gesture recognizer doesn’t recognize its gesture, the view receives all touches in the multi-touch sequence.
- [delaysTouchesBegan](uigesturerecognizer/delaystouchesbegan.md) — As long as a gesture recognizer, when analyzing touch events, hasn’t failed recognition of its gesture, the window withholds delivery of touch objects in the [UITouchPhaseBegan](uitouch/phase-swift.enum/began.md) phase to the attached view. If the gesture recognizer subsequently recognizes its gesture, the view doesn’t receive these touch objects. If the gesture recognizer doesn’t recognize its gesture, the window delivers these objects in an invocation of the view’s [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>) method (and possibly a follow-up [- touchesMoved:withEvent:](<uiresponder/touchesmoved(__with_).md>) invocation to inform it of the touches current location).
- [delaysTouchesEnded](uigesturerecognizer/delaystouchesended.md) — As long as a gesture recognizer, when analyzing touch events, hasn’t failed recognition of its gesture, the window withholds delivery of touch objects in the [UITouchPhaseEnded](uitouch/phase-swift.enum/ended.md) phase to the attached view. If the gesture recognizer subsequently recognizes its gesture, the touches are canceled (in a [- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) message). If the gesture recognizer doesn’t recognize its gesture, the window delivers these objects in an invocation of the view’s [- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>) method.

Note that “recognize” in the above descriptions doesn’t necessarily equate to a transition to the Recognized state.

### Subclassing notes

You may create a subclass of [UIGestureRecognizer](uigesturerecognizer.md) that recognizes a distinctive gesture — for example, a “check mark” gesture. If you’re going to create such a concrete gesture recognizer, be sure to import the `UIGestureRecognizerSubclass.h` header file (for Objective-C) or the `UIKit.UIGestureRecognizerSubclass` module (for Swift). This file declares all the methods and properties a subclass must either override, call, or reset.

Gesture recognizers operate within a predefined state machine, transitioning to subsequent states as they handle multi-touch events. The states and their possible transitions differ for continuous and discrete gestures. All gesture recognizers begin a multi-touch sequence in the Possible state ([UIGestureRecognizerStatePossible](uigesturerecognizer/state-swift.enum/possible.md)). Discrete gestures transition from Possible to either Recognized ([UIGestureRecognizerStateRecognized](uigesturerecognizer/state-swift.enum/recognized.md)) or Failed ([UIGestureRecognizerStateFailed](uigesturerecognizer/state-swift.enum/failed.md)), depending on whether they successfully interpret the gesture or not. If the gesture recognizer transitions to Recognized, it sends its action message to its target.

For continuous gestures, the state transitions a gesture recognizer might make are more numerous, as indicated in the following sequence:

- Possible —\> Began —\> [Changed] —\> Cancelled
- Possible —\> Began —\> [Changed] —\> Ended

The Changed state is optional and may occur multiple times before the Cancelled or Ended state is reached. The gesture recognizer sends action messages at each state transition. Thus for a continuous gesture such as a pinch, action messages are sent as the two fingers move toward or away from each other. The `enum` constants representing these states are of type [State](uigesturerecognizer/state-swift.enum.md). (Note that the constants for Recognized and Ended states are synonymous.)

Subclasses must set the [state](uigesturerecognizer/state-swift.property.md) property to the appropriate value when they transition between states.

#### Methods to override

The methods that subclasses must override are described in [Implementing subclasses](uigesturerecognizer.md#Implementing-subclasses). Subclasses must also periodically reset the [state](uigesturerecognizer/state-swift.property.md) property (as described above) and may call the [- ignoreTouch:forEvent:](<uigesturerecognizer/ignore(__for_)-5f685.md>) method.

#### Special considerations

The [state](uigesturerecognizer/state-swift.property.md) property is declared in `UIGestureRecognizer.h` as being read-only. This property declaration is intended for clients of gesture recognizers. Subclasses of `UIGestureRecognizer` must import the `UIGestureRecognizerSubclass.h` header file (for Objective-C) or the `UIKit.UIGestureRecognizerSubclass` module (for Swift). This file contains a redeclaration of `state` that makes it read-write.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIHoverGestureRecognizer](uihovergesturerecognizer.md), [UILongPressGestureRecognizer](uilongpressgesturerecognizer.md), [UIPanGestureRecognizer](uipangesturerecognizer.md), [UIPinchGestureRecognizer](uipinchgesturerecognizer.md), [UIRotationGestureRecognizer](uirotationgesturerecognizer.md), [UISwipeGestureRecognizer](uiswipegesturerecognizer.md), [UITapGestureRecognizer](uitapgesturerecognizer.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing a gesture recognizer

- [- initWithTarget:action:](<uigesturerecognizer/init(target_action_).md>) — Creates a gesture recognizer with a target and an action selector.
- [- initWithCoder:](<uigesturerecognizer/init(coder_).md>) — Creates a gesture recognizer from data in an unarchiver.
- [- init](<uigesturerecognizer/init().md>) — Creates a gesture recognizer.

### Managing gesture-related interactions

- [delegate](uigesturerecognizer/delegate.md) — The delegate of the gesture recognizer.
- [UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md) — A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.

### Adding and removing targets and actions

- [- addTarget:action:](<uigesturerecognizer/addtarget(__action_).md>) — Adds a target and an action to a gesture-recognizer object.
- [- removeTarget:action:](<uigesturerecognizer/removetarget(__action_).md>) — Removes a target and an action from a gesture-recognizer object.

### Getting the touches and location of a gesture

- [- locationInView:](<uigesturerecognizer/location(in_).md>) — Returns the point computed as the location in a given view of the gesture represented by the gesture recognizer.
- [- locationOfTouch:inView:](<uigesturerecognizer/location(oftouch_in_).md>) — Returns the location of one of the gesture’s touches in the local coordinate system of a given view.
- [numberOfTouches](uigesturerecognizer/numberoftouches.md) — The number of touches involved in the gesture represented by the gesture recognizer.

### Getting the recognizer’s state and view

- [state](uigesturerecognizer/state-swift.property.md) — The current state of the gesture recognizer.
- [State](uigesturerecognizer/state-swift.enum.md) — Constants that represent the current state a gesture recognizer is in.
- [view](uigesturerecognizer/view.md) — The view the gesture recognizer is attached to.
- [enabled](uigesturerecognizer/isenabled.md) — A Boolean property that indicates whether the gesture recognizer is enabled.
- [buttonMask](uigesturerecognizer/buttonmask.md) — A bit mask of the buttons in the gesture represented by the gesture recognizer.
- [modifierFlags](uigesturerecognizer/modifierflags.md) — The bit mask of modifier flags in the gesture represented by the gesture recognizer.

### Canceling and delaying touches

- [cancelsTouchesInView](uigesturerecognizer/cancelstouchesinview.md) — A Boolean value that determines whether touches are delivered to a view when a gesture is recognized.
- [delaysTouchesBegan](uigesturerecognizer/delaystouchesbegan.md) — A Boolean value that determines whether the gesture recognizer delays sending touches in a begin phase to its view.
- [delaysTouchesEnded](uigesturerecognizer/delaystouchesended.md) — A Boolean value that determines whether the gesture recognizer delays sending touches in an end phase to its view.

### Specifying dependencies between gesture recognizers

- [- requireGestureRecognizerToFail:](<uigesturerecognizer/require(tofail_).md>) — Creates a dependency relationship between the gesture recognizer and another gesture recognizer when the objects are created.

### Recognizing different gestures

- [allowedPressTypes](uigesturerecognizer/allowedpresstypes.md) — An array of press types used to distinguish the type of button press.
- [allowedTouchTypes](uigesturerecognizer/allowedtouchtypes.md) — An array of touch types used to distinguish type of touches.
- [requiresExclusiveTouchType](uigesturerecognizer/requiresexclusivetouchtype.md) — A Boolean value that indicates whether the gesture recognizer considers touches of different types simultaneously.

### Debugging gesture recognizers

- [name](uigesturerecognizer/name.md) — The unique name of the gesture recognizer.

### Implementing subclasses

- [- touchesBegan:withEvent:](<uigesturerecognizer/touchesbegan(__with_).md>) — Sent to the gesture recognizer when one or more fingers touch down in the associated view.
- [- touchesMoved:withEvent:](<uigesturerecognizer/touchesmoved(__with_).md>) — Sent to the gesture recognizer when one or more fingers move in the associated view.
- [- touchesEnded:withEvent:](<uigesturerecognizer/touchesended(__with_).md>) — Sent to the gesture recognizer when one or more fingers lift from the associated view.
- [- touchesCancelled:withEvent:](<uigesturerecognizer/touchescancelled(__with_).md>) — Sent to the gesture recognizer when a system event (such as an incoming phone call) cancels a touch event.
- [- touchesEstimatedPropertiesUpdated:](<uigesturerecognizer/touchesestimatedpropertiesupdated(__).md>) — Sent to the gesture recognizer when the estimated properties for a touch have changed so that they are no longer estimated, or an update is no longer expected.
- [- reset](<uigesturerecognizer/reset().md>) — Overridden to reset internal state when a gesture recognition attempt completes.
- [- ignoreTouch:forEvent:](<uigesturerecognizer/ignore(__for_)-5f685.md>) — Tells the gesture recognizer to ignore a specific touch of the given event.
- [- canBePreventedByGestureRecognizer:](<uigesturerecognizer/canbeprevented(by_).md>) — Overridden to indicate that the specified gesture recognizer can prevent the receiver from recognizing a gesture.
- [- canPreventGestureRecognizer:](<uigesturerecognizer/canprevent(__).md>) — Overridden to indicate that the receiver can prevent the specified gesture recognizer from recognizing its gesture.
- [- shouldReceiveEvent:](<uigesturerecognizer/shouldreceive(__).md>)
- [- shouldRequireFailureOfGestureRecognizer:](<uigesturerecognizer/shouldrequirefailure(of_).md>) — Overridden to indicate that the receiver requires the specified gesture recognizer to fail.
- [- shouldBeRequiredToFailByGestureRecognizer:](<uigesturerecognizer/shouldberequiredtofail(by_).md>) — Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [- ignorePress:forEvent:](<uigesturerecognizer/ignore(__for_)-8qqor.md>) — Tells the gesture recognizer to ignore a specific press of the given event.
- [- pressesBegan:withEvent:](<uigesturerecognizer/pressesbegan(__with_).md>) — Sent to the receiver when a physical button is pressed in the associated view.
- [- pressesChanged:withEvent:](<uigesturerecognizer/presseschanged(__with_).md>) — Sent to the receiver when the [force](uipress/force.md) of the press has changed in the associated view.
- [- pressesEnded:withEvent:](<uigesturerecognizer/pressesended(__with_).md>) — Sent to the receiver when a button is released from the associated view.
- [- pressesCancelled:withEvent:](<uigesturerecognizer/pressescancelled(__with_).md>) — Sent to the receiver when a system event (such as a low-memory warning) cancels a press event.

## See Also

### Custom gestures

- [Implementing a custom gesture recognizer](implementing-a-custom-gesture-recognizer.md) — Discover when and how to build your own gesture recognizers.
- [UIGestureRecognizerDelegate](uigesturerecognizerdelegate.md) — A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.
- [Supporting gesture interaction in your apps](supporting-gesture-interaction-in-your-apps.md) — Enrich your app’s user experience by supporting standard and custom gesture interaction.
