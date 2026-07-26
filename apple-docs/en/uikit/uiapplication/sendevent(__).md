---
title: 'sendEvent(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/sendevent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/sendevent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/sendevent%28_%3A%29.json'
content_hash: 'sha256:8141efd28126a708'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# sendEvent(_:)

<sub>Instance Method</sub>

Dispatches an event to the appropriate responder objects in the app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sendEvent(_ event: UIEvent)
```

## Parameters

- `event` — A [UIEvent](../uievent.md) object encapsulating the information about an event, including the touches involved.

## Discussion

If you require it, you can intercept incoming events by subclassing [UIApplication](../uiapplication.md) and overriding this method. For every event you intercept, you must dispatch it by calling `[super sendEvent:event]` after handling the event in your implementation.

## See Also

### Controlling and handling events

- [- sendAction:to:from:forEvent:](<sendaction(__to_from_for_).md>) — Sends an action message identified by the selector to a specified target.
- [applicationSupportsShakeToEdit](applicationsupportsshaketoedit.md) — A Boolean value that determines whether shaking the device displays the undo-redo user interface.
