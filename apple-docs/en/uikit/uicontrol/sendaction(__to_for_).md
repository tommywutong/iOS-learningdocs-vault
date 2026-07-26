---
title: 'sendAction(_:to:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/sendaction(_:to:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/sendaction(_:to:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/sendaction%28_%3Ato%3Afor%3A%29.json'
content_hash: 'sha256:f3a49168b172e2cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# sendAction(_:to:for:)

<sub>Instance Method</sub>

Calls the specified action method.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sendAction(_ action: Selector, to target: Any?, for event: UIEvent?)
```

## Parameters

- `action` — A selector identifying the action method to call. This parameter must not be `nil`.

- `target` — The target object — that is, the object that implements the specified action. Specify nil if you want the app to search the responder chain for an object capable of performing the action.

- `event` — The event that triggered the calling of the action method. You may specify nil for this parameter if you are calling this method directly, instead of in response to an event. For example, you might specify `nil` when changing the value of a control programmatically.

## Discussion

This method takes the provided information and forwards it to the singleton [UIApplication](../uiapplication.md) object for dispatching. If you supplied a valid target object, the app calls the action method on that target object. If the target object is `nil`, the app searches the responder chain for an object that defines the method.

Subclasses may override this method and use it to observe or modify the action-dispatching behavior. Implementations need to call `super` when they want to continue with the execution of the action method.

## See Also

### Related Documentation

- [- addTarget:action:forControlEvents:](<addtarget(__action_for_).md>) — Associates a target object and action method with the control.

### Triggering actions

- [- performPrimaryAction](<performprimaryaction().md>) — Calls the method associated with the control’s primary action.
- [- sendAction:](<sendaction(__).md>) — Like -sendAction:to:forEvent:, this method is called by -sendActionsForControlEvents:. You may override this method to observe or modify behavior. If you override this method, you should call super precisely once to dispatch the action, or not call super to suppress sending that action.
- [- sendActionsForControlEvents:](<sendactions(for_).md>) — Calls the action methods associated with the specified events.
