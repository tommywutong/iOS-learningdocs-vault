---
title: 'camera(framing:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapproxy/camera(framing:)-1asl2'
source_url: 'https://developer.apple.com/documentation/mapkit/mapproxy/camera(framing:)-1asl2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapproxy/camera%28framing%3A%29-1asl2.json'
content_hash: 'sha256:17398b2c7139fd48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapProxy](../mapproxy.md)

# camera(framing:)

<sub>Instance Method</sub>

Creates a camera in the context of the map that frames the given coordinate region.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func camera(framing region: MKCoordinateRegion) -> MapCamera
```

## Parameters

- `region` — The coordinate region to frame.

## Return Value

Returns a [MapCamera](../mapcamera.md) with the framing region you specified.

## See Also

### Creating a camera proxy

- [camera(framing:)](<camera(framing_)-uxov.md>) — Creates a camera in the context of the map that frames the given map rectangle.
- [camera(framing:allowPitch:)](<camera(framing_allowpitch_).md>) — Creates a camera in the context of the map that frames the given map item.
