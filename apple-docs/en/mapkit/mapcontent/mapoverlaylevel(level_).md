---
title: 'mapOverlayLevel(level:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mapcontent/mapoverlaylevel(level:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mapcontent/mapoverlaylevel(level:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mapcontent/mapoverlaylevel%28level%3A%29.json'
content_hash: 'sha256:859f3c8bce90ff41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MapContent](../mapcontent.md)

# mapOverlayLevel(level:)

<sub>Instance Method</sub>

Specifies the position of overlays relative to other map content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func mapOverlayLevel(level: MKOverlayLevel) -> some MapContent

```

## Parameters

- `level` — One of the [MKOverlayLevel](../mkoverlaylevel.md) levels.

## Return Value

Returns [MapContent](../mapcontent.md) with overlays drawn with the positioning level you specified.
