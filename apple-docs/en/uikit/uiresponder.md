---
title: UIResponder
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder.json'
content_hash: 'sha256:e0669f851fb6a3ba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIResponder

<sub>Class</sub>

An abstract interface for responding to and handling events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIResponder
```

## Overview

Responder objects — instances of [UIResponder](uiresponder.md) — constitute the event-handling backbone of a UIKit app. Many key objects are also responders, including the [UIApplication](uiapplication.md) object, [UIViewController](uiviewcontroller.md) objects, and all [UIView](uiview.md) objects (which includes [UIWindow](uiwindow.md)). As events occur, UIKit dispatches them to your app’s responder objects for handling.

There are several kinds of events, including touch events, motion events, remote-control events, and press events. To handle a specific type of event, a responder must override the corresponding methods. For example, to handle touch events, a responder implements the [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>), [- touchesMoved:withEvent:](<uiresponder/touchesmoved(__with_).md>), [- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>), and [- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) methods. In the case of touches, the responder uses the event information provided by UIKit to track changes to those touches and to update the app’s interface appropriately.

In addition to handling events, UIKit responders also manage the forwarding of unhandled events to other parts of your app. If a given responder doesn’t handle an event, it forwards that event to the next event in the responder chain. UIKit manages the responder chain dynamically, using predefined rules to determine which object should be next to receive an event. For example, a view forwards events to its superview, and the root view of a hierarchy forwards events to its view controller.

Responders process [UIEvent](uievent.md) objects but can also accept custom input through an input view. The system’s keyboard is the most obvious example of an input view. When the user taps a [UITextField](uitextfield.md) and [UITextView](uitextview.md) object onscreen, the view becomes the first responder and displays its input view, which is the system keyboard. Similarly, you can create custom input views and display them when other responders become active. To associate a custom input view with a responder, assign that view to the [inputView](uiresponder/inputview.md) property of the responder.

For information about responders and the responder chain, see [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIAccessibilityElement](uiaccessibilityelement.md), [UIApplication](uiapplication.md), [UIScene](uiscene.md), [UIView](uiview.md), [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Managing the responder chain

- [nextResponder](uiresponder/next.md) — Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [isFirstResponder](uiresponder/isfirstresponder.md) — Returns a Boolean value indicating whether this object is the first responder.
- [canBecomeFirstResponder](uiresponder/canbecomefirstresponder.md) — Returns a Boolean value indicating whether this object can become the first responder.
- [- becomeFirstResponder](<uiresponder/becomefirstresponder().md>) — Asks UIKit to make this object the first responder in its window.
- [canResignFirstResponder](uiresponder/canresignfirstresponder.md) — Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [- resignFirstResponder](<uiresponder/resignfirstresponder().md>) — Notifies this object that it has been asked to relinquish its status as first responder in its window.

### Responding to touch events

- [- touchesBegan:withEvent:](<uiresponder/touchesbegan(__with_).md>) — Tells this object that one or more new touches occurred in a view or window.
- [- touchesMoved:withEvent:](<uiresponder/touchesmoved(__with_).md>) — Tells the responder when one or more touches associated with an event changed.
- [- touchesEnded:withEvent:](<uiresponder/touchesended(__with_).md>) — Tells the responder when one or more fingers are raised from a view or window.
- [- touchesCancelled:withEvent:](<uiresponder/touchescancelled(__with_).md>) — Tells the responder when a system event (such as a system alert) cancels a touch sequence.
- [- touchesEstimatedPropertiesUpdated:](<uiresponder/touchesestimatedpropertiesupdated(__).md>) — Tells the responder that updated values were received for previously estimated properties or that an update is no longer expected.

### Responding to motion events

- [- motionBegan:withEvent:](<uiresponder/motionbegan(__with_).md>) — Tells the responder that a motion event has begun.
- [- motionEnded:withEvent:](<uiresponder/motionended(__with_).md>) — Tells the responder that a motion event has ended.
- [- motionCancelled:withEvent:](<uiresponder/motioncancelled(__with_).md>) — Tells the responder that a motion event has been canceled.

### Responding to press events

- [- pressesBegan:withEvent:](<uiresponder/pressesbegan(__with_).md>) — Tells this object when a physical button is first pressed.
- [- pressesChanged:withEvent:](<uiresponder/presseschanged(__with_).md>) — Tells this object when a value associated with a press has changed.
- [- pressesEnded:withEvent:](<uiresponder/pressesended(__with_).md>) — Tells the object when a button is released.
- [- pressesCancelled:withEvent:](<uiresponder/pressescancelled(__with_).md>) — Tells this object when a system event (such as a low-memory warning) cancels a press event.

### Responding to remote-control events

- [- remoteControlReceivedWithEvent:](<uiresponder/remotecontrolreceived(with_).md>) — Tells the object when a remote-control event is received.

### Managing input views

- [inputView](uiresponder/inputview.md) — The custom input view to display when the responder becomes the first responder.
- [inputViewController](uiresponder/inputviewcontroller.md) — The custom input view controller to use when the responder becomes the first responder.
- [inputAccessoryView](uiresponder/inputaccessoryview.md) — The custom input accessory view to display when the responder becomes the first responder.
- [inputAccessoryViewController](uiresponder/inputaccessoryviewcontroller.md) — The custom input accessory view controller to display when the responder becomes the first responder.
- [- reloadInputViews](<uiresponder/reloadinputviews().md>) — Updates the custom input and accessory views when the object is the first responder.

### Getting the undo manager

- [undoManager](uiresponder/undomanager.md) — Returns the nearest shared undo manager in the responder chain.

### Building and validating commands

- [- buildMenuWithBuilder:](<uiresponder/buildmenu(with_).md>) — Asks the receiving responder to add and remove items from a menu system.
- [- validateCommand:](<uiresponder/validate(__).md>) — Asks the receiving responder to validate the command.
- [- canPerformAction:withSender:](<uiresponder/canperformaction(__withsender_).md>) — Requests the receiving responder to enable or disable the specified command in the user interface.
- [- targetForAction:withSender:](<uiresponder/target(foraction_withsender_).md>) — Returns the target object that responds to an action.

### Accessing the available key commands

- [keyCommands](uiresponder/keycommands.md) — The key commands that trigger actions on this responder.

### Managing the text input mode

- [textInputMode](uiresponder/textinputmode.md) — The text input mode for this responder object.
- [textInputContextIdentifier](uiresponder/textinputcontextidentifier.md) — An identifier signifying that the responder should preserve its text input mode information.
- [+ clearTextInputContextIdentifier:](<uiresponder/cleartextinputcontextidentifier(__).md>) — Clears text input mode information from the app’s user defaults.
- [inputAssistantItem](uiresponder/inputassistantitem.md) — The input assistant to use when configuring the keyboard’s shortcuts bar.

### Supporting user activities

- [userActivity](uiresponder/useractivity.md) — An object encapsulating a user activity supported by this responder.
- [- restoreUserActivityState:](<uiresponder/restoreuseractivitystate(__).md>) — Restores the state needed to continue the given user activity.
- [- updateUserActivityState:](<uiresponder/updateuseractivitystate(__).md>) — Updates the state of the given user activity.

### Managing activity items

- [activityItemsConfiguration](uiresponder/activityitemsconfiguration.md)

### Accessing the editing interaction

- [editingInteractionConfiguration](uiresponder/editinginteractionconfiguration.md)
- [UIEditingInteractionConfiguration](uieditinginteractionconfiguration.md)

### Capturing text from the camera

- [- captureTextFromCamera:](<uiresponder/capturetextfromcamera(__).md>) — Starts scanning text using the device’s camera.

### Managing the Touch Bar

- [- makeTouchBar](<uiresponder/maketouchbar().md>) — Asks the receiving responder to create and configure a Touch Bar object.
- [touchBar](uiresponder/touchbar.md) — The Touch Bar object for the responder.

### Constants

- [UIKeyboardAnimationCurveUserInfoKey](uiresponder/keyboardanimationcurveuserinfokey.md) — A user info key to retrieve the animation curve that the system uses to animate the keyboard onto or off the screen.
- [UIKeyboardAnimationDurationUserInfoKey](uiresponder/keyboardanimationdurationuserinfokey.md) — A user info key to retrieve the duration of the keyboard animation in seconds.
- [UIKeyboardDidChangeFrameNotification](uiresponder/keyboarddidchangeframenotification.md) — A notification that posts immediately after a change in the keyboard’s frame.
- [UIKeyboardDidHideNotification](uiresponder/keyboarddidhidenotification.md) — A notification that posts immediately after dismissing the keyboard.
- [UIKeyboardDidShowNotification](uiresponder/keyboarddidshownotification.md) — A notification that posts immediately after displaying the keyboard.
- [UIKeyboardFrameBeginUserInfoKey](uiresponder/keyboardframebeginuserinfokey.md) — A user info key to retrieve the keyboard’s frame at the beginning of its animation.
- [UIKeyboardFrameEndUserInfoKey](uiresponder/keyboardframeenduserinfokey.md) — A user info key to retrieve the keyboard’s frame at the end of its animation.
- [UIKeyboardIsLocalUserInfoKey](uiresponder/keyboardislocaluserinfokey.md) — A user info key to retrieve a Boolean value that indicates whether the keyboard belongs to the current app.
- [UIKeyboardWillChangeFrameNotification](uiresponder/keyboardwillchangeframenotification.md) — A notification that posts immediately prior to a change in the keyboard’s frame.
- [UIKeyboardWillHideNotification](uiresponder/keyboardwillhidenotification.md) — A notification that posts immediately prior to dismissing the keyboard.
- [UIKeyboardWillShowNotification](uiresponder/keyboardwillshownotification.md) — A notification that posts immediately prior to displaying the keyboard.

### Structures

- [KeyboardDidChangeFrameMessage](uiresponder/keyboarddidchangeframemessage.md)
- [KeyboardDidHideMessage](uiresponder/keyboarddidhidemessage.md)
- [KeyboardDidShowMessage](uiresponder/keyboarddidshowmessage.md)
- [KeyboardWillChangeFrameMessage](uiresponder/keyboardwillchangeframemessage.md)
- [KeyboardWillHideMessage](uiresponder/keyboardwillhidemessage.md)
- [KeyboardWillShowMessage](uiresponder/keyboardwillshowmessage.md)

### Instance Properties

- [pencilKitResponderState](uiresponder/pencilkitresponderstate.md) — The PencilKit state associated with the responder object.

### Instance Methods

- [- providerForDeferredMenuElement:](<uiresponder/provider(for_).md>) — Asks the responder for an element provider to fulfill the given focus-based deferred element. Check the `identifier` of the deferred element to identify which deferred element this is. By default, this returns nil. Return a non-nil `provider` to make this responder responsible for providing elements for this fulfillment of the deferred element.

## See Also

### Essentials

- [Using responders and the responder chain to handle events](using-responders-and-the-responder-chain-to-handle-events.md) — Learn how to handle events that propagate through your app.
- [UIEvent](uievent.md) — An object that describes a single user interaction with your app.
