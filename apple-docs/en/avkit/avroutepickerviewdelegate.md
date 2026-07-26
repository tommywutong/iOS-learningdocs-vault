---
title: AVRoutePickerViewDelegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avroutepickerviewdelegate
source_url: 'https://developer.apple.com/documentation/avkit/avroutepickerviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avroutepickerviewdelegate.json'
content_hash: 'sha256:2f1c6b383211afd9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVRoutePickerViewDelegate

<sub>Protocol</sub>

A protocol that defines the methods to adopt to respond to route picker view presentation events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
protocol AVRoutePickerViewDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Presenting Routes

- [- routePickerViewWillBeginPresentingRoutes:](<avroutepickerviewdelegate/routepickerviewwillbeginpresentingroutes(__).md>) — Tells the delegate that the route picker view is about to begin presenting routes to the user.
- [- routePickerViewDidEndPresentingRoutes:](<avroutepickerviewdelegate/routepickerviewdidendpresentingroutes(__).md>) — Tells the delegate when the route picker view finishes presenting routes to the user.

## See Also

### Configuring the delegate

- [delegate](avroutepickerview/delegate.md) — The delegate object for the route picker.
