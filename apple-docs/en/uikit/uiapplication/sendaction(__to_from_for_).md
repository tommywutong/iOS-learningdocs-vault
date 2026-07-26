---
title: 'sendAction(_:to:from:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/sendaction(_:to:from:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/sendaction(_:to:from:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/sendaction%28_%3Ato%3Afrom%3Afor%3A%29.json'
content_hash: 'sha256:58da99eb87e3873f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# sendAction(_:to:from:for:)

<sub>Instance Method</sub>

Sends an action message identified by the selector to a specified target.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sendAction(_ action: Selector, to target: Any?, from sender: Any?, for event: UIEvent?) -> Bool
```

## Parameters

- `action` — A selector identifying an action method. See the discussion for information on the permitted selector forms.

- `target` — The object to receive the action message. If `target` is `nil`, the app sends the message to the first responder, from whence it progresses up the responder chain until it is handled.

- `sender` — The object that is sending the action message. The default sender is the [UIControl](../uicontrol.md) object that invokes this method.

- `event` — A [UIEvent](../uievent.md) object that encapsulates information about the event originating the action message.

## Return Value

[true](../../swift/true.md) if a responder object handled the action message, [false](../../swift/false.md) if no object in the responder chain handled the message.

## Discussion

Normally, this method is invoked by a [UIControl](../uicontrol.md) object that the user has touched. The default implementation dispatches the action method to the given target object or, if no target is specified, to the first responder. Subclasses may override this method to perform special dispatching of action messages.

By default, this method pushes two parameters when calling the target. These last two parameters are optional for the receiver because it is up to the caller (usually a [UIControl](../uicontrol.md) object) to remove any parameters it added. This design enables the action selector to be one of the following:

- `- (void)action`
- `- (void)action:(id)sender`
- `- (void)action:(id)sender forEvent:(UIEvent *)event`

## See Also

### Controlling and handling events

- [- sendEvent:](<sendevent(__).md>) — Dispatches an event to the appropriate responder objects in the app.
- [applicationSupportsShakeToEdit](applicationsupportsshaketoedit.md) — A Boolean value that determines whether shaking the device displays the undo-redo user interface.
