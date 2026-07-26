---
title: 'enumerateEventHandlers:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/enumerateeventhandlers:'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/enumerateeventhandlers:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/enumerateeventhandlers%3A.json'
content_hash: 'sha256:5d91be9f1b563e38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# enumerateEventHandlers:

<sub>Instance Method</sub>

Iterate over the event handlers installed on this control at the time this method is called. For each call, either actionHandler or action will be non-nil. controlEvents is always non-zero. Setting *stop to YES will terminate the enumeration early. It is legal to manipulate the control’s event handlers within the block.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) enumerateEventHandlers:(void (^)(UIAction *actionHandler, id target, SEL action, UIControlEvents controlEvents, BOOL *stop)) iterator;
```

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
- [Event](event.md) — Constants describing the types of events possible for controls.
