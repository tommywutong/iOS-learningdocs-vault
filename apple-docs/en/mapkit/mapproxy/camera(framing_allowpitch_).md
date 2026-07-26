---
title: 'camera(framing:allowPitch:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapproxy/camera(framing:allowpitch:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapproxy/camera(framing:allowpitch:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapproxy/camera%28framing%3Aallowpitch%3A%29.json'
content_hash: 'sha256:356e4613f8e37415'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapProxy](../mapproxy.md)

# camera(framing:allowPitch:)

<sub>Instance Method</sub>

Creates a camera in the context of the map that frames the given map item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func camera(framing item: MKMapItem, allowPitch: Bool = true) -> MapCamera
```

## Parameters

- `item` — The [MKMapItem](../mkmapitem.md) to frame.

- `allowPitch` — A Boolean value that indicates whether you can pitch the camera to frame the content.

## Return Value

Returns a [MapCamera](../mapcamera.md) with the framing region and pitch you specified.

## See Also

### Creating a camera proxy

- [camera(framing:)](<camera(framing_)-1asl2.md>) — Creates a camera in the context of the map that frames the given coordinate region.
- [camera(framing:)](<camera(framing_)-uxov.md>) — Creates a camera in the context of the map that frames the given map rectangle.
