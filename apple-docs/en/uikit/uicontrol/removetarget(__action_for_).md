---
title: 'removeTarget(_:action:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/removetarget(_:action:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/removetarget(_:action:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/removetarget%28_%3Aaction%3Afor%3A%29.json'
content_hash: 'sha256:053d99b73cc6a272'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# removeTarget(_:action:for:)

<sub>Instance Method</sub>

Stops the delivery of events to the specified target object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeTarget(_ target: Any?, action: Selector?, for controlEvents: UIControl.Event)
```

## Parameters

- `target` — A target object registered with the control. Specify `nil` to remove the specified control events for all target objects.

- `action` — A selector identifying a registered action method. You may specify `nil` for this parameter.

- `controlEvents` — A bitmask specifying the control events that you want to remove for the specified `target` object. For a list of possible constants, see [Event](event.md).

## Discussion

Use this method to prevent the delivery of control events to target objects associated with control. If you specify a valid object in the `target` parameter, this method stops the delivery of the specified events to all action methods associated with that object. If you specify `nil` for the `target` parameter, this method prevents the delivery of those events to all action methods of all target objects.

Although the `action` parameter is not considered when stopping the delivery of events, you should specify an appropriate value anyway. If the specified target/action combination no longer has any valid control events associated with it, the control cleans up its corresponding internal data structures. Doing so can affect the set of objects returned by the [allTargets](alltargets.md) method.

## See Also

### Managing the control’s targets and actions

- [- addTarget:action:forControlEvents:](<addtarget(__action_for_).md>) — Associates a target object and action method with the control.
- [allTargets](alltargets.md) — Returns all target objects associated with the control.
- [- addAction:forControlEvents:](<addaction(__for_).md>) — Adds the UIAction to a given event. UIActions are uniqued based on their identifier, and subsequent actions with the same identifier replace previously added actions. You may add multiple UIActions for corresponding controlEvents, and you may add the same action to multiple controlEvents.
- [- removeAction:forControlEvents:](<removeaction(__for_).md>) — Removes the action from the set of passed control events.
- [- removeActionForIdentifier:forControlEvents:](<removeaction(identifiedby_for_).md>) — Removes the action with the provided identifier from the set of passed control events.
- [- actionsForTarget:forControlEvent:](<actions(fortarget_forcontrolevent_).md>) — Returns the actions performed on a target object when the specified event occurs.
- [allControlEvents](allcontrolevents.md) — Returns the events for which the control has associated actions.
- [enumerateEventHandlers(_:)](<enumerateeventhandlers(__).md>)
- [Event](event.md) — Constants describing the types of events possible for controls.
