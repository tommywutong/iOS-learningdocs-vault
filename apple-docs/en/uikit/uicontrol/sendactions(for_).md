---
title: 'sendActions(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicontrol/sendactions(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicontrol/sendactions(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontrol/sendactions%28for%3A%29.json'
content_hash: 'sha256:fe77587fec8885e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIControl](../uicontrol.md)

# sendActions(for:)

<sub>Instance Method</sub>

Calls the action methods associated with the specified events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sendActions(for controlEvents: UIControl.Event)
```

## Parameters

- `controlEvents` — A bitmask with flags that specify the control events for which the control sends action messages. See [Event](event.md) for bitmask constants.

## Discussion

You call this method when you want the control to perform the actions associated with the specified events. This method iterates over the control’s registered targets and action methods and calls the [- sendAction:to:forEvent:](<sendaction(__to_for_).md>) method for each one that is associated with an event in the `controlEvents` parameter.

## See Also

### Related Documentation

- [- addTarget:action:forControlEvents:](<addtarget(__action_for_).md>) — Associates a target object and action method with the control.

### Triggering actions

- [- performPrimaryAction](<performprimaryaction().md>) — Calls the method associated with the control’s primary action.
- [- sendAction:](<sendaction(__).md>) — Like -sendAction:to:forEvent:, this method is called by -sendActionsForControlEvents:. You may override this method to observe or modify behavior. If you override this method, you should call super precisely once to dispatch the action, or not call super to suppress sending that action.
- [- sendAction:to:forEvent:](<sendaction(__to_for_).md>) — Calls the specified action method.
