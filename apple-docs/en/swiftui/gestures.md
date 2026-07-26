---
title: Gestures
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gestures
source_url: 'https://developer.apple.com/documentation/swiftui/gestures'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gestures.json'
content_hash: 'sha256:cd32604b205e7907'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Gestures

<sub>API Collection</sub>

Define interactions from taps, clicks, and swipes to fine-grained gestures.

## Overview

Respond to gestures by adding gesture modifiers to your views. You can listen for taps, drags, pinches, and other standard gestures.

![](../../../attachments/6a1478e9bc9c150def717738cb949d52/gestures-hero@2x.png)

You can also compose custom gestures from individual gestures using the [simultaneously(with:)](<gesture/simultaneously(with_).md>), [sequenced(before:)](<gesture/sequenced(before_).md>), or [exclusively(before:)](<gesture/exclusively(before_).md>) modifiers, or combine gestures with keyboard modifiers using the [modifiers(_:)](<gesture/modifiers(__).md>) modifier.

> [!important] Important
> When you need a button, use a [Button](button.md) instance rather than a tap gesture. You can use any view as the button’s label, and the button type automatically provides many of the standard behaviors that users expect from a button, like accessibility labels and hints.

For design guidance, see [Gestures](../design/human-interface-guidelines/gestures.md) in the Human Interface Guidelines.

## Topics

### Essentials

- [Adding interactivity with gestures](adding-interactivity-with-gestures.md) — Use gesture modifiers to add interactivity to your app.

### Recognizing tap gestures

- [onTapGesture(count:perform:)](<view/ontapgesture(count_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture.
- [onTapGesture(count:coordinateSpace:perform:)](<view/ontapgesture(count_coordinatespace_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction.
- [onTapGesture(count:coordinateSpace:inputKinds:perform:)](<view/ontapgesture(count_coordinatespace_inputkinds_perform_).md>) — Adds an action to perform when this view recognizes a tap gesture, and provides the action with the location of the interaction. _(beta)_
- [TapGesture](tapgesture.md) — A gesture that recognizes one or more taps.
- [SpatialTapGesture](spatialtapgesture.md) — A gesture that recognizes one or more taps and reports their location.

### Recognizing long-press gestures

- [onLongPressGesture(minimumDuration:maximumDistance:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_maximumdistance_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_maximumdistance_inputkinds_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture. _(beta)_
- [onLongPressGesture(minimumDuration:perform:onPressingChanged:)](<view/onlongpressgesture(minimumduration_perform_onpressingchanged_).md>) — Adds an action to perform when this view recognizes a long press gesture.
- [onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)](<view/onlongtouchgesture(minimumduration_perform_ontouchingchanged_).md>) — Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [LongPressGesture](longpressgesture.md) — A gesture that succeeds when the user performs a long press.

### Recognizing spatial events

- [SpatialEventGesture](spatialeventgesture.md) — A gesture that provides information about ongoing spatial events like clicks and touches.
- [SpatialEventCollection](spatialeventcollection.md) — A collection of spatial input events that target a specific view.
- [Chirality](chirality.md) — The chirality, or handedness, of a pose.

### Recognizing gestures that change over time

- [gesture(_:)](<view/gesture(__).md>) — Attaches an [NSGestureRecognizerRepresentable](nsgesturerecognizerrepresentable.md) to the view.
- [gesture(_:isEnabled:)](<view/gesture(__isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:name:isEnabled:)](<view/gesture(__name_isenabled_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [gesture(_:including:)](<view/gesture(__including_).md>) — Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [DragGesture](draggesture.md) — A dragging motion that invokes an action as the drag-event sequence changes.
- [WindowDragGesture](windowdraggesture.md) — A gesture that recognizes the motion of and handles dragging a window.
- [MagnifyGesture](magnifygesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification.
- [RotateGesture](rotategesture.md) — A gesture that recognizes a rotation motion and tracks the angle of the rotation.
- [RotateGesture3D](rotategesture3d.md) — A gesture that recognizes 3D rotation motion and tracks the angle and axis of the rotation.
- [GestureMask](gesturemask.md) — Options that control how adding a gesture to a view affects other gestures recognized by the view and its subviews.

### Recognizing Apple Pencil gestures

- [onPencilDoubleTap(perform:)](<view/onpencildoubletap(perform_).md>) — Adds an action to perform after the user double-taps their Apple Pencil.
- [onPencilSqueeze(perform:)](<view/onpencilsqueeze(perform_).md>) — Adds an action to perform when the user squeezes their Apple Pencil.
- [preferredPencilDoubleTapAction](environmentvalues/preferredpencildoubletapaction.md) — The action that the user prefers to perform after double-tapping their Apple Pencil, as selected in the Settings app.
- [preferredPencilSqueezeAction](environmentvalues/preferredpencilsqueezeaction.md) — The action that the user prefers to perform when squeezing their Apple Pencil, as selected in the Settings app.
- [PencilPreferredAction](pencilpreferredaction.md) — An action that the user prefers to perform after double-tapping their Apple Pencil.
- [PencilDoubleTapGestureValue](pencildoubletapgesturevalue.md) — Describes the value of an Apple Pencil double-tap gesture.
- [PencilSqueezeGestureValue](pencilsqueezegesturevalue.md) — Describes the value of an Apple Pencil squeeze gesture.
- [PencilSqueezeGesturePhase](pencilsqueezegesturephase.md) — Describes the phase and value of an Apple Pencil squeeze gesture.
- [PencilHoverPose](pencilhoverpose.md) — A value describing the location and distance of an Apple Pencil hovering in the area above a view’s bounds.

### Combining gestures

- [Composing SwiftUI gestures](composing-swiftui-gestures.md) — Combine gestures to create complex interactions.
- [simultaneousGesture(_:including:)](<view/simultaneousgesture(__including_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:isEnabled:)](<view/simultaneousgesture(__isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [simultaneousGesture(_:name:isEnabled:)](<view/simultaneousgesture(__name_isenabled_).md>) — Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [SequenceGesture](sequencegesture.md) — A gesture that’s a sequence of two gestures.
- [SimultaneousGesture](simultaneousgesture.md) — A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
- [ExclusiveGesture](exclusivegesture.md) — A gesture that consists of two gestures where only one of them can succeed.

### Customizing gestures

- [GestureInputKinds](gestureinputkinds.md) — An option set that specifies which input kinds a gesture should recognize. _(beta)_

### Defining custom gestures

- [highPriorityGesture(_:including:)](<view/highprioritygesture(__including_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:isEnabled:)](<view/highprioritygesture(__isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [highPriorityGesture(_:name:isEnabled:)](<view/highprioritygesture(__name_isenabled_).md>) — Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [handGestureShortcut(_:isEnabled:)](<view/handgestureshortcut(__isenabled_).md>) — Assigns a hand gesture shortcut to the modified control.
- [defersSystemGestures(on:)](<view/deferssystemgestures(on_).md>) — Sets the screen edge from which you want your gesture to take precedence over the system gesture.
- [Gesture](gesture.md) — An instance that matches a sequence of events to a gesture, and returns a stream of values for each of its states.
- [AnyGesture](anygesture.md) — A type-erased gesture.
- [HandActivationBehavior](handactivationbehavior.md) — An activation behavior specific to hand-driven input.
- [HandGestureShortcut](handgestureshortcut.md) — Hand gesture shortcuts describe finger and wrist movements that the user can perform in order to activate a button or toggle.

### Managing gesture state

- [GestureState](gesturestate.md) — A property wrapper type that updates a property while the user performs a gesture and resets the property back to its initial state when the gesture ends.
- [GestureStateGesture](gesturestategesture.md) — A gesture that updates the state provided by a gesture’s updating callback.

### Handling activation events

- [allowsWindowActivationEvents(_:)](<view/allowswindowactivationevents(__).md>) — Configures whether gestures in this view hierarchy can handle events that activate the containing window.

### Deprecated gestures

- [MagnificationGesture](magnificationgesture.md) — A gesture that recognizes a magnification motion and tracks the amount of magnification. _(deprecated)_
- [RotationGesture](rotationgesture.md) — A gesture that recognizes a rotation motion and tracks the angle of the rotation. _(deprecated)_

## See Also

### Event handling

- [Input events](input-events.md) — Respond to input from a hardware device, like a keyboard or a Touch Bar.
- [Clipboard](clipboard.md) — Enable people to move or duplicate items by issuing Copy and Paste commands.
- [Drag and drop](drag-and-drop.md) — Enable people to move or duplicate items by dragging them from one location to another.
- [Focus](focus.md) — Identify and control which visible object responds to user interaction.
- [System events](system-events.md) — React to system events, like opening a URL.
