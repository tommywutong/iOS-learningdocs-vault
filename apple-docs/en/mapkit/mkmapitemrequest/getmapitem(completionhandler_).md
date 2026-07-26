---
title: 'getMapItem(completionHandler:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 15.0+, tvOS 18.0+, visionOS 1.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkmapitemrequest/getmapitem(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkmapitemrequest/getmapitem(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkmapitemrequest/getmapitem%28completionhandler%3A%29.json'
content_hash: 'sha256:c4edc027ee827e1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKMapItemRequest](../mkmapitemrequest.md)

# getMapItem(completionHandler:)

<sub>Instance Method</sub>

Requests a map item and calls the provided completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getMapItem(completionHandler: @escaping @MainActor @Sendable (MKMapItem?, (any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mapItem: MKMapItem { get async throws }
```

## Parameters

- `completionHandler` — A completion handler the framework calls to indicate the success or failure of the map item request.

## See Also

### Starting and stopping requests

- [- cancel](<cancel().md>) — Cancels an in-progress map item request.
