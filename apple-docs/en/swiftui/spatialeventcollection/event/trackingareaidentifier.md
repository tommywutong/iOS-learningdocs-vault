---
title: trackingAreaIdentifier
framework: CompositorServices
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/spatialeventcollection/event/trackingareaidentifier
source_url: 'https://developer.apple.com/documentation/swiftui/spatialeventcollection/event/trackingareaidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/spatialeventcollection/event/trackingareaidentifier.json'
content_hash: 'sha256:2a3916cb0a12d765'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [SwiftUI](../../../swiftui.md) · [SpatialEventCollection](../../spatialeventcollection.md) · [Event](../event.md)

# trackingAreaIdentifier

<sub>Instance Property</sub>

The tracking area identifier of the event, if the gesture is attached to a `CompositorLayer`, or `nil` if the event didn’t hit a tracking area or the gesture isn’t attached to a `CompositorLayer`.

<sub>macOS, visionOS</sub>

```swift
var trackingAreaIdentifier: LayerRenderer.Drawable.TrackingArea.Identifier { get }
```
