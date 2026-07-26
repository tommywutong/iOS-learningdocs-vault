---
title: 'addTarget(_:action:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/addtarget(_:action:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/addtarget(_:action:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/addtarget%28_%3Aaction%3Afor%3A%29.json'
content_hash: 'sha256:239826def86fc12a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# addTarget(_:action:for:)

<sub>Instance Method</sub>

Associates a target object and action method with the control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addTarget(_ target: Any?, action: Selector, for controlEvents: UIControl.Event)
```

## Parameters

- `target` — The target object—that is, the object whose `action` method is called. If you specify `nil`, UIKit searches the responder chain for an object that responds to the specified action message and delivers the message to that object.

- `action` — A selector identifying the action method to be called. You may specify a selector whose signature matches any of the signatures in the code example in [UIControl](../uicontrol.md). This parameter must not be `nil`.

- `controlEvents` — A bitmask specifying the control-specific events for which the action method is called. Always specify at least one constant. For a list of possible constants, see [Event](event.md).

## Discussion

You may call this method multiple times to configure multiple targets and actions for the control. It is also safe to call this method multiple times with the same values for the `target` and `action` parameters. The control maintains a list of its attached targets and actions along with the events each supports.

The control does not retain the object in the `target` parameter. It is your responsibility to maintain a strong reference to the target object while it is attached to a control.

Specifying a value of `0` for the `controlEvents` parameter does not prevent events from being sent to a previously registered `target` and `action` method. To stop the delivery of events, always call the [- removeTarget:action:forControlEvents:](<removetarget(__action_for_).md>) method.

## See Also

### Managing the control’s targets and actions

- [- removeTarget:action:forControlEvents:](<removetarget(__action_for_).md>) — Stops the delivery of events to the specified target object.
- [allTargets](alltargets.md) — Returns all target objects associated with the control.
- [- addAction:forControlEvents:](<addaction(__for_).md>) — Adds the UIAction to a given event. UIActions are uniqued based on their identifier, and subsequent actions with the same identifier replace previously added actions. You may add multiple UIActions for corresponding controlEvents, and you may add the same action to multiple controlEvents.
- [- removeAction:forControlEvents:](<removeaction(__for_).md>) — Removes the action from the set of passed control events.
- [- removeActionForIdentifier:forControlEvents:](<removeaction(identifiedby_for_).md>) — Removes the action with the provided identifier from the set of passed control events.
- [- actionsForTarget:forControlEvent:](<actions(fortarget_forcontrolevent_).md>) — Returns the actions performed on a target object when the specified event occurs.
- [allControlEvents](allcontrolevents.md) — Returns the events for which the control has associated actions.
- [enumerateEventHandlers(_:)](<enumerateeventhandlers(__).md>)
- [Event](event.md) — Constants describing the types of events possible for controls.
