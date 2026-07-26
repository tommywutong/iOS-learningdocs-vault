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
doc_path: '/documentation/uikit/uiwindow/sendevent(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindow/sendevent(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindow/sendevent%28_%3A%29.json'
content_hash: 'sha256:8079445b9f24f376'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindow](../uiwindow.md)

# sendEvent(_:)

<sub>Instance Method</sub>

Dispatches the specified event to its views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func sendEvent(_ event: UIEvent)
```

## Parameters

- `event` — The event to dispatch.

## Discussion

The [UIApplication](../uiapplication.md) object calls this method to dispatch events to the window. Window objects dispatch touch events to the view in which the touch occurred, and dispatch other types of events to the most appropriate target object. You can call this method as needed in your app to dispatch custom events that you create. For example, you might call this method to dispatch a custom event to the window’s responder chain.
