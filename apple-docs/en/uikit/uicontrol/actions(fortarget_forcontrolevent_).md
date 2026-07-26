---
title: 'actions(forTarget:forControlEvent:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/actions(fortarget:forcontrolevent:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/actions(fortarget:forcontrolevent:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/actions%28fortarget%3Aforcontrolevent%3A%29.json'
content_hash: 'sha256:6d3e58c952814a97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# actions(forTarget:forControlEvent:)

<sub>Instance Method</sub>

Returns the actions performed on a target object when the specified event occurs.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func actions(forTarget target: Any?, forControlEvent controlEvent: UIControl.Event) -> [String]?
```

## Parameters

- `target` — The target object—that is, an object that has an action method associated with this control. You must pass an explicit object for this method to return a meaningful result. Specifying `nil` always returns `nil`.

- `controlEvent` — A single control event constant representing the event for which you want the list of action methods. For a list of possible constants, see [Event](event.md)

## Return Value

An array [NSString](../../foundation/nsstring.md) objects containing the selector names of the corresponding action methods, or `nil` if there are no action methods associated with the specified target object and control event.

## Discussion

Use this method to determine what action methods are called on the specified object in response to a particular control event. You can use the [NSSelectorFromString(_:)](<../../foundation/nsselectorfromstring(__).md>) function to convert the returned strings to valid selectors, as needed.

## See Also

### Related Documentation

- [- sendAction:to:forEvent:](<sendaction(__to_for_).md>) — Calls the specified action method.
- [- sendActionsForControlEvents:](<sendactions(for_).md>) — Calls the action methods associated with the specified events.

### Managing the control’s targets and actions

- [- addTarget:action:forControlEvents:](<addtarget(__action_for_).md>) — Associates a target object and action method with the control.
- [- removeTarget:action:forControlEvents:](<removetarget(__action_for_).md>) — Stops the delivery of events to the specified target object.
- [allTargets](alltargets.md) — Returns all target objects associated with the control.
- [- addAction:forControlEvents:](<addaction(__for_).md>) — Adds the UIAction to a given event. UIActions are uniqued based on their identifier, and subsequent actions with the same identifier replace previously added actions. You may add multiple UIActions for corresponding controlEvents, and you may add the same action to multiple controlEvents.
- [- removeAction:forControlEvents:](<removeaction(__for_).md>) — Removes the action from the set of passed control events.
- [- removeActionForIdentifier:forControlEvents:](<removeaction(identifiedby_for_).md>) — Removes the action with the provided identifier from the set of passed control events.
- [allControlEvents](allcontrolevents.md) — Returns the events for which the control has associated actions.
- [enumerateEventHandlers(_:)](<enumerateeventhandlers(__).md>)
- [Event](event.md) — Constants describing the types of events possible for controls.
