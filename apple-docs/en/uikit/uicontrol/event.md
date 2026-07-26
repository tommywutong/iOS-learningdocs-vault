---
title: UIControl.Event
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontrol/event
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/event'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/event.json'
content_hash: 'sha256:a0291cd60b2751ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# UIControl.Event

<sub>Structure</sub>

Constants describing the types of events possible for controls.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Event
```

## Overview

You set up a control so that it sends an action message to a target object by associating both target and action with one or more control events. To do this, send [- addTarget:action:forControlEvents:](<addtarget(__action_for_).md>) to the control for each target-action pair you want to specify.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [UIControlEventTouchDown](event/touchdown.md) — A touch-down event in the control.
- [UIControlEventTouchDownRepeat](event/touchdownrepeat.md) — A repeated touch-down event in the control; for this event the value of the UITouch `tapCount` method is greater than one.
- [UIControlEventTouchDragInside](event/touchdraginside.md) — An event where a finger is dragged inside the bounds of the control.
- [UIControlEventTouchDragOutside](event/touchdragoutside.md) — An event where a finger is dragged just outside the bounds of the control.
- [UIControlEventTouchDragEnter](event/touchdragenter.md) — An event where a finger is dragged into the bounds of the control.
- [UIControlEventTouchDragExit](event/touchdragexit.md) — An event where a finger is dragged from within a control to outside its bounds.
- [UIControlEventTouchUpInside](event/touchupinside.md) — A touch-up event in the control where the finger is inside the bounds of the control.
- [UIControlEventTouchUpOutside](event/touchupoutside.md) — A touch-up event in the control where the finger is outside the bounds of the control.
- [UIControlEventTouchCancel](event/touchcancel.md) — A system event canceling the current touches for the control.
- [UIControlEventValueChanged](event/valuechanged.md) — A touch dragging or otherwise manipulating a control, causing it to emit a series of different values.
- [UIControlEventMenuActionTriggered](event/menuactiontriggered.md) — A menu action has triggered prior to the menu being presented.
- [UIControlEventPrimaryActionTriggered](event/primaryactiontriggered.md) — A semantic action triggered by buttons.
- [UIControlEventEditingDidBegin](event/editingdidbegin.md) — A touch initiating an editing session in a text field by entering its bounds.
- [UIControlEventEditingChanged](event/editingchanged.md) — A touch making an editing change in a text field.
- [UIControlEventEditingDidEnd](event/editingdidend.md) — A touch ending an editing session in a text field by leaving its bounds.
- [UIControlEventEditingDidEndOnExit](event/editingdidendonexit.md) — A touch ending an editing session in a text field.
- [UIControlEventAllTouchEvents](event/alltouchevents.md) — All touch events.
- [UIControlEventAllEditingEvents](event/alleditingevents.md) — All editing touches for text fields.
- [UIControlEventApplicationReserved](event/applicationreserved.md) — A range of control-event values available for app use.
- [UIControlEventSystemReserved](event/systemreserved.md) — A range of control-event values reserved for internal framework use.
- [UIControlEventAllEvents](event/allevents.md) — All events, including system events.

### Initializers

- [init(rawValue:)](<event/init(rawvalue_).md>) — Creates a control event with the specified raw value.

## See Also

### Managing the control’s targets and actions

- [- addTarget:action:forControlEvents:](<addtarget(__action_for_).md>) — Associates a target object and action method with the control.
- [- removeTarget:action:forControlEvents:](<removetarget(__action_for_).md>) — Stops the delivery of events to the specified target object.
- [allTargets](alltargets.md) — Returns all target objects associated with the control.
- [- addAction:forControlEvents:](<addaction(__for_).md>) — Adds the UIAction to a given event. UIActions are uniqued based on their identifier, and subsequent actions with the same identifier replace previously added actions. You may add multiple UIActions for corresponding controlEvents, and you may add the same action to multiple controlEvents.
- [- removeAction:forControlEvents:](<removeaction(__for_).md>) — Removes the action from the set of passed control events.
- [- removeActionForIdentifier:forControlEvents:](<removeaction(identifiedby_for_).md>) — Removes the action with the provided identifier from the set of passed control events.
- [- actionsForTarget:forControlEvent:](<actions(fortarget_forcontrolevent_).md>) — Returns the actions performed on a target object when the specified event occurs.
- [allControlEvents](allcontrolevents.md) — Returns the events for which the control has associated actions.
- [enumerateEventHandlers(_:)](<enumerateeventhandlers(__).md>)
