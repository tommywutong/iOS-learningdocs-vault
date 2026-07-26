---
title: 'addAction(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/addaction(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/addaction(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/addaction%28_%3Afor%3A%29.json'
content_hash: 'sha256:6028689f5f568cb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# addAction(_:for:)

<sub>Instance Method</sub>

Adds the UIAction to a given event. UIActions are uniqued based on their identifier, and subsequent actions with the same identifier replace previously added actions. You may add multiple UIActions for corresponding controlEvents, and you may add the same action to multiple controlEvents.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addAction(_ action: UIAction, for controlEvents: UIControl.Event)
```

## See Also

### Managing the control’s targets and actions

- [- addTarget:action:forControlEvents:](<addtarget(__action_for_).md>) — Associates a target object and action method with the control.
- [- removeTarget:action:forControlEvents:](<removetarget(__action_for_).md>) — Stops the delivery of events to the specified target object.
- [allTargets](alltargets.md) — Returns all target objects associated with the control.
- [- removeAction:forControlEvents:](<removeaction(__for_).md>) — Removes the action from the set of passed control events.
- [- removeActionForIdentifier:forControlEvents:](<removeaction(identifiedby_for_).md>) — Removes the action with the provided identifier from the set of passed control events.
- [- actionsForTarget:forControlEvent:](<actions(fortarget_forcontrolevent_).md>) — Returns the actions performed on a target object when the specified event occurs.
- [allControlEvents](allcontrolevents.md) — Returns the events for which the control has associated actions.
- [enumerateEventHandlers(_:)](<enumerateeventhandlers(__).md>)
- [Event](event.md) — Constants describing the types of events possible for controls.
